# User Memory - Digital Finance Chart Generation

## User Preferences (December 2024)

### Chart Requirements
- **Sources Required**: All numerical data must include source citations
- **Check-in Frequency**: Ask questions after every 10 generated charts
- **Token Check-in**: Ask questions after every 30k tokens used
- **Execution Mode**: Individual chart generation (safer, catch errors immediately)
- **Style Balance**: Equal priority on data accuracy, visual clarity, and consistency

### CRITICAL: Charts Must Contain Numbers Only (Added Dec 11, 2024)
- **ONLY create charts with numerical data** (bar charts, line charts, pie charts, scatter plots)
- **DO NOT create text-heavy diagrams** - use bullet points on slides instead
- **Each Python script MUST include:**
  1. DATA VERIFICATION SECTION with source URL and page references
  2. Source citation in chart footer: `fig.text(0.98, 0.02, 'Source: ...', ...)`
  3. CHART_METADATA dict with source and URL
- **If content is mostly labels/text, skip the chart** - present as slide bullets instead

### Source Citation Format
- Add source in chart annotation: `Source: [Organization, Year]`
- For synthetic/illustrative data: Use `[SYNTHETIC DATA]` or `[ILLUSTRATIVE]` label
- Prefer real data when available, clearly mark projections

### Quality Standards
- Grayscale-friendly colors
- **Minimum font size: 11pt** (40% larger than original 8pt - updated Dec 2024)
  - Titles: 20pt (was 14pt)
  - Section headers: 17pt (was 12pt)
  - Main text: 14pt (was 10pt)
  - Details/annotations: 11pt (was 8pt)
  - Source citations: 10pt (was 7pt)
  - rcParams base: font.size=14, axes.labelsize=14
- PDF output at 300 DPI
- One Python script per chart
- Each chart in its own folder

### Progress Tracking
- Total charts needed: ~400-415
- Module 1: 163 charts
- Module 2: ~116 charts
- Module 3: ~60 new charts
- Module 4: ~65 new charts
