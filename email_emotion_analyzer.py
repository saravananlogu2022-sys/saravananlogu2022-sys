#!/usr/bin/env python3
"""
Core Emotion Analyzer for Emails
=================================
Analyzes the core emotion in an email using:
  - Nonviolent Communication (NVC) framework by Marshall B. Rosenberg
  - Emotional spectrum from "Letting Go" by David R. Hawkins (Map of Consciousness)

Usage:
    python email_emotion_analyzer.py

Requires:
    ANTHROPIC_API_KEY environment variable to be set.
    Install dependencies: pip install -r requirements.txt
"""

import os
import sys
import textwrap

import anthropic


# ---------------------------------------------------------------------------
# Hawkins' Map of Consciousness (from "Letting Go" by David R. Hawkins)
# Emotions are arranged from lowest to highest energetic level.
# ---------------------------------------------------------------------------
HAWKINS_EMOTION_SPECTRUM = """
Level 20  — Shame       (humiliation, worthlessness)
Level 30  — Guilt       (blame, remorse)
Level 50  — Apathy      (hopelessness, despair, defeat)
Level 75  — Grief       (sadness, loss, regret)
Level 100 — Fear        (anxiety, worry, dread)
Level 125 — Desire      (craving, wanting, needing)
Level 150 — Anger       (frustration, hatred, resentment)
Level 175 — Pride       (disdain, scorn, dismissiveness)
Level 200 — Courage     (confidence, affirmation, empowerment)
Level 250 — Neutrality  — (release, non-attachment, okayness)
Level 310 — Willingness (optimism, intention, openness)
Level 350 — Acceptance  (forgiveness, harmony, harmony)
Level 400 — Reason      (understanding, logic, discernment)
Level 500 — Love        (reverence, care, appreciation)
Level 540 — Joy         (serenity, compassion, effortless)
Level 600 — Peace       (bliss, perfection, oneness)
"""

# ---------------------------------------------------------------------------
# NVC universal human needs (from Rosenberg's NVC framework)
# Used to help the model identify which need is unmet.
# ---------------------------------------------------------------------------
NVC_UNIVERSAL_NEEDS = """
Connection: acceptance, affection, appreciation, belonging, closeness, community,
  companionship, consideration, empathy, inclusion, intimacy, love, mutuality,
  respect, safety, security, stability, trust, understanding, warmth

Autonomy: choice, freedom, independence, space, spontaneity

Honesty: authenticity, integrity, presence, transparency

Play: humor, joy, ease, fun, lightness

Peace: beauty, clarity, ease, equanimity, harmony, order

Physical well-being: air, food, movement/exercise, protection, rest, safety, shelter, touch, water

Meaning: awareness, celebration, challenge, clarity, competence, consciousness,
  contribution, creativity, discovery, efficacy, effectiveness, growth, hope,
  learning, mourning, participation, purpose, self-expression, stimulation, vision
"""


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def prompt_multiline(label: str) -> str:
    """Prompt for multi-line input terminated by a blank line."""
    print(f"\n{label}")
    print("(Press Enter on a blank line when done)")
    lines = []
    while True:
        line = input()
        # Two consecutive newlines (blank line) signals end of input
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def prompt_choice(label: str, options: list[str]) -> str:
    """Display a numbered menu and return the user's choice."""
    print(f"\n{label}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print("  Or type your own:")
    while True:
        raw = input("> ").strip()
        # Accept a number from the menu
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        # Accept free-text
        if raw:
            return raw
        print("Please enter a number or describe the relationship.")


def collect_inputs() -> tuple[str, str, str]:
    """Gather all three inputs from the user: email, sender title, relationship."""
    print("\n" + "=" * 60)
    print("  CORE EMOTION ANALYZER — Email Edition")
    print("  Powered by NVC (Rosenberg) + Letting Go (Hawkins)")
    print("=" * 60)

    email_content = prompt_multiline("Paste the email content:")
    if not email_content:
        print("Error: Email content cannot be empty.")
        sys.exit(1)

    print("\nSender's title or role (e.g., 'CEO', 'Direct Manager', 'Customer'):")
    sender_title = input("> ").strip()
    if not sender_title:
        sender_title = "Unknown"

    relationship = prompt_choice(
        "Your relationship to the sender:",
        [
            "Peer",
            "Direct manager (they manage you)",
            "Manager of peer organization",
            "Executive / Senior leadership",
            "Customer",
            "External partner",
        ],
    )

    return email_content, sender_title, relationship


# ---------------------------------------------------------------------------
# Core analysis via Claude API
# ---------------------------------------------------------------------------

def build_prompt(email_content: str, sender_title: str, relationship: str) -> str:
    """
    Construct the analysis prompt combining NVC methodology and Hawkins' spectrum.
    This is the heart of the tool — a well-structured prompt produces better analysis.
    """
    return f"""You are an expert in two frameworks:
1. **Nonviolent Communication (NVC)** by Marshall B. Rosenberg — which identifies the
   Observation → Feeling → Need → Request chain beneath every message.
2. **The Map of Consciousness** from "Letting Go" by David R. Hawkins — which places
   emotions on an energetic spectrum from Shame (lowest) to Enlightenment (highest).

---

## Context about the email

- **Sender's title / role:** {sender_title}
- **Your relationship to the sender:** {relationship}

## Email to analyze

{email_content}

---

## Instructions

Analyze the email thoroughly and return your output in the following EXACT sections.
Be empathetic, specific, and grounded in the text — avoid generic observations.

---

### 1. CORE EMOTION (Hawkins Spectrum)

Identify the ONE dominant emotion the sender is experiencing right now.
Pick from the spectrum below and state the level and name:

{HAWKINS_EMOTION_SPECTRUM}

Format:
> **Core emotion:** <Level> — <Emotion Name>
> **Brief description:** One sentence on what this level feels like for the sender.

---

### 2. NVC BREAKDOWN (Rosenberg Framework)

Walk through the four NVC components:

**Observation** (neutral facts without judgment or evaluation — what happened or was said):
- …

**Feeling** (the emotion beneath the words; distinguish genuine feelings from thoughts
  like "I feel ignored" which is really a thought about others' behavior):
- …

**Unmet Need** (the universal human need that is frustrated; pick from the list below):

{NVC_UNIVERSAL_NEEDS}

- Primary unmet need: …
- Secondary unmet need (if present): …

**Implicit Request** (what the sender is really asking for — stated or unstated):
- …

---

### 3. RELATIONSHIP & POWER DYNAMICS

In 2–3 sentences, explain how the fact that the sender is a **{sender_title}**
and your relationship is **{relationship}** shapes the way the emotion is expressed
or suppressed in this email.

---

### 4. RECOMMENDED RESPONSE

Write a response that:
- Opens with an empathetic acknowledgment of their feeling (no fixing, no defending yet)
- Names the unmet need so they feel truly heard
- Addresses the practical concern or request clearly
- Uses honest, first-person language about your own position where relevant
- Closes with a concrete next step or clear offer
- Maintains the appropriate tone and power dynamic for a **{relationship}** relationship

The response should feel human, not clinical. Keep it concise (under 200 words).
"""


def analyze_email(email_content: str, sender_title: str, relationship: str) -> str:
    """
    Send the prompt to Claude and return the formatted analysis.
    Errors from the API (auth, rate limit, etc.) bubble up naturally.
    """
    client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY from environment

    prompt = build_prompt(email_content, sender_title, relationship)

    print("\nAnalyzing… (this may take a few seconds)\n")

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def display_result(result: str) -> None:
    """Print the analysis with a clean visual wrapper."""
    print("\n" + "=" * 60)
    print("  ANALYSIS RESULT")
    print("=" * 60 + "\n")
    # Wrap long lines for readability in narrow terminals
    for line in result.splitlines():
        if len(line) > 100:
            print(textwrap.fill(line, width=100))
        else:
            print(line)
    print("\n" + "=" * 60)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    # Guard: require API key before prompting for any input
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\nError: ANTHROPIC_API_KEY is not set.")
        print("Export it first:  export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    # Step 1 — collect user inputs
    email_content, sender_title, relationship = collect_inputs()

    # Step 2 — run the analysis via Claude
    try:
        result = analyze_email(email_content, sender_title, relationship)
    except anthropic.AuthenticationError:
        print("\nError: Invalid API key. Check your ANTHROPIC_API_KEY value.")
        sys.exit(1)
    except anthropic.RateLimitError:
        print("\nError: Rate limit reached. Wait a moment and try again.")
        sys.exit(1)
    except anthropic.APIConnectionError:
        print("\nError: Could not reach the Anthropic API. Check your internet connection.")
        sys.exit(1)
    except anthropic.APIStatusError as e:
        print(f"\nAPI error ({e.status_code}): {e.message}")
        sys.exit(1)

    # Step 3 — display the result
    display_result(result)


if __name__ == "__main__":
    main()
