# Changelog

All notable changes are documented here following the keep-a-changelog style and Semantic Versioning.

---

## [5.1.0]

### Added
- Dynamic schema engine — runtime schema negotiation via description request/reply protocol; no hardcoded data structures.
- Schema filter dialog — user can choose which fields to display per data type.
- Generic record decoder — single decoder handles all current and future data categories using runtime descriptors.
- Schema registry — in-memory cache of server-declared field descriptors, populated at startup.
- 15-second connection probe — periodic background health check with automatic LED state update.
- Activation data pipeline — full request/reply cycle for activation events including Aktiv/Inaktiv status labeling.
- Benutzername field detection — operator name and action status rendered per event.
- Category tab architecture — all four log categories in place; dynamic, programming, error categories engine-ready.

### Changed
- Parser is fully data-driven from server-declared field descriptors.
- Data request padded to 60 bytes as per protocol specification.
- Connection label shows localized "Connected" / "No connection" strings.

### Fixed
- UDP port reuse on rapid GUI restart.
- Schema not reloaded on language change.

### Known Limitations
- Categories for drive data, programming logs, and drive errors: parsing engine ready, GUI activation pending final server command specification.

---

## [5.0.0]

### Added
- Full activation data category (days request plus data request pipeline).
- Calendar bitfield parser for year/month/day discovery.
- QThread worker model — all network I/O off the GUI thread.
- Dark industrial theme (PyQt6 custom stylesheet).

### Changed
- Replaced prototype static parser with structured binary decoder.

---

## [4.0.0]

### Added
- All four category tabs: activation, programming, drive data, drive errors.
- Pult selector dropdown.
- Year selector input.
- Hierarchical date tree explorer (year → month → day).
- Category-colour accent system.

---

## [3.0.0]

### Added
- Connection status LED (green / yellow / red).
- Periodic connectivity probe.
- Internationalisation framework — runtime language switching via `lang/*.json`.
- German and English language packs.
- Language combo in top bar.

---

## [2.0.0]

### Added
- Worker thread (QThread) for non-blocking UDP requests.
- Status bar with request and reply statistics.
- Save log to file (export).
- Clear log button.

---

## [1.0.0]

### Added
- Initial UDP client skeleton.
- Basic PyQt6 window.
- Days request/reply parser.
- String item parser (UTF-16-LE).
- Hardcoded drive-field struct parser (5 × short).