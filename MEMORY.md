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

## Architectural Notes
- **Local Filesystem Constraints**: Browsers block `fetch('data.json')` for `file://` protocol due to CORS. 
  - *Solution*: Data is injected into `<script>` inside `index.html` by `scripts/build_dashboard.py`.
- **Variable Declaration**: Avoid `const` for data injection variables if the script might be re-evaluated or if injection fails. Use `var` or `window.DATA` checking.
- [ ] Process `4.audiolecs` and `5.other`.

## Context & Constraints
- Working with diverse material types (text, social media, audio).
- Target: Clean, searchable, and structured archive for future projects.
