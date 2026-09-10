# Lab bind — asml-product-p4-complitho

See [`SPEC.md`](SPEC.md).

| Path | Sandbox | Card |
|------|---------|------|
| P4 polarization | `labs/p4-polarization/solver.py` | `imaging-optics-v1` |
| P7 wavelength | `labs/p7-wavelength/solver.py` | `wavelength-agile-v1` |

Env: `ASML_BENCH_ROOT`, `ASML_P4_SOLVER_PATH`, `ASML_P7_SOLVER_PATH`.

Bundled `reference_solver` = lab SEED baselines (M1). Product KEEP sync only after dual-gate Critic+Repro+Diplomat.
