# asml-product-p4-complitho — Product Spec

**Parent:** asml-bench [#47](https://github.com/gtmsko46-debug/asml-bench/issues/47)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Applications-recognizable process-window / EPE that treat polarization and wavelength as first-class imaging inputs (P4 + P7 share this product).

## Public API
```python
from asml_product_p4_complitho import process_window, wavelength_window

pol = process_window({
    "na": 0.55, "pitch_nm": 40.0, "pol_degree": 0.9, "pol_angle_deg": 45.0,
    "dose": 1.0, "defocus": 0.0, "blur": 0.1,
})  # -> PolarizationReport (pw_area, epe_nm)

wav = wavelength_window({
    "wavelength_nm": 6.7, "na": 0.55, "multilayer_R": 0.7,
    "resist_blur_nm": 2.0, "dose": 1.0, "k1_proxy": 0.5,
})  # -> WavelengthReport (pw_area, relative_to_135); 6.7 is not free
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p4-polarization/solver.py` + `labs/p7-wavelength/solver.py` |
| Frozen eval | `labs/p4-polarization/eval.py` and `labs/p7-wavelength/eval.py` |
| Assumption cards | P4: `imaging-optics-v1` · P7: `wavelength-agile-v1` (companion `stochastics-resist-v1` for blur narrative) |
| Dual-gate | product SEED then KEEP; Critic forbids unconstrained MLP-only fits |
| HOLDOUT | pin when EI freezes; no eval edits by solvers |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_solver` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. [x] **M0 Spec**
2. [x] **M1 Package** — `process_window` + `wavelength_window` (PR #2)
3. [ ] **M2 Dual-gate** — drafts offline (`tickets/M2-dual-gate-DRAFT.md`); file when CoS frees bay after 1026∥1030
4. [ ] **M3 Ship** — `reference_solver` sync + ship-queue Issue close

## Bay
No Operator steal while P1 deepen / P2 HT-1030 run. Spec/docs/M1 offline OK.
