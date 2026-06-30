# fabric-protocol

Canonical wire contracts for the AceTeam Sovereign Compute Fabric — the single
source of truth for messages that cross the **node ↔ control-plane** boundary.

Consumed by:
- **citadel-cli** (Go) — `gen/go`
- **aceteam** python-backend worker (Python) — `gen/python`
- **aceteam** Next.js (TypeScript) — `gen/ts`

Before this repo, each language hand-maintained its own struct/Pydantic/Zod
mirror of these messages — three copies that silently drift. This repo makes the
`.proto` authoritative and generates the rest.

## Layout

```
proto/aceteam/fabric/v1/
  node_state.proto      # citadel#353 reconcile: DesiredState / ActualState (binary on the wire)
  node_activity.proto   # citadel#294 / aceteam#4139 activity telemetry (documents existing JSON transport)
gen/{go,python,ts}/     # generated, committed so consumers can `go get` / import without a build step
```

## Versioning

`protocol_version` on each envelope mirrors `FabricProtocolVersion` (citadel-cli
`internal/protocol/protocol.go`, aceteam #363). Bump that constant on any
breaking change; `buf breaking` guards it in CI.

## Codegen

```bash
buf lint
buf generate          # writes gen/{go,python,ts}
buf breaking --against '.git#branch=main'
```

CI runs all three on every PR; `gen/` is committed so downstream repos consume
generated code directly (vendored), no build-time protoc dependency.
