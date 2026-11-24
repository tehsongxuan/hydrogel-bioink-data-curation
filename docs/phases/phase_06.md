# Phase 6 — Image-file audit and computer-vision readiness

[← Back to project README](../../README.md)

- Notebook: [`notebooks/06_image_file_audit_optional.ipynb`](../../notebooks/06_image_file_audit_optional.ipynb)
- Executed report: [`reports/06_image_file_audit_optional.html`](../../reports/06_image_file_audit_optional.html) · [view in browser](https://htmlpreview.github.io/?https://github.com/tehsongxuan/hydrogel-bioink-data-curation/blob/main/reports/06_image_file_audit_optional.html)

## Scope and method

**Question:** Do the physical image files match the curated `image_index.csv` metadata, and are they suitable for later exploratory computer-vision analysis?

This optional phase uses the locally retained `images.zip` archive rather than repeated large uploads. The archive contains the printed-construct image files used by the source dataset, and the audit checks whether the expected filenames match the image-index records, whether the images are readable, and whether the image metadata has enough coverage for cautious exploratory review.

**Data-science concept:** file-level audit, metadata linkage, image-feature engineering and leakage control must come before computer vision. The notebook treats every image as evidence with provenance, not as an automatic training example.

**Bioink concept:** hydrogel construct images can show visible morphology, shape context and imaging artefacts. They do not by themselves prove material performance, rheology, crosslinking success, printability, cell response or clinical relevance.

**Output and handoff:** image-file inventory, image-index match report, integrity checks, label-distribution summary and optional simple image features. Exit when image files and metadata can be traced without inventing image-to-rheology identity.

## Phase 6 implementation status

The original Phase 6 scope and handoff statement above are retained. The submitted `06_image_file_audit_optional.ipynb` and matching HTML export document a completed image-file audit using the verified Phase 4/5 context and the local `images.zip` archive. The notebook ran in the selected Windows `Python (hydrogel-bioink)` environment. These results refer to that executed run; they are not an independent verification of physical-sample identity, printability or biological outcome.

The implemented workflow includes:
- restart-kernel-safe project-root discovery and controlled input verification for the image archive, image-index CSV and available Phase 4/5 context files;
- direct ZIP integrity testing, file inventory construction and image suffix counting before image decoding;
- deterministic matching from `image_index.csv` records to archive filenames using documented identifier rules;
- Pillow-based image readability checks, dimensions, colour mode, hashes and thumbnail-derived descriptors;
- NumPy-safe image-feature extraction that avoids dependency failure from binary-incompatible `scikit-image` builds under NumPy 2.x;
- metadata completeness profiling for image ID, date, recorded ink type, recorded shape, irradiation-intensity token, `completeness_sam` and `contain_sps`;
- simple visual descriptors including brightness, contrast, edge-density cue and foreground-area fraction;
- duplicate and near-duplicate screening using exact hashes and thumbnail-hash cues;
- visual review panels grouped by recorded ink type, shape and irradiation intensity, plus panels for missing metadata, duplicate groups and unusual images;
- a figure register, validation summary, QC findings table, output inventory and run manifest.

## Phase 6 verified results and scientific interpretation

The executed Phase 6 run verified the expected image-evidence layer:
- `1,031` image-index metadata records were loaded.
- `1,031` image candidate files were present in `images.zip`, all with `.png` suffix.
- `0` image files were unreadable.
- `0` image-index records were unmatched to archive files.
- `0` archive-only image files were detected.
- `20` PNG figures and `25` supporting CSV/JSON/HTML outputs were generated.
- `10` of `10` validation checks passed, with `0` critical failures.
- `3` review-level QC findings were recorded: `2` duplicate or near-duplicate diagnostic groups, `943` missing `completeness_sam` values and `922` missing `contain_sps` values.

The metadata layer is useful but incomplete. The source image index contains `48` recorded `ink_type_ph` values, `4` recorded shape values and `7` recorded irradiation-intensity tokens. However, the two source annotation fields most suggestive of print completeness or SPS status are mostly blank in this run. Those blanks remain missing evidence, not negative labels and not values to fill by assumption.

### Phase 6 validation ledger

| Check | Status | Severity | Evidence |
| --- | --- | --- | --- |
| `images_zip_exists` | passed | critical | data/raw/zenodo_19602891/images.zip |
| `image_index_loaded` | passed | critical | 1031 records |
| `zip_integrity_test` | passed | critical | bad_member=None |
| `archive_has_image_files` | passed | critical | 1031 image files |
| `image_files_readable` | passed | warning | 0 unreadable image files |
| `image_index_archive_matching_complete` | passed | review | 0 unmatched; 0 multiple matches |
| `archive_only_images` | passed | review | 0 archive-only image files |
| `phase4_supporting_context_available` | passed | warning | data/processed/record_linkage_and_analysis_ready_evidence_layer |
| `phase5_supporting_context_available` | passed | warning | data/processed/hydrogel_rheology_and_printing_context_analysis |
| `scientific_boundary_preserved` | passed | critical | Notebook does not infer physical-sample identity, printability success, cell viability, tissue performance, or clinical outcomes from image features. |

### Phase 6 image-index metadata profile

| Field | Records | Present | Missing | Missing fraction | Unique non-missing values | Example values |
| --- | --- | --- | --- | --- | --- | --- |
| `image_id` | 1031 | 1031 | 0 | 0.000 | 1031 | 7586; 7587; 7588; 7589; 7590; 7591; 7592; 7593 |
| `date` | 1031 | 1031 | 0 | 0.000 | 18 | 2025/05/28; 2025/05/29; 2025/06/05; 2025/06/10; 2025/06/12; 2025/06/26; 2025/07/01; 2025/07/02 |
| `ink_type_ph` | 1031 | 1031 | 0 | 0.000 | 48 | ALG2.0; ALG1.0; ALG3.0; ALG4.0; ALG5.0; ALG1.5; ALG2.5; HA1.0 |
| `shape` | 1031 | 1031 | 0 | 0.000 | 4 | grid; star; ichou; nose |
| `intensity` | 1031 | 1031 | 0 | 0.000 | 7 | 1; 50; 100; 0; 75; 25; 10 |
| `completeness_sam` | 1031 | 88 | 943 | 0.915 | 1 | no |
| `contain_sps` | 1031 | 109 | 922 | 0.894 | 1 | no |

### Phase 6 QC findings

| Finding | Type | Severity | Evidence | Recommended action | Interpretation |
| --- | --- | --- | --- | --- | --- |
| `P6_QC_0001` | duplicate_or_near_duplicate_image_diagnostics | review | 2 duplicate diagnostic groups were detected. | Review exact and thumbnail-hash duplicate groups before any modelling split. | Duplicates can cause data leakage if the same visual evidence appears in both train and test sets. |
| `P6_QC_0002` | metadata_missing_values | review | Field completeness_sam has 943 missing values. | Retain missingness and avoid inventing labels or concentrations. | Missing metadata is part of the evidence layer and should not be imputed as source fact. |
| `P6_QC_0003` | metadata_missing_values | review | Field contain_sps has 922 missing values. | Retain missingness and avoid inventing labels or concentrations. | Missing metadata is part of the evidence layer and should not be imputed as source fact. |

### Data-science rationale

Phase 6 treats image files as a new evidence layer. In data-science terms, the notebook first asks whether every row in the metadata table can be traced to an actual file and whether every file can be opened reproducibly. Only after that audit does it compute basic descriptors. This sequence matters because image analysis without file provenance can create attractive but unreliable charts.

The simple descriptors are deliberately conservative:
- **brightness** and **contrast** summarise pixel intensity and can be affected by lighting, exposure, background and camera settings;
- **edge density** is a rough cue for boundaries and texture, not a validated measurement of filament quality;
- **foreground-area fraction** estimates how much of the thumbnail differs from the border-like background, but it is not a calibrated physical area;
- **duplicate cues** flag possible repeated visual evidence and protect future modelling from train/test leakage;
- **unusual-image flags** identify records for review before modelling or interpretation.

In simpler terms, the data-science task is to check whether the pictures and labels line up, then produce cautious screen-level summaries. It is not yet training a computer-vision model and it is not claiming a success/failure label.

### Polymer science, hydrogel and image-evidence interpretation

The source project concerns phenol-modified alginate and hyaluronic-acid hydrogel inks. In polymer-science language, recorded ink type, shape and irradiation intensity may relate to formulation, printed geometry and light-driven crosslinking context. Those concepts matter because hydrogel print appearance can depend on polymer concentration, network formation, viscosity, relaxation, strand spreading, collapse, swelling and imaging conditions.

Phase 6 keeps those ideas connected but bounded. A visible grid, star, ichou or nose shape can indicate that a recorded construct image exists and that the metadata label is plausible. It cannot prove that the ink had the desired storage modulus, that viscosity was optimal for extrusion, that the construct remained stable after printing, or that cells survived. The image descriptors therefore act as audit signals: they point to records worth reviewing, but physical interpretation still requires rheology, formulation, processing and biological evidence.

The useful conceptual link is:
- data science organises and screens the evidence;
- polymer science explains what the evidence might mean physically;
- scientific caution defines what the evidence cannot establish.

### Phase 6 interpretation guide

This notebook creates a defensible image evidence layer for the hydrogel bioink project.

Phase 6 supports:
- checking whether the original image archive is readable;
- counting image files in the archive;
- linking image-index metadata to actual files;
- recording metadata completeness and missingness;
- computing basic digital image properties such as dimensions, colour mode, brightness, contrast, edge density and foreground-area fraction;
- reviewing panels by recorded ink type, shape and irradiation intensity;
- reviewing panels for missing metadata, duplicate cues and unusual images;
- exporting traceable review items for ambiguous or unusual evidence.

How to read the richer visualisations:
- **Grouped image grids** show whether metadata labels such as ink type, shape or intensity are connected to plausible source images.
- **Feature heatmaps** show whether simple image descriptors vary across recorded metadata groups. They are scaled for visual comparison, not physical measurement.
- **Missing-metadata panels** identify source records where metadata review is needed instead of guessing.
- **Duplicate panels** protect later modelling from data leakage, where the same or near-same image appears in both training and testing evidence.
- **Unusual-image panels** collect very bright, dark, low-contrast or feature-outlying images for review before interpretation.

Phase 6 cannot prove by itself:
- that a printed construct is biologically successful;
- that one formulation is clinically better than another;
- that a rheology measurement and an image came from the same physical sample;
- that a computed image feature is a validated printability metric;
- that a bright, dark, high-foreground or low-contrast image is automatically a successful or failed hydrogel print;
- that missing concentrations, dates or labels can be filled in from assumptions.

The central principle is simple: data science organises and screens evidence, while polymer science determines the possible physical meaning and the limits of that evidence. This boundary makes the project more credible, not weaker.

### Phase 6 outputs and handoff

The Phase 6 handoff is an image-evidence audit package. It is appropriate for repository documentation, visual review and later model-readiness decisions, provided that source-image reuse conditions are checked before public release.

The generated output set contains:
- image-file and ZIP inventories;
- image-index profile and metadata completeness tables;
- metadata-to-archive linkage table;
- image integrity and image-feature tables;
- duplicate diagnostics and duplicate-image ID table;
- grouped feature summaries and visual review panel index;
- missing-metadata, duplicate-group and unusual-image review panels;
- validation summary, QC findings, data dictionary, output inventory and run manifest;
- 20 figures, including grouped example grids, heatmaps and review panels.

The next checkpoint can use this layer to decide whether image-derived analysis is scientifically defensible, whether duplicate records require exclusion before modelling splits, and whether metadata gaps block any intended supervised image task.

### Phase 6 visualisations — browser viewing

The generated `phase6_figure_gallery.html` is the safest way to inspect the Phase 6 visual evidence as a coherent set. It keeps figure titles, source populations, methods and limitations with the plots. Individual PNG upload is also reasonable for Phase 6 because several review panels are central evidence artefacts, but the original `images.zip` archive should not be committed to GitHub.

### Phase 6 figure categories

| Figure file | Title | Records analysed | Method | Scientific boundary |
| --- | --- | --- | --- | --- |
| `phase6_01_image_file_format_counts.png` | Image archive file-format counts | 1031 image candidate files | ZIP inventory grouped by file suffix | File suffix is a storage format cue, not a scientific measurement. |
| `phase6_02_image_index_matching_coverage.png` | Image-index to archive matching coverage | 1031 image-index records | Metadata-to-file matching using documented filename rules | File matching does not prove physical-sample identity. |
| `phase6_03_image_dimensions_scatter.png` | Readable image pixel dimensions | 1031 readable images | Pillow image metadata extraction | Pixel dimensions describe digital files, not physical print dimensions unless calibration metadata is available. |
| `phase6_04_metadata_missingness_map.png` | Image metadata missingness map | 1031 image-index records | Binary missingness display across selected metadata fields | Missingness records source availability only; missing values are not imputed. |
| `phase6_05_ink_type_distribution.png` | Ink-type Metadata Distribution | 1031 image-index records | Value counts for image_index.ink_type_ph | Metadata categories describe source labels; they are not automatically standardised experimental variables. |
| `phase6_06_printed_shape_distribution.png` | Printed-shape Metadata Distribution | 1031 image-index records | Value counts for image_index.shape | Metadata categories describe source labels; they are not automatically standardised experimental variables. |
| `phase6_07_irradiation_intensity_distribution.png` | Irradiation-intensity Metadata Distribution | 1031 image-index records | Value counts for image_index.intensity | Metadata categories describe source labels; they are not automatically standardised experimental variables. |
| `phase6_08_brightness_contrast_scatter.png` | Image brightness and contrast screening | 1031 readable images | Thumbnail grayscale intensity summary | Brightness and contrast may reflect imaging conditions as well as printed material appearance. |
| `phase6_09_foreground_area_by_shape.png` | Foreground-area fraction by recorded shape category | 1031 linked readable images | Border-background thresholding on thumbnail images | Foreground area is a computed descriptor and not a validated printability score. |
| `phase6_10_example_image_grid.png` | Example source image grid | 12 readable source images | First readable images loaded from the ZIP archive and displayed as thumbnails | The grid supports visual audit only and is not a representative statistical sample unless sampling is defined. |
| `phase6_11_source_processed_comparison.png` | Source versus processed image comparison | 4 readable source images | Thumbnail display, grayscale conversion, and border-background foreground mask | Preprocessing can change interpretation; the mask is a review tool, not a ground-truth segmentation. |
| `phase6_12_example_grid_by_ink_type.png` | Example Image Grid by Recorded Ink Type | 18 thumbnails from 6 ink_type_ph groups | Deterministic first-3 sampling from the most frequent linked readable ink_type_ph groups | Thumbnails are examples for audit only; group appearance may be affected by lighting, cropping, scale and source-image selection. |
| `phase6_13_example_grid_by_shape.png` | Example Image Grid by Recorded Shape | 12 thumbnails from 4 shape groups | Deterministic first-3 sampling from the most frequent linked readable shape groups | Thumbnails are examples for audit only; group appearance may be affected by lighting, cropping, scale and source-image selection. |
| `phase6_14_example_grid_by_irradiation_intensity.png` | Example Image Grid by Recorded Irradiation Intensity | 18 thumbnails from 6 intensity groups | Deterministic first-3 sampling from the most frequent linked readable intensity groups | Thumbnails are examples for audit only; group appearance may be affected by lighting, cropping, scale and source-image selection. |
| `phase6_15_feature_heatmap_by_ink_type.png` | Image Feature Heatmap by Recorded Ink Type | 308 linked readable images across 6 ink_type_ph groups | Median image descriptors by metadata group, min-max scaled per descriptor for visual comparison | Scaled heatmap shows descriptor patterns only; it does not establish causality, printability or biological performance. |
| `phase6_16_feature_heatmap_by_shape.png` | Image Feature Heatmap by Recorded Shape | 1031 linked readable images across 4 shape groups | Median image descriptors by metadata group, min-max scaled per descriptor for visual comparison | Scaled heatmap shows descriptor patterns only; it does not establish causality, printability or biological performance. |
| `phase6_17_feature_heatmap_by_irradiation_intensity.png` | Image Feature Heatmap by Recorded Irradiation Intensity | 1027 linked readable images across 6 intensity groups | Median image descriptors by metadata group, min-max scaled per descriptor for visual comparison | Scaled heatmap shows descriptor patterns only; it does not establish causality, printability or biological performance. |
| `phase6_18_missing_metadata_image_review_panel.png` | Image Review Panel for Rows with Missing Metadata | 18 linked readable images with missing metadata | Rows ranked by count of missing selected metadata fields | Missing metadata is source evidence, not a reason to invent labels or drop records automatically. |
| `phase6_19_duplicate_group_review_panel.png` | Duplicate and Near-duplicate Image Review Panel | 4 images from duplicate diagnostic groups | Exact SHA-256 and thumbnail-hash duplicate cues displayed as thumbnails | Duplicate cues require human review; visual hash matches may be repeated images, similar images or hash collisions. |
| `phase6_20_unusual_image_review_panel.png` | Unusual-image Review Panel | 18 linked readable images with screening flags or robust feature outliers | Review panel ranked by simple flags and robust outlier scores from thumbnail descriptors | Unusual-image flags are screening cues only; they may reflect imaging conditions rather than hydrogel behaviour. |
