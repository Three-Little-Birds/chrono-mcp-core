from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from chrono_mcp_core import StructuralInput, run_structural_analysis


def test_run_structural_analysis_produces_positive_deflection() -> None:
    config = StructuralInput(
        vehicle_mass_kg=0.45,
        payload_mass_kg=0.05,
        stiffness_n_m=1800.0,
        damping_ratio=0.2,
        reference_area_m2=0.12,
        gravity_m_s2=9.80665,
    )

    metrics = run_structural_analysis(config)

    assert metrics.total_mass_kg == 0.5
    assert metrics.deflection_m > 0.0
    assert metrics.natural_frequency_hz > 0.0
