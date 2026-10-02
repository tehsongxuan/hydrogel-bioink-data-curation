# Open Materials Data Pipeline for Hydrogel Bioink Design

A reproducible materials-informatics project for curating hydrogel bioink data, preserving experimental context, and deciding whether open records support reliable analysis or machine learning.

Phase 1 source-audit execution is complete for the rheology archive and image-index CSV. The audit produced file and field inventories, source-integrity checks, metadata profiles and a review log. Physical image inspection, experimental sample linkage, unit standardization and modelling remain outside this checkpoint. Phase 2 schema design is the next step.

<details>
<summary>Original planning status — retained for project history</summary>

**Status:** Proposed. Source feasibility and data audit come first. No analysis or model results are claimed until the source records have been inspected and the planned checks have been completed.

</details>

## Quick navigation

- [Repository home](https://github.com/tehsongxuan/hydrogel-bioink-data-curation)
- [Project overview](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#project-overview)
- [Current status and next step](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#current-status-and-next-step)

### Phase 0 — Scope and source registry

- [Jupyter notebook — scope and source registry](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/00_scope_and_source_registry.ipynb)
- [HTML export — scope and source registry](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html)
- [View HTML report in browser — scope and source registry](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html)
- [Phase 0 workflow and methodology](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#phase-0--define-scope-and-register-sources)
- [Phase 0 publication checkpoint](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#github-publication-phase-0-checkpoint)

### Phase 1 — Zenodo source audit

- [Jupyter notebook — Zenodo source audit](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/01_zenodo_source_audit.ipynb)
- [HTML export — Zenodo source audit](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/01_zenodo_source_audit.html)
- [View HTML report in browser — Zenodo source audit](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/01_zenodo_source_audit.html)
- [Phase 1 workflow and methodology](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#phase-1--audit-the-zenodo-source)
- [Phase 1 audit results and scientific interpretation](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#phase-1-audit-results-and-scientific-interpretation)
- [Phase 1 output inventory](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#phase-1-output-inventory)
- [Phase 1 files and publication procedure](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md#github-publication-phase-1-checkpoint)

The notebook and HTML export links above point to the canonical files stored in the repository. GitHub may display an HTML file as source text or offer it for download rather than render it as a webpage. The separate **View HTML report in browser** links use HTML Preview to render the same repository HTML files directly in a browser.

## Project overview

Materials research creates records at several levels: ingredients, formulations, processing steps, physical samples, measurements, printing runs, constructs, and images. Those records may live in different tables, instrument exports, archives, and image folders. They are scientifically useful together only when their meanings, units, and relationships are clear.

This project uses an open hydrogel bioink dataset as its experimental case study and uses three complementary materials-informatics resources to practise computational data ingestion, model evaluation, and schema design. The central question is:

> Can open materials records be organized into a traceable workflow that connects documented bioink formulations and processing conditions with rheological measurements and printed-construct information, while preserving the limits of the source data?

The workflow is deliberately data-first: verify sources; audit files; define the data model; validate and standardize values; examine comparable observations; then decide whether prediction is justified. Machine learning is a possible final step, not an assumption made at the beginning.

## Problem statement

The primary experimental source concerns phenol-modified alginate (ALG-Ph) and hyaluronic-acid (HA-Ph) hydrogel inks used in 3D bioprinting. The Zenodo record describes shear-dependent viscosity, storage modulus (`G′`), loss modulus (`G″`), printing metadata, indexed construct images, and files associated with the source authors’ analyses. The planned version is `v0.0.2`, to be checked again before processing. [Zenodo record](https://zenodo.org/records/19602891) · [Dataset DOI](https://doi.org/10.5281/zenodo.19602891)

A rheology file may contain many points from one experiment. Those points are repeated observations, not separate formulations. An image index may describe an image or construct, not an independent material sample. A formulation label may not uniquely identify a physical sample. A successful software join between two tables does not prove they describe the same experiment.

The project therefore asks what each row and file represents, which material and process it describes, and whether a link is supported by source identifiers or documentation. Unexplained rows, missing information, and unmatched records will be recorded rather than silently removed, filled with zero, or forced into a relationship. Keeping these records traceable preserves evidence for review and prevents the curated dataset from appearing more complete or certain than its source.

## Polymer and hydrogel context

A hydrogel is a water-rich polymer network. A bioink is a formulation intended for bioprinting; it may be hydrogel-based and may contain cells, but the word alone does not prove that a dataset includes cells or measures biological performance. The Zenodo case study describes acellular hydrogel printing, so this project will not infer cell viability or tissue response from its rheology or images.

Polymer behaviour depends on more than polymer identity. Concentration, molecular characteristics, chemical modification, additives, crosslinking, processing history, temperature, and test conditions can matter. The source may not report every factor. The project will preserve this incompleteness rather than inventing chemical descriptors or sample conditions.

Rheology describes flow and deformation. Viscosity measures resistance to flow. If viscosity decreases as shear rate increases, the material exhibits shear-thinning behaviour. This can be relevant to extrusion through a printing nozzle, but shear thinning alone does not prove printability. Recovery after extrusion, crosslinking kinetics, nozzle geometry, speed, pressure, and other processing conditions may also matter.

Hydrogels are viscoelastic: their response can include elastic energy storage and viscous energy dissipation. `G′` describes the elastic contribution and `G″` the viscous contribution under the specified oscillatory test conditions. These values should be interpreted alongside information such as frequency, strain, temperature, and sample history. A difference between formulations cannot be attributed to chemistry alone if test conditions or sample identity are uncertain.

The scientific chain of interest is:

**ingredients and polymer chemistry → formulation → processing or crosslinking → measured rheology → printing conditions → construct or documented outcome**

Each connection must be supported by the source. If an identifier or documented convention does not establish a link, it remains unresolved.

## Resources and their roles

The platforms provide different evidence types. They will share data-management and provenance principles, but they will not be merged into one artificial training dataset.

| Resource | Role in this project | Boundary |
|---|---|---|
| [Zenodo bioink dataset](https://zenodo.org/records/19602891) | Primary experimental case study for rheology, printing metadata, and indexed construct images. | Only source-supported links and outcomes will be used. Shape labels and images are not automatically validated print-quality scores. |
| [Materials Project](https://next-gen.materialsproject.org/) | Practise reproducible API retrieval of selected computational materials records, retaining material IDs, query details, returned fields, and calculation provenance. | Its inorganic computational records are not hydrogel rheology measurements and remain in a separate branch. |
| [Matbench](https://matbench.materialsproject.org/) | Reproduce a defined materials-property benchmark to practise controlled model evaluation. The proposed `matbench_dielectric` task predicts refractive index from inorganic crystal structure. | It is not a polymer or hydrogel benchmark; its scores cannot validate a hydrogel model. |
| [Citrine / GEMD](https://citrineinformatics.github.io/gemd-docs/) | Use materials-process-measurement concepts to guide schema design and represent experimental history. | GEMD is a data model, not a hydrogel dataset. Citrination access will be checked before depending on any data there. |

Materials Project provides a Python API client. API retrieval requires an API key, and a query should specify fields that are actually available and needed. The query, selected fields, and retrieval date form part of the provenance record. [API setup](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started) · [Query guidance](https://docs.materialsproject.org/downloading-data/using-the-api/querying-data)

Matbench provides curated tasks for materials-property machine learning. Reproducing its task protocol is a separate exercise in controlled evaluation; it does not transfer a model’s validity from inorganic crystals to polymer networks. [Matbench documentation](https://docs.materialsproject.org/services/ml-and-ai-applications/matbench) · [Matbench repository](https://github.com/materialsproject/matbench)

GEMD helps represent ingredients, materials, processes, measurements, conditions, and results as a connected material history. This can guide the experimental schema even if no Citrination dataset is used. Dataset availability and terms will be checked before any Citrination records are treated as a project input. [GEMD overview](https://citrineinformatics.github.io/gemd-docs/high-level-overview/) · [Citrine Python data model](https://citrineinformatics.github.io/citrine-python/getting_started/data_model.html)

## Linked workflow

Each phase has an input, checks, output, and exit condition. The output from one phase becomes a controlled input to the next. This prevents later plots or models from depending on undocumented joins or guessed unit conversions.

### Phase 0 — Define scope and register sources

**Question:** What does each source contain, and what conclusions can it support?

Record each source URL or DOI, dataset/API identifier, version, retrieval date, access and reuse terms, source type, citation, and local file details or checksum where practical. Confirm the Zenodo version and files; select a bounded Materials Project query; identify the exact Matbench task and protocol; and distinguish Citrine/GEMD documentation from access to Citrination datasets.

**Data-science concept:** provenance starts at acquisition. A property value is not fully described without its source, unit, experiment or material identifier, and processing history.

**Output and handoff:** a project-scope note and source manifest. This manifest controls what is audited in Phase 1 and records the project’s non-goals. Exit when each source and version has a defined, limited purpose.

### Phase 1 — Audit the Zenodo source

**Question:** What files, fields, units, identifiers, and relationships are actually present?

Inventory archives, filenames, formats, tables, columns, row counts, data types, units, labels, IDs, missing values, duplicates, and image files. Compare image names with the image index and read the source documentation for stated record relationships. Separate facts from assumptions: for example, a `shape` label is not automatically a numerical fidelity score.

Log unexpected or unexplained rows, inconsistent labels or units, missing identifiers, and duplicate-looking records. Preserve the original source and record the evidence reviewed. An unusual value is a reason to inspect context, not automatic evidence for deleting or correcting it.

**Data-science concept:** profiling exposes structural problems before transformations or modelling. **Polymer concept:** concentration, crosslinking, and measurement conditions can change the meaning of a rheology value, so the audit checks whether these are measured, reported, or absent.

**Output and handoff:** file and field inventories plus a quality-control issue log. The observed fields and keys—not assumed ones—define Phase 2. Exit when source structure and uncertainty are documented well enough to design the schema.

#### Phase 1 implementation status

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

### Phase 2 — Design the experimental schema

**Question:** What real-world entity does one row represent in each table?

Separate formulation records, physical samples if identified, rheology experiments, rheology measurement points, printing events, constructs, and images. One experiment may produce many rheology points; one run may have several images. These are different levels of observation. A replicate in a filename is not proof of physical sample identity unless the source says so.

Define field names, meanings, types, units, allowed values, missing-value semantics, identifiers, and source mapping. A formulation table might hold composition; an experiment table holds test type and conditions; a measurement table holds point-level values. A printing event and image index should be separate if the source supports them. The schema must not invent fields just because they would be useful for modelling.

GEMD concepts can be used as a reference: ingredients enter processes; processes produce or modify materials; measurements characterize materials under conditions and yield results. Intended specifications should be distinguished from what actually occurred in an experimental run.

**Data-science concept:** schema design makes data granularity and relationships explicit. **Polymer concept:** separating material identity, formulation, process, and measurement context keeps the property attached to the conditions that produced it.

**Output and handoff:** schema map, data dictionary, identifier rules, and source-to-schema mapping. These become validation rules for Phase 3. Exit when every field has a definition and each relationship is supported or marked unresolved.

### Phase 3 — Standardize values and run quality checks

**Question:** Can equivalent information be represented consistently without losing the original evidence?

Standardize field names, labels, types, and units only where meaning is clear. Keep original values and units alongside standardized values, units, and conversion rules. Do not convert an ambiguous unit by guessing. Distinguish zero from not measured, not reported, not applicable, unknown, and unavailable.

Validate required fields, ID uniqueness, foreign keys, duplicate records, numeric types, row counts, unit consistency, and scientifically justified ranges. Treat range checks as flags for review, not automatic correction. Keep a decision trail in the issue log.

**Data-science concept:** executable checks make assumptions repeatable and expose violations. Passing checks does not prove that a scientific relationship is true. **Polymer concept:** `G′` in pascals and viscosity in pascal-seconds describe different properties; even equal units do not ensure comparability if frequency or temperature differs.

**Output and handoff:** standardized tables, validation summary, and transformation lineage. Their verified identifiers support Phase 4. Exit when transformations are reproducible and unresolved problems remain visible.

### Phase 4 — Assess record linkage

**Question:** Which formulation, rheology, printing, and image records can genuinely be connected?

For each candidate join, record the key and its source. Check match rates, unmatched rows, duplicated keys, and one-to-one or one-to-many relationships. Some one-to-many links are expected: a rheology experiment can contain many points. A join that runs successfully in software does not prove that the records describe the same physical formulation or run.

Classify links as confirmed by an explicit ID, documented by a source convention, possible, or unresolved. Similar labels alone may suggest a match but do not confirm one. Report ambiguous records rather than forcing them into a combined table.

**Data-science concept:** this is entity resolution and join validation. It also determines the independent experimental unit for later summaries and model splits. **Polymer concept:** formulation-to-rheology linkage is necessary before a measured response can be interpreted as formulation-dependent.

**Output and handoff:** linkage map, join-coverage report, and unresolved-link register. Only supported links move into Phase 5. Exit when each comparison has a defined population and evidence basis.

### Phase 5 — Explore rheology and printing context

**Question:** What patterns occur in validated, comparable measurements?

Plot shear-dependent viscosity against shear rate and describe whether the observed curve is consistent with shear-thinning over the measured range. Plot `G′` and `G″` against the source’s measured variable when test conditions allow comparison. Keep individual experiments visible and group summaries at the correct level; do not treat curve points as independent samples.

A derived value such as `tan δ = G″/G′` should be calculated only when both moduli are available and compatible. Record the formula, retain source values, and leave the result undefined when the denominator is zero. Do not alter a measurement to make a derived column complete.

Explore image and printing metadata only if source-defined identifiers link them to rheology or formulation. Define what each image label represents. A requested shape, image category, and validated print-quality outcome are not interchangeable. Describe associations rather than causal effects; unrecorded conditions may explain observed differences.

**Data-science concept:** exploratory analysis describes distributions, coverage, variation, and possible relationships before inference. **Polymer concept:** viscosity, `G′`, and `G″` describe different aspects of flow and viscoelasticity; their printing relevance depends on test and process conditions.

**Output and handoff:** reproducible figures, tables, and a written interpretation with comparability limits. These inform model readiness in Phase 10. Exit when each plot states the source population, unit, condition, and experimental unit.

### Phase 6 — Ingest a bounded Materials Project extract

**Question:** Can computational materials records be retrieved and traced reproducibly?

Use the official `mp-api` client for a bounded query. Retain material IDs, query parameters, requested fields, retrieval date, and available calculation provenance. Verify actual returned fields rather than assuming every material has every property. Store API credentials outside version control.

**Data-science concept:** a saved query and source ID make API acquisition reproducible and easier to refresh. **Materials concept:** a calculated inorganic property is a different evidence type from an experimental hydrogel measurement; each keeps its method and provenance.

**Output and handoff:** a documented extract and executable query notebook. This is a separate test case for the metadata design in Phase 9, not a feature table for the hydrogel model. Exit when a reviewer can reproduce the query and identify the origin of each returned value.

### Phase 7 — Reproduce a Matbench task

**Question:** Can a materials-property model be evaluated under a defined protocol?

Reproduce the selected `matbench_dielectric` task using the documented data, folds, and metrics. Its target is refractive index from inorganic crystal structure; despite the name, it is not a hydrogel or polymer dielectric task. Start with a transparent baseline and report features, model, evaluation protocol, and error metrics. Do not tune on the benchmark test data and still call the result a faithful reproduction.

**Data-science concept:** baselines, fixed evaluation procedures, metrics, and leakage checks make results comparable. **Materials-informatics concept:** crystal-structure features do not substitute for polymer chemistry or formulation descriptors.

**Output and handoff:** a reproducible benchmark notebook and score interpretation. The evaluation practices inform Phase 10, but benchmark performance is not evidence that the hydrogel data can support prediction. Exit when task identity, target, inputs, protocol, and limitations are explicit.

### Phase 8 — Map the schema to GEMD

**Question:** Can the documented experimental history be represented as materials, ingredients, processes, measurements, and results?

Map source-supported entities to GEMD concepts. An ingredient may enter a formulation process; a process may create or modify a material; a measurement may be performed on that material under specified conditions. Printing and imaging can be separate processes or records if the source documents them.

GEMD distinguishes intended specifications from experimental runs. A planned concentration is not necessarily the concentration of a prepared and measured sample. A more expressive schema cannot fill a missing sample ID or create evidence absent from the dataset.

**Data-science concept:** knowledge representation captures relationships and constraints that would otherwise remain implicit in column names. **Polymer concept:** formulation and process history can be essential to interpreting a hydrogel’s measured behaviour.

**Output and handoff:** source-to-GEMD mapping, a small example representation, and a list of unsupported fields. This informs common metadata in Phase 9. Exit when mappings do not imply unsupported physical relationships.

### Phase 9 — Apply shared provenance rules

**Question:** What metadata must remain attached so records retain their origin and meaning?

Across the separate source-specific tables, retain source platform and ID, version, source type, material system, property name, original value and unit, standardized value and unit if justified, method, conditions, retrieval date, processing history, and QC status. Distinguish source-reported, transformed, derived, calculated, predicted, and benchmark values.

Record code version, environment, API query, and file checksum where practical. A shared provenance layer supports interoperability; it does not make records scientifically equivalent.

**Data-science concept:** lineage supports audit, debugging, reproducibility, and version updates. **Materials-informatics concept:** consistent metadata can support data exchange while preserving differences among polymer experiments, inorganic calculations, and benchmark tasks.

**Output and handoff:** provenance fields and reusable validation logic. These records allow the final readiness review to rely on traceable evidence. Exit when every processed value can be traced to a source and transformation history.

### Phase 10 — Decide whether hydrogel prediction is justified

**Question:** Do the curated experimental records support a meaningful, independent prediction task?

Define the target before training. “Printability” is not a target until an outcome and measurement method are specified. A source-defined completeness label, objectively calculated shape deviation, or measured rheological property might be candidates if available and consistent. A shape category should not be relabelled as quality without evidence.

Count independent formulations, samples, or printing runs—not just measurement points or image files. Group dependent records together during validation. Check whether predictors are available at the intended prediction time: post-print images cannot serve as predictors for a pre-print decision. Look for target-derived features, missingness, class imbalance, and incompatible measurement conditions.

Possible outcomes are: a defined task is supported; only a restricted task is supportable; or the data support curation and exploration but not reliable prediction. The last outcome identifies which identifiers, measurements, or independent experiments a future dataset would need. If modelling is justified, start with a baseline, grouped validation, error analysis, and a stated domain of applicability.

**Data-science concept:** model readiness depends on target definition, sample size, predictors, leakage-safe validation, and coverage. **Polymer concept:** models need formulation, process, and measurement context; they cannot learn unrecorded chemistry or conditions.

**Output:** a model-readiness report and, only if supported, a limited baseline model. Exit with a defensible statement of what the data can and cannot predict.

## Concepts that connect the phases

- **Data granularity:** define whether a row represents a formulation, sample, experiment, point, run, construct, or image. This guides schema design, summaries, joins, and validation splits.
- **Provenance and lineage:** preserve source identifiers, versions, units, query details, and transformations. This begins in Phase 0 and remains attached through every later output.
- **Missingness semantics:** distinguish zero from unknown, not measured, not reported, not applicable, or unavailable. This affects QC and model feature selection.
- **Standardization:** normalize names and units only with documented rules; keep raw source values available for review.
- **Experimental hierarchy:** points from one curve and images from one run are nested records, not necessarily independent materials. This matters for uncertainty and model evaluation.
- **Leakage control:** related records must not be split carelessly between training and testing. The split should reflect the intended future prediction and the true independent unit.
- **Exploration versus causation:** patterns can motivate hypotheses but do not isolate causal effects when formulation, process, and conditions vary together.

## Planned outputs

Subject to feasibility, the repository may contain:

- Versioned source manifest and file inventory
- Field inventory, data dictionary, and schema map
- Quality-control issue log and validation summary
- Standardized tables with source-to-output traceability
- Record-linkage report with match coverage and unresolved links
- Reproducible notebooks for audit, validation, and exploratory analysis
- Figures and summaries based on validated, comparable observations
- A bounded Materials Project API-ingestion example
- A Matbench reproduction with documented protocol and metrics
- A GEMD mapping and example representation
- A hydrogel model-readiness report and, only if appropriate, a baseline model

Large source archives and API credentials will not be committed by default. The repository will provide source links, retrieval instructions, environment details, and code for reproducing derived outputs, subject to each provider’s terms.

### Proposed repository structure

```text
open-materials-hydrogel-bioink-pipeline/
├── README.md
├── environment.yml
├── .gitignore
├── DATA_SOURCES.md
├── DATA_DICTIONARY.md
├── PROVENANCE.md
├── notebooks/
│   ├── 00_scope_and_source_registry.ipynb
│   ├── 01_zenodo_source_audit.ipynb
│   ├── 02_schema_and_quality_control.ipynb
│   ├── 03_record_linkage.ipynb
│   ├── 04_hydrogel_rheology_analysis.ipynb
│   ├── 05_materials_project_api_ingestion.ipynb
│   ├── 06_matbench_reproduction.ipynb
│   ├── 07_gemd_mapping.ipynb
│   └── 08_model_readiness.ipynb
├── src/
│   ├── ingestion/
│   ├── validation/
│   └── analysis/
├── data/
│   └── metadata/
├── reports/
│   ├── figures/
│   └── tables/
└── docs/
    ├── schema_design.md
    ├── quality_control_rules.md
    └── scientific_boundaries.md
```

This structure is provisional. It will be updated to reflect work actually implemented; listing a notebook here does not claim that it already exists.

## Scientific boundaries

- Materials Project records remain computational and separate from hydrogel experimental data.
- Matbench scores demonstrate benchmark practice, not hydrogel-model validity.
- GEMD guides representation but cannot supply missing source evidence.
- No physical sample or experiment link will be invented.
- Missing values will not be replaced by zero without source justification.
- Unit conversions and derived variables will be traceable to original values.
- Repeated rheology points will not be counted as independent formulations.
- Rheology and images alone will not be used to infer cell viability, tissue function, or clinical performance.
- Observational patterns will not be described as causal effects of polymer chemistry or concentration.
- Modelling will proceed only if the target, independent sample size, record linkage, predictors, and evaluation design support it.
- The project does not claim new polymer synthesis, instrument or sensor development, robotics, or biological testing.

These boundaries shape the source audit, schema, joins, plots, and modelling decision from the beginning.

## Success criteria

The workflow should be able to answer, with evidence: Where did each value originate? What does each row represent? Which values are experimental, computational, derived, or benchmark data? What material, formulation, process, and measurement conditions are documented? Which records can be linked, and which relationships remain uncertain? Which transformations and QC decisions were applied? Which observations are independent? What comparisons are scientifically appropriate? Is there a meaningful, leakage-safe prediction target? What does the dataset support, and what remains unknown?

A finding that the source data are not yet ready for hydrogel machine learning can still be a useful result. It identifies the data gaps that future experiments or repositories need to address.

## Current status and next step

**Current checkpoint:** Phase 1 execution is complete for the rheology ZIP and image-index CSV, with 15 review findings retained. The next step is Phase 2: define the experimental entities, source-to-schema mappings, original and standardized unit fields, missing-value semantics and evidence requirements for record linkage. Schema design can proceed while unresolved matters remain explicitly recorded. Physical image review and the Materials Project, Matbench and GEMD extensions remain deferred.

<details>
<summary>Original planning statement — retained for project history</summary>

**Planning and source-feasibility review.** Begin with Phase 0: confirm the Zenodo version and reuse conditions, register the sources, then inspect the primary archive. Finalize the schema, joins, analysis, and any prediction task from the records actually found. Materials Project, Matbench, and GEMD remain separate extensions until the primary audit establishes a manageable scope.

</details>

## GitHub publication: Phase 0 checkpoint

The first publishable checkpoint consists of the project documentation, the Jupyter notebook that checks the working environment and expected project files, and an optional HTML rendering of that notebook. Add the files to the repository using the paths below so these links work on GitHub.

- **Jupyter notebook (executable Python):** [`00_scope_and_source_registry.ipynb`](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/00_scope_and_source_registry.ipynb)
- **HTML notebook export:** [`00_scope_and_source_registry.html`](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html)
- **Browser-rendered HTML report:** [View `00_scope_and_source_registry.html` in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html)

The notebook is the editable, rerunnable source. The HTML file is the matching read-only export. The repository link preserves the file in its version-controlled location, while the separate browser-view link uses HTML Preview to render the same report directly in a browser.

### Files for the initial GitHub upload

- `README.md` — this project overview and workflow plan.
- [`notebooks/00_scope_and_source_registry.ipynb`](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/00_scope_and_source_registry.ipynb) — the Phase 0 Jupyter notebook.
- [`reports/00_scope_and_source_registry.html`](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html) — optional HTML export of the notebook; [view the rendered HTML report in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html).
- `.gitignore` — recommended to keep local datasets, notebook checkpoints, and environment-specific files out of version control.

Do not include the downloaded Zenodo archive or `image_index.csv` in this initial public upload while reuse and redistribution conditions are being checked. Keep those source files in the local project folder. Additional dataset archives are not required for this Phase 0 checkpoint and can be added to the local project later when downloaded and reviewed.

## GitHub publication: Phase 1 checkpoint

### Core publication files

| File | Repository destination | Direct link |
|---|---|---|
| Updated project README | `README.md` at repository root | [Open README](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/README.md) |
| Executable source-audit notebook | `notebooks/01_zenodo_source_audit.ipynb` | [Open notebook](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/01_zenodo_source_audit.ipynb) |
| Matching HTML report | `reports/01_zenodo_source_audit.html` | [Open HTML export](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/01_zenodo_source_audit.html) · [View rendered HTML in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/01_zenodo_source_audit.html) |

The existing `reports/` convention is retained for both Phase 0 and Phase 1 HTML files. Existing Phase 0 files remain in place. Download suffixes such as `(1)` or `(2)` are removed from the published notebook and HTML filenames so navigation links resolve consistently. A separate `.py` file is not required: the `.ipynb` contains the executable Python cells and the explanatory Markdown.

The 12 generated audit files listed above are additional supporting outputs. They can be reproduced locally from the notebook. They are not required for this documentation-and-code checkpoint; publication of source-derived metadata should follow review of its contents and applicable source terms. The raw ZIP, `image_index.csv`, image archives, model archives and installed environment folders remain local for this checkpoint.

### Execution environment

The submitted run reports Python 3.12.15, NumPy 1.26.4, pandas 2.2.3, openpyxl 3.1.5 and IPython 9.17.1. The selected project kernel is `Python (hydrogel-bioink)`. Its setup excludes user-site package injection to avoid the observed NumPy/pandas binary incompatibility. The notebook includes one-time environment setup and restart instructions. No dependency installation occurs during a routine audit run.

The two required source files are stored locally at:

- `data/raw/zenodo_19602891/ALG-Ph_HA-Ph_rheology_data.zip`
- `data/raw/zenodo_19602891/image_index.csv`

### Browser upload procedure

1. Open [the project repository](https://github.com/tehsongxuan/hydrogel-bioink-data-curation) and select the intended branch, normally `main` for this personal project checkpoint.
2. At the repository root, use **Add file → Upload files** to upload the updated file named exactly `README.md`. Review the change and commit it with a descriptive message.
3. Open `notebooks/`, use **Add file → Upload files**, and choose `01_zenodo_source_audit.ipynb`. Wait until the upload finishes, then commit. Uploading inside this folder avoids placing the notebook at repository root.
4. Return to the repository root, open `reports/`, and upload `01_zenodo_source_audit.html` in the same way. If the folder is absent, **Add file → Create new file** at the root can create `reports/.gitkeep`; commit it, open `reports/`, then upload the HTML. A placeholder is optional after a real file exists.
5. Open the README and check the Phase 1 navigation links. The notebook link should open the executable notebook, the HTML export link should open the stored `01_zenodo_source_audit.html` file, and the separate **View HTML report in browser** link should render the report through HTML Preview.
6. Supporting audit exports, when reviewed and selected for publication, belong together in `data/metadata/zenodo_source_audit/`. Preserve their generated filenames. Upload the actual exports from the local notebook run, not substitute tables from another execution environment.

Suggested commit messages: `Update README with Phase 1 source-audit results`, `Add Phase 1 Zenodo source-audit notebook`, and `Add Phase 1 source-audit HTML report`.

Upload reference: [GitHub documentation — adding a file to a repository](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

## Sources and technical documentation

### Experimental hydrogel bioink data

- [Zenodo dataset record](https://zenodo.org/records/19602891)
- [Dataset DOI](https://doi.org/10.5281/zenodo.19602891)
- [Associated publication](https://doi.org/10.1080/17452759.2026.2671497)
- [Authors’ source-code repository](https://github.com/KORINZ/generative-ai-bioprinting-framework)

### Materials Project

- [Materials Project home](https://next-gen.materialsproject.org/)
- [Materials Explorer](https://next-gen.materialsproject.org/materials)
- [General documentation](https://docs.materialsproject.org/)
- [API getting started](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started)
- [API query guidance](https://docs.materialsproject.org/downloading-data/using-the-api/querying-data)
- [Python API client documentation](https://materialsproject.github.io/api/)
- [API client source code](https://github.com/materialsproject/api)

### Matbench and matminer

- [Matbench benchmark and leaderboard](https://matbench.materialsproject.org/)
- [Materials Project Matbench documentation](https://docs.materialsproject.org/services/ml-and-ai-applications/matbench)
- [Matbench source repository](https://github.com/materialsproject/matbench)
- [Matbench methodology paper](https://doi.org/10.1038/s41524-020-00406-3)
- [matminer documentation](https://hackingmaterials.lbl.gov/matminer/)
- [matminer dataset summary](https://hackingmaterials.lbl.gov/matminer/dataset_summary.html)

### Citrine, GEMD, and Citrination

- [Citrine Informatics](https://citrine.io/)
- [Citrine DataManager](https://citrine.io/platform/citrine-datamanager/)
- [GEMD documentation](https://citrineinformatics.github.io/gemd-docs/)
- [GEMD high-level overview](https://citrineinformatics.github.io/gemd-docs/high-level-overview/)
- [Citrine Python data-model overview](https://citrineinformatics.github.io/citrine-python/getting_started/data_model.html)
- [gemd-python source repository](https://github.com/CitrineInformatics/gemd-python)
- [Citrination](https://citrination.com/) — included as a platform reference; dataset availability and access will be verified before use.


