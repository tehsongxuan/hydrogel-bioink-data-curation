# Phase 1 — Zenodo source audit

[← Back to project README](../../README.md)

- Notebook: [`notebooks/01_zenodo_source_audit.ipynb`](../../notebooks/01_zenodo_source_audit.ipynb)
- Executed report: [`reports/01_zenodo_source_audit.html`](../../reports/01_zenodo_source_audit.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/01_zenodo_source_audit.html)

## Scope and method

**Question:** What files, fields, units, identifiers, and relationships are actually present?
Inventory archives, filenames, formats, tables, columns, row counts, data types, units, labels, IDs, missing values, duplicates, and image files. Compare image names with the image index and read the source documentation for stated record relationships. Separate facts from assumptions: for example, a `shape` label is not automatically a numerical fidelity score.
Log unexpected or unexplained rows, inconsistent labels or units, missing identifiers, and duplicate-looking records. Preserve the original source and record the evidence reviewed. An unusual value is a reason to inspect context, not automatic evidence for deleting or correcting it.
**Data-science concept:** profiling exposes structural problems before transformations or modelling. **Polymer concept:** concentration, crosslinking, and measurement conditions can change the meaning of a rheology value, so the audit checks whether these are measured, reported, or absent.
**Output and handoff:** file and field inventories plus a quality-control issue log. The observed fields and keys—not assumed ones—define Phase 2. Exit when source structure and uncertainty are documented well enough to design the schema.

## Phase 1 implementation status

The executable audit now reads all 92 Excel workbooks directly from `ALG-Ph_HA-Ph_rheology_data.zip` and profiles `image_index.csv`. Manual ZIP extraction is unnecessary. The planned image-file comparison above is deferred: this checkpoint records expected image filenames but does not verify actual image files. Filename correspondence remains candidate evidence rather than a confirmed physical sample relationship.
The original Phase 1 scope above is retained in full. The following results describe only the work implemented and observed in the submitted notebook and HTML export.

## Phase 1 audit results and scientific interpretation

| Audit item | Observed result | Interpretation |
|---|---|---|
| Source files | Rheology ZIP and image-index CSV | Two defined inputs; optional images and model archives are deferred. |
| Reference checksums | Both local MD5 checksums matched the recorded references | Supports file identity against the reviewed source snapshot. |
| Workbook coverage | 92 workbooks and 92 worksheets | 46 modulus workbooks and 46 viscosity workbooks were audited. |
| Measurement records | 4,600 nonblank data rows | Curve points, not 4,600 independent samples or formulations. |
| Image-index records | 1,031 rows | Metadata records; image existence and visual quality were not tested. |
| Strain headers | 44 modulus sheets use `ɣ in -`; 2 use `ɣ in %` | Fraction and percentage representations require explicit handling before comparison. |
| Review register | 15 findings across 7 issue categories | Review items remain visible; findings are not Python execution failures. |
| Audit exports | 11 CSV tables and 1 JSON run manifest | Evidence for schema design and later validation. |
| Input preservation | Source SHA-256 hashes unchanged during execution | The audit did not modify the original ZIP or CSV. |

### Data-science rationale

**Provenance and integrity.** File checksums, archive member paths, workbook sheets and original column headers preserve the origin of observations. A checksum match establishes byte-level agreement with a reference; it does not validate the experimental method or prove that a proposed scientific interpretation is correct.
**Profiling before transformation.** Column profiles describe missing values, numeric content, distinct values and numerical ranges before conversion, imputation or aggregation. The audit preserves unknown information instead of replacing blank metadata with zero or an assumed outcome. It records potential problems so later decisions can cite explicit evidence.
**Granularity and independence.** The 4,600 rows are measurement points nested within rheology workbooks. Treating each point as an independent material would overstate the available evidence and could produce pseudoreplication. Later model evaluation must keep dependent observations together once the source-supported experimental hierarchy is established.
**Record linkage.** Matching workbook stems can suggest a correspondence between viscosity and modulus exports. A matching string does not establish that measurements were made on the same physical sample, batch or replicate. Similarly, an image-index identifier is not automatically a formulation or sample identifier. These distinctions constrain joins and prevent unsupported many-to-many relationships.
**Reproducibility.** The notebook initializes its imports, configuration and audit objects in execution order. It reports the running package versions, reads the two source files and regenerates named outputs instead of appending duplicate results. The submitted export contains completed outputs for all nine code cells and no Python error traceback. Its execution labels are `4, 6, 8, …, 20`; that export alone does not independently verify a fresh-kernel execution sequence.

### Materials-science context

**Strain representation and oscillatory rheology.** Strain is dimensionless, but fraction and percentage are different numerical representations: a strain fraction of 0.01 corresponds to 1%. Source values and headers are retained during the audit. Any later conversion must record its rule and preserve the original unit representation. Comparing unconverted numerical values could introduce a factor-of-100 error.
**Measurement conditions.** Storage modulus `G′` describes elastic energy storage and loss modulus `G″` describes viscous energy dissipation under the specified oscillatory conditions. Their interpretation depends on strain, frequency, temperature and material history. A modulus file must not be called a frequency sweep merely because it contains a frequency column; varying strain at fixed frequency suggests an amplitude-sweep protocol, subject to documentation review. The linear viscoelastic region must be assessed before treating moduli as independent of deformation amplitude.
**Viscosity and complex viscosity.** Steady-shear viscosity and oscillatory complex viscosity describe different measurement modes. Identical-looking units do not establish interchangeability. The source token `mPas` is retained; conversion to Pa·s requires confirmation that it denotes mPa·s. Any correspondence between steady and oscillatory responses requires scientific justification rather than a column-name match.
**Unusual measurements.** Nonpositive rheology values are flagged for review, not automatically deleted, replaced or transformed for plotting. Possible explanations include the measurement range, signal limits or acquisition context, but this audit does not establish their cause. The eight findings are issue-log entries, not a claim that exactly eight individual measurement points are affected.
**Formulation and printing context.** Polymer identity, concentration, chemical modification, crosslinking and processing conditions can affect flow and network response. Missing formulation or irradiation metadata limit interpretation. Blank completeness or reagent annotations remain unknown; they do not prove successful printing, reagent absence or a biological outcome. This checkpoint does not establish causal chemistry–property relationships or cell viability.

### Review findings carried forward

| Issue category | Finding entries | Follow-up |
|---|---:|---|
| `DATASET_LICENCE_UNRESOLVED` | 1 | Confirm the dataset-specific reuse and redistribution terms. |
| `IMAGE_FILES_NOT_AUDITED` | 1 | Audit physical images in a later, explicitly scoped step. |
| `IMAGE_METADATA_BLANK` | 2 | Preserve missingness and review annotation definitions. |
| `INTENSITY_UNIT_UNRESOLVED` | 1 | Establish the source-defined intensity scale and units. |
| `MIXED_STRAIN_UNITS` | 1 | Define traceable fraction/percentage rules in the schema. |
| `NONPOSITIVE_RHEOLOGY_VALUE` | 8 | Review recorded source locations and measurement context. |
| `PHYSICAL_SAMPLE_LINK_UNRESOLVED` | 1 | Seek explicit identifiers or documented relationships. |

### Phase 1 output inventory

All files below are generated locally in `data/metadata/zenodo_source_audit/`. This inventory describes generated outputs; it does not imply that every output has already been committed to GitHub.
| Generated filename | Purpose |
|---|---|
| `source_manifest.csv` | Source identity, selected filenames, reference checksums and input hashes. |
| `archive_member_inventory.csv` | ZIP member paths, sizes and integrity metadata. |
| `workbook_structure_inventory.csv` | Workbook and worksheet structure and row coverage. |
| `source_header_inventory.csv` | Exact source headers and their occurrence counts. |
| `measurement_column_profile.csv` | Column completeness, numeric content and ranges. |
| `measurement_axis_profile.csv` | Observed strain, frequency, shear-rate and temperature coverage. |
| `image_index_column_profile.csv` | Image-index schema and completeness. |
| `image_index_value_counts.csv` | Frequencies of source metadata values. |
| `candidate_filename_correspondences.csv` | Candidate cross-folder filename relationships. |
| `image_filename_expectations.csv` | Expected image filenames; existence remains untested. |
| `audit_issue_log.csv` | Findings, evidence and proposed review actions. |
| `audit_run_manifest.json` | Run timestamp, software versions, counts and file hashes. |
