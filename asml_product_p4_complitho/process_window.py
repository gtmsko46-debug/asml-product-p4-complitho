"""Champion-facing process-window / EPE API (P4 polarization + P7 wavelength)."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

from .loader import get_solver

ASSUMPTION_CARD_P4 = "imaging-optics-v1"
ASSUMPTION_CARD_P7 = "wavelength-agile-v1"

_P4_KEYS = ("na", "pitch_nm", "pol_degree", "pol_angle_deg", "dose", "defocus", "blur")
_P7_KEYS = (
    "wavelength_nm",
    "na",
    "multilayer_R",
    "resist_blur_nm",
    "dose",
    "k1_proxy",
)


@dataclass
class PolarizationReport:
    pw_area: float
    epe_nm: float
    assumption_card_id: str = ASSUMPTION_CARD_P4
    solver_source: str = "reference"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WavelengthReport:
    pw_area: float
    relative_to_135: float
    assumption_card_id: str = ASSUMPTION_CARD_P7
    solver_source: str = "reference"
    note: str = "6.7 nm is not free — multilayer + resist penalties apply"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def process_window(row: Mapping[str, Any]) -> PolarizationReport:
    """P4 polarization-aware process-window + EPE proxy."""
    for key in _P4_KEYS:
        if key not in row:
            raise KeyError(f"missing required field: {key}")
    source, fn = get_solver("polarization")
    out = fn(dict(row))
    return PolarizationReport(
        pw_area=float(out["pw_area"]),
        epe_nm=float(out["epe_nm"]),
        solver_source=source,
    )


def wavelength_window(row: Mapping[str, Any]) -> WavelengthReport:
    """P7 wavelength-agile process-window vs matched 13.5 nm reference."""
    for key in _P7_KEYS:
        if key not in row:
            raise KeyError(f"missing required field: {key}")
    source, fn = get_solver("wavelength")
    out = fn(dict(row))
    return WavelengthReport(
        pw_area=float(out["pw_area"]),
        relative_to_135=float(out["relative_to_135"]),
        solver_source=source,
    )
