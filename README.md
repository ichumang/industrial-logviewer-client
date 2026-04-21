# Industrial Log Viewer — Client

> **Python/PyQt6 desktop client for real-time industrial log data visualization**
> B2B industrial automation | UDP protocol | Cross-platform | i18n-ready

---

## Overview

The **Industrial Log Viewer** is a desktop application built for industrial automation environments. It connects to a log-data server running on a diagnostic PC, retrieves structured log data over UDP, and presents it in a clear, operator-friendly GUI.

The application is designed as the **client layer** of a two-tier architecture:

```
┌──────────────────────────────────────┐
│   Industrial Log Viewer (this repo)  │   ← Python/PyQt6, operator laptop
│   UDP Client · GUI · i18n            │
└──────────────┬───────────────────────┘
               │ UDP / LAN
               ▼
┌──────────────────────────────────────┐
│   Log Data Server (CIC / server PC)  │   ← C++ service, diagnostic PC
│   Reads log files · Serves over UDP  │
└──────────────────────────────────────┘
```

The server owns the log file formats. The client never needs to know the raw format — it asks the server, receives structured binary responses, and renders them. **Adding a new log type on the server side requires zero client code changes.**

---

## Key Features

| Feature | Status |
|---|---|
| UDP-based log data retrieval | ✅ |
| Activation days — calendar bitfield parser | ✅ |
| Activation data — string & drive-field types | ✅ |
| PyQt6 GUI with output viewer + status bar | ✅ |
| Worker thread (non-blocking GUI) | ✅ |
| Connection status indicator (green/yellow) | ✅ |
| Configurable server IP address | ✅ |
| i18n — external JSON language files | ✅ |
| All 4 log categories | ✅ |
| Dynamic type descriptions (server-driven) | ✅ |
| PyInstaller single-exe packaging | ✅ |

---

## Architecture

### Two-Tier Deployment

```
Operator Laptop (anywhere on LAN)
└── logviewer.exe
    └── lang/
        ├── en.json
        └── de.json

CIC / Server PC (fixed on industrial network)
└── LogDataServer.exe   (not in this repo)
```

### UDP Protocol

The client communicates using a lightweight binary UDP protocol:

- **Transport:** UDP, configurable server IP, fixed ports
- **Request packet:** 4 bytes — Command group ID (2B) + Sub-command ID (2B), little-endian
- **Reply packet:** Binary struct with header + payload, little-endian

**Implemented commands:**

| Command | Direction | Description |
|---|---|---|
| `GET_ACTIVATION_DAYS_REQ` | Client → Server | Request list of days with log data |
| `GET_ACTIVATION_DAYS_REPLY` | Server → Client | Year + monthly bitfield of active days |
| `GET_ACTIVATION_DATA_REQ` | Client → Server | Request log entries |
| `GET_ACTIVATION_DATA_REPLY` | Server → Client | SYSTEMTIME + typed log items |

**Reply data types:**

| Type | Format | Description |
|---|---|---|
| `ITEMTYPE_STRING` | UTF-16-LE, max 100 chars | Text log entries |
| `ITEMTYPE_DRIVE_FIELD` | 5 × short struct | Drive motion data (nr, upper/lower, speed, pos) |

### Target GUI Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🟢 Connected · 192.168.x.x  │  [Param] [Activation] [Drive]│
├──────────────────────────┬──────────────────────────────────┤
│  DATE EXPLORER           │  CONTENT VIEWER                  │
│  📁 2026                 │  21.04.2026 — log entry          │
│    📁 April              │  drv  OG    UG    speed  aktpos  │
│      📄 21.04.2026  ────►│    3  1000  200   120    356     │
└──────────────────────────┴──────────────────────────────────┘
│ Status: connection · category · year · root path             │
└─────────────────────────────────────────────────────────────┘
```

---

## Internationalisation (i18n)

All visible UI strings are externalised into JSON language files. No recompile needed to change or add a language.

```
lang/
├── en.json    ← English (default / master)
├── de.json    ← German
└── fr.json    ← French (added by customer, zero code change)
```

To add a new language: copy `lang/en.json`, rename to `lang/xx.json`, translate the values. Done.

---

## Project Roadmap

### ✅ Sprint 1 — UDP Communication 


### ✅ Sprint 2 — Connection Management & i18n


### ✅ Sprint 3 — Full Category Support


### ✅ Sprint 4 — GUI Integration


### ✅ Sprint 5 — Dynamic Type System


### ✅ Sprint 6 — Packaging & Release


---

## Technology Stack

| Layer | Technology |
|---|---|
| GUI Framework | PyQt6 |
| Language | Python 3.11+ |
| Networking | `socket` (UDP, stdlib) |
| Binary parsing | `struct` (stdlib) |
| i18n | JSON files (stdlib) |
| Threading | `QThread` (PyQt6) |
| Packaging | PyInstaller (planned) |

---

## Getting Started

```bash
pip install PyQt6
python itc_log_client.py
```

Start the log data server first (separate deployment).

---

## Design Principles

1. **Server owns the format** — client never hardcodes log file structure.
2. **Zero recompile for text changes** — all UI strings live in external JSON.
3. **Graceful degradation** — missing JSON key falls back to English; unreachable server shows yellow status.
4. **Thread safety** — all UDP calls on worker thread, GUI thread never blocked.
5. **Separation of concerns** — UDP module, parser, and GUI are independent.

---

## License

Private / proprietary. All rights reserved.
