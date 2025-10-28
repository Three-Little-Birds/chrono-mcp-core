# chrono-mcp-core

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-brightgreen.svg)](pyproject.toml)
[![CI](https://github.com/yevheniikravchuk/chrono-mcp-core/actions/workflows/ci.yml/badge.svg)](https://github.com/yevheniikravchuk/chrono-mcp-core/actions/workflows/ci.yml)

Reusable, domain-neutral Python toolkit for building [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) services around [Project Chrono](https://projectchrono.org/) structural simulations.

## Features

- Pydantic models (`StructuralInput`, `StructuralMetrics`) that describe structural load cases in a tooling-friendly way.
- Deterministic reference solver (`run_structural_analysis`) suitable for unit testing, stubs, or environments without Chrono installed.
- MIT-licensed, type hinted package that drops cleanly into MCP servers built with the [python-sdk](https://github.com/modelcontextprotocol/python-sdk).

## Installation

Install directly from GitHub until a PyPI release is available:

```bash
pip install "git+https://github.com/yevheniikravchuk/chrono-mcp-core.git"
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

### Quickstart (MCP integration)

```python
from mcp.server.fastmcp import FastMCP
from chrono_mcp_core import StructuralInput, run_structural_analysis

mcp = FastMCP("chrono-mcp", "Chrono structural analysis")

@mcp.tool()
def solve(request: StructuralInput):
    return run_structural_analysis(request)

if __name__ == "__main__":
    mcp.run()
```

Run the tool using the MCP CLI:

```bash
uv run mcp dev examples/chrono_tool.py
```

## Local development

Prerequisites:

- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv)

```bash
uv pip install --system -e ".[dev]"
uv run ruff check .
uv run pytest
```

## Repository structure

```
chrono-mcp-core/
├── src/chrono_mcp_core/
├── tests/
├── pyproject.toml
└── .github/workflows/ci.yml
```

## License

Released under the MIT License. See [LICENSE](LICENSE).

## Support

Open an issue or submit a pull request with improvements. Please include tests and documentation updates where appropriate.
