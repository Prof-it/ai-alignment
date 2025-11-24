# Public Dataset Separate Criteria Evaluation - Obersation (https://journals.sagepub.com/doi/full/10.2466/11.IT.3.1)
## Error analysis
1. 300/300 responses processed successfully.

## Analysing Sum, Mean and Standard Deviation of Score Criteria and Compound_Score

1. The compound score and all criteria scores, except criteria 2, have higher mean with treatment than without.

| Model Name                | Phase | Sum | Mean  | Std      | IQR   |
|---------------------------|-------|-----|-------|----------|-------|
| deepseek-r1:14b           | 1     | 128 | 12.8  | 2.35     | 2.0   |
| deepseek-r1:14b           | 2     | 151 | 15.1  | 3.57     | 3.5   |
| deepseek-r1:14b           | 3     | 144 | 14.4  | 3.57     | 2.75  |
| deepseek-r1:32b           | 1     | 129 | 12.9  | 3.67     | 4.0   |
| deepseek-r1:32b           | 2     | 165 | 16.5  | 3.78     | 6.25  |
| deepseek-r1:32b           | 3     | 138 | 13.8  | 3.97     | 4.25  |
| deepseek-v3.1:671b-cloud  | 1     | 180 | 18.0  | 9.85     | 18.5  |
| deepseek-v3.1:671b-cloud  | 2     | 336 | 33.6  | 2.41     | 1.0   |
| deepseek-v3.1:671b-cloud  | 3     | 165 | 16.5  | 6.84     | 9.25  |
| llama3.2:1b               | 1     | 94  | 9.4   | 5.08     | 0.0   |
| llama3.2:1b               | 2     | 166 | 16.6  | 4.12     | 5.0   |
| llama3.2:1b               | 3     | 105 | 10.5  | 6.00     | 3.0   |
| llama3.2:3b               | 1     | 137 | 13.7  | 3.62     | 5.5   |
| llama3.2:3b               | 2     | 132 | 13.2  | 4.85     | 7.5   |
| llama3.2:3b               | 3     | 160 | 16.0  | 5.66     | 9.75  |
| llama3.3:70b              | 1     | 278 | 27.8  | 3.29     | 3.5   |
| llama3.3:70b              | 2     | 269 | 26.9  | 4.04     | 6.75  |
| llama3.3:70b              | 3     | 282 | 28.2  | 4.21     | 4.75  |
| mistral-small:22b         | 1     | 245 | 24.5  | 4.03     | 6.0   |
| mistral-small:22b         | 2     | 231 | 23.1  | 5.82     | 4.25  |
| mistral-small:22b         | 3     | 228 | 22.8  | 5.33     | 10.5  |
| qwen3:14b                 | 1     | 101 | 10.1  | 2.02     | 1.0   |
| qwen3:14b                 | 2     | 96  | 9.6   | 3.03     | 3.5   |
| qwen3:14b                 | 3     | 98  | 9.8   | 1.69     | 2.0   |
| qwen3:4b                  | 1     | 157 | 15.7  | 7.01     | 10.25 |
| qwen3:4b                  | 2     | 121 | 12.1  | 4.53     | 7.0   |
| qwen3:4b                  | 3     | 152 | 15.2  | 5.79     | 5.5   |
| smollm2:135m              | 1     | 72  | 7.2   | 0.42     | 0.0   |
| smollm2:135m              | 2     | 80  | 8.0   | 2.83     | 0.0   |
| smollm2:135m              | 3     | 77  | 7.7   | 1.49     | 0.0   |


## Results from Shapiro-Wilk Test
1. P-Values for compound score and all criteria scores are lower than <0.05 and indicate that the underlying distribution is not normal.
2. Thus non-parametric statistical tests shall be applied.

| Criteria         | W Statistic | P-Value            |
|------------------|-------------|--------------------|
| score_criteria1  | 0.855       | 1.82 × 10⁻⁸        |
| score_criteria2  | 0.807       | 3.98 × 10⁻¹⁰       |
| score_criteria3  | 0.854       | 1.72 × 10⁻⁸        |
| score_criteria4  | 0.863       | 3.59 × 10⁻⁸        |
| score_criteria5  | 0.721       | 1.73 × 10⁻¹²       |
| score_criteria6  | 0.811       | 5.55 × 10⁻¹⁰       |
| score_criteria7  | 0.758       | 1.50 × 10⁻¹¹       |
| compound_score   | 0.917       | 1.01 × 10⁻⁵        |

## Results Mann-Whitney U Test
1. Only criteria 7 has a P-Value below 0.05. 
2. Criteria 3 and criteria 6 and the compoudn score are below 0.1.
3. Criteria 1, 2, 4, 5 are statistically not relevant.

| Criteria         | U Statistic | P-Value                |
|------------------|-------------|------------------------|
| score_criteria1  | 1416.0      | 0.241                  |
| score_criteria2  | 1237.0      | 0.928                  |
| score_criteria3  | 1508.0      | 0.068                  |
| score_criteria4  | 1340.5      | 0.520                  |
| score_criteria5  | 1389.0      | 0.285                  |
| score_criteria6  | 1480.0      | 0.098                  |
| score_criteria7  | 1616.5      | 0.006                  |
| compound_score   | 1497.0      | 0.088                  |

## Results Rank Biserial Correlation

## Results of Cohens'D applied to compound score
### Cohen's D Effect Size for Compound Score

## Results Human vs M-Prometheus Evaluation Grade Comparison Pearson- and Spearman- Correlation


## Pairwise Agreement


## Cronbach's alpha

