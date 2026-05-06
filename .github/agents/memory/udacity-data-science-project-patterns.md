---
date: 2026-05-06
topic: Udacity Data Science project scaffolding patterns
topics: [udacity, data-science, project-structure, notebook, README, blog]
source: local reference repos Udacity_Generative_AI and Udacity_Agentic_AI
---

# Agent Memory Entry

- **Date:** 2026-05-06
- **Topic:** Udacity Data Science project scaffolding patterns
- **Source:** `Udacity_Generative_AI`, `Udacity_Agentic_AI`, and `Udacity_Data_Science`

## Context

The Data Science course 2 project folder was scaffolded for the Udacity
`Data Science Blog Post` project using patterns from the user's completed
Udacity Generative AI and Agentic AI repositories.

## Key Insights

- The strongest recurring pattern is a project-level `README.md` that acts as
  the evaluation contract: objective, rubric mapping, setup, file inventory,
  expected outputs, and final result summary.
- Notebook-first projects keep the main notebook in the project root and align
  sections directly to the Udacity rubric.
- Reference projects use `docs/` for study notes, `data/` for small or
  reproducible inputs, `images/` for visual evidence, and `evidence/` for
  curated execution proof.
- Technical work belongs in GitHub/README/notebook; stakeholder communication
  belongs in a short blog draft with plain language and visuals.
- Data Science projects should keep preprocessing inside scikit-learn pipelines
  to avoid leakage and to make categorical/missing-value handling auditable.
- Course 2 project notebooks should visibly reuse the exercise techniques:
  EDA with `describe`/histograms/correlation, `train_test_split`, dummy
  baselines, decision trees, classification metrics, model feature signals, and
  group-level performance review.

## Decisions / Rules

1. Use the existing course `project/` folder as the submission boundary.
2. Keep the main notebook in the project root unless the rubric requires a
   different file layout.
3. Add `docs/`, `data/raw/`, `data/processed/`, `blog/`, `images/`, `evidence/`,
   and `src/` only when they serve a clear project or submission purpose.
4. For Udacity Data Science blog projects, keep code notebook-contained unless
   extraction is necessary; the rubric expects executable notebook code.
5. Do not commit raw CMS CSVs or generated processed CSVs when the notebook can
   regenerate them from official metadata.
6. Capture durable project patterns both in repo memory and the private Obsidian
   vault; do not copy private vault notes into repo content.

## References

- `2_Introduction_to_Data_Science_and_Supervised_ML/project/README.md`
- `2_Introduction_to_Data_Science_and_Supervised_ML/project/docs/project_patterns.md`
- `2_Introduction_to_Data_Science_and_Supervised_ML/project/cms_hospital_quality_analysis.ipynb`

## Next Actions

- After the CMS notebook is executed, update the README and blog draft with
  concrete statistics, final charts, model metrics, and limitations.
- Consider adding similar project memory entries after courses 3, 4, and 5 are
  implemented.

## 2026-05-06 Refinement Note

The CMS notebook went through four data-scientist review loops:

1. aligned the notebook to exercise techniques;
2. separated validation model selection from final test reporting;
3. added model interpretation, group performance checks, and exported evidence;
4. created `project_results.json` and updated README/blog with concrete numbers.

After user review, the project folder was simplified back to the course-project
pattern:

```text
project/
  README.md
  cms_hospital_quality_analysis.ipynb
  blog_post_draft.md
  data/
  images/
```

Do not add separate `docs/`, `evidence/`, or `src/` folders for this course 2
project unless the user asks. Keep feature importance and bias notes inside the
notebook/README.

## 2026-05-06 SHAP / Aequitas Correction

User review caught that the first correlation chart used mostly constant CMS
measure-count columns and did not clearly explain feature importance or bias.
The notebook was corrected to:

- select numeric features with real variation before correlation analysis;
- use SHAP for feature importance on the selected model;
- use Aequitas `Group` and `Bias` crosstabs/disparity metrics for hospital type
  and ownership groups;
- add interpretation cells directly in the notebook rather than adding extra
  project folders.
