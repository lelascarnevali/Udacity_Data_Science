# Udacity Data Scientist Nanodegree

This repository contains the projects and exercises developed as part of the **Data Scientist Nanodegree program** by Udacity. Throughout this program, core data science skills are developed — from supervised machine learning and software engineering best practices to pipelines, unsupervised learning, and recommendation systems.

## Program Overview

The Nanodegree is divided into four main courses (plus an introductory module):

### 2. Introduction to Data Science and Supervised Machine Learning
Learn core data science concepts and apply supervised machine learning models in real projects. Build your portfolio, master evaluation techniques, and gain practical skills to stand out in data-driven careers.

- **The Data Science Process:** CRISP-DM process and how to apply it to data science problems.
- **Supervised Machine Learning Algorithms:** Regression, classification, linear models, decision trees, random forests, and neural networks with scikit-learn.
- **Model Evaluation:** Alternative metrics beyond default accuracy for real-world datasets.
- **Model Interpretability and Fairness:** Feature importances, SHAP values, and the Aequitas framework.
- **Communicating to Stakeholders:** GitHub repository and Medium blog post.
- **Project: Data Science Blog Post**

### 3. Software Engineering for Data Scientists
Prepare for advanced data science work with software engineering best practices. Explore OOP, testing, reproducibility, and build a FastHTML dashboard.

- **Object-Oriented Programming:** Classes, instances, magic methods, inheritance, and polymorphism.
- **Code Reproducibility:** Virtual environments, Python packages, file paths, testing, and linting.
- **Data Science Dashboards:** Web servers, web forms, dynamic endpoints, and interactive dashboards with FastHTML.
- **Project: Data Science Dashboard**

### 4. Data Science Pipelines
Streamline complex machine learning projects by designing pipelines that combine preprocessing, modeling, and evaluation.

- **Scikit-Learn Pipelines:** Efficient data workflows, preprocessing, feature engineering, and model optimization.
- **Computer Vision Pipelines:** Image preprocessing, feature extraction, and classification with OpenCV and PyTorch.
- **NLP Pipelines:** Text features, tokenization, vectorization, and part-of-speech tagging with spaCy.
- **Project: Data Science Pipeline**

### 5. Unsupervised Machine Learning and Recommendation Systems
Advanced data science topics: unsupervised learning, clustering, dimensionality reduction, and recommendation systems.

- **Clustering:** K-means algorithms, metrics, and applications.
- **Dimensionality Reduction:** Fundamentals and visualization with scikit-learn and matplotlib.
- **Recommendation Systems:** Ranking-based, content-based, and collaborative filtering approaches.
- **Unsupervised Model Evaluation:** Evaluating clustering, dimensionality reduction, and recommendation systems.
- **Project: Recommendation System**

---

## Quickstart

Get up and running fast on macOS with `uv` and Jupyter:

```bash
# Clone and enter repository
git clone git@pessoal.github.com:lelascarnevali/Udacity_Data_Science.git
cd Udacity_Data_Science

# Create and activate Python virtual env
uv venv --python 3.11 .venv
source .venv/bin/activate

# Install dependencies and Jupyter
uv pip install -r requirements.txt
uv pip install jupyter

# Launch notebooks
jupyter notebook
# or
jupyter lab
```

## Environment Setup

This project uses **[uv](https://github.com/astral-sh/uv)** for fast Python package management.

### Prerequisites

- **uv installed:**
  ```bash
  # macOS/Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone git@pessoal.github.com:lelascarnevali/Udacity_Data_Science.git
   cd Udacity_Data_Science
   ```

2. **Create a virtual environment:**
   ```bash
   uv venv --python 3.11 .venv
   ```

3. **Activate the environment:**
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`

4. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   uv pip install jupyter
   ```

## Repository Structure

```
.
├── 2_Introduction_to_Data_Science_and_Supervised_ML/
│   ├── exercises/          # Notebooks and scripts for hands-on practice
│   └── project/            # Project: Data Science Blog Post
├── 3_Software_Engineering_for_Data_Scientists/
│   ├── exercises/          # Notebooks and scripts for hands-on practice
│   └── project/            # Project: Data Science Dashboard
├── 4_Data_Science_Pipelines/
│   ├── exercises/          # Notebooks and scripts for hands-on practice
│   └── project/            # Project: Data Science Pipeline
├── 5_Unsupervised_ML_and_Recommendation_Systems/
│   ├── exercises/          # Notebooks and scripts for hands-on practice
│   └── project/            # Project: Recommendation System
├── requirements.txt
└── .gitignore
```

---
*Each project in this repository represents a hands-on application of the concepts learned, reinforcing job-ready skills in the field of Data Science.*
