# asml-product-p4-complitho

**Applications-recognizable process-window / EPE toys that treat polarization and wavelength as first-class imaging inputs (P4 + P7 share this product).**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`labs/p4-polarization/solver.py (+ labs/p7-wavelength/solver.py)`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
