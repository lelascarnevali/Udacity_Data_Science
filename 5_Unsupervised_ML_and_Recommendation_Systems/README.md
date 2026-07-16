# Course 5: Unsupervised Machine Learning and Recommendation Systems

Advanced data science topics related to unsupervised machine learning. Apply techniques including clustering and dimensionality reduction, then learn about different strategies for generating personalized recommendations. The final lesson covers practical advice for data scientists using unsupervised models in the real world, including how to test them both "online" and "offline".

**Estimated time:** ~17h 30min

## Lessons

| # | Lesson | Description |
|---|--------|-------------|
| 1 | Clustering | Unsupervised learning in data science: clustering techniques, k-means algorithms, metrics, and applications |
| 2 | Dimensionality Reduction | Fundamentals of dimensionality reduction; scikit-learn and matplotlib to calculate and visualize the process |
| 3 | Recommendation Systems | Different methods used to create recommendation engines with Python |
| 4 | Unsupervised Machine Learning Model Evaluation | Evaluating clustering, dimensionality reduction, and recommendation systems |

## Project

**Project: Recommendation System**

The project implementation builds recommendations for technical articles from
the IBM Watson Studio Community using rank-based recommendations, user-user
collaborative filtering, TF-IDF and KMeans content groups, and SVD article
similarity. It also documents cold-start behavior and offline and online
evaluation strategies.

See [`project/README.md`](project/README.md) for the dataset, environment setup,
execution commands, rubric contract, and validation status.

## Structure

```
.
├── exercises/                              # Course practice notebooks and data
└── project/
    ├── README.md                           # Project guide and validation contract
    ├── Recommendations_with_IBM.ipynb      # Main project notebook
    ├── project_tests.py                    # Udacity helper checks
    ├── top_5.p, top_10.p, top_20.p         # Rank-based test fixtures
    └── data/
        ├── README.md                       # Dataset documentation
        └── user-item-interactions.csv      # IBM Community interactions
```
