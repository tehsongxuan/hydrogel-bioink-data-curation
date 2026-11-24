# Phase 3 — Standardisation and quality checks

[← Back to project README](../../README.md)

- Notebook: [`notebooks/03_standardisation_and_quality_checks.ipynb`](../../notebooks/03_standardisation_and_quality_checks.ipynb)
- Executed report: [`reports/03_standardisation_and_quality_checks.html`](../../reports/03_standardisation_and_quality_checks.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/03_standardisation_and_quality_checks.html)

## Scope and method

**Question:** Can equivalent information be represented consistently without losing the original evidence?
Standardize field names, labels, types, and units only where meaning is clear. Keep original values and units alongside standardized values, units, and conversion rules. Do not convert an ambiguous unit by guessing. Distinguish zero from not measured, not reported, not applicable, unknown, and unavailable.
Validate required fields, ID uniqueness, foreign keys, duplicate records, numeric types, row counts, unit consistency, and scientifically justified ranges. Treat range checks as flags for review, not automatic correction. Keep a decision trail in the issue log.
**Data-science concept:** executable checks make assumptions repeatable and expose violations. Passing checks does not prove that a scientific relationship is true. **Polymer concept:** `G′` in pascals and viscosity in pascal-seconds describe different properties; even equal units do not ensure comparability if frequency or temperature differs.
**Output and handoff:** standardized tables, validation summary, and transformation lineage. Their verified identifiers support Phase 4. Exit when transformations are reproducible and unresolved problems remain visible.

## Phase 3 implementation status

The original Phase 3 scope above is retained in full. The executed `03_standardisation_and_quality_checks.ipynb` implements a production standardisation-and-quality-control layer on top of the verified Phase 2 checkpoint. It does not rebuild Phases 1 or 2, does not infer physical sample identity, and does not treat successful software joins as proof of experimental relationships.
The implemented scope includes:
- content-addressed discovery and SHA-256 verification of the raw source files, Phase 1 checkpoint, Phase 2 manifest and all 26 Phase 2 exports;
- runtime recording for Python, pandas, NumPy, openpyxl and IPython;
- exact reconciliation of source coordinates against the original rheology ZIP;
- a 13-rule transformation register tied to the observed Phase 2 source-header mapping;
- source-preserving standardisation of supported numerical quantities;
- percent-to-fraction strain conversion only where the source explicitly uses `%`;
- retention of source-labelled fractional strain without clipping or reinterpretation;
- explicit deferral of `mPas` viscosity conversion because the raw unit token remains insufficiently defined;
- conservative image-metadata handling in which blanks remain `unknown_blank`;
- lossless ISO date-format standardisation for all 1,031 valid source dates without assigning an event meaning;
- carry-forward of all 24 Phase 2 QC finding records plus one Phase 3 document-range review finding;
- source-coordinate links between QC findings and affected observations;
- an observation-preserving 4,600-row point view that keeps rheological acquisition conditions attached;
- deterministic export of 13 CSV tables plus one JSON run manifest; and
- a final preservation check confirming that the protected inputs remained byte-identical.

The notebook is designed for the lifecycle **save → close Jupyter → reopen Jupyter → Restart Kernel → Run All → complete from top to bottom**. Browser-added filename suffixes can be tolerated only when the file bytes match the hashes recorded in the controlled manifests. Scientific identity is therefore established by content rather than by a convenient filename alone.

## Phase 3 verified results and scientific interpretation

| Phase 3 item | Verified result | Interpretation |
|---|---|---|
| Controlled input verification | 41 hash-pinned dependencies resolved and recorded | The Phase 3 run is tied to the raw source snapshot plus the complete Phase 1 and Phase 2 checkpoints rather than to similarly named files |
| Runtime environment | Python 3.12.15; pandas 2.2.3; NumPy 1.26.4; openpyxl 3.1.5; IPython 9.17.1 | Matches the scientific Python stack used by the preceding checkpoint |
| Source worksheets | 92 retained | Digital source records; not 92 independent physical samples |
| Measurement points | 4,600 retained | Nested observations within source worksheets |
| Source measurement cells | 39,100 retained | Original Phase 2 cell-level evidence remains available alongside Phase 3 standardisation fields |
| Image-index records | 1,031 retained | Source metadata records; not automatically formulations, physical samples or validated print-quality outcomes |
| Transformation rules | 13 | One explicit rule per observed rheology source header in the verified mapping |
| Strain cells | 2,300 total: 2,200 source-labelled fractions and 100 source-labelled percentages | Explicit percentages are divided by 100; source-labelled fractions are preserved without clipping |
| Viscosity conversion | 4,600 viscosity cells retained with unresolved `mPas` semantics | No unsupported Pa·s conversion is manufactured |
| Image date format | 1,031 dates standardised losslessly to an additional ISO representation | Format is harmonised without inferring whether the date represents printing, imaging or another event |
| Image missingness | `completeness_sam`: 943 blanks; `contain_sps`: 922 blanks | Blank remains unknown rather than being converted to yes, no, zero, success or reagent absence |
| QC finding records | 25 | The original 24 Phase 2 findings remain visible and one Phase 3 document-range review finding is added |
| QC observation links | 2,302 | Provenance associations between findings and affected source coordinates; not 2,302 samples or independent findings |
| Unresolved review items | 4 | Viscosity notation, LVR selection, publication-range difference and modelling-population reconciliation remain open |
| Phase 3 validation checks | 674 passed | The implemented integrity, transformation, preservation and export contracts passed in the submitted run |
| Phase 3 exports | 13 CSV files plus 1 JSON run manifest | Reproducible local handoff to Phase 4 |
| Physical-sample linkage | Unresolved | No physical-sample, replicate, formulation, printing or rheology-to-image identity is asserted |
| Model readiness | Not established | Passing structural and standardisation checks is not evidence that the data support a leakage-safe predictive model |

### Data-science rationale

**Content-addressed provenance.** Phase 3 accepts controlled inputs by their recorded SHA-256 content rather than trusting a filename alone. This allows a browser-suffixed local copy to be recognised only when it is byte-identical to the expected checkpoint and rejects altered similarly named files.
**Source-preserving transformation.** `measurement_values_standardised.csv` retains every original Phase 2 measurement-value column and adds canonical-field, rule, evidence, standardised-value, standardised-unit and transformation-status fields. A standardised representation therefore does not erase the source scalar, source unit or exact source coordinate.
**Validation versus cleaning.** The workflow tests rules without silently repairing the source. A QC finding remains a review signal. Flagged values are not automatically deleted, clipped, imputed, winsorised or replaced.
**Measurement hierarchy and pseudoreplication.** The 39,100 source cells are nested within 4,600 measurement points and 92 source worksheets. They are not 39,100 independent materials. Preserving this hierarchy is necessary before later summaries, record linkage or model validation.
**Missingness semantics.** Blank image annotations remain observed unknowns. Structural absence, a literal source token, a numeric zero and a deferred transformation are represented differently so later analysis does not manufacture labels from missing metadata.
**Idempotence and reproducibility.** The notebook recreates its named Phase 3 outputs from verified upstream inputs and does not append duplicate records on rerun. The run timestamp may change; the scientific content should remain logically stable for the same controlled inputs.

### Polymer, hydrogel and rheology interpretation

**Strain.** Strain is dimensionless but may be represented as a fraction or percentage. A 1% strain corresponds to a fraction of 0.01. Phase 3 divides by 100 only where the source explicitly labels strain as `%`, and a round-trip check verifies the arithmetic. The source-labelled `ɣ in -` values are retained rather than reinterpreted solely because some values appear unusual.
**Storage and loss moduli.** `G′` represents the elastic contribution and `G″` the viscous/dissipative contribution under the recorded oscillatory conditions. Standardising their representation does not establish gelation, an LVR, printability or equivalence across experiments.
**Viscosity quantities.** Apparent steady-shear viscosity and oscillatory complex-viscosity magnitude `|η*|` remain separate observables. The source token `mPas` is retained because the reviewed evidence does not define the raw export notation strongly enough to approve production conversion to Pa·s.
**Acquisition conditions.** Temperature, strain, frequency, shear rate, time, segment time and stress remain attached to their source observations where present. The same hydrogel can exhibit different measured behaviour under different deformation and thermal conditions, so those axes are part of the scientific meaning of the measurement.
**QC findings.** Nonpositive rheological values and source values outside a nominal publication range remain evidence to review, not automatic reasons for deletion. Their numerical sign or range does not identify the physical cause.
**Record-linkage boundary.** Source-coordinate provenance is not physical-sample identity. Similar filenames, matching stems or a successful software join cannot establish that two records describe the same formulation, batch, aliquot, rheology specimen, printing run or image. Those questions remain Phase 4.

### Phase 3 output inventory

The Phase 3 notebook generated the following local outputs in its standardisation-and-quality-checks output folder. The executed portable run used a `phase3_outputs/standardisation_and_quality_checks/` folder beside the resolved Phase 2 checkpoint because a canonical repository root was not detected. When the canonical repository structure is available, the notebook supports `data/processed/standardisation_and_quality_checks/`. This inventory describes reproducible local outputs; it does not imply that all source-derived tables should be redistributed publicly.
| Generated filename | Rows | Purpose |
|---|---:|---|
| `input_verification.csv` | 41 | Canonical logical paths, resolved local filenames, hashes and verification notes for protected dependencies |
| `document_evidence_register.csv` | 3 | Document-level evidence used for Phase 3 scientific decisions |
| `standardisation_decisions.csv` | 7 | Explicit Phase 3 decisions, evidence and resolution status |
| `phase3_issue_decisions.csv` | 15 | Phase 3 dispositions linked to the carried Phase 1/2 issue history |
| `transformation_rules.csv` | 13 | One machine-readable transformation rule per observed rheology source header |
| `measurement_values_standardised.csv` | 39,100 | Source-preserving long table with added canonical fields, transformation lineage and QC provenance |
| `measurement_points_view.csv` | 4,600 | Convenience view with one row per verified source measurement point |
| `image_records_standardised.csv` | 1,031 | Source-preserving image metadata with conservative date-format and QC additions |
| `qc_findings.csv` | 25 | Carried Phase 2 findings plus the Phase 3 document-range review finding |
| `qc_observation_links.csv` | 2,302 | Finding-to-source-coordinate associations; association count is not an independent-sample count |
| `acquisition_context_coverage.csv` | 18 | Coverage summary for recorded measurement conditions and response fields |
| `unresolved_review_items.csv` | 4 | Open review topics carried forward without forced resolution |
| `validation_summary.csv` | 674 | Complete structured ledger of Phase 3 validation checks |
| `standardisation_run_manifest.json` | — | Runtime, input hashes, output row counts, output hashes, transformation/QC summaries and unresolved decisions |

### Phase 3 handoff

The verified Phase 3 outputs form the controlled computational handoff to conceptual Phase 4. In this project, a **handoff** means that the next workflow stage receives documented, validated outputs together with provenance, transformation rules, QC status and unresolved issues. It does not mean that uncertainty has disappeared or that physical relationships have been proven.
The long standardised measurement table remains traceable to the original archive member, worksheet, Excel row, column position, source header, source scalar and source unit. The point view is a convenience representation, not a replacement for the source-preserving long table. The image table preserves original tokens and missingness states. An empty standardised viscosity value means conversion was deliberately deferred; it does not mean that the source measurement is missing.
The next project stage is evidence-led record linkage in `04_record_linkage_and_analysis_ready_evidence_layer.ipynb`. It should use the verified identifiers and provenance produced here to assess which formulation, rheology, printing and image records can genuinely be connected. Curve fitting, formulation comparison and machine learning should not begin merely because the Phase 3 software checks passed.
