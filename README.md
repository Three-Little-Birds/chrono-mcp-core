# chrono-mcp-core

Reusable Python toolkit for building MCP (Model Context Protocol) services around [Project Chrono](https://projectchrono.org/) structural simulations.

## Features

- Lightweight Pydantic models (`StructuralInput`, `StructuralMetrics`) for describing structural load cases.
- Deterministic reference solver (`run_structural_analysis`) for unit tests and stub deployments.
- Utility module intended to be replaced or extended with high-fidelity Chrono calls in production.
- MIT-licensed, type hinted, and packaged with `uv`-friendly metadata.

## Installation

```bash
pip install chrono-mcp-core
```

## Usage

```python
from chrono_mcp_core import StructuralInput, run_structural_analysis

config = StructuralInput(
    vehicle_mass_kg=0.45,
    payload_mass_kg=0.05,
    stiffness_n_m=1800.0,
    damping_ratio=0.2,
    reference_area_m2=0.12,
    gravity_m_s2=9.80665,
)

metrics = run_structural_analysis(config)
print(metrics.deflection_m)
```

## Local development

Prerequisites:

- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`

```bash
uv pip install --system -e .[dev]
uv run pytest
uv run ruff check .
```

## Repository structure

```
chrono-mcp-core/
├── src/chrono_mcp_core/        # Library source
├── tests/                      # Pytest-based regression tests
├── pyproject.toml              # Build metadata
└── .github/workflows/ci.yml    # Lint + test automation
```

## License

Released under the MIT License. See [LICENSE](LICENSE).
