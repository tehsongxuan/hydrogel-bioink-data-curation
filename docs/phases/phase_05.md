# Phase 5 — Rheology and printing-context exploratory analysis

[← Back to project README](../../README.md)

- Notebook: [`notebooks/05_hydrogel_rheology_and_printing_context_analysis.ipynb`](../../notebooks/05_hydrogel_rheology_and_printing_context_analysis.ipynb)
- Executed report: [`reports/05_hydrogel_rheology_and_printing_context_analysis.html`](../../reports/05_hydrogel_rheology_and_printing_context_analysis.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/05_hydrogel_rheology_and_printing_context_analysis.html)

## Scope and method

**Question:** What patterns occur in validated, comparable measurements?
Plot shear-dependent viscosity against shear rate and describe whether the observed curve is consistent with shear-thinning over the measured range. Plot `G′` and `G″` against the source’s measured variable when test conditions allow comparison. Keep individual experiments visible and group summaries at the correct level; do not treat curve points as independent samples.
A derived value such as `tan δ = G″/G′` should be calculated only when both moduli are available and compatible. Record the formula, retain source values, and leave the result undefined when the denominator is zero. Do not alter a measurement to make a derived column complete.
Explore image and printing metadata only if source-defined identifiers link them to rheology or formulation. Define what each image label represents. A requested shape, image category, and validated print-quality outcome are not interchangeable. Describe associations rather than causal effects; unrecorded conditions may explain observed differences.
**Data-science concept:** exploratory analysis describes distributions, coverage, variation, and possible relationships before inference. **Polymer concept:** viscosity, `G′`, and `G″` describe different aspects of flow and viscoelasticity; their printing relevance depends on test and process conditions.
**Output and handoff:** reproducible figures, tables, and a written interpretation with comparability limits. These inform model readiness in Phase 12. Exit when each plot states the source population, unit, condition, and experimental unit.

## Phase 5 implementation status

The original Phase 5 scope and handoff statement above are retained. The submitted `05_hydrogel_rheology_and_printing_context_analysis.ipynb` and matching HTML export document a completed descriptive-analysis checkpoint using the verified Phase 4 evidence layer. The notebook ran in the selected Windows `Python (hydrogel-bioink)` environment, producing the named outputs below. These results refer to that executed run; they are not an independent verification of physical-sample identity or a predictive model.

The implemented workflow includes:
- a kernel-specific start-up check for NumPy, pandas, Matplotlib and IPython, with a bounded one-time Matplotlib installation attempt when it is missing; the executed report says Matplotlib was already available in this particular run;
- documented project-root discovery and controlled input resolution for all ten required Phase 4 CSV/JSON files;
- source-provenance, field-presence, record-count and output-validation checks;
- distinction among 39,100 source-cell evidence rows, 4,600 measurement points and 92 source rheology worksheets, so nested observations are not mistaken for independent formulations;
- exploratory steady-shear curves, log-scale eligibility screening and worksheet-level apparent shear-thinning diagnostics;
- storage modulus `G′`, loss modulus `G″` and valid loss-tangent `tan δ = G″/G′` exploration in the recorded oscillatory strain context;
- summaries of candidate material-name tokens extracted from source filenames without turning them into confirmed formulation IDs;
- independent descriptive analysis of the 1,031 image-index metadata records, without assuming a rheology-to-image join;
- explicit QC propagation, missingness summaries, independent-observation checks, plotting exclusions and unresolved-boundary documentation;
- 25 PNG scientific figures, saved to `figures/`, plus an offline HTML figure gallery; only four previews appear inline to reduce Jupyter display load;
- 20 CSV analysis exports, one JSON run manifest and one generated Markdown summary; and
- a persistent execution-progress log for local troubleshooting, which is **not** a public research deliverable.

## Phase 5 verified results and scientific interpretation

| Phase 5 item | Result in submitted executed notebook | Scientific meaning |
|---|---:|---|
| Required Phase 4 inputs | 10 | Controlled tables and manifest read from the preceding verified evidence layer. |
| Source measurement-cell evidence | 39,100 rows | Original source-cell granularity; **not** 39,100 independent samples. |
| Rheology measurement points | 4,600 rows | 2,300 steady-shear points and 2,300 oscillatory points, nested within worksheets. |
| Source rheology worksheets | 92 | Digital worksheet acquisitions; independent physical specimens have not been established. |
| Image-index metadata | 1,031 records | Categorical and date metadata only; source image pixels were not audited. |
| Candidate filename-linkage records | 62 | Candidate naming correspondence; none confirms a physical sample or rheology-to-image relationship. |
| Carried QC finding records | 25 | Review findings are retained; the number is not a sample count. |
| Measurement points with propagated QC flags | 415 | Flagged source points retained for transparency, rather than silently removed. |
| Unresolved linkage-review entries | 11 | Experimental comparability and identity questions remain open. |
| Steady-shear points eligible for positive log–log plot | 2,280 of 2,300 | 20 source points excluded **from that logarithmic visualisation**, not deleted from curated data. |
| Oscillatory points shown in positive moduli log–log plot | 2,300 | Exploratory point coverage, not confirmation of a linear viscoelastic region. |
| Scientific figures | 25 PNG files | All saved to disk; the notebook shows four selected previews to avoid overloading Jupyter. |
| Analysis outputs | 20 CSV files | Generated population summaries, exploratory curve statistics and QC tables. |
| Additional documentation | 1 HTML gallery, 1 JSON manifest, 1 Markdown summary | Browsable figures and reproducible computational handoff. |
| Phase 5 validation checks | 86 passed | Internal code/data contracts passed in the reported run. |
| Critical validation failures | 0 | Does not resolve outstanding sample, unit or printability questions. |
| Supervised model or validated printability target | Not created | Independent sample units and a defensible training target have not been established. |

### Data-science rationale

**Exploratory analysis and observational hierarchy.** Curves are made of repeated points, and multiple curves can arise from related material preparations. Phase 5 therefore reports results at the point and worksheet levels separately. Counts from `measurement_point_linkage_layer.csv` and source-cell evidence do not establish a dataset with thousands of independent formulations. Treating those points as independent training samples would risk pseudoreplication and optimistic model validation.

**Audit before plotting.** Each log-scale rheology figure requires positive, finite inputs. Twenty steady-shear source points do not satisfy the relevant log–log plotting conditions and are recorded as exclusions for that plot. They remain available in the curated source and QC evidence. A plotting mask is not a silent decision to delete data or identify the cause of an unusual measurement.

**Descriptive slopes are screening measures.** Per-worksheet log–log viscosity slopes describe measured trends over the source acquisition range; they are not fitted constitutive-law parameters validated across material batches. The analysis preserves worksheet-to-worksheet variation and does not claim that apparent trends are chemically causal.

**Provenance-aware visualisation.** The figure atlas includes worksheet coverage, field completeness, QC prevalence, evidence hierarchy, candidate linkage status and source-label coverage. Such diagnostics show what is actually available for analysis, rather than merely making attractive plots. The input manifest and hashes document the Phase 4 data consumed in the run.

**Metadata is not ground truth.** Image-index shape names, reported ink-type strings, irradiation-intensity tokens and dates can be tabulated without claiming to have analysed image pixels, printing performance, geometric fidelity, nozzle conditions or a physical sample-to-image link. The source date field is not assigned a fabricated experimental-event meaning.

### Polymer science, hydrogel rheology and printing-context interpretation

**Steady-shear flow.** Apparent viscosity changes with shear rate and may decrease over the recorded range. A decreasing viscosity curve is consistent with shear-thinning in that measurement window. It is relevant to extrusion-based bioink processing, but alone cannot demonstrate a usable extrusion pressure, structural recovery after deposition or printability. The original `mPas` token remains unresolved and has **not** been converted to Pa·s.

**Oscillatory viscoelastic response.** Storage modulus `G′` represents an elastic response, while loss modulus `G″` represents viscous energy dissipation during oscillation. The submitted dataset's oscillatory analysis treats variation against recorded strain, with a recorded 1 Hz frequency for the reviewed modulus worksheets. These observations are not recast as frequency sweeps. `G′ > G″` at a given point suggests elastic predominance under those measured conditions; it does not by itself establish a gel point, yield stress, print fidelity or a validated linear viscoelastic region.

**Loss tangent.** Where compatible positive values exist, `tan δ = G″ / G′` gives a dimensionless relative measure of viscous and elastic response. A larger tan δ indicates a greater dissipative component *relative to elastic storage* at those conditions. It is undefined when the denominator is zero. Comparing tan δ between unlinked worksheets as if they represented replicates of the same formulation would be unsupported.

**Polymer and process variables.** Alginate and hyaluronic-acid formulation labels are useful for organising review, but source filename tokens are not independently validated composition records. Concentration, chemical modification, crosslinking, processing sequence and thermal history may affect the rheology; an observed difference cannot be attributed to one factor when those factors and physical-sample identities are incompletely linked.

**Printing context.** The source image-index categories describe metadata associated with reported constructs. Their distribution is not a print-quality measurement. Without auditing `images.zip`, measurement protocols, sample identity and source-defined print-quality criteria, Phase 5 does not claim printability prediction, causal formulation–printing relationships, printed geometry accuracy or biological outcomes.

### Phase 5 outputs and handoff

The executed notebook writes its local scientific outputs to:

`data/processed/hydrogel_rheology_and_printing_context_analysis/`

In the **local analysis directory**, `figures/` contains 25 generated PNG files and the 20 CSV files preserve the exploratory tables. The notebook additionally produces `phase5_run_manifest.json` and `phase5_readme_summary.md`. The individual PNGs and CSVs are not necessarily separate public repository files. The current public-facing `phase5_figure_gallery.html` **embeds all 25 graphs directly within one browser-viewable HTML page**, as shown in the reviewed browser screenshot; it therefore does not require a separate public `figures/` folder. The figure gallery complements, rather than replaces, the executed notebook HTML report. The inclusion of source-derived plots in a publicly accessible HTML page remains subject to a data-reuse and publication-rights review.

The computational and scientific handoff to the completed Phase 6 image-file audit includes: documented populations, QC eligibility rules, point/worksheet hierarchy, safe interpretation boundaries and pending sample-linkage questions. Phase 6 audits actual construct image files as an image-evidence layer; Optional Phase 7 can examine the source authors’ model artefacts. Neither extension should reinterpret filename candidates as verified specimen IDs or assume that Phase 5 has produced a supervised training set.

### Phase 5 visualisations — browser viewing

**Figures:** [View Phase 5 figures in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/data/processed/hydrogel_rheology_and_printing_context_analysis/phase5_figure_gallery.html) renders the complete 25-graph gallery directly from `phase5_figure_gallery.html`, with the images embedded and accompanied by scientific context. The separate PNG files are not required to view this page.

**Executed scientific report:** [View HTML report in browser — Phase 5 exploratory analysis](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/05_hydrogel_rheology_and_printing_context_analysis.html) renders the notebook export at `reports/05_hydrogel_rheology_and_printing_context_analysis.html`, including the methodology, code, tables, results and four inline previews. It is a different HTML page from the 25-graph gallery.

**Publication boundary:** The 25 embedded plots appear to be accessible through the public GitHub HTML viewing link. This technical availability does not establish the right to redistribute source-derived content: the source dataset's reuse conditions remain under review. If public release is not authorised, replace the public gallery with a descriptions-only version while preserving the complete version locally. Earlier Git commits may also retain previous versions.

### Phase 5 figure categories

| Category | Figure coverage | Interpretation |
|---|---|---|
| Dataset and hierarchy | Measurement family, worksheet counts, observation levels and field-completeness heatmap | Shows where the scientific evidence comes from and which variables are available. |
| Steady-shear behaviour | Log–log viscosity, individual curves, shear stress, exploratory slopes and exclusion/QC counts | Screens flow properties without claiming a validated constitutive model or printability. |
| Oscillatory mechanics | `G′`, `G″`, tan δ, modulus balance, scatterplot and individual worksheet curves | Distinguishes energy storage and dissipation under recorded test conditions. |
| Candidate naming and linkage | Source-label coverage, presence/absence and filename-linkage status | Candidate labels only; no confirmed physical sample or rheology–image links. |
| Printing/image metadata | Shape, ink type, intensity token, cross-tabulation, annotation missingness and date coverage | Describes index fields, not image pixels, print fidelity or validated quality. |
| Quality control | QC prevalence, measurement field completeness and plot-eligibility diagnostics | Keeps exclusions and scientific uncertainty visible and reproducible. |

The [Phase 5 publication checkpoint and local-output register](../project_log.md#github-publication-phase-5-checkpoint) preserve the complete original file inventory and descriptions without adding broken links to missing individual PNG or CSV files. The earlier **52-item plan** is retained as planning history: the stand-alone `requirements-phase5.txt` item has been withdrawn because dependencies are documented in this README. The 25 embedded figures already visible in the public HTML remain subject to a source-data reuse-rights review.
