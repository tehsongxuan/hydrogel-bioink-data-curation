# Open Materials Data Pipeline for Hydrogel Bioink Design

A reproducible materials-informatics project focused on curating hydrogel bioink data, preserving experimental context and provenance, and determining whether open records provide a scientifically defensible basis for analysis or machine learning.

Phase 1 source-audit execution is complete for the rheology archive and image-index CSV. The audit generated file and field inventories, source-integrity checks, metadata profiles, and a structured review log. Physical image inspection, experimental sample linkage, unit standardization, and modelling remain outside this checkpoint. Phase 2 schema design is the next planned step.

<details>
<summary>Original planning status — retained for project history</summary>

**Status:** Proposed. Source feasibility and data auditing come first. No analysis or modelling results are claimed until the source records have been inspected and the planned checks have been completed.

</details>

## Quick navigation

### Phase 0 — Scope and source registry

- [Jupyter notebook — scope and source registry](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/notebooks/00_scope_and_source_registry.ipynb)
- [HTML export — scope and source registry](https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/00_scope_and_source_registry.html)

### Phase 1 — Zenodo source audit

- [Jupyter notebook — Zenodo source audit](notebooks/01_zenodo_source_audit.ipynb)
- [HTML export — Zenodo source audit](reports/01_zenodo_source_audit.html)
- [Phase 1 audit results and scientific interpretation](#phase-1-audit-results-and-scientific-interpretation)
- [Phase 1 files and publication procedure](#github-publication-phase-1-checkpoint)

The HTML links refer to files stored within the repository. GitHub may display the HTML source or offer the file for download; downloading the file and opening it in a browser displays the rendered report. A live GitHub Pages report URL is not claimed because the Pages deployment configuration has not yet been verified.

## Project overview

Materials research generates records at several levels: ingredients, formulations, processing steps, physical samples, measurements, printing runs, constructs, and images. These records may be distributed across different tables, instrument exports, archives, and image folders. They become scientifically useful together only when their meanings, units, provenance, and relationships are made explicit.

This project uses an open hydrogel bioink dataset as its experimental case study and three complementary materials-informatics resources to practise reproducible data ingestion, controlled model evaluation, and schema design. The central question is:

> Can open materials records be organized into a traceable workflow that connects documented bioink formulations and processing conditions with rheological measurements and printed-construct information, while preserving the limitations and uncertainty of the source data?

The workflow is intentionally data-first: verify the sources; audit the files; define the data model; validate and standardize values; examine only comparable observations; and then determine whether prediction is justified. Machine learning is a possible final stage, not an assumption imposed at the beginning of the project.

## Problem statement

The primary experimental source concerns phenol-modified alginate (ALG-Ph) and hyaluronic-acid (HA-Ph) hydrogel inks used in 3D bioprinting. The Zenodo record describes shear-dependent viscosity, storage modulus (`G′`), loss modulus (`G″`), printing metadata, indexed construct images, and files associated with the source authors’ analyses. The planned version is `v0.0.2`, which will be checked again before further processing. [Zenodo record](https://zenodo.org/records/19602891) · [Dataset DOI](https://doi.org/10.5281/zenodo.19602891)

A rheology file may contain many measurement points from a single experiment. Those points are repeated observations, not separate formulations. Likewise, an image-index record may describe an image or construct rather than an independent material sample, and a formulation label may not uniquely identify a physical sample. A technically successful software join between two tables does not by itself demonstrate that the records describe the same experiment.

The project therefore asks what each row and file represents, which material and process it describes, and whether any proposed link is supported by source identifiers or documentation. Unexplained rows, missing information, and unmatched records will be retained and documented rather than silently removed, filled with zero, or forced into a relationship. Preserving these records and their uncertainty maintains an auditable evidence trail and prevents the curated dataset from appearing more complete or certain than its source.

## Polymer and hydrogel context

A hydrogel is a water-rich polymer network. A bioink is a formulation intended for bioprinting; it may be hydrogel-based and may contain cells, but the term itself does not prove that a dataset includes cells or evaluates biological performance. The Zenodo case study describes acellular hydrogel printing, so this project will not infer cell viability or tissue response from rheology measurements or images.

Polymer behaviour depends on more than polymer identity alone. Concentration, molecular characteristics, chemical modification, additives, crosslinking, processing history, temperature, and test conditions can all influence the observed response. The source may not report every relevant factor. This project preserves that incompleteness rather than inventing chemical descriptors, sample histories, or experimental conditions.

Rheology describes how materials flow and deform. Viscosity measures resistance to flow. When viscosity decreases as shear rate increases, the material exhibits shear-thinning behaviour. This behaviour can be relevant to extrusion through a printing nozzle, but shear thinning alone does not establish printability. Recovery after extrusion, crosslinking kinetics, nozzle geometry, speed, pressure, and other processing conditions may also be important.

Hydrogels are viscoelastic: their response can include both elastic energy storage and viscous energy dissipation. `G′` describes the elastic contribution and `G″` the viscous contribution under the specified oscillatory test conditions. These quantities must be interpreted together with information such as frequency, strain, temperature, and sample history. Differences between formulations cannot be attributed to chemistry alone when test conditions or sample identity are uncertain.

The scientific chain of interest is:

**ingredients and polymer chemistry → formulation → processing or crosslinking → measured rheology → printing conditions → construct or documented outcome**

Every connection in this chain must be supported by the source evidence. If an identifier or documented convention does not establish a relationship, that relationship remains explicitly unresolved.

## Resources and their roles

The platforms contribute different types of evidence. They will follow shared principles for provenance and data management, but they will not be merged into a single artificial training dataset.

| Resource | Role in this project | Boundary |
|---|---|---|
| [Zenodo bioink dataset](https://zenodo.org/records/19602891) | Primary experimental case study for rheology, printing metadata, and indexed construct images. | Only source-supported links and outcomes will be used. Shape labels and images are not automatically validated print-quality scores. |
| [Materials Project](https://next-gen.materialsproject.org/) | Practise reproducible API retrieval of selected computational materials records, retaining material IDs, query details, returned fields, and calculation provenance. | Its inorganic computational records are not hydrogel rheology measurements and remain in a separate branch. |
| [Matbench](https://matbench.materialsproject.org/) | Reproduce a defined materials-property benchmark to practise controlled model evaluation. The proposed `matbench_dielectric` task predicts refractive index from inorganic crystal structure. | It is not a polymer or hydrogel benchmark; its scores cannot validate a hydrogel model. |
| [Citrine / GEMD](https://citrineinformatics.github.io/gemd-docs/) | Use materials-process-measurement concepts to guide schema design and represent experimental history. | GEMD is a data model, not a hydrogel dataset. Citrination access will be checked before depending on any data there. |

Materials Project provides a Python API client. API retrieval requires an API key, and each query should request fields that are both available and relevant. The query definition, selected fields, and retrieval date form part of the provenance record. [API setup](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started) · [Query guidance](https://docs.materialsproject.org/downloading-data/using-the-api/querying-data)

Matbench provides curated tasks for materials-property machine learning. Reproducing a documented task protocol is a separate exercise in controlled evaluation; success on an inorganic benchmark does not transfer model validity to polymer networks or hydrogel systems. [Matbench documentation](https://docs.materialsproject.org/services/ml-and-ai-applications/matbench) · [Matbench repository](https://github.com/materialsproject/matbench)

GEMD provides concepts for representing ingredients, materials, processes, measurements, conditions, and results as a connected material history. These concepts can guide the experimental schema even if no Citrination dataset is used. Dataset availability and terms will be checked before any Citrination records are treated as project inputs. [GEMD overview](https://citrineinformatics.github.io/gemd-docs/high-level-overview/) · [Citrine Python data model](https://citrineinformatics.github.io/citrine-python/getting_started/data_model.html)

## Linked workflow

Each phase has a defined input, set of checks, output, and exit condition. The output of one phase becomes a controlled input to the next. This staged design reduces the risk that later plots or models depend on undocumented joins, ambiguous identifiers, or guessed unit conversions.

### Phase 0 — Define scope and register sources

**Question:** What does each source contain, and what conclusions can it support?

Record each source URL or DOI, dataset/API identifier, version, retrieval date, access and reuse terms, source type, citation, and, where practical, local file details or checksums. Confirm the Zenodo version and files; select a bounded Materials Project query; identify the exact Matbench task and protocol; and distinguish Citrine/GEMD documentation from access to Citrination datasets.

**Data-science concept:** provenance begins at acquisition. A property value is not fully described without its source, unit, material or experiment identifier, and relevant processing history.

**Output and handoff:** a project-scope note and source manifest. The manifest controls what enters the Phase 1 audit and records the project’s non-goals. Exit when every source and version has a clearly defined and appropriately limited purpose.

### Phase 1 — Audit the Zenodo source

**Question:** What files, fields, units, identifiers, and relationships are actually present?

Inventory the archives, filenames, formats, tables, columns, row counts, data types, units, labels, IDs, missing values, duplicates, and image records. Compare image names with the image index and review the source documentation for stated record relationships. Separate documented facts from assumptions; for example, a `shape` label is not automatically equivalent to a numerical fidelity score.

Log unexpected or unexplained rows, inconsistent labels or units, missing identifiers, and duplicate-looking records. Preserve the original source and record the evidence reviewed. An unusual value is a reason to investigate context; it is not, by itself, evidence that the value should be deleted or corrected.

**Data-science concept:** profiling exposes structural problems before transformation or modelling. **Polymer concept:** concentration, crosslinking, and measurement conditions can change the meaning of a rheology value, so the audit distinguishes what is measured, what is reported, and what is absent.

**Output and handoff:** file and field inventories together with a quality-control issue log. The observed fields and keys—not assumed ones—define Phase 2. Exit when the source structure and uncertainty are documented well enough to support defensible schema design.

#### Phase 1 implementation status — 2 October 2026

The executable audit now reads all 92 Excel workbooks directly from `ALG-Ph_HA-Ph_rheology_data.zip` and profiles `image_index.csv`; manual ZIP extraction is not required. The planned comparison with physical image files is deferred. At this checkpoint, expected image filenames are recorded, but the actual image files are not verified. Filename correspondence therefore remains candidate evidence rather than a confirmed physical-sample relationship.

The original Phase 1 scope above is retained in full for traceability. The results below describe only the work that was implemented and observed in the submitted notebook and matching HTML export.

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

**Provenance and integrity.** File checksums, archive-member paths, workbook sheets, and original column headers preserve the origin of observations. A checksum match establishes byte-level agreement with a reference; it does not validate the experimental method or prove that a proposed scientific interpretation is correct.

**Profiling before transformation.** Column profiles describe missing values, numeric content, distinct values, and numerical ranges before conversion, imputation, or aggregation. The audit preserves unknown information instead of replacing blank metadata with zero or an assumed outcome. Potential problems are recorded explicitly so that later decisions can cite the evidence on which they are based.

**Granularity and independence.** The 4,600 rows are measurement points nested within rheology workbooks. Treating each point as an independent material would overstate the amount of independent evidence and could introduce pseudoreplication. Once the source-supported experimental hierarchy is established, later model evaluation must keep dependent observations together.

**Record linkage.** Matching workbook stems can suggest a correspondence between viscosity and modulus exports, but a matching string does not establish that the measurements were made on the same physical sample, batch, or replicate. Similarly, an image-index identifier is not automatically a formulation or sample identifier. Maintaining these distinctions constrains joins and prevents unsupported many-to-many relationships.

**Reproducibility.** The notebook initializes imports, configuration, and audit objects in execution order. It reports the running package versions, reads the two source files, and regenerates named outputs rather than appending duplicate results. The submitted export contains completed outputs for all nine code cells and no Python error traceback. Its execution labels are `4, 6, 8, …, 20`; the export alone therefore does not independently demonstrate a fresh-kernel execution sequence.

### Materials-science context

**Strain representation and oscillatory rheology.** Strain is dimensionless, but fraction and percentage are different numerical representations: a strain fraction of 0.01 corresponds to 1%. The source values and headers are retained during the audit. Any later conversion must document the rule used and preserve the original unit representation. Comparing numerical values without conversion could introduce a factor-of-100 error.

**Measurement conditions.** Storage modulus `G′` describes elastic energy storage, whereas loss modulus `G″` describes viscous energy dissipation under the specified oscillatory conditions. Their interpretation depends on strain, frequency, temperature, and material history. A modulus file should not be labelled a frequency sweep merely because it contains a frequency column; varying strain at fixed frequency is more consistent with an amplitude-sweep protocol, subject to confirmation from the source documentation. The linear viscoelastic region must be assessed before moduli are treated as independent of deformation amplitude.

**Viscosity and complex viscosity.** Steady-shear viscosity and oscillatory complex viscosity arise from different measurement modes. Similar or identical-looking units do not establish interchangeability. The source token `mPas` is retained; conversion to Pa·s requires confirmation that it denotes mPa·s. Any comparison between steady and oscillatory responses requires scientific justification rather than a column-name match.

**Unusual measurements.** Nonpositive rheology values are flagged for review rather than automatically deleted, replaced, or transformed for plotting. Possible explanations may involve measurement range, signal limits, or acquisition context, but this audit does not establish their cause. The eight findings are issue-log entries; they should not be interpreted as a claim that exactly eight individual measurement points are affected.

**Formulation and printing context.** Polymer identity, concentration, chemical modification, crosslinking, and processing conditions can influence flow and network response. Missing formulation or irradiation metadata therefore limit interpretation. Blank completeness or reagent annotations remain unknown; they do not demonstrate successful printing, reagent absence, or any biological outcome. This checkpoint does not claim causal chemistry–property relationships or cell viability.

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

All files listed below are generated locally in `data/metadata/zenodo_source_audit/`. This inventory documents the outputs produced by the audit; it does not imply that every generated file has already been committed to GitHub.

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

Separate formulation records, physical samples where explicitly identified, rheology experiments, rheology measurement points, printing events, constructs, and images. One rheology experiment may produce many measurement points, and one printing run may have several images. These represent different observational levels. A replicate marker in a filename is not proof of physical-sample identity unless the source documentation explicitly establishes that relationship.

Define field names, meanings, data types, units, allowed values, missing-value semantics, identifiers, and source mappings. A formulation table may store composition; an experiment table may store test type and conditions; and a measurement table may store point-level values. Printing events and image-index records should remain separate when the source supports that distinction. The schema must not invent fields simply because they would be convenient for later modelling.

GEMD concepts can serve as a reference framework: ingredients enter processes; processes create or modify materials; and measurements characterize materials under defined conditions and produce results. Intended specifications should remain distinct from what actually occurred in an experimental run.

**Data-science concept:** schema design makes granularity and relationships explicit. **Polymer concept:** separating material identity, formulation, processing history, and measurement context keeps each property attached to the conditions under which it was produced.

**Output and handoff:** a schema map, data dictionary, identifier rules, and source-to-schema mapping. These become executable or reviewable validation rules for Phase 3. Exit when every field has a definition and every relationship is either supported by evidence or marked unresolved.

### Phase 3 — Standardize values and run quality checks

**Question:** Can equivalent information be represented consistently without losing the original evidence?

Standardize field names, labels, data types, and units only when their meaning is clear. Preserve original values and units alongside standardized values, standardized units, and the conversion rule used. Do not convert an ambiguous unit by assumption. Distinguish zero from not measured, not reported, not applicable, unknown, and unavailable.

Validate required fields, identifier uniqueness, foreign keys, duplicate records, numeric types, row counts, unit consistency, and scientifically justified ranges. Treat range checks as review flags rather than automatic correction rules. Maintain the decision trail in the issue log.

**Data-science concept:** executable checks make assumptions repeatable and expose rule violations. Passing checks does not prove that a scientific relationship is true. **Polymer concept:** `G′` in pascals and viscosity in pascal-seconds describe different properties; even apparently comparable measurements may not be scientifically comparable when frequency, temperature, or other conditions differ.

**Output and handoff:** standardized tables, a validation summary, and transformation lineage. Verified identifiers then support Phase 4. Exit when all transformations are reproducible and unresolved problems remain visible rather than being silently absorbed into the processed data.

### Phase 4 — Assess record linkage

**Question:** Which formulation, rheology, printing, and image records can genuinely be connected?

For each candidate join, record the key used and its source. Check match rates, unmatched rows, duplicated keys, and one-to-one or one-to-many relationships. Some one-to-many structures are scientifically expected—for example, one rheology experiment can contain many measurement points. A join that executes successfully in software does not demonstrate that the connected records describe the same physical formulation, sample, or run.

Classify links as confirmed by an explicit identifier, documented by a source convention, possible, or unresolved. Similar labels may suggest a relationship, but they do not confirm one. Ambiguous records should be reported rather than forced into a combined table.

**Data-science concept:** this phase is entity resolution and join validation. It also helps determine the independent experimental unit for later summaries and model splits. **Polymer concept:** formulation-to-rheology linkage is required before a measured response can be interpreted as formulation-dependent.

**Output and handoff:** a linkage map, join-coverage report, and unresolved-link register. Only source-supported links proceed to Phase 5. Exit when every intended comparison has a clearly defined population and evidence basis.

### Phase 5 — Explore rheology and printing context

**Question:** What patterns occur in validated, comparable measurements?

Plot shear-dependent viscosity against shear rate and describe whether the observed response is consistent with shear-thinning over the measured range. Plot `G′` and `G″` against the variable actually changed in the source experiment when the test conditions permit comparison. Keep individual experiments visible and compute group summaries at the correct observational level; curve points must not be treated as independent samples.

A derived quantity such as `tan δ = G″/G′` should be calculated only when both moduli are available and scientifically compatible. Record the formula, retain the original source values, and leave the derived result undefined when the denominator is zero. Do not modify a measurement merely to make a derived column complete.

Explore image and printing metadata only when source-defined identifiers support a link to rheology or formulation records. Define what each image label represents. A requested shape, an image category, and a validated print-quality outcome are not interchangeable concepts. Describe observed associations rather than causal effects because unrecorded conditions may explain apparent differences.

**Data-science concept:** exploratory analysis describes distributions, coverage, variation, and possible relationships before inferential or predictive modelling. **Polymer concept:** viscosity, `G′`, and `G″` capture different aspects of flow and viscoelasticity; their relevance to printing depends on both the measurement conditions and the printing process.

**Output and handoff:** reproducible figures, tables, and written interpretations that state comparability limits. These outputs inform the Phase 10 model-readiness review. Exit when every plot states the source population, unit, condition, and experimental unit represented.

### Phase 6 — Ingest a bounded Materials Project extract

**Question:** Can computational materials records be retrieved and traced reproducibly?

Use the official `mp-api` client for a bounded query. Retain material IDs, query parameters, requested fields, retrieval date, and available calculation provenance. Verify the fields actually returned rather than assuming that every material has every requested property. Store API credentials outside version control.

**Data-science concept:** a saved query and source identifier make API acquisition reproducible and easier to refresh. **Materials concept:** a calculated inorganic property is a different evidence type from an experimental hydrogel measurement; each must retain its own method and provenance.

**Output and handoff:** a documented extract and executable query notebook. This remains a separate test case for the metadata design in Phase 9 rather than a feature table for hydrogel modelling. Exit when another reviewer can reproduce the query and identify the origin of every returned value.

### Phase 7 — Reproduce a Matbench task

**Question:** Can a materials-property model be evaluated under a defined protocol?

Reproduce the selected `matbench_dielectric` task using its documented data, folds, and metrics. The target is refractive index from inorganic crystal structure; despite the task name, this is not a hydrogel or polymer dielectric benchmark. Begin with a transparent baseline and report the features, model, evaluation protocol, and error metrics. Do not tune on benchmark test data and still describe the result as a faithful reproduction.

**Data-science concept:** baselines, fixed evaluation procedures, metrics, and leakage checks make results comparable. **Materials-informatics concept:** crystal-structure features cannot substitute for polymer chemistry, formulation descriptors, or processing history.

**Output and handoff:** a reproducible benchmark notebook and interpretation of its scores. The evaluation practices inform Phase 10, but benchmark performance does not demonstrate that the hydrogel dataset can support prediction. Exit when task identity, target, inputs, protocol, and limitations are explicit.

### Phase 8 — Map the schema to GEMD

**Question:** Can the documented experimental history be represented as materials, ingredients, processes, measurements, and results?

Map source-supported entities to GEMD concepts. An ingredient may enter a formulation process; a process may create or modify a material; and a measurement may be performed on that material under specified conditions. Printing and imaging can be represented as separate processes or records when the source documentation supports doing so.

GEMD distinguishes intended specifications from experimental runs. A planned concentration is not necessarily identical to the concentration of the material that was actually prepared and measured. A more expressive schema cannot recover a missing sample identifier or create evidence that is absent from the original dataset.

**Data-science concept:** knowledge representation makes relationships and constraints explicit rather than leaving them hidden in column names. **Polymer concept:** formulation and processing history can be essential for interpreting a hydrogel’s measured behaviour.

**Output and handoff:** a source-to-GEMD mapping, a small example representation, and a list of unsupported fields. This work informs the common metadata design in Phase 9. Exit when the mappings represent only source-supported relationships and do not imply unsupported physical connections.

### Phase 9 — Apply shared provenance rules

**Question:** What metadata must remain attached so records retain their origin and meaning?

Across the separate source-specific tables, retain the source platform and ID, version, source type, material system, property name, original value and unit, standardized value and unit where justified, method, conditions, retrieval date, processing history, and QC status. Clearly distinguish source-reported, transformed, derived, calculated, predicted, and benchmark values.

Record the code version, software environment, API query, and file checksum where practical. A shared provenance layer improves interoperability and traceability; it does not make scientifically different records equivalent.

**Data-science concept:** lineage supports auditing, debugging, reproducibility, and version updates. **Materials-informatics concept:** consistent metadata can support data exchange while preserving important differences among polymer experiments, inorganic calculations, and benchmark tasks.

**Output and handoff:** shared provenance fields and reusable validation logic. These records allow the final readiness review to rely on traceable evidence. Exit when every processed value can be traced back to its source and transformation history.

### Phase 10 — Decide whether hydrogel prediction is justified

**Question:** Do the curated experimental records support a meaningful, independent prediction task?

Define the prediction target before training. “Printability” is not a valid target until the outcome and measurement method are specified. A source-defined completeness label, an objectively calculated shape-deviation measure, or a measured rheological property could be candidates if they are available and consistently defined. A shape category should not be relabelled as a quality score without evidence.

Count independent formulations, samples, or printing runs—not merely measurement points or image files. Keep dependent records together during validation. Check whether predictors would be available at the intended prediction time: post-print images cannot legitimately serve as predictors for a pre-print decision. Examine target-derived features, missingness, class imbalance, and incompatible measurement conditions.

Possible outcomes include: a clearly defined prediction task is supported; only a restricted task is supportable; or the dataset supports curation and exploration but not reliable prediction. The final outcome is still informative because it identifies which identifiers, measurements, or independent experiments a future dataset would need. If modelling is justified, begin with a baseline, grouped validation, error analysis, and a stated domain of applicability.

**Data-science concept:** model readiness depends on target definition, independent sample size, predictors, leakage-safe validation, and data coverage. **Polymer concept:** useful models require formulation, process, and measurement context; they cannot learn chemical or experimental information that was never recorded.

**Output:** a model-readiness report and, only when supported by the evidence, a limited baseline model. Exit with a defensible statement of what the data can and cannot predict.

## Concepts that connect the phases

- **Data granularity:** define whether a row represents a formulation, sample, experiment, point, run, construct, or image. This guides schema design, summaries, joins, and validation splits.
- **Provenance and lineage:** preserve source identifiers, versions, units, query details, and transformations. This begins in Phase 0 and remains attached through every later output.
- **Missingness semantics:** distinguish zero from unknown, not measured, not reported, not applicable, or unavailable. This affects QC and model feature selection.
- **Standardization:** normalize names and units only with documented rules; keep raw source values available for review.
- **Experimental hierarchy:** points from one curve and images from one run are nested records, not necessarily independent materials. This matters for uncertainty and model evaluation.
- **Leakage control:** related records must not be split carelessly between training and testing. The split should reflect the intended future prediction and the true independent unit.
- **Exploration versus causation:** patterns can motivate hypotheses but do not isolate causal effects when formulation, process, and conditions vary together.

## Planned outputs

Subject to source feasibility and the evidence established in earlier phases, the repository may contain:

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

Large source archives and API credentials will not be committed by default. Instead, the repository will provide source links, retrieval instructions, environment details, and code for reproducing derived outputs, subject to each provider’s access and reuse terms.

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

This structure is provisional and will be updated to reflect work that has actually been implemented. Listing a notebook here is a planning aid and does not claim that the notebook already exists.

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

These boundaries guide the source audit, schema design, joins, visualisations, and modelling decision from the beginning of the workflow.

## Success criteria

The workflow should be able to answer, with evidence: Where did each value originate? What does each row represent? Which values are experimental, computational, derived, or benchmark data? What material, formulation, process, and measurement conditions are documented? Which records can be linked, and which relationships remain uncertain? Which transformations and QC decisions were applied? Which observations are independent? Which comparisons are scientifically appropriate? Is there a meaningful, leakage-safe prediction target? What does the dataset support, and what remains unknown?

A conclusion that the source data are not yet ready for hydrogel machine learning can still be a valuable result. It identifies the specific data gaps, identifiers, or experimental evidence that future datasets and experiments would need to address.

## Current status and next step

**Current checkpoint:** Phase 1 execution is complete for the rheology ZIP and image-index CSV, with 15 review findings retained. The next step is Phase 2: define the experimental entities, source-to-schema mappings, original and standardized unit fields, missing-value semantics, and evidence requirements for record linkage. Schema design can proceed while unresolved matters remain explicitly documented. Physical image review and the Materials Project, Matbench, and GEMD extensions remain deferred.

<details>
<summary>Original planning statement — retained for project history</summary>

**Planning and source-feasibility review.** Begin with Phase 0 by confirming the Zenodo version and reuse conditions, registering the sources, and inspecting the primary archive. Finalize the schema, joins, analyses, and any prediction task from the records actually observed. Materials Project, Matbench, and GEMD remain separate extensions until the primary audit establishes a manageable and evidence-based scope.

</details>

## GitHub publication: Phase 0 checkpoint

The first publishable checkpoint consists of the project documentation, the Jupyter notebook used to check the working environment and expected project files, and an optional HTML rendering of that notebook. Add these files to the repository using the paths below so the relative links resolve correctly on GitHub.

- **Jupyter notebook (executable Python):** [`00_scope_and_source_registry.ipynb`](notebooks/00_scope_and_source_registry.ipynb)
- **HTML notebook export (read-only view):** [`00_scope_and_source_registry.html`](reports/00_scope_and_source_registry.html)

The notebook is the editable, rerunnable source, while the HTML file provides a convenient browser-readable snapshot. Keep both links relative to the repository so they continue to work if the repository is renamed or moved.

### Files for the initial GitHub upload

- `README.md` — this project overview and workflow plan.
- `notebooks/00_scope_and_source_registry.ipynb` — the Phase 0 Jupyter notebook.
- `reports/00_scope_and_source_registry.html` — optional HTML export of the notebook.
- `.gitignore` — recommended to keep local datasets, notebook checkpoints, and environment-specific files out of version control.

Do not include the downloaded Zenodo archive or `image_index.csv` in the initial public upload while reuse and redistribution conditions are still being checked. Keep those source files in the local project directory. Additional dataset archives are not required for the Phase 0 checkpoint and can be added locally later when they have been downloaded and reviewed.

## GitHub publication: Phase 1 checkpoint

### Core publication files

| File | Repository destination |
|---|---|
| Updated project README | `README.md` at repository root |
| Executable source-audit notebook | `notebooks/01_zenodo_source_audit.ipynb` |
| Matching HTML report | `reports/01_zenodo_source_audit.html` |

The existing `reports/` convention is retained for both Phase 0 and Phase 1 HTML files, and the existing Phase 0 files remain in place. Download suffixes such as `(1)` or `(2)` are removed from the published notebook and HTML filenames so the navigation links resolve consistently. A separate `.py` file is not required because the `.ipynb` already contains the executable Python cells together with the explanatory Markdown.

The 12 generated audit files listed above are supporting outputs that can be reproduced locally by running the notebook. They are not required for this documentation-and-code checkpoint. Publication of source-derived metadata should follow review of the file contents and applicable source terms. The raw ZIP, `image_index.csv`, image archives, model archives, and installed environment folders remain local for this checkpoint.

### Execution environment

The submitted run reports Python 3.12.15, NumPy 1.26.4, pandas 2.2.3, openpyxl 3.1.5, and IPython 9.17.1. The selected project kernel is `Python (hydrogel-bioink)`. Its setup excludes user-site package injection to avoid the previously observed NumPy/pandas binary incompatibility. The notebook includes one-time environment setup and restart instructions. Routine audit execution does not install dependencies.

The two required source files are stored locally at the following paths:

- `data/raw/zenodo_19602891/ALG-Ph_HA-Ph_rheology_data.zip`
- `data/raw/zenodo_19602891/image_index.csv`

### Browser upload procedure

1. Open [the project repository](https://github.com/tehsongxuan/hydrogel-bioink-data-curation) and select the intended branch, normally `main` for this personal project checkpoint.
2. At the repository root, use **Add file → Upload files** to upload the updated file named exactly `README.md`. Review the change and commit it with a descriptive message.
3. Open `notebooks/`, use **Add file → Upload files**, and choose `01_zenodo_source_audit.ipynb`. Wait until the upload finishes, then commit. Uploading inside this folder avoids placing the notebook at repository root.
4. Return to the repository root, open `reports/`, and upload `01_zenodo_source_audit.html` in the same way. If the folder is absent, **Add file → Create new file** at the root can create `reports/.gitkeep`; commit it, open `reports/`, then upload the HTML. A placeholder is optional after a real file exists.
5. Open the README and check both Phase 1 navigation links. The notebook link should open the notebook file; the HTML link should open the stored HTML file, which can be downloaded and opened locally in a browser.
6. Supporting audit exports, when reviewed and selected for publication, belong together in `data/metadata/zenodo_source_audit/`. Preserve their generated filenames. Upload the actual exports from the local notebook run, not substitute tables from another execution environment.

Suggested commit messages are: `Update README with Phase 1 source-audit results`, `Add Phase 1 Zenodo source-audit notebook`, and `Add Phase 1 source-audit HTML report`.

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






