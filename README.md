# asml-product-p4-complitho

**Applications-recognizable process-window / EPE** with polarization and wavelength as first-class imaging inputs (P4 + P7).

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47) |
| Stage | **M1 package** (SEED reference — not product KEEP) |
| Labs | `labs/p4-polarization/`, `labs/p7-wavelength/` |

```bash
pip install -e '.[dev]'
pytest
python examples/smoke_import.py
```

```python
from asml_product_p4_complitho import process_window, wavelength_window

pol = process_window({...})   # pw_area, epe_nm
wav = wavelength_window({...})  # pw_area, relative_to_135 (6.7 not free)
```

Live weights: set `ASML_BENCH_ROOT` or `ASML_P4_SOLVER_PATH` / `ASML_P7_SOLVER_PATH`.
Hill-climbs only via Foreman→Operator on bench sandboxes. Dual-gate product tickets after bay frees from P1 deepen ∥ P2.
