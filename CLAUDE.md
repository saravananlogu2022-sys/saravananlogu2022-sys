# CLAUDE.md — AI Assistant Guide for saravananlogu2022-sys

## Repository Overview

This is a **GitHub profile repository** for Saravanan Logu (sarav), a Product Manager specializing in AI agents and retail workflows. GitHub treats a repository named the same as the username as a special profile README — its `README.md` is displayed directly on the user's GitHub profile page.

**Repository type:** Personal portfolio / GitHub profile README
**Owner:** Saravanan Logu (`saravananlogu2022`)
**Domain focus:** AI agents and workflows for Retail Product Management
**Contact:** saravananlogu2022@gmail.com | linkedin.com/in/saravananlogu

---

## Repository Structure

```
saravananlogu2022-sys/
├── README.md       # GitHub profile page content (the only source file)
└── CLAUDE.md       # This file — AI assistant guidance
```

There is no application code, build system, test suite, or package manager configuration. The sole deliverable is `README.md`, which renders as the public GitHub profile page.

---

## What README.md Does

The `README.md` serves as a personal landing page that communicates:

- **What Saravanan builds** — AI agents and workflows for Retail PMs
- **Active work** — Email Sentiment Analyzer, GitHub/AI agent learning, collaboration interests
- **Featured Projects table** — Links to real projects with stack info (currently placeholder links)
- **Connect section** — LinkedIn, portfolio/blog, email

---

## Development Conventions

### File Editing
- The only file requiring ongoing maintenance is `README.md`
- Preserve the existing section order: bio → What I Build → What I'm Working On → Featured Projects → Connect → footer tagline
- Use standard GitHub-flavored Markdown (GFM)
- Emojis are present and intentional — keep them when editing existing sections

### README Sections
| Section | Purpose | Notes |
|---|---|---|
| Header (`# Hi, I'm...`) | Personal intro | Keep concise |
| What I Build | Core identity statement | 1-2 sentences |
| What I'm Working On | Current active projects | Bullet list, update as projects change |
| Featured Projects | Portfolio table | Replace `[Project 1]`, placeholder links, and `[One line]` with real data |
| Connect | Social/contact links | LinkedIn URL, email, portfolio |
| Footer tagline | Brand statement | Italic, one line |

### Placeholder Fields to Fill
These fields in `README.md` are currently placeholders and should be updated with real content:
- `[Project 1]`, `[Project 2]`, `[Project 3]` → real project names with correct URLs (replace `link`)
- `[One line]` → one-sentence project descriptions
- `[Portfolio/Blog](your-link)` → actual portfolio/blog URL

---

## Git Workflow

### Branch Strategy
- **`master`** — main branch, mirrors the live GitHub profile
- Feature branches follow the pattern `claude/<task-id>` for AI-assisted changes

### Commit Signing
All commits must be GPG/SSH signed. The environment is pre-configured:
```
user.signingkey=/home/claude/.ssh/commit_signing_key.pub
gpg.format=ssh
commit.gpgsign=true
```
Do not use `--no-gpg-sign` or disable signing.

### Commit Message Style
Use clear, descriptive commit messages. Examples from history:
- `Initial commit`
- `Update README.md`

For AI-assisted changes, prefer messages like:
- `Add CLAUDE.md with repository guide`
- `Update featured projects with real links`
- `Add new project to What I'm Working On`

### Push Command
```bash
git push -u origin <branch-name>
```
Branch names must start with `claude/` for AI-assisted branches.

---

## How to Help Saravanan

When assisting with this repository, common tasks include:

1. **Updating Featured Projects** — Replace placeholder rows with real project entries (name, link, description, stack)
2. **Adding new projects** to "What I'm Working On" as the list evolves
3. **Improving README formatting** — Badges, sections, visual polish
4. **Adding new sections** — Skills, GitHub stats widgets, contribution graphs, etc.
5. **Fixing broken links** — Ensure project links, portfolio, and social links resolve correctly

### Adding GitHub Stats (Optional Enhancement)
If requested, common GitHub profile README enhancements include:
```markdown
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=saravananlogu2022)
```

### Do Not
- Add source code, build tooling, or package files (this is documentation-only)
- Remove or significantly reorder existing sections without instruction
- Change contact information without explicit confirmation
- Push to `master` directly — use a feature branch and PR

---

## Context for AI Assistants

- **No build step** — nothing to install, compile, or run
- **No tests** — there is no test suite to execute
- **No linting config** — no automated style enforcement
- **All changes are low-risk** — only Markdown edits; reversible via git history
- **Audience is public** — the README is Saravanan's professional face on GitHub; maintain a professional, clear tone
