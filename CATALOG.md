# Materials Catalog

## Raw Materials (READ-ONLY)
| Category | Source Folder | Status | NotebookLM / Local Access |
| :--- | :--- | :--- | :--- |
| LiveJournal | `materials/1.LJ` | Processed | **NotebookLM**: `932e0d71...` (Isaev: FB and LJ). Sourced from `LJ_posts.md` |
| Facebook | `materials/2.fb_dsisaev` | Processed | **NotebookLM**: `932e0d71...` (Isaev: FB and LJ). Sourced from `FB_posts.md` |
| YouTube | `materials/3.yt` | Processed | **NotebookLM**: `d043eadc...` (Isaev: YouTube). Contains Full Transcripts. |
| Audio | `materials/4.audiolecs` | NLM-Stored | **NotebookLM**: `05bcc6a9...` (Isaev: live lectures). Transcripts of private groups. |
| Other | `materials/5.other` | Pending | TBD. |

## Centralized Archive
| Component | Path | Description |
| :--- | :--- | :--- |
| **Master Dashboard** | `dashboard/index.html` | Unified Single-Page Application (SPA) for browsing all materials. Features search, filtering, and graph visualization. **Self-contained** (runs offline). |
| Data Builder | `scripts/build_dashboard.py` | Python script to aggregate data from LJ, FB, and YT into the dashboard. |
