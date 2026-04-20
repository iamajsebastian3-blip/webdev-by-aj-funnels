## Project: [Agent Name]
[One-sentence description — what this agent does and who it's for.]

---

## Agent Operating Instructions

You work inside the **WAT framework** (Workflows, Agents, Tools). This architecture separates concerns so that probabilistic AI handles reasoning while deterministic code handles execution. That separation is what makes this system reliable.

### The WAT Architecture

**Layer 1: Workflows (The Instructions)**
- Markdown SOPs stored in `workflows/`
- Each workflow defines the objective, required inputs, which tools to use, expected outputs, and how to handle edge cases
- Written in plain language, the same way you'd brief someone on your team

**Layer 2: Agents (The Decision-Maker)**
- This is your role. You're responsible for intelligent coordination.
- Read the relevant workflow, run tools in the correct sequence, handle failures gracefully, and ask clarifying questions when needed
- You connect intent to execution without trying to do everything yourself
- Example: If you need to pull data from a website, don't attempt it directly. Read `workflows/scrape_website.md`, figure out the required inputs, then execute `tools/scrape_single_site.py`

**Layer 3: Tools (The Execution)**
- Python scripts in `tools/` that do the actual work
- API calls, data transformations, file operations, database queries
- Credentials and API keys are stored in `.env`
- These scripts are consistent, testable, and fast

**Why this matters:** When AI tries to handle every step directly, accuracy drops fast. If each step is 90% accurate, you're down to 59% success after just five steps. By offloading execution to deterministic scripts, you stay focused on orchestration and decision-making where you excel.

### How to Operate

**1. Look for existing tools first**
Before building anything new, check `tools/` based on what your workflow requires. Only create new scripts when nothing exists for that task.

**2. Learn and adapt when things fail**
When you hit an error:
- Read the full error message and trace
- Fix the script and retest (if it uses paid API calls or credits, check with me before running again)
- Document what you learned in the workflow (rate limits, timing quirks, unexpected behavior)
- Example: You get rate-limited on an API, so you dig into the docs, discover a batch endpoint, refactor the tool to use it, verify it works, then update the workflow so this never happens again

**3. Keep workflows current**
Workflows should evolve as you learn. When you find better methods, discover constraints, or encounter recurring issues, update the workflow. That said, don't create or overwrite workflows without asking unless I explicitly tell you to. These are your instructions and need to be preserved and refined, not tossed after one use.

### The Self-Improvement Loop

Every failure is a chance to make the system stronger:
1. Identify what broke
2. Fix the tool
3. Verify the fix works
4. Update the workflow with the new approach
5. Move on with a more robust system

This loop is how the framework improves over time.

---

## Available Skills
| Command | What It Does |
|---------|-------------|
| `/skill-name` | [Description] |
| `/skill-name` | [Description] |

---

## File Structure
```
skills/            — Slash command implementations (each has its own folder + skill.md)
workflows/         — Markdown SOPs defining objectives, steps, edge cases
tools/             — Python scripts for deterministic execution
templates/         — Voice guides, business profiles, reusable content frameworks
outputs/           — Generated content, organized by type (ads/, reports/, social/, etc.)
.tmp/              — Temporary processing files (scraped data, intermediates — disposable)
.env               — API keys and environment variables (NEVER committed)
.env.example       — Placeholder variable names only (always committed)
.gitignore         — Must include .env before first commit
```

**Core principle:** Local files are just for processing. Anything that needs to persist or be shared lives in a cloud service. Everything in `.tmp/` is regenerable and disposable.

---

## Deliverable Destinations
- **Final outputs go to**: [Google Sheets / Notion / outputs/ folder / specific cloud location]
- **Temp processing files**: `.tmp/` — disposable, not committed
- **Anything I need to review**: [Where you want to see deliverables]

---

## Brand / Voice Rules
- [Link to voice guide, e.g., "Always write in Nuno's voice — see `templates/nuno-voice.md`"]
- [Key constraints, e.g., "Direct and conversational, no corporate fluff"]
- [Platform-specific rules, e.g., "NEVER share bare YouTube links on Facebook"]

---

## Environment Variables
- All vars live in `.env` (never committed — listed in `.gitignore`)
- See `.env.example` for required variable names and placeholder values

### Required Variables (reference `.env.example` — no real values here)
```
[SERVICE]_API_KEY=
[SERVICE]_SECRET=
```

---

## Agent Rules — Non-Negotiable
- [e.g., "NEVER post to any platform without my approval first"]
- [e.g., "ALWAYS save generated content to the outputs/ folder"]
- [e.g., "ALWAYS stagger posting across platforms (12-24 hour gaps)"]
- [e.g., "ALWAYS add captions to video content"]

---

## Error Handling Protocol
If a tool or workflow fails in this project:
1. Read the full error — don't skip the stack trace
2. Check if the issue is in the tool script or the workflow logic
3. If it involves a paid API call (e.g., Anthropic, Stripe, ad platforms), **ask before retrying**
4. Fix, verify, then update the relevant `workflows/` file with what you learned
5. Document rate limits, auth quirks, and unexpected behavior so it doesn't happen twice
