# AI Agent Instructions

This repository may be edited by multiple AI agents and human collaborators. Follow these rules before changing files.

## Required Workflow

1. Inspect the working tree before editing:

```powershell
git status --short
```

2. Do not modify unrelated dirty files.
3. Do not commit directly to `main` unless the human explicitly requests it.
4. Prefer a task branch named with `agent/`, `feature/`, `fix/`, `docs/`, or `research/`.
5. Keep changes narrowly scoped to the requested task.
6. Before committing, show or review `git diff`.
7. Commit only files related to the task.
8. Never run destructive Git commands such as `git reset --hard` or force-push without explicit human approval.

## Coordination Rules

- If another collaborator has changed a file, preserve their work.
- If the task requires editing a high-conflict file, mention it before editing.
- If merge conflicts occur, resolve them manually and explain which version was kept.
- Generated files should be committed only when they are part of the requested deliverable.

## High-Conflict Files

Coordinate before editing:

- `README.md`
- `generate_report.py`
- `generate_agentic_workflow_ppt.py`
- `.github/*`
- final `.pptx`, `.html`, `.ipynb`, `.wav`, or report artifacts

## Reporting Back

When finished, report:

- files changed
- branch name, if created
- tests or checks run
- anything intentionally left uncommitted
