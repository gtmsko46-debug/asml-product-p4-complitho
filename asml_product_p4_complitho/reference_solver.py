"""SEED reference solvers — baseline lab solvers at M1 (not product KEEP).

Polarization path mirrors labs/p4-polarization/solver.py.
Wavelength path mirrors labs/p7-wavelength/solver.py.
Harness hill-climbs edit bench sandbox only; sync here after dual-KEEP.
"""
from __future__ import annotations

import math


def solve_polarization(row: dict) -> dict:
    na = float(row["na"])
    pitch_nm = float(row["pitch_nm"])
    pol_degree = float(row["pol_degree"])
    pol_angle_deg = float(row["pol_angle_deg"])
    dose = float(row["dose"])
    defocus = float(row["defocus"])
    blur = float(row["blur"])

    contrast = (
        0.38
        + 0.33 * pol_degree * abs(math.sin(2.0 * math.radians(pol_angle_deg)))
        + 0.14 * (na / 0.55)
    )
    pw_area = contrast * dose / (1.0 + 0.55 * blur + 0.28 * abs(defocus)) * (pitch_nm / 40.0)
    epe_nm = 2.6 / max(contrast, 0.1) + 0.75 * abs(defocus) + 0.22 * blur
    return {"pw_area": float(pw_area), "epe_nm": float(epe_nm)}


def solve_wavelength(row: dict) -> dict:
    wavelength_nm = float(row["wavelength_nm"])
    na = float(row["na"])
    multilayer_R = float(row["multilayer_R"])
    resist_blur_nm = float(row["resist_blur_nm"])
    dose = float(row["dose"])
    k1_proxy = float(row["k1_proxy"])

    if wavelength_nm >= 13.0:
        optics_penalty = 1.0
    else:
        optics_penalty = 0.52 + 0.48 * multilayer_R
    resist_penalty = 1.0 + 0.085 * resist_blur_nm * (13.5 / wavelength_nm)
    pw_area = (dose * k1_proxy * na * optics_penalty) / resist_penalty
    pw135 = (dose * k1_proxy * na * 1.0) / (1.0 + 0.085 * resist_blur_nm)
    relative_to_135 = pw_area / max(pw135, 1e-9)
    return {"pw_area": float(pw_area), "relative_to_135": float(relative_to_135)}
