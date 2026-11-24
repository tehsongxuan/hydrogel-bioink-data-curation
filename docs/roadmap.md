# Roadmap — planned phases 7 to 12

[← Back to project README](../README.md)

These phases are planned, not implemented. They are kept here so the main README describes only completed work.

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

## Phase 7 — Audit authors’ models and generation workflow as a bioink-specific extension

**Question:** Can the authors’ trained models, fitted rheology-parameter files and generation workflow be inventoried or compared reproducibly without treating them as new experimental evidence?

This optional phase uses `models.zip`, `csv_data_files_generation.zip` and the authors’ source-code repository as reference artefacts. It can inspect file structure, model metadata, fitted-parameter tables, expected inputs and reproducibility requirements. It can compare authors’ artefacts with the curated evidence layer only where identifiers and source documentation support the comparison.

**Data-science concept:** model reproduction separates trained artefact inventory, input-data compatibility, environment requirements and evaluation claims. **Materials-informatics concept:** generated images or fitted parameters are derived artefacts; they must not replace source experimental records or create unsupported material labels.

**Output and handoff:** model-artefact inventory, generation-workflow feasibility note, fitted-parameter audit and comparison boundary. Exit when the project can state what is reproducible, what is only partially comparable, and what remains outside the curated experimental evidence layer.

## Phase 8 — Ingest a bounded Materials Project extract

**Question:** Can computational materials records be retrieved and traced reproducibly?
Use the official `mp-api` client for a bounded query. Retain material IDs, query parameters, requested fields, retrieval date, and available calculation provenance. Verify actual returned fields rather than assuming every material has every property. Store API credentials outside version control.
**Data-science concept:** a saved query and source ID make API acquisition reproducible and easier to refresh. **Materials concept:** a calculated inorganic property is a different evidence type from an experimental hydrogel measurement; each keeps its method and provenance.
**Output and handoff:** a documented extract and executable query notebook. This is a separate test case for the metadata design in Phase 11, not a feature table for the hydrogel model. Exit when a reviewer can reproduce the query and identify the origin of each returned value.

## Phase 9 — Reproduce a Matbench task

**Question:** Can a materials-property model be evaluated under a defined protocol?
Reproduce the selected `matbench_dielectric` task using the documented data, folds, and metrics. Its target is refractive index from inorganic crystal structure; despite the name, it is not a hydrogel or polymer dielectric task. Start with a transparent baseline and report features, model, evaluation protocol, and error metrics. Do not tune on the benchmark test data and still call the result a faithful reproduction.
**Data-science concept:** baselines, fixed evaluation procedures, metrics, and leakage checks make results comparable. **Materials-informatics concept:** crystal-structure features do not substitute for polymer chemistry or formulation descriptors.
**Output and handoff:** a reproducible benchmark notebook and score interpretation. The evaluation practices inform Phase 12, but benchmark performance is not evidence that the hydrogel data can support prediction. Exit when task identity, target, inputs, protocol, and limitations are explicit.

## Phase 10 — Map the schema to GEMD

**Question:** Can the documented experimental history be represented as materials, ingredients, processes, measurements, and results?
Map source-supported entities to GEMD concepts. An ingredient may enter a formulation process; a process may create or modify a material; a measurement may be performed on that material under specified conditions. Printing and imaging can be separate processes or records if the source documents them.
GEMD distinguishes intended specifications from experimental runs. A planned concentration is not necessarily the concentration of a prepared and measured sample. A more expressive schema cannot fill a missing sample ID or create evidence absent from the dataset.
**Data-science concept:** knowledge representation captures relationships and constraints that would otherwise remain implicit in column names. **Polymer concept:** formulation and process history can be essential to interpreting a hydrogel’s measured behaviour.
**Output and handoff:** source-to-GEMD mapping, a small example representation, and a list of unsupported fields. This informs common metadata in Phase 11. Exit when mappings do not imply unsupported physical relationships.

## Phase 11 — Apply shared provenance rules

**Question:** What metadata must remain attached so records retain their origin and meaning?
Across the separate source-specific tables, retain source platform and ID, version, source type, material system, property name, original value and unit, standardized value and unit if justified, method, conditions, retrieval date, processing history, and QC status. Distinguish source-reported, transformed, derived, calculated, predicted, and benchmark values.
Record code version, environment, API query, and file checksum where practical. A shared provenance layer supports interoperability; it does not make records scientifically equivalent.
**Data-science concept:** lineage supports audit, debugging, reproducibility, and version updates. **Materials-informatics concept:** consistent metadata can support data exchange while preserving differences among polymer experiments, inorganic calculations, and benchmark tasks.
**Output and handoff:** provenance fields and reusable validation logic. These records allow the final readiness review to rely on traceable evidence. Exit when every processed value can be traced to a source and transformation history.

## Phase 12 — Decide whether hydrogel prediction is justified

**Question:** Do the curated experimental records support a meaningful, independent prediction task?
Define the target before training. “Printability” is not a target until an outcome and measurement method are specified. A source-defined completeness label, objectively calculated shape deviation, or measured rheological property might be candidates if available and consistent. A shape category should not be relabelled as quality without evidence.
Count independent formulations, samples, or printing runs—not just measurement points or image files. Group dependent records together during validation. Check whether predictors are available at the intended prediction time: post-print images cannot serve as predictors for a pre-print decision. Look for target-derived features, missingness, class imbalance, and incompatible measurement conditions.
Possible outcomes are: a defined task is supported; only a restricted task is supportable; or the data support curation and exploration but not reliable prediction. The last outcome identifies which identifiers, measurements, or independent experiments a future dataset would need. If modelling is justified, start with a baseline, grouped validation, error analysis, and a stated domain of applicability.
**Data-science concept:** model readiness depends on target definition, sample size, predictors, leakage-safe validation, and coverage. **Polymer concept:** models need formulation, process, and measurement context; they cannot learn unrecorded chemistry or conditions.
**Output:** a model-readiness report and, only if supported, a limited baseline model. Exit with a defensible statement of what the data can and cannot predict.


## Planned outputs

Subject to feasibility, the repository may contain:
- Versioned source manifest and file inventory
- Field inventory, data dictionary, and schema map
- Quality-control issue log and validation summary
- Standardized tables with source-to-output traceability
- Record-linkage report with match coverage and unresolved links
- Reproducible notebooks for audit, validation, and exploratory analysis
- Figures and summaries based on validated, comparable observations
- A completed Phase 6 bioink image-file audit using the local `images.zip` archive
- An authors’ model and beta-CVAE workflow audit using `models.zip` and `csv_data_files_generation.zip`, if Optional Phase 7 is adopted
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
│   ├── 03_standardisation_and_quality_checks.ipynb
│   ├── 04_record_linkage_and_analysis_ready_evidence_layer.ipynb
│   ├── 05_hydrogel_rheology_and_printing_context_analysis.ipynb
│   ├── 06_image_file_audit_optional.ipynb
│   ├── 07_authors_model_and_generation_workflow_audit_optional.ipynb
│   ├── 08_materials_project_api_ingestion.ipynb
│   ├── 09_matbench_reproduction.ipynb
│   ├── 10_gemd_mapping.ipynb
│   ├── 11_shared_provenance.ipynb
│   └── 12_model_readiness.ipynb
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

### Revised notebook numbering after the implemented Phase 4 checkpoint

The original provisional structure above is retained for project history. The implemented Phase 4 notebook now occupies notebook number `04`, so the later notebook numbers should follow the revised sequence below when those phases are created:
```text
notebooks/
├── 00_scope_and_source_registry.ipynb
├── 01_zenodo_source_audit.ipynb
├── 02_schema_and_quality_control.ipynb
├── 03_standardisation_and_quality_checks.ipynb
├── 04_record_linkage_and_analysis_ready_evidence_layer.ipynb
├── 05_hydrogel_rheology_and_printing_context_analysis.ipynb
├── 06_image_file_audit_optional.ipynb
├── 07_authors_model_and_generation_workflow_audit_optional.ipynb
├── 08_materials_project_api_ingestion.ipynb
├── 09_matbench_reproduction.ipynb
├── 10_gemd_mapping.ipynb
├── 11_shared_provenance.ipynb
└── 12_model_readiness.ipynb
```
This numbering aligns the executable notebook sequence with the implemented Phase 4 checkpoint and the optional bioink-specific image/model extensions. The external Materials Project, Matbench and GEMD work remains separate from the curated hydrogel experimental evidence layer.
