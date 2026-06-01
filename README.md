# 🛰️ Industrial Log Intelligence Platform

> **Schema-driven, real-time telemetry & diagnostics client for industrial control systems**
> Built with Python + PyQt6 · Zero hardcoded data structures · Fully self-describing protocol

[![Status](https://img.shields.io/badge/status-active%20development-brightgreen)](https://github.com/ichumang/industrial-logviewer-client)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://python.org)
[![UI](https://img.shields.io/badge/UI-PyQt6-41cd52)](https://pypi.org/project/PyQt6/)
[![Architecture](https://img.shields.io/badge/architecture-schema--driven-orange)](#architecture)
[![Version](https://img.shields.io/badge/version-5.1.0-informational)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey)](#license)

---

## 🎯 Product Vision

**Industrial Log Intelligence Platform** transforms raw binary diagnostic streams from industrial controllers into **structured, human-readable, queryable intelligence** — in real time.

Where legacy tools ship rigid, hardcoded data layouts that break on every firmware revision, this platform is **self-describing**: it negotiates the data schema with the server at runtime, so new data types and fields appear automatically — **zero client rebuild required**.

> **Core differentiator:** *Schema-as-a-Service.* The data layout is a contract delivered over the wire at runtime, not baked into the binary.

---

## 💡 The Problem We Solve

| Legacy Tool Pain | Our Solution |
|---|---|
| Hardcoded structs break on every firmware/field change | **Runtime schema negotiation** — client learns layout from server |
| One rigid binary per data category | **Single generic decoder** adapts to all log types |
| Cryptic hex dumps requiring expert interpretation | **Field-level rendering** with named values from schema |
| Overwhelming data, no filtering | **User-configurable field filters** per data type |
| GUI freezes during network fetch | **Worker-thread model** — UI always responsive |
| No internationalization | **Runtime i18n** via external JSON locale files |

---

## ✨ Key Features

| Feature | Status |
|---|---|
| UDP-based log data retrieval | ✅ Done |
| Activation days — calendar bitfield parser | ✅ Done |
| Activation data — string and drive-field items | ✅ Done |
| PyQt6 GUI with output viewer and status bar | ✅ Done |
| Worker thread (non-blocking GUI) | ✅ Done |
| Connection status indicator (green/yellow/red) | ✅ Done |
| Configurable server IP address | ✅ Done |
| i18n — external JSON language files | ✅ Done |
| All four log categories wired in UI | ✅ Done |
| Dynamic type descriptions (server-driven schema) | ✅ Done |
| PyInstaller single-exe packaging | ✅ Done |

Additional product-level highlights:

- 🔌 Self-describing protocol — runtime schema negotiation
- 📊 Multi-category log view (Activation, Drive Data, Programming, Errors)
- 🗂️ Hierarchical date explorer — year → month → day
- 🎨 Configurable field filtering per data type
- 🟢 Live connection health — color-coded LED indicator + 15s probe
- 🌍 Runtime language switching (DE/EN + extensible)
- ⚡ Non-blocking UI — QThread worker for all network I/O
- 💾 One-click export for audit and reporting
- 📦 Single-file distributable (PyInstaller)
- 🤖 AI-assisted anomaly detection (roadmap)
- 📈 Time-series trend visualization (roadmap)
- ☁️ SaaS dashboard / multi-device fleet view (roadmap)

---

## 🏗️ Architecture Overview

The platform follows a clean **separation-of-concerns** design with a thin presentation layer over a fully reusable protocol + data-intelligence engine.

```
┌──────────────────────────────────────────────────────────────┐
│               Presentation Layer  (PyQt6)                    │
│   Category tabs · Date explorer · Live viewer · Filters      │
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│          Protocol & Data Intelligence Engine                 │
│   • Runtime schema negotiation  (self-describing contracts)  │
│   • Dynamic record decoder  (zero hardcoded layouts)         │
│   • Connection health monitoring  (periodic background probe)│
└───────────────────────────┬──────────────────────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│          Transport Layer  (async UDP datagram socket)        │
└───────────────────────────┬──────────────────────────────────┘
                            │
                ┌───────────▼───────────┐
                │  Log Data Server      │
                │  (C++ service, CIC PC)│
                └───────────────────────┘
```

### Core Principle: Zero Hardcoded Structs

```
CMD-5 (schema request) ──► Server sends field descriptors ──► SCHEMA_REGISTRY[itemtyp]
                                                                        │
CMD-3 (data request)   ──► Server sends typed records     ──► Decoded against runtime schema
                                                                        │
                                                             Rendered as named key:value pairs
```

The decoder builds its record layout **entirely from descriptors the server sends**. If the schema is missing, the engine surfaces a clear diagnostic — a **fail-safe, contract-first** approach.

---

## 📊 Data Categories

| Category | Description | Engine State |
|---|---|---|
| **Activation Data** | Activation / deactivation events, operator context, drive field state | ✅ Live |
| **Dynamic Drive Data** | Per-cycle drive and group telemetry, motion parameters | ✅ Engine ready |
| **Programming Logs** | Configuration changes, user actions, parameter history | ✅ Engine ready |
| **Drive Errors** | Actuator fault events, error codes, diagnostic context | ✅ Engine ready |

> All categories share the **same generic parsing engine** — each category is distinguished only by its runtime schema (itemtyp). Adding a new category = one new server-side schema contract, zero client code changes.

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| UI Framework | PyQt6 (Qt 6) |
| Language | Python 3.13 |
| Concurrency | QThread worker model — non-blocking network I/O |
| Networking | Native UDP datagram sockets |
| Data Engine | Binary protocol decoder, dynamic struct-free parser |
| Schema Store | Runtime in-memory schema registry |
| Localization | External JSON locale files (zero recompile) |
| Packaging | PyInstaller — single-file distributable |
| Tooling | VS Code · venv · Git + SemVer |

---

## 📈 Product KPIs

| KPI | Target | Rationale |
|---|---|---|
| Schema adaptation latency | < 1s on startup | New data types usable immediately |
| Decode accuracy | 100% byte-for-byte | Verified against reference server |
| UI freeze events during network fetch | **0** | Worker-thread architecture |
| Client rebuilds per schema change | **0** | Core value proposition |
| Connection recovery detection | ≤ 15s | Background 15s health probe |
| Log categories supported without code change | Unlimited | Generic schema engine |
| Distributable binary size | ~20–36 MB | Python + Qt6 runtime bundle |

---

## 🤖 AI & Intelligence Roadmap

The platform is architected to evolve from a **viewer** into an **intelligence engine**:

- **Anomaly Detection** — ML models over decoded numeric fields to flag outliers (e.g. abnormal cycle timing, unexpected fault frequency).
- **Natural-Language Querying** — "Show all faults after activation on March 4" → structured filter.
- **Predictive Diagnostics** — pattern recognition across historical sessions to anticipate faults.
- **Auto-Summarization** — LLM-generated session summaries for non-expert stakeholders.
- **Root-Cause Ranking** — surface top candidate explanations for drive error sequences.

> Because every record is **fully structured at decode time** (field names plus typed values), all fields are immediately available as ML features — no brittle log scraping required.

---

## 🧠 Skills Demonstrated

| Domain | Details |
|---|---|
| **Software Architecture** | Layered design, separation of concerns, reusable engine |
| **Binary Protocol Engineering** | Wire-format decoding, schema negotiation, endianness, struct parsing |
| **Desktop GUI Development** | PyQt6, event-driven design, custom widgets, dark theme |
| **Concurrency** | Thread-safe QThread worker model, non-blocking network I/O |
| **Network Programming** | UDP datagram sockets, request/reply protocol, timeout handling |
| **Dynamic Data Modeling** | Runtime schema registry, descriptor-driven record parsing |
| **Internationalization** | Externalized locale JSON, runtime language switching |
| **Product Thinking** | KPI definition, roadmap planning, pain-driven feature design |
| **DevOps & Release Engineering** | SemVer, CHANGELOG, reproducible builds, .gitignore hygiene |
| **Quality Engineering** | Wire-level verification, fail-safe contract-first design |

---

## 🗂️ Project Structure

```
industrial-logviewer-client/
├── logviewer.py            # GUI entry point  (PyQt6 presentation layer)
├── protocol.py             # Protocol + data intelligence engine
├── lang/                   # i18n locale resources
│   ├── de.json             #   German (primary)
│   └── en.json             #   English
├── docs/                   # Product and architecture documentation
│   ├── PRODUCT_VISION.md
│   ├── architecture.md
│   ├── ROADMAP.md
│   ├── KPI_FRAMEWORK.md
│   └── RELEASE_PROCESS.md
├── CHANGELOG.md            # Version history
├── requirements.txt        # Pinned dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

```bash
# 1. Clone
git clone https://github.com/ichumang/industrial-logviewer-client.git
cd industrial-logviewer-client

# 2. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1     # Windows PowerShell
# source .venv/bin/activate       # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run (requires Log Data Server running on local network)
python logviewer.py
```

### Build a distributable

```bash
pyinstaller --onefile --windowed --icon=assets/app.ico --name LogViewer logviewer.py
```

---

## 🔄 Two-Tier Deployment

```
Operator Laptop  (any PC on LAN)
└── LogViewer.exe
    └── lang/
        ├── de.json
        └── en.json

Diagnostic Server PC  (CIC, fixed industrial network)
└── LogDataServer.exe   ← C++ service, not in this repo
```

---

## 🛡️ Design Principles

1. **Contract-first** — server schema is the source of truth, client adapts.
2. **Zero recompile for format changes** — schema delivered at runtime.
3. **Zero recompile for text changes** — all UI strings in external JSON.
4. **Fail-safe** — missing schema surfaces a diagnostic, never a silent wrong decode.
5. **Thread safety** — all UDP I/O on worker thread, GUI thread never blocked.
6. **Separation of concerns** — transport, schema registry, parser, and GUI are independent layers.

---

## 📜 Changelog

See [CHANGELOG.md](CHANGELOG.md) for full version history.

**Latest: v5.1.0** — Dynamic schema engine, schema filter dialog, 15s connection probe, full i18n.

---

## 📄 License

Proprietary — All rights reserved.
This repository is a sanitized portfolio version. No proprietary protocol details, company names, internal server names, or real operational log data are included.

---

<p align="center"><i>Built with precision engineering and a product mindset.</i></p>
