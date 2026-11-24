# Phase 4 — Record linkage and analysis-ready evidence layer

[← Back to project README](../../README.md)

- Notebook: [`notebooks/04_record_linkage_and_analysis_ready_evidence_layer.ipynb`](../../notebooks/04_record_linkage_and_analysis_ready_evidence_layer.ipynb)
- Executed report: [`reports/04_record_linkage_and_analysis_ready_evidence_layer.html`](../../reports/04_record_linkage_and_analysis_ready_evidence_layer.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/04_record_linkage_and_analysis_ready_evidence_layer.html)

## Scope and method

**Question:** Can the curated rheology, image metadata, acquisition context and QC evidence be linked into an analysis-ready materials-informatics evidence layer without inventing physical sample relationships?

Phase 4 evaluates the joinability of the project’s curated records. It connects standardised rheology values, measurement-point records, worksheet provenance, image metadata, QC findings, unresolved review items and Phase 2 filename-candidate evidence while preserving the distinction between a computational key and a scientifically confirmed relationship.

For each candidate relationship, the notebook records the join basis, source evidence, match coverage, unresolved cases and scientific boundary. A successful merge is treated as software evidence only. It does not prove that two records describe the same formulation, prepared sample, aliquot, rheology specimen, printing run or image unless the source data explicitly support that interpretation.

**Data-science concept:** this is record linkage, entity-resolution auditing and join validation. The output defines which fields are safe for descriptive analysis, which are candidate-only evidence, and which must remain excluded from modelling-readiness decisions. **Polymer concept:** formulation-to-rheology or rheology-to-image interpretation requires source-supported material and process identity, not only similar filenames or labels.

**Output and handoff:** a conservative linkage layer, measurement-point linkage view, image-metadata linkage view, candidate linkage table, QC linkage summary, analysis-readiness summary, unresolved-linkage register and validation ledger. Only evidence-supported populations move into Phase 5 exploratory analysis. Exit when each retained relationship has a stated evidence basis and each unsupported relationship remains visibly unresolved.

## Phase 4 implementation status

The original Phase 4 scope above is retained. The submitted notebook and matching HTML report implement the phase as a reproducible checkpoint named `04_record_linkage_and_analysis_ready_evidence_layer.ipynb`.

The implemented scope includes:
- controlled input resolution for canonical and browser-suffixed filenames, including files such as `input_verification(1).csv`, `validation_summary(2).csv`, `filename_candidates_unconfirmed(2).csv`, `worksheet_register(3).csv`, `ALG-Ph_HA-Ph_rheology_data(5).zip` and `image_index(6).csv`;
- verification of the exact Phase 3 checkpoint and Phase 2 evidence files used for linkage;
- raw-source verification for the rheology archive and `image_index.csv` where available;
- stable source-coordinate keys for worksheet, point and source-cell provenance;
- one row per source measurement point in the measurement-point linkage layer;
- source-cell-level linked measurement evidence with transformation, QC and candidate-linkage context;
- image metadata linkage back to the raw image-index identifiers;
- candidate-only rheology filename correspondences, separated from any physical-sample claim;
- propagation of QC findings and unresolved review items into the Phase 4 evidence layer;
- an analysis-readiness summary that states which fields are safe for Phase 5 descriptive analysis and which remain candidate-only or excluded;
- a run manifest, data dictionary, validation ledger and README summary for reproducible handoff.

## Phase 4 verified results and scientific interpretation

| Phase 4 item | Verified result | Interpretation |
|---|---:|---|
| Controlled input roles resolved | 21 | Required raw, Phase 2 and Phase 3 inputs were located, hashed and mapped to canonical roles. Browser suffixes were recorded instead of ignored. |
| Raw rheology workbook coverage | 92 workbook members | The archive coverage matches the worksheet register used for linkage. |
| Raw image-index coverage | 1,031 image records | Image metadata remained source-grounded; image pixels were not audited in Phase 4. |
| Linked measurement evidence layer | 39,100 rows | Source-cell-level evidence was preserved with provenance, transformation status, QC context and candidate linkage information. These rows are not independent material samples. |
| Measurement-point linkage layer | 4,600 rows | The notebook created one row per verified source measurement point, suitable for Phase 5 descriptive summaries at the correct hierarchy. |
| Image metadata linkage layer | 1,031 rows | Standardised image records were matched back to raw image-index identifiers and source metadata. |
| Candidate rheology-image linkage table | 62 rows | Filename-stem correspondences were retained as candidate evidence only; they are not confirmed rheology-image physical-sample links. |
| QC findings retained | 25 | Phase 4 carried forward the quality-control evidence rather than hiding it during linkage. |
| Unresolved linkage-review rows | 11 | Open and deferred linkage issues remain visible for scientific review. |
| Phase 4 validation checks | 26 | The run created an explicit validation ledger for input resolution, row counts, linkage outputs and boundary conditions. |
| Critical validation failures | 0 | The submitted run completed its declared validation checks without critical failures. |
| Confirmed physical sample linkage | Not asserted | Phase 4 does not claim formulation, replicate, physical-sample, printing-run or rheology-to-image identity where the source does not prove it. |
| Model readiness | Not established | The outputs support Phase 5 exploration and later modelling-readiness review, not immediate prediction. |

### Data-science rationale

**Record linkage is not the same as relationship proof.** Phase 4 separates computational joinability from scientific identity. A shared filename stem, compatible source coordinate or successful table merge can support a candidate relationship, but it does not prove that two records refer to the same physical material or experiment.

**Source-coordinate keys protect provenance.** The linkage layer retains archive member paths, worksheet names, row positions, source headers, source values, units, transformation status and QC context. This allows later plots and summaries to be traced back to source evidence rather than to an unexplained derived table.

**Granularity controls interpretation.** The 39,100 linked measurement rows are source-cell observations nested within worksheets and measurement points. The 4,600 measurement-point rows are a more appropriate level for many descriptive checks, but they still should not be treated as independent formulations or replicate experiments unless later evidence supports that grouping.

**Candidate-only tables reduce overclaiming.** Phase 4 keeps filename-candidate evidence available because it may be useful in Phase 5 review. It also labels that evidence as candidate-only so later analysis does not accidentally turn a naming pattern into a confirmed experimental relationship.

**Analysis readiness is narrower than modelling readiness.** A table can be useful for descriptive analysis while remaining unsuitable for supervised learning. Modelling still requires a defined target, independent experimental units, leakage-safe splits, adequate sample counts and predictors available at the intended prediction time.

### Polymer, hydrogel, rheology and image-metadata interpretation

**Rheology hierarchy.** A rheology workbook may contain many curve points from one acquisition. Viscosity, `G′` and `G″` describe material response under specific test conditions, but each point is not a separate bioink formulation. Phase 4 therefore preserves the nested measurement structure before Phase 5 plots or summaries are attempted.

**Formulation and sample identity remain unresolved.** Polymer identity, concentration, modification, crosslinking and processing history influence hydrogel behaviour. Phase 4 does not create a physical sample ID where the source records do not provide one. This protects later interpretation from attributing measurement differences to formulation variables that may not be uniquely linked.

**Image metadata is not image evidence.** The image-index records include metadata such as image identifier, date, ink type or concentration, shape, irradiation intensity and SPS status where reported. Phase 4 checks metadata linkage only. It does not inspect image files, quantify construct geometry, judge print quality or use images as labels.

**QC context remains part of the science.** Missing annotations, unresolved units, publication-range discrepancies and candidate-only relationships are scientifically meaningful limitations. Keeping them in the evidence layer makes the later analysis more honest and easier to review.

### Phase 4 output inventory

| Output file | Rows | Purpose |
|---|---:|---|
| `phase4_input_file_resolution.csv` | 21 | Maps required canonical inputs to the actual uploaded filenames, file hashes, roles and resolution notes. |
| `linked_measurement_evidence_layer.csv` | 39,100 | Long source-cell-level rheology evidence table with provenance, transformation status, QC context and candidate worksheet linkage. |
| `measurement_point_linkage_layer.csv` | 4,600 | One row per source measurement point with worksheet context and candidate linkage status. |
| `image_metadata_linkage_layer.csv` | 1,031 | Image metadata linked back to raw `image_index.csv` identifiers without auditing image pixels. |
| `candidate_rheology_image_linkage.csv` | 62 | Candidate naming correspondences between rheology and image-related records; no confirmed physical link is asserted. |
| `unresolved_linkage_review_items.csv` | 11 | Open or deferred scientific and linkage questions carried into later review. |
| `qc_linkage_summary.csv` | 25 | Quality-control findings propagated into the Phase 4 linkage context. |
| `analysis_readiness_summary.csv` | 8 | Field- and population-level guidance for Phase 5 descriptive analysis and modelling-readiness boundaries. |
| `phase4_validation_summary.csv` | 26 | Validation ledger for input resolution, output row counts, linkage checks and scientific boundary checks. |
| `phase4_data_dictionary.csv` | 138 | Column-level description of the generated Phase 4 outputs. |
| `phase4_readme_summary.md` | — | Short generated handoff summary, including the optional image-audit note. |
| `phase4_run_manifest.json` | — | Runtime metadata, input-resolution records, output paths, row counts, hashes and validation summary. |

### Phase 4 handoff

The verified Phase 4 outputs form the controlled computational handoff to Phase 5. Phase 5 can use the measurement-point and linked-evidence layers to describe rheology distributions, acquisition coverage and candidate formulation or printing context. It should state the population behind each plot and avoid treating source-cell rows as independent materials.

Candidate filename links may be reviewed and visualised as candidate evidence, but they should not be used as confirmed labels, training targets or ground-truth rheology-image relationships. Image metadata can support coverage and grouping checks; it should not be interpreted as image quality or construct geometry until the actual image files are audited.

### Optional bioink-specific Phase 6 and Phase 7 extensions

The Phase 4 outputs also make two later bioink-specific extensions realistic, provided they remain explicitly optional and source-bounded.

| Optional phase | Extension | What it would do | Required source file |
|---|---|---|---|
| Optional Phase 6 | Image-file audit | Count image files, check the expected `resized_IMG_{image_id}.png` filename pattern, match images to `image_index.csv`, inspect dimensions, colour mode and corruption, review label balance, and optionally compute simple exploratory image features such as area, brightness or edge density. | `images.zip` |
| Optional Phase 7 | Authors’ model and generation-workflow audit | Inventory the authors’ trained model artefacts and fitted rheology-parameter files, compare them with the curated evidence layer, and assess whether beta-CVAE generation or model reproduction is feasible without treating authors’ artefacts as new experimental ground truth. | `models.zip` and `csv_data_files_generation.zip` |

For Optional Phase 6, the image audit would be scoped as:

| Phase 6 section | What it does |
|---|---|
| Image archive audit | Count image files, check filename pattern, and match `resized_IMG_{image_id}.png` to `image_index.csv`. |
| Image metadata QC | Check missing labels, duplicate image IDs, shape distribution and ink formulation distribution. |
| Linkage to curated metadata | Connect image records to Phase 4/5 formulation and printing-condition records where the source evidence supports the link. |
| Basic image inspection | Read dimensions, file integrity, colour mode and corrupted-file status. |
| Optional simple CV features | Calculate area, brightness and edge-density style features for exploratory analysis, not deep learning yet. |

For Optional Phase 7, model comparison remains a reproduction and audit exercise, not proof that the curated Phase 4 tables are ready for supervised hydrogel prediction.
