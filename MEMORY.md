# Project Memory: Materials Centralization

## Project Objective
- Collect and centralize materials for a common repository.
- Maintain a structured catalog/archive.
- Prepare materials for future derivative projects.

## Core Rules
- `materials/` directory is STICTLY READ-ONLY.
- All modifications/reorganizations happen in the root or a new `centralized/` directory.

## Current Progress
- [x] Established project rules in `.agent/rules/materials-policy.md`.
- [x] Created initial `CATALOG.md`.
- [x] Классификация Facebook: 82 поста обработаны.
- [x] Классификация YouTube: 35 видео обработаны.
- [x] **Dashboard Implementation**: Unified UI created (`dashboard/index.html`).
  - Architecture: **Single-File HTML** (JSON injected at build time) to avoid local CORS issues.
  - Visualization: **D3.js Force Graph** for tag connections.
  - UI: Glassmorphism / "NEXUS" Dark Theme.
- [x] **External Integrations**:
  - **NotebookLM**: Connected via MCP. Cleaned up and renamed notebooks (YouTube, All Materials, Live Lectures).
  - **Google Drive**: Implemented `gdrive_tracker` skill. Authenticated and monitoring `Книга_впроцессник` folder.

## Architectural Notes
- **Local Filesystem Constraints**: Browsers block `fetch('data.json')` for `file://` protocol due to CORS. 
  - *Solution*: Data is injected into `<script>` inside `index.html` by `scripts/build_dashboard.py`.
- **Variable Declaration**: Avoid `const` for data injection variables if the script might be re-evaluated or if injection fails. Use `var` or `window.DATA` checking.
- **MCP Integration**: Uses both `notebooklm` (for transcripts/analysis) and `google-drive-mcp` (for tracking drafting progress).
- [ ] Process `4.audiolecs` and `5.other`.
- [ ] Map all 36 YouTube transcripts to the Book Structure identified in Google Drive.

## Context & Constraints
- Working with diverse material types (text, social media, audio).
- Target: Clean, searchable, and structured archive for future projects.
