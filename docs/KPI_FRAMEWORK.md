# KPI Framework

This document defines the key performance indicators (KPIs) for the Industrial Log Intelligence Platform across three domains: operational diagnostics, engineering quality, and product adoption.

---

## Operational KPIs

These KPIs measure value delivered to engineers using the tool.

| KPI | Description | Target |
|---|---|---|
| Daily activation event count | Number of activation/deactivation events per day | Trending baseline |
| Fault events per operating period | Number of drive errors in a session window | ↓ over time |
| Fault recurrence rate | Frequency of the same fault code repeating | < 5% |
| Mean time between faults | Average time between consecutive drive error events | ↑ over time |
| Configuration change count | Number of programming/parameter actions per session | Tracked |
| User action count | Total operator-triggered activations per day | Tracked |
| Time-to-locate-event | Time from opening the tool to finding the relevant log entry | < 60s |

---

## Engineering / Platform KPIs

These KPIs measure the health of the platform itself.

| KPI | Description | Target |
|---|---|---|
| Schema adaptation latency | Time from startup to schema loaded and usable | < 1s |
| Decode accuracy | Byte-for-byte match against reference server output | 100% |
| UI freeze events | GUI thread blocks during network operation | 0 |
| Client rebuilds per schema change | How often a new .exe is needed after server schema update | 0 |
| Connection recovery detection | Time to detect CIC connection loss / restore | ≤ 15s |
| Parse success rate | % of received records successfully decoded | > 99% |
| Unsupported record count | Records with unknown itemtyp received | 0 expected |
| Timeout rate | % of requests that exceed timeout threshold | < 1% |
| Crash-free sessions | % of sessions without unhandled exceptions | > 99% |
| Distributable size | Final packaged .exe size | ~20–36 MB |

---

## Product / Adoption KPIs

These KPIs measure how the product is used and where to invest next.

| KPI | Description |
|---|---|
| Category adoption | Which log categories users open most frequently |
| Export / report usage | How often users save sessions to file |
| Schema filter usage | How often users customise visible fields |
| Language preference distribution | DE vs EN vs other |
| Session duration | Average time spent in an analysis session |
| Date tree depth | How far users drill into the date hierarchy |

---

## Future AI/ML KPIs

| KPI | Description |
|---|---|
| Anomaly detection precision | % of flagged anomalies confirmed relevant by engineer |
| Auto-summary acceptance rate | % of AI summaries used without modification |
| Root-cause suggestion accuracy | % of top-1 suggestions matching confirmed root cause |
| Natural-language query success rate | % of NL queries returning useful results |
