
## 2026-02-13 (Late): Facebook Data Consolidation
- **Standardization**: Converted processed Facebook data from JSON/Markdown structure to a single `fb_classified.csv` file.
- **Cleanup**: Removed individual markdown files and intermediate JSON to match the LiveJournal data format.
- **Dashboard**: Updated `build_dashboard.py` to read from the new CSV source.
