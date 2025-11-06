# chrono-mcp-core - Multibody building blocks for MCP services

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB.svg" alt="Python 3.10 or newer"></a>
  <img src="https://img.shields.io/badge/MCP-core-blueviolet.svg" alt="MCP core library badge">
</p>

> **TL;DR**: Reusable input/output models plus a deterministic structural stub that MCP services can share while you wire in [Project Chrono](https://projectchrono.org/) or other multibody solvers.

## Table of contents

1. [What it provides](#what-it-provides)
2. [Quickstart](#quickstart)
3. [Key modules](#key-modules)
4. [Stretch ideas](#stretch-ideas)
5. [Accessibility & upkeep](#accessibility--upkeep)
6. [Contributing](#contributing)

## What it provides

| Scenario | Value |
|----------|-------|
| Shared schema | `StructuralInput` / `StructuralMetrics` dataclasses so multiple services agree on requests and responses. |
| Deterministic stub | `run_structural_analysis` delivers consistent metrics without Chrono – ideal for unit tests and CI. |
| Drop-in hook | Replace the stub with real Chrono calls while preserving the response schema.

## Quickstart

```bash
uv pip install "git+https://github.com/Three-Little-Birds/chrono-mcp-core.git"
```

Use the built-in stub during development:

```python
from chrono_mcp_core import StructuralInput, run_structural_analysis

request = StructuralInput(
    vehicle_mass_kg=4.2,
    payload_mass_kg=0.8,
    stiffness_n_m=1800.0,
    damping_ratio=0.12,
)
metrics = run_structural_analysis(request)
print(metrics)
```

When you are ready to call a high-fidelity Chrono or FEM solver, swap out `run_structural_analysis` with your integration but keep the same I/O models.

## Key modules

- `chrono_mcp_core.models` - Pydantic dataclasses describing structural inputs and metrics.
- `chrono_mcp_core.solver` - deterministic stub returning stiffness/deflection/energy metrics.

Use them inside a FastAPI or python-sdk transport to produce MCP-ready services.

## Stretch ideas

1. Extend the metrics schema to include fatigue/deflection data for structural dashboards.
2. Add container discovery helpers similar to the diffSPH stack.
3. Contribute a Chrono smoke test script for CI parity with other solvers.

## Accessibility & upkeep

- Keep the badge set short and give each badge alt text so screen readers announce status clearly.
- Tests run via `uv run pytest`; feel free to add more stubs to grow coverage.
- Keep configuration defaults in sync with the consuming services (`mcp_chrono`).

## Contributing

1. `uv pip install --system -e .[dev]`
2. `uv run ruff check .` & `uv run pytest`
3. Document new helpers in the README so downstream services know what changed.

MIT license - see [LICENSE](LICENSE).
