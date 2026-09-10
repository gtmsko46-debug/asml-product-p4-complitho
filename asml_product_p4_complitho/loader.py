"""Resolve live sandbox solvers from asml-bench when env is set."""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from types import ModuleType
from typing import Callable, Literal

from . import reference_solver

SolveFn = Callable[[dict], dict]
Mode = Literal["polarization", "wavelength"]

_CACHED: dict[str, tuple[str, SolveFn]] = {}


def _load_module_from_path(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load solver from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _resolve_path(mode: Mode) -> Path | None:
    env_key = (
        "ASML_P4_SOLVER_PATH" if mode == "polarization" else "ASML_P7_SOLVER_PATH"
    )
    explicit = os.environ.get(env_key)
    if explicit:
        p = Path(explicit).expanduser().resolve()
        if p.is_dir():
            p = p / "solver.py"
        return p if p.is_file() else None

    bench = os.environ.get("ASML_BENCH_ROOT")
    if bench:
        sub = "p4-polarization" if mode == "polarization" else "p7-wavelength"
        p = Path(bench).expanduser().resolve() / "labs" / sub / "solver.py"
        return p if p.is_file() else None
    return None


def get_solver(mode: Mode, *, force_reload: bool = False) -> tuple[str, SolveFn]:
    if mode in _CACHED and not force_reload:
        return _CACHED[mode]

    path = _resolve_path(mode)
    if path is not None:
        mod = _load_module_from_path(path, f"asml_p4_{mode}_sandbox")
        if not hasattr(mod, "solve"):
            raise AttributeError(f"{path} has no solve")
        _CACHED[mode] = (str(path), mod.solve)
        return _CACHED[mode]

    fn = (
        reference_solver.solve_polarization
        if mode == "polarization"
        else reference_solver.solve_wavelength
    )
    _CACHED[mode] = ("reference", fn)
    return _CACHED[mode]


def reset_loader_cache() -> None:
    _CACHED.clear()
