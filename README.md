# chrono-mcp-core - Multibody building blocks for MCP services

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB.svg" alt="Python 3.10 or newer"></a>
  <img src="https://img.shields.io/badge/status-incubating-ff9800.svg" alt="Project status: incubating">
  <img src="https://img.shields.io/badge/MCP-core-blueviolet.svg" alt="MCP core library badge">
</p>

> **TL;DR**: Reusable helpers (config loading, process management, metrics logging) for wrapping [Project Chrono](https://projectchrono.org/) in MCP services.

## Table of contents

1. [Integration highlights](#integration-highlights)
2. [Quickstart](#quickstart)
3. [Key modules](#key-modules)
4. [Stretch ideas](#stretch-ideas)
5. [Accessibility & upkeep](#accessibility--upkeep)
6. [Contributing](#contributing)

## Integration highlights

| Persona | Immediate value | Longer-term payoff |
|---------|-----------------|--------------------|
| **Service authors** | Ready-made config loaders and logging helpers for Chrono simulations. | Consistent archives and metadata across MCP services. |
| **Tooling teams** | Typed dataclasses for request/response payloads. | Makes it easy to reuse the same MCP layer in other multibody solvers.

## Quickstart

```bash
uv pip install "git+https://github.com/Three-Little-Birds/chrono-mcp-core.git"
```

Inspect the examples under `examples/` to see how to launch Chrono jobs and capture metrics.

## Key modules

- `chrono_mcp_core.config` - discover solver paths, activate environments.
- `chrono_mcp_core.runner` - spawn Chrono jobs with timeout + archive logic.
- `chrono_mcp_core.metrics` - standardise JSON metrics for the Continuous Evidence Engine.

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
