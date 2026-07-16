# IBM Community Article Recommendation System

## Project Overview

This Udacity project builds a recommendation system for technical articles from
the IBM Watson Studio Community. The available data contains implicit feedback:
an interaction shows that a user opened an article, but it does not provide an
explicit rating or indicate whether the user liked the content.

The notebook compares complementary recommendation strategies for different
amounts of user history:

- rank-based recommendations for anonymous or new users;
- user-user collaborative filtering for users with interaction history;
- content-based recommendations derived from article titles; and
- article similarity from latent features learned through matrix factorization.

The submission boundary is this `project/` directory. The main deliverable is
the executed `Recommendations_with_IBM.ipynb`, including saved outputs and
written interpretation.

## Dataset

The project uses the course-provided IBM Community interaction dataset at
`data/user-item-interactions.csv`. No external download is required.

Verified source-data aggregates:

| Measure | Value |
|---|---:|
| User-article interactions | 45,993 |
| Unique article IDs | 714 |
| Unique article titles | 714 |
| Known hashed user identifiers | 5,148 |
| Rows with a missing user identifier | 17 |
| Modeled users after mapping missing identifiers to one `unknown_user` | 5,149 |

Repeated interactions remain meaningful in the exploratory and popularity
analysis. The collaborative-filtering matrix converts them to binary values:
`1` means that a user interacted with an article at least once, and `0` means
that no interaction was observed.

The expected Part I evaluation contract is:

| Notebook variable | Expected value |
|---|---:|
| `median_val` | 3 |
| `user_article_interactions` | 45,993 |
| `max_views_by_user` | 364 |
| `max_views` | 937 |
| `most_viewed_article_id` | 1429 |
| `unique_articles` | 714 |
| `unique_users` | 5,149 |
| `total_articles` | 714 |

Article IDs are handled consistently as integers in the notebook and local
tests. See [`data/README.md`](data/README.md) for schema, integrity, and data
handling notes.

## Notebook Workflow

### Part I: Exploratory Data Analysis

Inspect missing values and interaction distributions, map the missing user
identifiers, and calculate the rubric-required user, article, and popularity
statistics.

### Part II: Rank-Based Recommendations

Rank articles by interaction count and return both the top article IDs and the
corresponding titles. This strategy is also the cold-start fallback when no user
history is available.

### Part III: User-User Collaborative Filtering

Build a binary user-item matrix, identify similar users, and recommend unseen
articles. The improved method resolves similarity ties using neighbor activity
and ranks candidate articles by their interaction popularity.

### Part IV: Content-Based Recommendations

Transform the available article-title text with TF-IDF, reduce the text feature
space, evaluate KMeans cluster sizes, and recommend popular articles from the
most relevant content group. Titles are the only article text supplied with the
dataset.

### Part V: Matrix Factorization

Factorize the user-item matrix, evaluate reconstruction behavior across latent
feature counts, and use cosine similarity over reduced article representations
to identify related articles. The notebook must explain the selected latent
dimension and the limitations of evaluating on observed interactions.

## Repository Structure

```text
project/
├── README.md
├── Recommendations_with_IBM.ipynb
├── project_tests.py
├── top_5.p
├── top_10.p
├── top_20.p
└── data/
    ├── README.md
    └── user-item-interactions.csv
```

- `Recommendations_with_IBM.ipynb`: implementation, tests, figures, and written
  discussion.
- `project_tests.py`: Udacity-provided helper checks.
- `top_*.p`: expected rank-based recommendation fixtures used by the helper
  tests.
- `data/user-item-interactions.csv`: immutable project input data.

## Environment and Dependencies

The repository root owns the Python environment. It requires Python 3.11 or
newer and uses `pyproject.toml` plus `uv.lock` for reproducible dependency
resolution. The project relies on packages already declared there, primarily:

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn`
- `jupyter`, `notebook`, and `ipykernel`

Do not create a separate `requirements.txt` for this project.

## Setup and Interactive Run

From the repository root:

```bash
uv sync --locked
cd 5_Unsupervised_ML_and_Recommendation_Systems/project
uv run jupyter lab Recommendations_with_IBM.ipynb
```

Run the notebook from the `project/` directory because its dataset, test helper,
and pickle fixture paths are relative to that directory. In Jupyter, restart the
kernel and run all cells from top to bottom before reviewing the results.

## Headless Validation

To reproduce the validated run, execute and save the notebook with the locked
environment:

```bash
uv run jupyter nbconvert \
  --to notebook \
  --execute \
  --inplace \
  Recommendations_with_IBM.ipynb \
  --ExecutePreprocessor.kernel_name=python3 \
  --ExecutePreprocessor.timeout=1200
```

A valid final run must satisfy all of the following:

- the command exits with status `0`;
- every code cell has a sequential execution count;
- no cell contains a traceback or error output;
- every Udacity helper check and explicit assertion passes;
- the Part I values match the evaluation contract above;
- the cluster and latent-feature plots have saved outputs and written rationale;
- the content and SVD recommendation examples contain the requested results;
- the final discussion compares offline and online evaluation options.

Some supplied helper functions report a mismatch by printing a message instead
of raising an exception. Therefore, final validation must also confirm that the
saved outputs contain the expected passing remarks and no failing `Oops!`
message.

## Rubric Validation Contract

| Rubric area | Evidence required in the final notebook |
|---|---|
| Functionality and readability | Successful saved execution, passing checks, DRY functions, and docstrings |
| Exploration and ranking | Required aggregate values, interaction plots, top-ID function, and top-title function |
| Collaborative filtering | Binary user-item matrix, similar-user ranking, original and improved recommendations, and cold-start fallback |
| Content-based recommendations | TF-IDF title features, justified KMeans cluster size, and same-content recommendations |
| Matrix factorization | Factor matrices, latent-feature metric plot and rationale, SVD article similarity, and result discussion |

**Validation status: complete.** The final notebook was executed twice from a
clean Python 3.11.13 kernel: first to a temporary audit copy and then in place.
Both runs completed in 11-15 seconds and produced semantically identical
sources, outputs, and execution counts.

### Validated Run Summary

| Result | Validated value |
|---|---:|
| Executed code cells | 29 of 29 |
| Notebook error outputs / stderr streams | 0 / 0 |
| Final aggregate checks | 12 of 12 passed |
| Pseudonymous user hashes in saved outputs | 0 |
| Plot outputs with descriptive alternative text | 4 of 4 |
| User-item matrix | 5,149 x 714 |
| User-item density | 0.9162% |
| TF-IDF / LSA shapes | 714 x 125 / 714 x 50 |
| LSA explained variance | 76.00% |
| Selected KMeans clusters | 50 |
| Median / minimum articles per selected cluster | 10.5 / 4 |
| Selected SVD latent features | 200 |
| SVD explained variance at 200 features | 82.29% |
| Reconstruction precision / recall / F1 at 200 | 1.0000 / 0.8456 / 0.9164 |

All supplied helper checks emitted their passing remarks. Explicit assertions
also verify exact popularity order, binary matrix shape and values, expected
neighbor IDs, cold-start behavior, unseen-item constraints, content candidates,
the exact SVD article order, and the deployment-facade smoke test.

## Evaluation Strategy and Limitations

The notebook's supplied checks validate deterministic intermediate results, but
they do not measure whether recommendations improve user outcomes. A production
evaluation should use a time-aware interaction holdout and ranking metrics such
as precision at `k`, recall at `k`, hit rate, catalog coverage, and novelty. An
online A/B test could compare click-through rate, article completion or dwell
time, and repeat engagement while monitoring coverage and latency guardrails.

Important limitations include:

- interactions are implicit feedback and do not prove user satisfaction;
- the matrix is sparse and dominated by non-interactions, so accuracy alone can
  be misleading;
- offline reconstruction on observed data can overestimate generalization;
- content recommendations use short titles rather than abstracts or article
  bodies;
- the local catalog contains only articles represented in the supplied data;
- popularity is useful for cold start but can reduce novelty and catalog
  exposure.

## Potential Extensions

The notebook includes a documented `IBMArticleRecommender` facade that reuses
the validated functions for known-user, cold-start, content, and latent
recommendations. A future iteration could move that facade into a small Python
package or web application while retaining the notebook as its executable model
card and evaluation report.

## Acknowledgements

The project scenario, interaction dataset, test helpers, and expected fixtures
are provided as part of the Udacity Data Scientist Nanodegree materials and are
based on IBM Watson Studio Community article interactions.
