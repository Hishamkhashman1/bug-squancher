# BugSquancher

## Overview
BugSquancher appends short, human-readable hints to terminal errors without changing how users run commands.

## Why It Exists
Terminal errors are loud and often unhelpful. BugSquancher adds a brief, structured hint block so you can decide what to try next without digging through long logs.

## What It Does
- Keeps the original output intact
- Appends a concise hint block at the end
- Avoids certainty and never auto-runs commands

## Output (Example)
```
Cause: <short explanation>

Possible fix: <short guidance>

Recommended:
<command>
(<context>)
```

## Status
MVP in progress.

## Notes
Details available on request.
