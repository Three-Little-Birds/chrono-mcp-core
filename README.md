# chrono-mcp-core · A Classroom Core for Project Chrono MCP Integrations

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-brightgreen.svg)](pyproject.toml)
[![CI](https://github.com/Three-Little-Birds/chrono-mcp-core/actions/workflows/ci.yml/badge.svg)](https://github.com/Three-Little-Birds/chrono-mcp-core/actions/workflows/ci.yml)

`chrono-mcp-core` packages a small, well-documented scaffold for running [Project Chrono](https://projectchrono.org/) structural analyses inside Model Context Protocol services. It also ships with a deterministic reference solver so learners can explore the API without installing Chrono.

## What you will practice

- Describe a structural load case with strongly typed models.
- Run the reference solver to understand the expected outputs.
- Wrap the helper in an MCP tool or FastAPI endpoint to share with your agent.

## Step 1 – Install the helper

```bash
uv pip install "git+https://github.com/Three-Little-Birds/chrono-mcp-core.git"
```

## Step 2 – Define a structural scenario

```python
from chrono_mcp_core import StructuralInput, run_structural_analysis

case = StructuralInput(
    vehicle_mass_kg=0.45,
    payload_mass_kg=0.05,
    stiffness_n_m=1800.0,
    damping_ratio=0.2,
    reference_area_m2=0.12,
    gravity_m_s2=9.80665,
)

metrics = run_structural_analysis(case)
print(metrics.deflection_m, metrics.stress_pa)
```

The default implementation uses a simplified mass-spring-damper model. When you integrate real Chrono simulations, import this package and swap the solver for your project-specific logic while keeping the same request/response types.

## Step 3 – Expose through MCP

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

Agents can now ask questions like “what is the deflection if payload doubles?” by tweaking payload mass in the request.

## Going further

- **Swap the solver:** drop your Chrono invocation into a function with the same signature as `run_structural_analysis`.
- **Add validation:** extend `StructuralInput` with custom validators for project-specific constraints.
- **Log experiments:** store the returned metrics alongside impact events or CFD data for a richer dataset.

## Development

```bash
uv pip install --system -e .[dev]
uv run ruff check .
uv run pytest
```

Tests use the deterministic solver, making it easy to understand the math behind the responses.

## License

MIT — see [LICENSE](LICENSE).
