# Product Vision

## Problem Statement

Industrial control systems generate high-volume operational data across multiple domains:

- Configuration and programming logs
- Activation and deactivation events
- Dynamic per-cycle process/drive data
- Drive and actuator fault events
- System messages and operator comments

Traditional diagnostic tools solve this with **hardcoded parsers** — a separate rigid binary struct per log type. Every firmware revision requires a client rebuild. New fields are invisible until a developer updates the code.

## Vision

Build a flexible analytics layer that **learns its own data layout at runtime**. The server declares the schema. The client adapts. New log categories, new fields, new versions — zero client rebuild required.

Long-term: evolve from a passive log viewer into an **active industrial intelligence platform** — surfacing anomalies, generating summaries, and predicting failure modes from structured telemetry.

## Target Users

| Role | Use Case |
|---|---|
| Service / commissioning engineers | Diagnose activation sequences and drive errors on-site |
| Embedded software developers | Validate firmware changes against log output |
| Maintenance teams | Track fault recurrence and drive health over time |
| QA / validation engineers | Verify correct behavior against specification |
| System integrators | Configure and verify multi-system deployments |

## Value Propositions

1. **Zero rebuild on schema change** — server declares layout, client adapts at runtime
2. **Single tool for all log categories** — one deployment, all data types
3. **Operator-friendly interface** — named fields, not hex dumps
4. **AI-ready data structure** — every record is fully typed at decode time
5. **Audit trail** — session export for traceability and reporting

## Product Principles

1. Schema-driven, never hardcoded
2. Modular by log domain
3. Graceful degradation when schema is missing
4. Thread-safe and non-blocking UI
5. Internationalised from day one
6. Safe for deployment without Python/Qt knowledge
