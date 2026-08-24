# Company / Repository Authority Map

This document owns the current institutional relationship among the company's active repositories. It does not replace Product authority inside those repositories.

## Current topology

```text
company / working brand
        │
        ▼
   conexus-hq
institutional authority
        │
        ├────────────── portfolio direction ──────────────┐
        │                                                 │
        ▼                                                 ▼
   conexus-os                                          products
platform Product authority                     MetalDocs / marketplace-central
        │                                                 │
        └──────── future governed convergence ────────────┘

conexus-methodology
        └── organizational engineering reasoning + repository operating standard
```

## Repository roles

| Repository | Authority | Does not own |
| --- | --- | --- |
| `developmentconexus-ops/conexus-hq` | company strategy, portfolio direction, brand/naming, institutional governance | Product domain semantics, Product technical architecture, engineering methodology |
| `developmentconexus-ops/conexus-methodology` | engineering reasoning method and repository operating standard | company strategy or Product semantics |
| `developmentconexus-ops/conexus-os` | platform Product meaning and architecture | MetalDocs/Marketplace domain meaning by convenience; final company brand naming |
| `developmentconexus-ops/MetalDocs` | controlled-document Product meaning and architecture | company strategy or generic platform authority |
| `developmentconexus-ops/marketplace-central` | marketplace operations + commercial-intelligence Product meaning and architecture | company strategy or generic platform authority |

## Convergence law

The strategic direction is one coherent company platform, not a permanent collection of unrelated products. MetalDocs and Marketplace Central are being matured independently because the target platform is not yet ready to host them safely.

Future convergence may include shared identity, navigation, Brain context, Connections, governed capabilities, Builder/Paved Road, Product Agents, release/runtime machinery, and a unified user experience **only where the owning Product and platform authorities explicitly admit it**.

Convergence does not imply:

```text
copying MetalDocs semantics into Conexus OS
copying Marketplace semantics into Conexus OS
one giant domain model
premature source-code migration
one database/schema by default
a product name or brand decision
```

A platform mechanism may be shared without becoming the semantic owner of every domain that uses it.

## Naming

All names in this map are current engineering/project identifiers. `Conexus` and `Conexus OS` remain working names pending the later brand/naming gates.
