# Project Changelog

## 2026-02-13: Dashboard v2.1 Implementation

### New Features
- **Unified Dashboard**: Created `dashboard/index.html`, a single-page application to browse 396 items from LiveJournal, Facebook, and YouTube.
- **Search & Filtering**: Implemented real-time search by content and tags, plus source/category filters.
- **Graph Visualization**: Added a D3.js-powered interactive network graph showing connections between posts via tags.
- **"NEXUS" Design System**:
    - Dark Mode with Glassmorphism nuances.
    - Premium typography (Outfit + Cormorant Garamond).
    - Responsive Grid Layout.

### Technical Details
- **Architecture**: Single-File HTML. All data is pre-compiled into the HTML file to ensure it works offline without a local server (bypassing CORS restrictions).
- **Build System**: Created `scripts/build_dashboard.py` to aggregate raw data and inject it into `dashboard/template.html`.
- **Performance**: Optimized D3.js graph to handle 300+ nodes with smooth physics.

### Bug Fixes
- **v2.1 Hotfix**: Resolved a critical "White Screen" issue caused by a JavaScript variable declaration conflict (`const` vs `var` re-declaration) when data was injected. Added global error boundary (Toast notifications).
