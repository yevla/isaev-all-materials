# Project Milestones & Development History

> **Objective**: Centralize Isaev's archive (LiveJournal, Facebook, YouTube) into a unified, explorable digital format.

## Milestone 1: Foundation & Taxonomy
- [x] **Analysis of LiveJournal (Primary Source)**
    - Scanned `materials/1.LJ` (279 posts).
    - Identified core themes: *Psychotherapy, Psychiatry, Social Psychology, Personal*.
    - **Outcome**: Developed a unified Tagging Taxonomy (Logic vs. Emo, Professional vs. Personal) to be applied across all other sources.

## Milestone 2: Data Processing & Normalization
- [x] **Facebook (`materials/2.fb_dsisaev`)**
    - **Problem**: Raw export was messy, containing reposts and system messages.
    - **Action**: Wrote `process_fb_data.py`.
    - **Logic**:
        - Filtered out short posts (<50 chars) and obvious reposts.
        - Applied LJ Taxonomy to classify remaining 82 posts.
    - **Result**: structured JSON + Markdown files for high-value content.

- [x] **YouTube (`materials/3.yt`)**
    - **Action**: Analyzed video titles and descriptions.
    - **Logic**: Classified 35 videos using the same taxonomy key.
    - **Result**: Generated `yt_classified.csv` with standardized headers (Source, Date, Title, Tags, Link).

- [x] **Repository Setup**
    - Initialized Git repository.
    - Configured `.gitignore` (ignoring system files, raw large assets).
    - Established `CATALOG.md` as the single source of truth for file locations.

## Milestone 3: Dashboard Architecture (The "Single-File" Challenge)
- [x] **Concept**: Create a "Master Dashboard" to browse everything without needing to look at folders.
- [x] **Constraint**: The user must be able to run this **offline** by just double-clicking a file.
- [x] **Technical Hurdle**:
    - Browsers block `fetch('data.json')` for local files (CORS policy).
    - **Solution**: "Injection Build System". `scripts/build_dashboard.py` reads all data and *injects* it directly into a JS variable inside the HTML. No external requests needed.

## Milestone 4: Dashboard Implementation (Iterations)
### Iteration 1: The Prototype
- Built basic grid layout.
- **Issue**: UI was too simple, lacked "Wow" factor.
- **Issue**: "White Screen of Death" reported by user.
    - *Diagnosis*: JavaScript error during initialization (conflicting variable declarations).

### Iteration 2: "NEXUS" Design System (Current)
- **Visual Overhaul**:
    - Switched to **Deep Space** theme (Dark background + Neon Accents).
    - Implemented **Glassmorphism** (Glass panels for sidebar/modals).
    - Typography upgrade: `Outfit` (UI) + `Cormorant Garamond` (Text).
- **Interactive Graph (Node Map)**:
    - Added **D3.js** integration.
    - Visualized posts (dots) connected to tags (hubs) with physics simulation.
    - Made nodes draggable and zoomable.

### Iteration 2.1: Critical Fixes
- **Bug**: Dashboard showed nothing on load.
- **Fix**: Removed `const` redeclaration in injected code. Changed to robust `window.ISAEV_DATA` check.
- **Safety**: Added a Global Error Boundary. If the dashboard crashes, it now shows a red "System Error" toast instead of failing silently.

## Milestone 5: Book Drafting & Intelligent Research
- [x] **NotebookLM Synchronization**
    - Refined and organized 35+ notebooks into a logical structure:
        - `Isaev: YouTube` (Video transcripts base).
        - `Isaev: all materials` (Unified posts archive).
        - `Isaev: live lectures` (Oral recordings).
- [x] **Google Drive Integration**
    - Established connection to `Книга_впроцессник` (Book-in-progress).
    - Map of book structure (5 parts: Foundation, Scenarios, Roles, Psychosomatics, Healing).
- [x] **Progress Tracking (New Skill)**
    - Created `gdrive_tracker` skill to monitor Dmitry's edits, revision history, and word counts.
    - Automated the "Snapshot" process to catch every new paragraph.

## Current State (Active Implementation)
- **Total Materials**: 396 items + 36 full YouTube transcripts.
- **Book Status**: Structure defined; 12,000+ chars drafted (Introduction).
- **Automation**: Assistant can now track Dima's live edits on Google Drive.
- **Git Status**: All local changes synced with `origin/main`.
