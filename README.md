# errhint (working name) **TBD**

## Product Definition

### Core Idea
Append a human-readable explanation and fix to terminal errors directly in the CLI, without changing how users run commands.

### User Flow

- User runs command normally
- Command fails
- Full output and error are shown as usual
- Tool appends at the end:
  - `Cause: ...`
  - `Possible fix: ...`
  - `Recommended: <command> (<where to run it>)`

### Principles

- Do not modify or suppress existing output
- Only append at the end
- Keep messages short and actionable
- Never assume certainty (always “Possible fix”)
- Do not auto-execute anything

## Architecture

### Flow

```
Shell (zsh)
    ↓
Detect command completion
    ↓
If exit code != 0:
capture command + output (stderr/stdout)
    ↓
Python analyzer
  - normalize text
  - match patterns
    ↓
Formatter
    ↓
Append summary to terminal
```

## Components

### Python Side

- **parser.py** — Extract and normalize error text
- **matcher.py** — Match error text against known patterns
- **patterns.py** — Static list of known error patterns
- **models.py** — Dataclasses for patterns
- **formatter.py** — Build final output string
- **main.py** — Orchestrates parsing, matching, formatting

### Shell Side

- **errhint.zsh** — Hooks into zsh lifecycle and triggers analyzer when a command fails

## Stack

### Core

- Python 3.10+
- `re` - Regular expression module for pattern matching
- `dataclasses` - data structure definitions for organizing code data
- `subprocess` - Process management (if needed)

### Shell

- zsh (MVP)

### Optional

- `rich` (only if you want styled output)

### Not Needed for MVP

- AI
- database
- external APIs

## Data Model

```python
from dataclasses import dataclass

@dataclass
class ErrorPattern:
    name: str
    keywords: list[str]
    cause: str
    possible_fix: str
    recommended_command: str
    context: str
```

## Matching Strategy

### MVP

- Convert full error text to lowercase
- Simple keyword matching

**Example:**

```python
if any(keyword in error_text for keyword in pattern.keywords):
    return pattern
```

First match wins.

### Later Improvements

- regex
- scoring (number of matches)
- multiple candidates

## Output Format

Always append at the end of terminal output:

```
Cause: <short explanation>

Possible fix: <short guidance>

Recommended:
<command>
(<context>)
```

**Example:**

```
Cause: Your database user does not have permission on the public schema.

Possible fix: Grant the required permissions to your database user.

Recommended:
GRANT CREATE ON SCHEMA public TO your_user;
(run this in PostgreSQL CLI or a tool like pgAdmin)
```

## Error Patterns (Initial Set)

Start with 5–10 high-value patterns.

### Postgres Permission

**Keywords:**
- `insufficientprivilege`
- `permission denied for schema public`

**Cause:** User does not have permission on the schema.

**Possible fix:** Grant the required permissions to the database user.

**Recommended:**
```
GRANT CREATE ON SCHEMA public TO your_user;
```

**Context:** Run in PostgreSQL CLI (psql) or admin tool.

### Port Already in Use

**Keywords:**
- `address already in use`
- `port already in use`

**Cause:** Another process is already using the required port.

**Possible fix:** Stop the process using the port or change the port.

**Recommended:**
```
lsof -i :8000
kill -9 <PID>
```

**Context:** Run in your terminal.

### Module Not Found

**Keywords:**
- `modulenotfounderror`
- `no module named`

**Cause:** Required Python module is not installed.

**Possible fix:** Install the missing module.

**Recommended:**
```
pip install <module_name>
```

**Context:** Run in your virtual environment.

### Command Not Found

**Keywords:**
- `command not found`

**Cause:** The command is not installed or not in PATH.

**Possible fix:** Install the tool or check your PATH.

**Recommended:**
```
which <command>
or install the missing package
```

**Context:** Run in your terminal.

### Uvicorn / ASGI Error

**Keywords:**
- `error loading asgi app`

**Cause:** Incorrect module path or app reference.

**Possible fix:** Check module path and app variable name.

**Recommended:**
```
uvicorn app.main:app --reload
```

**Context:** Run in your project directory.

## Shell Integration (ZSH)

### Goal

Trigger only when a command fails.

### Approach

- Use zsh hook (precmd or similar)
- Check exit code ($?)
- If non-zero:
  - Capture last command
  - Optionally capture output
  - Call Python analyzer
  - Print result

### Constraints

- Do not break normal terminal behavior
- Do not duplicate output
- Only append

## MVP Scope

- zsh only
- Python analyzer
- 5–10 patterns
- Append output only
- No styling required
- No config system

## Implementation Plan

### Day 1

- Build Python analyzer
- Implement patterns
- Simple CLI input for testing (pass text manually)

### Day 2

- Integrate with zsh
- Detect failed commands
- Append output

### Day 3

- Polish output text
- Test with real errors
- Package project

**Ship after Day 3.**

## Packaging

Use pip package.

**pyproject.toml:**

```toml
[project]
name = "errhint" (**TBD**)
version = "0.1.0"
description = "Append human-readable explanations to terminal errors"
requires-python = ">=3.10"
```

### Install Locally

```bash
pip install -e .
```

### Later

```bash
python -m build
twine upload dist/*
```

### Shell Integration

User adds a line in `.zshrc`:

```bash
source /path/to/errhint.zsh
```

## Design Rules

- Keep output short
Always show Cause / Possible fix / Recommended
Do not remove original error
Do not auto-run commands
Do not guess aggressively
Always use “Possible”
SUCCESS METRIC

User behavior change:

“I saw the error and understood what to do without searching online.”

FUTURE IDEAS
AI fallback when no pattern matches
bash support
fish support
community pattern contributions
command suggestions (did-you-mean)
better formatting (colors, spacing)
