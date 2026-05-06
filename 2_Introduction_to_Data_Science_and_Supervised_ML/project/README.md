# Udacity Project - Data Science Blog Post

## Project: CMS Hospital Quality Analysis

### Project Introduction

This project applies the CRISP-DM process to a public healthcare dataset from the
Centers for Medicare & Medicaid Services (CMS). The goal is to understand how
hospital characteristics and CMS quality measure counts relate to overall hospital
ratings, then build a simple supervised machine learning model that predicts
whether a hospital is highly rated.

This project was chosen because healthcare is closest to my current professional
background, and the CMS data offers a realistic tabular dataset with numeric
features, categorical attributes, missing values, and a real-world communication
challenge.

### Dataset

- **Source:** Centers for Medicare & Medicaid Services (CMS)
- **Dataset:** Hospital General Information
- **Dataset ID:** `xubh-q36u`
- **Landing page:** <https://data.cms.gov/provider-data/dataset/xubh-q36u>
- **Metadata endpoint:** <https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/xubh-q36u>
- **Data dictionary:** <https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf>

The notebook resolves the current CSV download URL from the CMS metadata endpoint
before loading the data. Raw data should be downloaded into `data/raw/` and treated
as reproducible source data, not as hand-edited project content.

### Business Questions

The analysis is organized around five stakeholder-facing questions:

1. How are CMS overall hospital ratings distributed across hospitals?
2. Do ratings differ by hospital type, ownership, emergency services, or birthing-friendly designation?
3. Which CMS measure fields are most associated with ratings, and which features matter most under SHAP?
4. Can a simple supervised model predict whether a hospital has a high rating?
5. Does Aequitas reveal different model behavior across hospital groups?

The notebook also includes a new hospital scenario prediction, as required by
the project instructions.

### CRISP-DM Workflow

1. **Business Understanding** - define questions and success criteria.
2. **Data Understanding** - load CMS data, inspect schema, missingness, distributions, and target availability.
3. **Data Preparation** - clean column names, coerce numeric fields, handle categorical and missing values.
4. **Modeling** - train baseline supervised models using scikit-learn pipelines.
5. **Evaluation** - compare accuracy, precision, recall, F1, ROC-AUC, and confusion matrix.
6. **Deployment** - communicate findings through this GitHub repository and a short blog post.

### Repository Structure

```text
project/
  README.md                              # Project overview, setup, rubric mapping
  cms_hospital_quality_analysis.ipynb    # Main CRISP-DM notebook
  blog_post_draft.md                     # Non-technical blog draft
  data/
    README.md                            # Data acquisition and storage policy
    raw/                                 # Downloaded CMS CSVs, not edited by hand
  images/
    *.png                                # Charts exported by the notebook
```

### Libraries

This project uses the environment defined at the repository root:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `scipy`
- `shap`
- `aequitas`
- `jupyter`

### Quick Start

From the repository root:

```bash
uv sync
source .venv/bin/activate
jupyter notebook
```

Open:

```text
2_Introduction_to_Data_Science_and_Supervised_ML/project/cms_hospital_quality_analysis.ipynb
```

Run the notebook top-to-bottom. The notebook downloads or refreshes the CMS CSV
from the official metadata endpoint.

### Project Evaluation Checklist

- [ ] README explains libraries, motivation, files, results, and acknowledgements.
- [ ] Notebook follows CRISP-DM from question definition through communication.
- [ ] Notebook contains 3-5 business questions and answers each with a visual, statistic, or table.
- [ ] Missing values are assessed and handled explicitly.
- [ ] Categorical variables are encoded through a scikit-learn preprocessing pipeline.
- [ ] Model evaluation reports accuracy, recall, precision, F1, and other relevant metrics.
- [ ] A new scenario is passed through the trained model for prediction.
- [ ] Blog post has a clear title, image, questions, findings, and non-technical language.

### Current Run Summary

The notebook smoke-test run completed successfully on the CMS dataset.

- CMS rows loaded: `5,426`
- Hospitals with numeric overall rating: `2,866`
- Hospitals without numeric overall rating: `2,560`
- Hospitals rated 4 or 5: `36.7%`
- Best validation model: `random_forest`
- Final test metrics: accuracy `0.720`, recall `0.688`, precision `0.603`, F1 `0.643`, ROC-AUC `0.788`
- Strongest SHAP signals: readmission, mortality, and safety measures marked as `better` or `worse`
- Aequitas check: false positive rates vary by hospital ownership group, so aggregate metrics need group-level review
- Example scenario prediction: `high-rated` with estimated probability `53.5%`

Generated charts are written to `images/` when the notebook is executed.

### Exercise Technique Alignment

The notebook was reviewed against the course exercises and now explicitly uses
the taught workflow: tabular EDA, histograms, correlation checks, train/validation/test
splits, a dummy baseline, a decision tree, sklearn classifiers, precision, recall,
F1, SHAP feature importance, and Aequitas group metrics.

Feature importance is handled with SHAP on the selected model. Bias review is
handled with Aequitas crosstabs and disparity metrics using hospital type and
ownership groups. Since the dataset is hospital-level rather than patient-level,
the bias section is framed as model behavior review, not a clinical fairness
audit.

### Acknowledgements

Data is provided by the Centers for Medicare & Medicaid Services (CMS). This
project is part of the Udacity Data Scientist Nanodegree.
