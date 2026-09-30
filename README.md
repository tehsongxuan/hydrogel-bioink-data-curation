# hydrogel-bioink-data-curation
Reproducible curation and linkage assessment of open hydrogel bioink formulation, rheology, and 3D-printing data.
# Open-Data Curation and Integration of Hydrogel Bioink Formulation, Rheology and Printing Records

[![Zenodo dataset](https://zenodo.org/badge/DOI/10.5281/zenodo.19602891.svg)](https://doi.org/10.5281/zenodo.19602891)

## Project status

**Proposed project — source-data feasibility review is the first step.**

This README describes the planned scope. The dataset files have not yet been audited in this project, so the final schema, joins, analyses and deliverables will depend on what the source records actually support. No results are claimed here.

## Project overview

This project will assess whether an openly available hydrogel bioink dataset can be organised into a traceable workflow connecting **formulation and printing-related metadata** with **rheological characterisation** and **construct/image records**, where the source files provide evidence for those links.

The selected Zenodo record accompanies research on generative AI-guided optimisation of deposition morphology for 3D bioprinting. It describes alginate-phenol and hyaluronic-acid-phenol conjugated inks, rheology data, image metadata, and image files. The image index is described as containing image identifiers and fields such as ink type and concentration, shape, irradiation intensity and sodium persulfate presence. The actual file contents and the meaning of each field will be checked before analysis. [Zenodo dataset record](https://zenodo.org/records/19602891)

## Problem statement

Materials-development data are often split across files that describe different parts of an experiment. A rheology curve, a formulation label and a printed-construct image are useful together only when their meanings, units and relationships are clear.

Before investigating how a hydrogel bioink behaves during printing, the records need to answer basic questions:

- What does each row or file represent: a formulation, a measurement point, a printing run or an image?
- Which formulation and printing fields are actually recorded, and how are they encoded?
- Are rheology variables and units consistent and scientifically interpretable?
- Can a rheology record be linked to a specific formulation or construct using documented identifiers?
- Which values are missing, and are they structurally absent, unreported or uncertain?
- Is there a well-defined application outcome suitable for comparison or modelling?

If these questions are not answered first, an analysis can join unrelated records, mistake missing values for measured zeroes, or claim a formulation–performance relationship that the data cannot establish.

## Research question

**Can the published records be curated into a reproducible dataset that links hydrogel bioink formulation and printing conditions with rheological and construct information, and what limitations remain before reliable formulation-to-performance modelling is possible?**

## Polymer chemistry and materials-informatics context

A hydrogel is a water-rich polymer network. A bioink is a material prepared for bioprinting; bioinks may be hydrogel-based, but the terms are not interchangeable. The selected dataset specifically concerns hydrogel printing and reports alginate-phenol and hyaluronic-acid-phenol conjugated inks.

The polymer formulation and the printing or curing conditions can influence how an ink flows during deposition and how it behaves after printing. Rheological quantities provide different views of this response:

- **Shear-rate-dependent viscosity** describes resistance to flow at different imposed shear rates and can inform print-process behaviour.
- **Storage modulus, G′**, describes the elastic component of the measured viscoelastic response.
- **Loss modulus, G″**, describes the viscous component of that response.

These measurements must be interpreted alongside the test conditions and source definitions. A rheology value alone does not prove printability, construct quality, biological performance or a causal effect of one formulation variable.

From a polymer-informatics perspective, the intended data chain is:

**polymer/ink formulation → processing or printing conditions → measured rheology → construct-level information**

The project will test whether the source records support each link. It will not invent sample identities, infer undocumented chemistry or assume that similarly named records belong together.

## Objectives

1. **Audit source files and provenance.** Record filenames, file types, available documentation, source identifiers, row counts and checksums where appropriate.
2. **Define record-level schemas.** Distinguish formulation or process metadata, rheology observations and image/construct metadata based on the actual files.
3. **Standardise and validate.** Check variable names, units, data types, identifiers, duplicates, missingness and value coverage; preserve original values and record all transformations.
4. **Test table relationships.** Measure how many records can be linked using documented identifiers. Report unmatched and ambiguous records instead of forcing a join.
5. **Explore supported patterns.** Summarise rheological responses and other clearly defined fields at the correct experimental level.
6. **Assess modelling readiness.** Determine whether the data contain a valid outcome, reliable links and enough independent formulations or constructs for a leakage-safe model.

## Planned workflow

### Stage 0 — Feasibility and source review

Read the Zenodo record, dataset documentation and actual files. Verify the dataset-specific reuse terms and citation requirements. Inventory what is available and identify which files are needed for a manageable first analysis.

The Zenodo record lists a small image-index table and rheology archive alongside a much larger image collection and model files. The initial review can begin with the documentation, tabular index and rheology data; image processing will be considered only if it is needed to answer a defined question. [Zenodo dataset record](https://zenodo.org/records/19602891)

### Stage 1 — Data audit

Inspect the actual file structures, column names, units, identifiers, row counts and missing values. Check whether documentation explains how records correspond to one another. Record unusual or unclear items in a quality-control log; do not silently delete or correct them.

### Stage 2 — Schema and data dictionary

Define a schema only after inspecting the source files. Candidate record levels may include formulation/process records, rheology measurement points and image or construct records, but the final tables and their fields must reflect the dataset as supplied.

For each retained field, document its source name, standardised name if needed, meaning, unit, applicable record type, missing-value rule and provenance.

### Stage 3 — Controlled ingestion and validation

Create reproducible, machine-readable tables while keeping each value traceable to its source file and source location. Validate identifiers and candidate joins, and distinguish:

- measured zeroes from missing values;
- structural absence from unknown or unreported values;
- source-reported quantities from any derived summaries; and
- a source label from a confirmed physical sample or run identity.

### Stage 4 — Linkage assessment

Test only relationships supported by source identifiers or documented metadata. Report match rates, unmatched records, duplicate keys and ambiguous links. Similar text labels alone are not proof that two records describe the same formulation, sample or printing run.

### Stage 5 — Exploratory analysis

If validated links and compatible measurement conditions are available, describe rheological values across the recorded ink and processing groups. Keep repeated points within a curve or run nested within that experimental record. Use descriptive summaries and avoid causal claims from observational comparisons.

Any derived quantity will be calculated only when its source variables, units and measurement conditions make the calculation valid and interpretable.

### Stage 6 — Modelling-readiness decision

A predictive model is optional, not a required outcome. Before modelling, establish a clear target, valid formulation-to-outcome links, enough independent examples and a split strategy that prevents related measurements from appearing in both training and test data.

The dataset documentation notes that the completeness_sam field has missing data and was not used in the published study. It will not be treated as a model target unless the actual records establish that its definition, completeness and use are suitable. The field named shape will also not be assumed to mean print quality without source documentation. [Zenodo dataset record](https://zenodo.org/records/19602891)

## Data-science and polymer-informatics value

This project focuses on **data integration and experimental workflow quality**, rather than building another generic model. It applies data-science concepts to a polymer biomaterial:

- **Relational data modelling:** define what one record represents and how formulation, rheology and construct records relate.
- **Data provenance:** retain source filenames, identifiers and locations so an analysis can be traced back to the original record.
- **Unit and label harmonisation:** make equivalent concepts machine-readable without changing values unless a numerical conversion is documented and justified.
- **Missing-data semantics:** represent why a field is missing rather than filling absent values with zero.
- **Join validation:** quantify coverage and ambiguity instead of assuming matching labels establish identity.
- **Experimental hierarchy:** avoid treating repeated measurement points from one curve or run as independent formulations.
- **Model validation:** assess independence and leakage risks before reporting predictive performance.

This complements two related materials-informatics capabilities: polymer structure-to-property modelling, and curation of experimental hydrogel rheology. The proposed third project extends the data story toward formulation, processing and application records.

## Relevance to materials research workflows

The project is designed to demonstrate practical skills that matter in research environments:

- building a documented data-ingestion workflow;
- organising materials and characterisation information into usable tables;
- checking data quality before analytics or machine learning;
- communicating what the evidence supports and what remains unresolved; and
- preparing data for future integration into broader experimental or materials databases.

This project cannot demonstrate hands-on polymer synthesis, development of measurement devices, lab automation or robotic experimentation. It focuses on the data and workflow component of materials research.

## Planned deliverables

Subject to the feasibility review, planned outputs may include:

- reproducible Jupyter notebooks for audit, schema design, validation and analysis;
- a source manifest and file inventory;
- a data dictionary and documented schema;
- a quality-control issue log and join-coverage report;
- standardised, derived tables where reuse terms allow publication;
- exploratory plots and a modelling-readiness assessment; and
- a GitHub README documenting methods, provenance, limitations and citations.

Original source files will not be republished unless dataset terms permit it. Code and documentation will distinguish source data from derived outputs.

## Scientific boundaries

- No sample, formulation or run linkage will be invented.
- No unit conversion or value correction will be made without a documented rule.
- No missing field will be treated as zero by default.
- No repeated measurement point will be counted as an independent formulation.
- No concentration or processing variable will be said to cause an outcome based only on descriptive association.
- No predictive model will be presented unless the target, links, sample size and validation design support it.
- The source authors’ generative-AI model will not be represented as work produced by this project.

## Dataset and citation

- Zenodo dataset: [Dataset for Disentangled Generative AI-Guided Closed-Loop Optimization of Deposition Morphology for 3D Bioprinting Applications](https://doi.org/10.5281/zenodo.19602891)
- Associated article DOI: [10.1080/17452759.2026.2671497](https://doi.org/10.1080/17452759.2026.2671497)

Please consult the dataset record for its current files, version, attribution and reuse conditions before using or sharing data.


