# asml-product-p4-complitho — Product Spec (M0)

**Parent:** asml-bench [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Applications-recognizable process-window / EPE toys that treat polarization and wavelength as first-class imaging inputs (P4 + P7 share this product).

## Public API (target)
```python
from asml_product_p4_complitho import process_window, epe_report
report = process_window(source_pol=..., wavelength_nm=..., mask=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p4-polarization/solver.py (+ labs/p7-wavelength/solver.py)` |
| Frozen eval | frozen labs/p4-polarization/eval.py and labs/p7-wavelength/eval.py (product may AND both) |
| Assumption card | `polarization-pw-v1 / wavelength-agile-v1` |
| Dual-gate | dual-gate product SEED then KEEP; Critic forbids unconstrained MLP-only fits |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.
