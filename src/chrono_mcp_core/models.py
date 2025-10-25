"""Pydantic models representing generic structural analysis inputs/outputs."""

from __future__ import annotations

from pydantic import BaseModel, Field


class StructuralInput(BaseModel):
    """Minimal set of parameters needed for the Chrono structural stub."""

    vehicle_mass_kg: float = Field(..., ge=0, description="Base vehicle mass without payload")
    payload_mass_kg: float = Field(0.0, ge=0, description="Payload mass to include in total load")
    stiffness_n_m: float = Field(
        ...,
        gt=0,
        description="Effective stiffness of the structural member",
    )
    damping_ratio: float = Field(
        ...,
        ge=0,
        le=1,
        description="Damping ratio for equivalent SDOF model",
    )
    reference_area_m2: float = Field(..., gt=0, description="Area used to compute stress")
    gravity_m_s2: float = Field(9.80665, gt=0, description="Gravity constant for the environment")


class StructuralMetrics(BaseModel):
    """Outputs produced by the simplified Chrono job runner."""

    total_mass_kg: float
    stiffness_n_m: float
    damping_ratio: float
    deflection_m: float
    stress_pa: float
    damping_coefficient: float
    natural_frequency_hz: float
