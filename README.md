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

Use the built-in stub during development (include `reference_area_m2`, which became a required field in the latest release):

```python
from chrono_mcp_core import StructuralInput, run_structural_analysis

request = StructuralInput(
    vehicle_mass_kg=4.2,
    payload_mass_kg=0.8,
    stiffness_n_m=1800.0,
    damping_ratio=0.12,
    reference_area_m2=0.5,
)
metrics = run_structural_analysis(request)
print(metrics)
```

When you are ready to call a high-fidelity Chrono or FEM solver, swap out `run_structural_analysis` with your integration but keep the same I/O models.

### Integrating a real solver

1. Keep the `StructuralInput` / `StructuralMetrics` models as your contract.
2. Replace `chrono_mcp_core.solver.run_structural_analysis` with a wrapper that launches your Chrono job, then map the results back into `StructuralMetrics`.
3. Preserve deterministic rounding (the stub uses `round(..., 6)`) so unit tests stay stable.

## Key modules

- `chrono_mcp_core.models` - Pydantic dataclasses describing structural inputs and metrics.
- `chrono_mcp_core.solver` - deterministic stub returning stiffness/deflection/energy metrics.

Use them inside a FastAPI or python-sdk transport to produce MCP-ready services.

### Metric definitions

| Field | Units | Formula (stub) |
|-------|-------|----------------|
| `total_mass_kg` | kg | `vehicle_mass_kg + payload_mass_kg` |
| `stiffness_n_m` | N/m | input stiffness (rounded) |
| `damping_ratio` | unitless | input damping ratio (rounded) |
| `deflection_m` | m | `(total_mass * g) / stiffness` |
| `stress_pa` | Pa | `(total_mass * g) / reference_area` |
| `damping_coefficient` | N·s/m | `2 ζ sqrt(k m)` |
| `natural_frequency_hz` | Hz | `sqrt(k / m) / (2π)` |

The stub uses `g = 9.80665` (from the input) and rounds to six decimal places to guarantee determinism.

Deterministic example:

```python
from chrono_mcp_core import StructuralInput, run_structural_analysis

metrics = run_structural_analysis(
    StructuralInput(
        vehicle_mass_kg=4.0,
        payload_mass_kg=1.0,
        stiffness_n_m=1500.0,
        damping_ratio=0.08,
        gravity_m_s2=9.80665,
        reference_area_m2=0.6,
    )
)
print(metrics.model_dump())
```

Expected result:

```json
{
  "total_mass_kg": 5.0,
  "stiffness_n_m": 1500.0,
  "damping_ratio": 0.08,
  "deflection_m": 0.032689,
  "stress_pa": 81.722083,
  "damping_coefficient": 13.856406,
  "natural_frequency_hz": 2.756644
}
```
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
