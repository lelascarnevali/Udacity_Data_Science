# Udacity Project - Data Science Pipeline

## Project: Fashion Forward Forecasting

### Project Introduction

This project builds a machine learning pipeline for StyleSense, an online women's
clothing retailer. The business problem is to predict whether a customer would
recommend a product when the recommendation flag is missing, using the rest of
the review record.

The final solution uses a reusable scikit-learn pipeline that combines text,
numeric, categorical, and engineered NLP features. Keeping preprocessing and
modeling together prevents data leakage and makes the trained object usable for
future inference.

### Dataset

- **Source:** Provided Udacity project dataset
- **Local file:** `data/reviews.csv`
- **Rows:** `18,442`
- **Target:** `Recommended IND`
- **Positive class:** customer recommends the product (`1`)
- **Negative class:** customer does not recommend the product (`0`)

Feature columns:

- `Clothing ID`: product identifier, treated as categorical
- `Age`: customer age
- `Title`: review title text
- `Review Text`: review body text
- `Positive Feedback Count`: number of users who marked the review helpful
- `Division Name`: product division
- `Department Name`: product department
- `Class Name`: product class

The current CSV has no missing values, but the pipeline includes imputers so it
can handle incomplete future records.

### Modeling Objective

Predict `Recommended IND` as a binary classification task. The dataset is
imbalanced: about `81.6%` of reviews are recommendations, so the project reports
accuracy together with balanced accuracy, precision, recall, F1, macro F1, and
ROC-AUC.

### Pipeline Workflow

1. Load and validate the review dataset.
2. Explore target balance, feature types, category behavior, and text lengths.
3. Split the data into stratified train and test sets.
4. Build a dummy majority-class baseline.
5. Build a full sklearn pipeline:
   - custom `ReviewFeatureBuilder` for combined text and NLP features;
   - numeric imputation and scaling;
   - categorical imputation and one-hot encoding;
   - TF-IDF vectorization for normalized review text;
   - logistic regression classifier.
6. Fine-tune the full pipeline with `GridSearchCV`.
7. Evaluate once on the held-out test set.
8. Demonstrate inference on new review examples, including a missing title.

### Repository Structure

```text
project/
  README.md                              # Project overview, setup, rubric mapping
  Fashion_Forward_Forecasting.ipynb      # Main notebook with the full ML pipeline
  data/
    README.md                            # Dataset notes and local data policy
    reviews.csv                          # Provided reviews dataset
```

### Libraries

This project uses the environment defined at the repository root:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
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
4_Data_Science_Pipelines/project/Fashion_Forward_Forecasting.ipynb
```

Run the notebook top-to-bottom. The notebook reads the local CSV at
`4_Data_Science_Pipelines/project/data/reviews.csv`.

### Project Evaluation Checklist

- [x] README explains the project motivation, files, data, setup, results, and acknowledgements.
- [x] Notebook is organized into clear sections with short markdown explanations.
- [x] Code uses named functions/classes and PEP 8-style naming.
- [x] A sklearn `Pipeline` performs preprocessing, feature engineering, tuning, training, and inference.
- [x] Numeric, categorical, and text features are processed separately and appropriately.
- [x] Missing values are handled inside the pipeline with imputers.
- [x] NLP processing includes text normalization, tokenization, engineered text features, and TF-IDF n-grams.
- [x] Training and testing data are separated before fitting the pipeline.
- [x] Fine-tuning uses cross-validation with `GridSearchCV`.
- [x] Evaluation reports accuracy, balanced accuracy, precision, recall, F1, macro F1, ROC-AUC, a classification report, and a confusion matrix.
- [x] The final fitted pipeline is used for new-record inference.

### Current Run Summary

The notebook was executed successfully end-to-end.

- Rows loaded: `18,442`
- Feature columns used: `8`
- Recommendation rate: `81.6%`
- Best cross-validation macro F1: `0.827`
- Best model: logistic regression inside the full preprocessing pipeline
- Best parameters:
  - `model__C`: `2.0`
  - `preprocess__text__max_features`: `10000`
  - `preprocess__text__min_df`: `5`
  - `preprocess__text__ngram_range`: `(1, 2)`
- Final test accuracy: `0.894`
- Final test balanced accuracy: `0.872`
- Final test precision: `0.961`
- Final test recall: `0.907`
- Final test F1: `0.933`
- Final test macro F1: `0.839`
- Final test ROC-AUC: `0.948`

### Results and Discussion

The tuned pipeline substantially outperforms the dummy majority baseline and
keeps minority-class performance visible through macro F1 and balanced accuracy.
The strongest feature signals are interpretable through logistic regression
coefficients, which are displayed in the notebook as top positive and negative
model associations.

Important limitations:

- The class distribution is imbalanced, so aggregate accuracy can overstate
  performance.
- `Positive Feedback Count` may reflect post-review popularity and should be
  monitored if used in production.
- The dataset is anonymized and already cleaned, so real production data may
  contain noisier missing values and unseen categories.
- Coefficients show model associations, not causal drivers of recommendations.

### Acknowledgements

The dataset and scenario are provided as part of the Udacity Data Scientist
Nanodegree project materials.
