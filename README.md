

# Aligning Large Language Models with an Organization's Culture, Values, and Goals

This repository contains the research code, publicly shareable experimental data, evaluation artifacts, and statistical analyses accompanying the paper:

> **Daniel Pascal Hefti and Tianxiang Lu.** “Trustworthy Large Language Models in Organisations: A Competence-Based Alignment Framework.” *Proceedings of the 2026 International Joint Conference on Neural Networks (IJCNN)*, IEEE World Congress on Computational Intelligence (WCCI 2026).

## Research Overview

Large language models (LLMs) increasingly influence strategic decision-making in organisations, yet their alignment with organisational culture, values, and goals (OCVG) remains underexplored. Existing bias mitigation techniques primarily address societal categories—such as gender, race, and religion—and offer limited relevance for small and medium-sized enterprises (SMEs) seeking to embed their unique ethos into AI systems.

This research proposes a novel, human-centred, competence-based approach for LLM alignment: adapting methods from competence management—traditionally used to align human behaviour with organisational expectations—to guide and evaluate LLM outputs. The approach centers around developing evaluation rubrics, providing explicit instructions, and rubric-driven assessment to ensure outputs are in accordance with OCVG.

**Key contributions:**
- Proposes and operationalizes a competence-based alignment framework for LLMs, tailored to organizational contexts.
- Demonstrates, via empirical study, that rubric-driven, competence-based instructions deliver a statistically significant improvement in OCVG alignment (Mann–Whitney U, p < .001; Rank Biserial Correlation rrb = .36) across diverse datasets and languages.
- Provides in-depth human validation, showing strong agreement (Pearson r = .71, p < .001) with automated rubric assessments based on a systematic sampling framework.
- Supplies transparent, reproducible workflows and artifact sharing for use by both researchers and practitioners.

These findings demonstrate that competence-based instructions offer a scalable, interpretable, and ethically grounded method for aligning LLMs with organizational values. The repository allows replication of main experiments using the provided public data and scripts.

## Abstract

Large language models (LLMs) increasingly influence strategic decision-making in organisations, yet their alignment with organisational culture, values, and goals (OCVG) remains underexplored. Existing bias mitigation techniques primarily address societal categories—such as gender, race, and religion—offering limited relevance for small and medium-sized enterprises (SMEs) seeking to embed their unique ethos into AI systems. Moreover, SMEs often lack the resources to implement complex alignment strategies. This study proposes a novel, human-centred approach: adapting methods from competence management—traditionally used to align human behaviour with organisational expectations—to guide and evaluate LLM outputs. Results show statistically significant improvements in alignment scores for treatment models across different datasets and languages (Mann–Whitney U, p < .001; Rank Biserial Correlation rrb = .36). Human validation of 8.73% of outputs confirmed strong agreement with automated evaluations (Pearson r = .71, p < .001), underscoring the reliability of our rubric-driven assessment. These findings demonstrate that competence-based instructions offer a scalable, interpretable, and ethically grounded method for aligning LLMs with organisational values.

## Repository Structure

- `dataset/`  
	- Contains public datasets used in experiments.
- `experiment/`  
	Contains scripts and data for running experiments, evaluating model responses, and sampling.
	- `CIA/` - Files required to use the Hercule model as an evaluator. 
    - `analysis/` - Contains statistical analysis scripts and results.
	- `evaluation` - Contains CSV files with grading from evaluator model.
	- `responses/` — Raw and joined model response CSVs, organized by phase.  
	- `sampling/` — Scripts for selecting models and responses for human evaluation.  

## Important Files
- **experiment\public_dataset_full-prompt.txt** - Prompt issued to LLMs including instruction for treatment group.
- **experiment\public_dataset_without_instruction-prompt.txt** - Prompt issued to LLMs without instruction for control group.
- **experiment\reference_answer.md** - Reference answer provided to evaluator LLM.
- **experiment\score_rubrics_en.json** - List of score rubrics used for evaluation.

## Main Scripts
- **experiment\experiment.py** - Runs experiment.
- **experiment\evaluation_with_reference_answer_[model-name].py** - Evaluates responses from experiment with reference answer.
- **experiment\evaluation_without_reference_answer_[model-name].py** - Evaluates responses from experiment without reference answer.
- **experiment\join_responses.py** - Joins all responses to facilitate downstream analysis.
- **experiment\analysis\with_reference_answer_[model-name]\generate_stats.py** - Analyzes and synthesizes results from experiment with reference answer.
- **experiment\analysis\without_reference_answer_[model-name]\generate_stats.py** - Analyzes and synthesizes results from experiment without reference answer.

## Getting Started

1. Clone the repository.
2. Install dependencies:
	 ```
	 pip install -r requirements.txt
	 ```
3. Run the scripts in the `experiment/` folder as needed, following the workflow described in the thesis.


## Project Purpose

The goal of this project is to evaluate and align large language models with organizational culture, values, and goals. It provides tools for automatic and human evaluation, statistical analysis, and reproducible experiments.

**Remark:** To guarantee transparency of the research, the files in this repository reflect the exact scripts used during the public phase of the experiments. The code is script-based and does not necessarily follow best practices in software engineering (e.g., clean code, modularity, reusability).

## Citation

If you use this repository or its methods, please cite:

```bibtex
@inproceedings{hefti2026trustworthy,
  author    = {Hefti, Daniel Pascal and Lu, Tianxiang},
  title     = {Trustworthy Large Language Models in Organisations: A Competence-Based Alignment Framework},
  booktitle = {Proceedings of the 2026 International Joint Conference on Neural Networks (IJCNN)},
  year      = {2026},
  publisher = {IEEE}
}
```
