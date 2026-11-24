# Background and scientific boundaries

[← Back to project README](../README.md)

This page holds the project rationale, scientific context and boundaries that previously sat in the main README.

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


## Linked workflow

Each phase has an input, checks, output, and exit condition. The output from one phase becomes a controlled input to the next. This prevents later plots or models from depending on undocumented joins or guessed unit conversions.

## Concepts that connect the phases

- **Data granularity:** define whether a row represents a formulation, sample, experiment, point, run, construct, or image. This guides schema design, summaries, joins, and validation splits.
- **Provenance and lineage:** preserve source identifiers, versions, units, query details, and transformations. This begins in Phase 0 and remains attached through every later output.
- **Missingness semantics:** distinguish zero from unknown, not measured, not reported, not applicable, or unavailable. This affects QC and model feature selection.
- **Standardization:** normalize names and units only with documented rules; keep raw source values available for review.
- **Experimental hierarchy:** points from one curve and images from one run are nested records, not necessarily independent materials. This matters for uncertainty and model evaluation.
- **Leakage control:** related records must not be split carelessly between training and testing. The split should reflect the intended future prediction and the true independent unit.
- **Exploration versus causation:** patterns can motivate hypotheses but do not isolate causal effects when formulation, process, and conditions vary together.

## Scientific boundaries

- Materials Project records remain computational and separate from hydrogel experimental data.
- Matbench scores demonstrate benchmark practice, not hydrogel-model validity.
- GEMD guides representation but cannot supply missing source evidence.
- No physical sample or experiment link will be invented.
- Missing values will not be replaced by zero without source justification.
- Unit conversions and derived variables will be traceable to original values.
- Repeated rheology points will not be counted as independent formulations.
- Rheology and images alone will not be used to infer cell viability, tissue function, or clinical performance.
- Image brightness, contrast, edge density, foreground area and thumbnail-hash similarity are screening descriptors, not validated material-performance metrics.
- Duplicate-image cues must be reviewed before any future image-based modelling split.
- Missing image metadata will remain missing evidence unless the source record supplies a value.
- Observational patterns will not be described as causal effects of polymer chemistry or concentration.
- Modelling will proceed only if the target, independent sample size, record linkage, predictors, and evaluation design support it.
- The project does not claim new polymer synthesis, instrument or sensor development, robotics, or biological testing.

These boundaries shape the source audit, schema, joins, plots, and modelling decision from the beginning.

## Success criteria

The workflow should be able to answer, with evidence: Where did each value originate? What does each row represent? Which values are experimental, computational, derived, or benchmark data? What material, formulation, process, and measurement conditions are documented? Which records can be linked, and which relationships remain uncertain? Which transformations and QC decisions were applied? Which observations are independent? What comparisons are scientifically appropriate? Is there a meaningful, leakage-safe prediction target? What does the dataset support, and what remains unknown?
A finding that the source data are not yet ready for hydrogel machine learning can still be a useful result. It identifies the data gaps that future experiments or repositories need to address.
