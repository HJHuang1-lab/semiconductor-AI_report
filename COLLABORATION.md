# Collaboration Guide

This repository is shared by human collaborators and AI coding agents such as Codex and Antigravity. The goal is to keep GitHub synchronized and avoid incompatible parallel edits.

## Golden Rules

1. Do not commit directly to `main` for normal work.
2. Start every task from the latest `main`.
3. Create one branch per task.
4. Commit small, reviewable changes.
5. Push the branch to GitHub and merge through a Pull Request.
6. Do not edit the same files at the same time unless the owners agree first.
7. Resolve merge conflicts manually; never overwrite another collaborator's work blindly.

## Start Of Day

```powershell
cd "E:\Python檔案\GitHub research\AI agent research"
git checkout main
git pull origin main
git status
```

If there are local changes, inspect them before starting new work:

```powershell
git status --short
git diff
```

## Start A Task

Use a descriptive branch name:

```powershell
git checkout main
git pull origin main
git checkout -b feature/report-structure
```

Suggested branch prefixes:

- `feature/` for new content or functionality
- `fix/` for bug fixes
- `docs/` for documentation-only changes
- `research/` for exploratory research notes
- `agent/` for AI-agent generated work that needs human review

## During Work

Check what changed often:

```powershell
git status --short
git diff
```

Commit focused changes:

```powershell
git add path/to/changed-file.md
git commit -m "Describe the specific change"
```

Prefer adding specific files instead of `git add .` when the working tree contains unrelated changes.

## End Of Task

```powershell
git status --short
git push origin your-branch-name
```

Then open a GitHub Pull Request into `main`.

## Pull Request Checklist

Before merging, confirm:

- The branch was created from the latest `main`.
- The PR description explains what changed.
- The PR lists files or areas touched.
- Generated artifacts are intentional.
- No unrelated local files were included.
- Conflicts are resolved manually.
- Any scripts, reports, notebooks, or slides still open correctly.

## Suggested Ownership Areas

Use this as the default split unless a task says otherwise:

- Human lead: `README.md`, report outline, final review, GitHub merge decisions.
- Antigravity: implementation drafts, code experiments, generated reports, data processing drafts.
- Codex: repo hygiene, review, conflict analysis, documentation, small scoped fixes.

High-conflict files require explicit coordination before editing:

- `README.md`
- `generate_report.py`
- `generate_agentic_workflow_ppt.py`
- `.github/*`
- dependency or environment files
- main report or presentation deliverables

## Conflict Resolution

When Git reports a conflict, open each conflicted file and look for markers like:

```text
<<<<<<< HEAD
current version
=======
incoming version
>>>>>>> branch-name
```

Edit the file into the intended final version, remove the markers, then run:

```powershell
git add path/to/conflicted-file
git commit -m "Resolve merge conflict"
```

Do not use `git reset --hard`, force-push, or delete files to solve conflicts unless the repository owner explicitly approves it.
