# Architecture Notes

## System Overview

The Industrial Log Viewer operates in a two-tier client-server model over a local area network (LAN) within an industrial environment.

### Tier 1: Log Data Server
- Runs on the diagnostic PC (fixed location on industrial network)
- Written in C++ for performance and direct file system access
- Reads raw log files from local disk (text and binary formats)
- Exposes a UDP interface — converts raw files into structured binary responses
- Versioned independently from the client

### Tier 2: Log Viewer Client (this repo)
- Runs on the operator laptop or any PC on the same LAN
- Written in Python/PyQt6
- Communicates with the server exclusively via UDP
- Renders server responses in a human-readable GUI
- Never touches raw log files directly

---

## Key Design Decision: Server-Described Data

The protocol is designed so the **server describes its own data structures**:

- Server can add new log types without any client update
- Future: client queries "what does type X look like?" before parsing
- Future: fully dynamic renderer driven by server-sent type descriptors

This means the client GUI is **format-agnostic** — it renders whatever the server sends, without hardcoded knowledge of file formats or struct layouts.

---

## UDP Protocol Design

### Packet Structure

**Request (client → server):**
```
Bytes 0-1: Command group ID  (USHORT, little-endian)
Bytes 2-3: Sub-command ID    (USHORT, little-endian)
```

**Reply header (server → client):**
```
Bytes 0-1: Command group ID
Bytes 2-3: Sub-command ID (reply variant)
Bytes 4+:  Payload (command-specific binary struct)
```

All multi-byte fields are **little-endian** (Windows x86 server).

---

## GUI Architecture

### Sprint 1 (current) — Standalone test client
```
MainWindow
├── QTextEdit          (output log display, monospace)
├── QPushButton × 2    (request days / request data)
├── QPushButton × 2    (clear / quit)
├── QStatusBar         (connection info + last action)
└── Worker (QThread)   (UDP send+recv, emits signal on completion)
```

### Sprint 4 (target) — Integrated log viewer
```
LogViewerWindow
├── TopBar
│   ├── ConnectionStatusDot   (green=connected, yellow=no connection)
│   ├── ServerIpInput
│   ├── CategoryTabs × 4
│   └── YearComboBox
├── QSplitter
│   ├── DateExplorer (QTreeWidget — dates from server)
│   └── ContentViewer (QTableWidget or QTextEdit)
├── QStatusBar
└── UdpClient (singleton, shared across all panels)
```

---

## Threading Model

```
Main thread (Qt event loop)
└── All GUI operations, user interactions, widget updates

Worker thread (QThread, per request)
└── UDP socket.sendto() + socket.recvfrom() — blocking up to 2s timeout
└── On success: emits done(bytes) signal → main thread parses + renders
└── On timeout: emits failed(str) signal → main thread shows error
```

GUI thread is **never blocked** regardless of network conditions.

---

## i18n Architecture

```
At startup:
  1. Detect LANG setting (config file or env var, default 'en')
  2. Load lang/{lang}.json → dict T
  3. All widgets: QPushButton(T['btn_x']), label.setText(T['lbl_x'])

Fallback chain:
  lang/{code}.json → lang/en.json → hardcoded English constant

At runtime language switch:
  1. Load new lang/{code}.json into T
  2. retranslate() updates all widget texts
  3. No restart required
```

---

## Future: Dynamic Type System

```
Client: "What is the layout of data type 5?"
Server: "Type 5 = [USHORT id, SHORT position, SHORT speed, USHORT flags]"
Client: Parses and renders any type-5 payload generically
```

This removes the last hardcoded parsing logic from the client and future-proofs it against any server-side changes.

---

## Versioning Strategy

- Client and server versions are **independent**
- New server features are **additive** (new command IDs), never breaking
- Client handles unknown command IDs gracefully (log + skip)
- Deployment: `logviewer.exe` + `lang/` folder shipped as one package to customer site
