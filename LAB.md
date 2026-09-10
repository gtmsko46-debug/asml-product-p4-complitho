# Lab bind — asml-product-p4-complitho

See [`SPEC.md`](SPEC.md).

- **Sandbox:** `labs/p4-polarization/solver.py (+ labs/p7-wavelength/solver.py)`
- **Eval:** frozen labs/p4-polarization/eval.py and labs/p7-wavelength/eval.py (product may AND both)
- **Card:** `polarization-pw-v1 / wavelength-agile-v1`
- **Dual-gate:** dual-gate product SEED then KEEP; Critic forbids unconstrained MLP-only fits

Live weights: `ASML_BENCH_ROOT` / product-specific override env (set at M1).
