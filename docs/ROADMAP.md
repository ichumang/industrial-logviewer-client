# Product Roadmap

---

## Completed Sprints

### ✅ Sprint 1 — UDP Foundation
- UDP client/server communication
- Binary request/reply framing
- Days request and bitfield calendar parser
- String item parser (UTF-16-LE)

### ✅ Sprint 2 — Connection & Internationalisation
- Connection status LED (green / yellow / red)
- Periodic background connectivity probe (15s)
- Runtime language switching via external JSON files
- German (DE) + English (EN) locale packs

### ✅ Sprint 3 — Full Category Architecture
- All four log category tabs
- Pult (console) selector dropdown
- Year input selector
- Hierarchical date tree (year → month → day)
- Category-colour accent system

### ✅ Sprint 4 — GUI Integration
- Right-panel content viewer with contextual header
- Schema/field-filter dialog
- Non-blocking QThread worker model
- Save/export session to file
- Status bar with request statistics

### ✅ Sprint 5 — Dynamic Schema Engine
- Runtime schema negotiation via description request/reply
- Schema registry (in-memory, keyed by itemtyp)
- Generic descriptor-driven record decoder
- Zero hardcoded data structures
- Fail-safe: surfaces diagnostic if schema missing
- Schema filter: user-configurable fields per data type
- Wire-verified against reference server

### ✅ Sprint 6 — Release & Packaging
- PyInstaller single-file distributable
- Semantic versioning (v5.1.0)
- CHANGELOG, requirements.txt, .gitignore
- Sanitized public portfolio repository

---

## Upcoming: Phase 3 — Analytics & Reporting

- [ ] Activate Fahrdaten (drive data) category — engine already ready, pending GUI wiring
- [ ] Activate Programmierung (programming logs) category — pending server schema spec
- [ ] Activate Antriebsfehler (drive errors) category — pending server schema spec
- [ ] Fault event timeline view (grouped by time window)
- [ ] Activation count aggregation per day
- [ ] Configurable KPI dashboard panel
- [ ] Exportable engineering report (PDF/HTML)

---

## Phase 4 — AI-Assisted Intelligence

- [ ] Anomaly detection — statistical models over decoded numeric fields
- [ ] Natural-language log query — "Show all faults after activation on March 4"
- [ ] Auto-summarization — LLM-generated session summaries
- [ ] Root-cause ranking — candidate explanations for fault sequences
- [ ] Predictive diagnostics — pattern recognition across historical sessions

> Because every record is fully structured at decode time (named fields + typed values), all data is immediately available as ML features without additional parsing.

---

## Phase 5 — SaaS / Fleet Expansion

- [ ] Multi-device fleet dashboard (web-based)
- [ ] Centralized log ingestion pipeline
- [ ] Role-based access (engineer / manager / read-only)
- [ ] Tenant isolation for multi-customer deployments
- [ ] REST/WebSocket API for third-party integrations
- [ ] Mobile-friendly status view

---

## Technology Alignment

| Phase | Key Tech |
|---|---|
| Current (desktop) | Python 3.13, PyQt6, UDP, PyInstaller |
| Phase 3 (analytics) | pandas, matplotlib/plotly, reportlab |
| Phase 4 (AI) | scikit-learn, LangChain, local LLM or OpenAI API |
| Phase 5 (SaaS) | FastAPI, WebSockets, React/Vue, PostgreSQL, Docker |
