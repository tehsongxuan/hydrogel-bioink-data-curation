# Phase 2 — Experimental schema and quality control

[← Back to project README](../../README.md)

- Notebook: [`notebooks/02_schema_and_quality_control.ipynb`](../../notebooks/02_schema_and_quality_control.ipynb)
- Executed report: [`reports/02_schema_and_quality_control.html`](../../reports/02_schema_and_quality_control.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/02_schema_and_quality_control.html)

## Scope and method

**Question:** What real-world entity does one row represent in each table?
Separate formulation records, physical samples if identified, rheology experiments, rheology measurement points, printing events, constructs, and images. One experiment may produce many rheology points; one run may have several images. These are different levels of observation. A replicate in a filename is not proof of physical sample identity unless the source says so.
Define field names, meanings, types, units, allowed values, missing-value semantics, identifiers, and source mapping. A formulation table might hold composition; an experiment table holds test type and conditions; a measurement table holds point-level values. A printing event and image index should be separate if the source supports them. The schema must not invent fields just because they would be useful for modelling.
GEMD concepts can be used as a reference: ingredients enter processes; processes produce or modify materials; measurements characterize materials under conditions and yield results. Intended specifications should be distinguished from what actually occurred in an experimental run.
**Data-science concept:** schema design makes data granularity and relationships explicit. **Polymer concept:** separating material identity, formulation, process, and measurement context keeps the property attached to the conditions that produced it.
**Output and handoff:** schema map, data dictionary, identifier rules, and source-to-schema mapping. These become validation rules for Phase 3. Exit when every field has a definition and each relationship is supported or marked unresolved.

## Phase 2 implementation status

The original Phase 2 scope above is retained in full. The executed `02_schema_and_quality_control.ipynb` implements a source-preserving schema-validation prototype using the verified Phase 1 checkpoint and the supplied literature context. It does not replace the Phase 1 audit and does not claim that worksheet, filename, image, formulation or printing labels identify independent physical samples.
The implemented scope includes:
- checkpoint integrity verification against the completed Phase 1 manifest;
- an evidence register separating source-reported statements, derived values, interpretation and unresolved questions;
- explicit row granularity and source-coordinate identifier rules;
- source-to-schema mappings for all observed rheology headers and image-index fields;
- four instantiated source-grounded prototype tables;
- explicit missing-value semantics for image metadata;
- a complete executable data dictionary for the prototype fields;
- documented structural, parsing, acquisition-axis, image and unresolved-semantics QC rules;
- value-level QC that retains flagged observations instead of silently cleaning them;
- a traceable strain percent-to-fraction conversion preview;
- a measurement-context and comparability review;
- preservation of all Phase 1 issue records plus Phase 2 decisions and additional review topics; and
- a deterministic export and checksum-based handoff for later standardization and record-linkage work.

This implementation deliberately exercises selected validation concepts described in the conceptual Phase 3 plan because schema rules are more useful when tested against real source records. It does **not** claim that Phase 3 production standardization is complete. Viscosity conversion remains deferred, physical sample linkage remains unresolved, and no rheology-to-image scientific foreign key is created.

## Phase 2 verified results and scientific interpretation

| Phase 2 item | Verified result | Interpretation |
|---|---|---|
| Phase 1 handoff | Two raw files and all eleven Phase 1 audit CSVs matched their recorded SHA-256 values; the reviewed Phase 1 manifest also matched | The Phase 2 schema is tied to the audited source snapshot rather than a silently changed input |
| Reviewed inputs | 19 reviewed inputs registered | Includes data/audit inputs plus supporting publication, supplementary, README, prompt and checkpoint material |
| Source worksheets | 92 | Digital measurement records; not 92 confirmed independent samples |
| Measurement points | 4,600 | Repeated observations within measurement records |
| Source cells | 39,100 | Includes acquisition labels, experimental conditions and measured responses |
| Image-index records | 1,031 | Metadata records; physical image existence was not tested |
| Source-grounded entities | 4 | `worksheet_register`, `measurement_points`, `measurement_values`, and `image_records` |
| Deferred entities | 4 | Formulation, physical sample, printing event and printed construct remain uninstantiated because their identities or relationships are not established |
| Rheology source fields mapped | 13 | Complete mapping of the observed rheology headers |
| Image-index fields mapped | 7 | Complete mapping of the observed image-index schema |
| Core data-dictionary entries | 37 | Every field in the four prototype tables is documented |
| QC rules documented | 14 | Covers checkpoint, source coverage, keys, parsing, response values, acquisition axes, duplicate rows, image metadata, vocabulary, unresolved semantics and strain preview |
| Validation checks | 43 passed | Structural and reconciliation checks passed within the declared contract |
| Value-QC findings | 24 finding records | 20 nonpositive response cells, 2 nonpositive shear-rate cells, and 2 column-level missing-annotation summaries |
| Nonpositive response values | 20 viscosity cells across 8 worksheets | Retained unchanged; their exact source locations reconcile with Phase 1 |
| Nonpositive shear-rate values | 2 cells | Retained as acquisition-axis review flags |
| Image missingness | `completeness_sam`: 943 blanks; `contain_sps`: 922 blanks | Blank remains `unknown_blank`; it is not converted to yes, no, zero, success or reagent absence |
| Strain conversion preview | 2,300 strain cells: 2,200 source-labelled fractions and 100 source-labelled percentages | Percent-to-fraction arithmetic was tested without overwriting source values |
| Modulus acquisition context | All 46 modulus worksheets report fixed 1 Hz frequency with varying strain | Consistent with amplitude-sweep context; no per-curve LVR is assigned |
| Viscosity acquisition context | All 46 viscosity worksheets include a shear-rate value below the publication's nominal lower bound of 0.01 s⁻¹ | Difference is preserved for review rather than removed to match prose |
| Phase 1 findings carried forward | 15 | Original evidence and severity remain visible |
| Additional Phase 2 review topics | 4 | Viscosity unit token, LVR selection, publication-range difference and modelling-population reconciliation remain open |
| Candidate source stems | 62 distinct stems; 30 occur exactly once in each measurement family | Filename correspondence is candidate evidence only |
| Confirmed physical-sample links | 0 | No physical-sample identity or rheology-to-image linkage is asserted |
| Phase 2 exports | 26 CSV files plus 1 JSON run manifest | Reproducible local handoff for later phases |
| Runtime input preservation | All 14 runtime input/checkpoint files remained byte-identical | Phase 2 did not rewrite the raw inputs or Phase 1 checkpoint files |

### Data-science rationale

**Granularity and keys.** The schema distinguishes a source worksheet, a nonblank measurement row, a single source cell and an image-index record. Primary and foreign keys therefore identify digital source coordinates, not physical hydrogel specimens. This prevents the 4,600 curve points from being misrepresented as 4,600 independent materials.
**Source-preserving representation.** Measurement values are retained with their archive member, worksheet, Excel row, source column position, exact source header, source unit and parsing status. A numeric interpretation is added without replacing the original source scalar. This keeps transformation lineage auditable.
**Schema drift and field mapping.** The two observed strain header conventions (`ɣ in -` and `ɣ in %`) are mapped explicitly rather than collapsed silently. All thirteen rheology headers and seven image-index fields must be accounted for, so an unexpected source representation cannot disappear from processing unnoticed.
**Missingness semantics.** Blank image-index values are represented as observed unknowns. The schema does not infer why they are blank and does not convert missing annotations into negative or positive experimental outcomes.
**Referential integrity and reconciliation.** Primary-key, parent-child, row-count, source-coverage, dictionary-coverage and source-header checks validate the internal structure of the prototype. Passing these tests establishes consistency with the reviewed snapshot; it does not prove experimental equivalence or independence.
**QC without silent cleaning.** A warning records a source value or semantic question for review; it does not automatically delete, replace or repair the observation. The 20 nonpositive viscosity values and two negative shear-rate values remain in the data with their source coordinates.
**Traceable transformation.** The strain-conversion preview retains the source scalar and unit, the numerical input, the standardised result, target unit and conversion rule. It demonstrates arithmetic traceability without claiming that all rheology values have been fully standardised.

### Polymer, hydrogel and rheology interpretation

**Oscillatory moduli.** Storage modulus `G′` describes elastic energy storage and loss modulus `G″` describes viscous dissipation under the recorded oscillatory conditions. Because the modulus worksheets show fixed 1 Hz frequency with varying strain, the observed axes are consistent with an amplitude-sweep context rather than a frequency sweep. The notebook does not assign a linear viscoelastic region from the column names alone.
**Strain representation.** Strain is dimensionless, but a percentage and a fraction use different numerical scales. The preview applies `strain_fraction = strain_percent / 100` only where the source explicitly labels the value as percent, while retaining the original representation. Source-labelled fraction values are not clipped merely because their range appears unusual.
**Viscosity.** Steady-shear apparent viscosity and oscillatory complex viscosity are kept distinct. The source token `mPas` is retained because the notebook does not yet establish the instrument notation strongly enough to approve production conversion to Pa·s.
**Measurement context.** Recorded temperature, strain, frequency, shear rate and other acquisition coordinates remain attached to their source measurements. A nominal method statement from the publication does not overwrite an observed workbook value.
**Physical identity and record linkage.** Matching filename stems can support a naming correspondence but do not demonstrate that two files describe the same aliquot, batch, physical sample, rheology specimen, printing run or construct. Phase 2 therefore confirms no physical-sample link.
**Model-readiness boundary.** Successful schema validation is not a machine-learning readiness result. Independent experimental units, validated composition relationships, production unit standardization, defensible record linkage and a prediction target are still unresolved.

### Phase 2 output inventory

The Phase 2 notebook writes its local outputs to `data/metadata/schema_and_quality_control/`. The files below document the executed schema and QC contract. Their existence as local exports does not imply that source-derived tables should all be redistributed publicly.
| Generated filename | Rows | Purpose |
|---|---:|---|
| `input_verification.csv` | 13 | Runtime verification of the two raw inputs and eleven Phase 1 audit CSVs |
| `reviewed_inputs.csv` | 19 | Register of the complete set of reviewed data, checkpoint and supporting documents |
| `literature_evidence_register.csv` | 10 | Evidence statements, scopes and permitted schema decisions |
| `entity_schema.csv` | 4 | Source-grounded entities, row granularity, keys and scientific boundaries |
| `deferred_entities.csv` | 4 | Physical or process entities not instantiated because source evidence is insufficient |
| `source_to_schema_mapping.csv` | 13 | Exact rheology-header mapping, logical type, units and conversion policy |
| `image_field_dictionary.csv` | 7 | Image-index field definitions and semantic limits |
| `data_dictionary.csv` | 37 | Complete field dictionary for the four prototype tables |
| `missing_value_rules.csv` | 5 | Explicit handling rules for blanks, source annotations, structural absence and unresolved semantics |
| `worksheet_register.csv` | 92 | One record per audited source worksheet |
| `measurement_points.csv` | 4,600 | One record per nonblank source measurement row |
| `measurement_values_source.csv` | 39,100 | Source-preserving cell-level measurement and condition table |
| `image_records_source.csv` | 1,031 | Source-preserving image-index metadata table |
| `image_missingness.csv` | 7 | Missingness summary for image-index fields |
| `image_observed_categories.csv` | 81 | Snapshot vocabulary and observed category counts |
| `quality_control_rules.csv` | 14 | Executable QC rule definitions, severities and actions |
| `validation_summary.csv` | 43 | Results of structural and reconciliation checks |
| `value_qc_findings.csv` | 24 | Retained value-level and column-level QC findings |
| `strain_conversion_preview.csv` | 2,300 | Traceable fraction/percentage strain conversion preview |
| `measurement_context_summary.csv` | 6 | Observed acquisition-axis coverage and numerical ranges |
| `context_review.csv` | 3 | Comparability and experimental-context review statements |
| `phase1_issue_carry_forward.csv` | 15 | Original Phase 1 findings retained for history and traceability |
| `phase2_issue_decisions.csv` | 15 | Phase 2 decisions linked to the corresponding Phase 1 findings |
| `additional_review_items.csv` | 4 | Newly recorded open questions requiring later review |
| `filename_candidates_unconfirmed.csv` | 62 | Candidate filename correspondences that are not physical-sample links |
| `linkage_summary.csv` | 3 | Counts summarising candidate naming coverage and confirmed physical-link status |
| `schema_qc_run_manifest.json` | — | Run metadata, software versions, input hashes and output checksums |

### Phase 2 handoff

The verified schema and QC contract is the controlled input to the next project stage. The next work should retain the source values, original unit tokens and unresolved-link statuses while implementing only scientifically justified standardization rules. Production viscosity conversion should wait until the source unit notation is established. Any formulation, sample, printing or image linkage should document the proposed key, supporting evidence, cardinality, unmatched records and physical claim being made.
Phase 2 does not remove the unresolved Phase 1 findings. Dataset-specific reuse terms, physical image inspection, image-annotation semantics, intensity calibration and physical sample linkage remain open. The source archive and source-derived local exports should therefore continue to be handled conservatively until redistribution terms are established.
