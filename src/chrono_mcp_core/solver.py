"""Deterministic structural metrics used by the Chrono MCP stub."""

from __future__ import annotations

import math

from .models import StructuralInput, StructuralMetrics


def run_structural_analysis(config: StructuralInput) -> StructuralMetrics:
    """Compute simplified structural response metrics.

    This is deliberately lightweight so it can run without a full Chrono installation
    during unit tests. Projects embedding the core package can replace this logic
    with high-fidelity Chrono calls while keeping the same input/output schema.
    """

    total_mass = config.vehicle_mass_kg + config.payload_mass_kg
    deflection = (total_mass * config.gravity_m_s2) / config.stiffness_n_m
    stress = (total_mass * config.gravity_m_s2) / config.reference_area_m2
    damping_coeff = (
        2.0 * config.damping_ratio * math.sqrt(config.stiffness_n_m * max(total_mass, 1e-6))
    )
    natural_freq = math.sqrt(config.stiffness_n_m / max(total_mass, 1e-6)) / (2 * math.pi)

    return StructuralMetrics(
        total_mass_kg=round(total_mass, 6),
        stiffness_n_m=round(config.stiffness_n_m, 6),
        damping_ratio=round(config.damping_ratio, 6),
        deflection_m=round(deflection, 6),
        stress_pa=round(stress, 6),
        damping_coefficient=round(damping_coeff, 6),
        natural_frequency_hz=round(natural_freq, 6),
    )
