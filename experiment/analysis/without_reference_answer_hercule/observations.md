# Public Dataset Separate Criteria Evaluation - Obersation (https://journals.sagepub.com/doi/full/10.2466/11.IT.3.1)
## Error analysis
1. 300/300 responses processed successfully.

## Analysing Sum, Mean and Standard Deviation of Score Criteria and Compound_Score

1. The compound score and criteria 2,3, 4, 5, 6, 7 have lower mean values with than without treatment. Only criteria 1 has higher mean value with than without treatment.
2. The compound score and all criteria scores, except criteria 3, have lower standard deviation with treatment than without.

| Model Name                | Phase | Sum | Mean  | Std      | IQR    |
|---------------------------|-------|-----|-------|----------|--------|
| deepseek-r1:14b           | 1     | 121 | 12.1  | 2.47     | 2.75   |
| deepseek-r1:14b           | 2     | 151 | 15.1  | 2.18     | 1.75   |
| deepseek-r1:14b           | 3     | 146 | 14.6  | 1.65     | 2.75   |
| deepseek-r1:32b           | 1     | 152 | 15.2  | 4.59     | 6.00   |
| deepseek-r1:32b           | 2     | 171 | 17.1  | 4.48     | 4.50   |
| deepseek-r1:32b           | 3     | 166 | 16.6  | 2.88     | 3.50   |
| deepseek-v3.1:671b-cloud  | 1     | 194 | 19.4  | 8.60     | 10.75  |
| deepseek-v3.1:671b-cloud  | 2     | 346 | 34.6  | 1.26     | 0.00   |
| deepseek-v3.1:671b-cloud  | 3     | 197 | 19.7  | 10.73    | 22.00  |
| llama3.2:1b               | 1     | 174 | 17.4  | 10.12    | 16.25  |
| llama3.2:1b               | 2     | 313 | 31.3  | 3.06     | 3.75   |
| llama3.2:1b               | 3     | 191 | 19.1  | 10.24    | 16.50  |
| llama3.2:3b               | 1     | 308 | 30.8  | 6.46     | 2.50   |
| llama3.2:3b               | 2     | 251 | 25.1  | 9.55     | 11.50  |
| llama3.2:3b               | 3     | 289 | 28.9  | 7.31     | 9.75   |
| llama3.3:70b              | 1     | 335 | 33.5  | 0.85     | 1.00   |
| llama3.3:70b              | 2     | 331 | 33.1  | 1.52     | 1.75   |
| llama3.3:70b              | 3     | 334 | 33.4  | 2.12     | 1.50   |
| mistral-small:22b         | 1     | 340 | 34.0  | 1.25     | 1.75   |
| mistral-small:22b         | 2     | 339 | 33.9  | 1.20     | 1.75   |
| mistral-small:22b         | 3     | 331 | 33.1  | 1.37     | 1.75   |
| qwen3:14b                 | 1     | 89  | 8.9   | 1.97     | 3.00   |
| qwen3:14b                 | 2     | 105 | 10.5  | 2.88     | 2.75   |
| qwen3:14b                 | 3     | 90  | 9.0   | 2.36     | 2.50   |
| qwen3:4b                  | 1     | 128 | 12.8  | 4.47     | 3.75   |
| qwen3:4b                  | 2     | 86  | 8.6   | 1.51     | 1.50   |
| qwen3:4b                  | 3     | 139 | 13.9  | 7.28     | 3.75   |
| smollm2:135m              | 1     | 83  | 8.3   | 2.11     | 1.75   |
| smollm2:135m              | 2     | 90  | 9.0   | 2.71     | 3.50   |
| smollm2:135m              | 3     | 85  | 8.5   | 2.92     | 1.00   |



## Results from Shapiro-Wilk Test

1. P-Values for compound score and all criteria scores are lower than <0.05 and indicate that the underlying distribution is not normal.
2. Thus non-parametric statistical tests shall be applied.

| Criteria         | W Statistic         | P-Value                |
|------------------|--------------------|------------------------|
| score_criteria1  | 0.7870             | 1.01e-10               |
| score_criteria2  | 0.7672             | 2.74e-11               |
| score_criteria3  | 0.7639             | 2.22e-11               |
| score_criteria4  | 0.8272             | 1.87e-09               |
| score_criteria5  | 0.7501             | 9.43e-12               |
| score_criteria6  | 0.7664             | 2.59e-11               |
| score_criteria7  | 0.7911             | 1.34e-10               |
| compound_score   | 0.8335             | 3.06e-09               |

## Results Mann-Whitney U Test
1. All P-values are higher than 0.2 and are not statistically significant.

| Criteria         | U Statistic | P-Value      |
|------------------|-------------|--------------|
| score_criteria1  | 1396.0      | 0.2946       |
| score_criteria2  | 1245.5      | 0.9768       |
| score_criteria3  | 1081.5      | 0.2217       |
| score_criteria4  | 1215.5      | 0.8090       |
| score_criteria5  | 1149.5      | 0.4616       |
| score_criteria6  | 1153.5      | 0.4839       |
| score_criteria7  | 1226.5      | 0.8685       |
| compound_score   | 1278.5      | 0.8464       |


## Results Rank Biserial Correlation

## Results of Cohens'D applied to compound score
### Cohen's D Effect Size for Compound Score

## Results Human vs M-Prometheus Evaluation Grade Comparison Pearson- and Spearman- Correlation


## Pairwise Agreement


## Cronbach's alpha

