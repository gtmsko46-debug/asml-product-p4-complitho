import os

import pytest

from asml_product_p4_complitho import process_window, wavelength_window
from asml_product_p4_complitho.loader import reset_loader_cache


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    monkeypatch.delenv("ASML_P4_SOLVER_PATH", raising=False)
    monkeypatch.delenv("ASML_P7_SOLVER_PATH", raising=False)
    reset_loader_cache()


def test_polarization_smoke():
    r = process_window(
        {
            "na": 0.55,
            "pitch_nm": 40.0,
            "pol_degree": 0.9,
            "pol_angle_deg": 45.0,
            "dose": 1.0,
            "defocus": 0.0,
            "blur": 0.1,
        }
    )
    assert r.pw_area > 0
    assert r.epe_nm > 0
    assert r.solver_source == "reference"


def test_wavelength_6x_not_free():
    r = wavelength_window(
        {
            "wavelength_nm": 6.7,
            "na": 0.55,
            "multilayer_R": 0.7,
            "resist_blur_nm": 2.0,
            "dose": 1.0,
            "k1_proxy": 0.5,
        }
    )
    assert r.pw_area > 0
    assert r.relative_to_135 > 0
    assert "not free" in r.note


def test_missing_key():
    with pytest.raises(KeyError):
        process_window({"na": 0.55})


def test_live_loader(tmp_path, monkeypatch):
    solver = tmp_path / "solver.py"
    solver.write_text(
        "def solve(row):\n"
        "    return {'pw_area': 42.0, 'epe_nm': 1.0}\n"
    )
    monkeypatch.setenv("ASML_P4_SOLVER_PATH", str(solver))
    reset_loader_cache()
    r = process_window(
        {
            "na": 0.55,
            "pitch_nm": 40.0,
            "pol_degree": 0.5,
            "pol_angle_deg": 0.0,
            "dose": 1.0,
            "defocus": 0.0,
            "blur": 0.0,
        }
    )
    assert r.pw_area == 42.0
    assert r.solver_source.endswith("solver.py")
