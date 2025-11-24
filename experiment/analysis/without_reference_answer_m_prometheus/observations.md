# Public Dataset Separate Criteria Evaluation - Obersation (https://journals.sagepub.com/doi/full/10.2466/11.IT.3.1)
## Error analysis
1. 295/300 responses processed successfully. 5 Responses of smolllm2:135M are missing.

## Analysing Sum, Mean and Standard Deviation of Score Criteria and Compound_Score

1. The compound score and all criteria scores have higher mean values with treatment than without.
2. The compound score and all criteria scores have lower standard deviation with treatment than without.

| Model Name                | Phase | Sum | Median | Std Dev   | Count | Mean    |
|---------------------------|-------|-----|--------|-----------|-------|---------|
| deepseek-r1:14b           | 1     | 256 | 26.0   | 4.12      | 10    | 25.6    |
| deepseek-r1:14b           | 2     | 277 | 27.5   | 2.31      | 10    | 27.7    |
| deepseek-r1:14b           | 3     | 246 | 25.0   | 3.13      | 10    | 24.6    |
| deepseek-r1:32b           | 1     | 258 | 27.5   | 7.55      | 10    | 25.8    |
| deepseek-r1:32b           | 2     | 263 | 26.0   | 4.62      | 10    | 26.3    |
| deepseek-r1:32b           | 3     | 232 | 23.5   | 3.33      | 10    | 23.2    |
| deepseek-v3.1:671b-cloud  | 1     | 349 | 35.0   | 0.32      | 10    | 34.9    |
| deepseek-v3.1:671b-cloud  | 2     | 347 | 35.0   | 0.48      | 10    | 34.7    |
| deepseek-v3.1:671b-cloud  | 3     | 347 | 35.0   | 0.48      | 10    | 34.7    |
| llama3.2:1b               | 1     | 262 | 27.5   | 5.51      | 10    | 26.2    |
| llama3.2:1b               | 2     | 267 | 29.5   | 6.29      | 10    | 26.7    |
| llama3.2:1b               | 3     | 212 | 25.5   | 8.44      | 10    | 21.2    |
| llama3.2:3b               | 1     | 264 | 29.0   | 6.57      | 10    | 26.4    |
| llama3.2:3b               | 2     | 264 | 27.5   | 5.78      | 10    | 26.4    |
| llama3.2:3b               | 3     | 284 | 30.5   | 4.55      | 10    | 28.4    |
| llama3.3:70b              | 1     | 317 | 32.0   | 1.49      | 10    | 31.7    |
| llama3.3:70b              | 2     | 313 | 32.0   | 1.70      | 10    | 31.3    |
| llama3.3:70b              | 3     | 313 | 32.0   | 1.42      | 10    | 31.3    |
| mistral-small:22b         | 1     | 322 | 32.5   | 1.62      | 10    | 32.2    |
| mistral-small:22b         | 2     | 301 | 32.0   | 3.75      | 10    | 30.1    |
| mistral-small:22b         | 3     | 323 | 32.5   | 1.16      | 10    | 32.3    |
| qwen3:14b                 | 1     | 271 | 29.0   | 4.04      | 10    | 27.1    |
| qwen3:14b                 | 2     | 279 | 28.5   | 5.11      | 10    | 27.9    |
| qwen3:14b                 | 3     | 253 | 23.5   | 4.60      | 10    | 25.3    |
| qwen3:4b                  | 1     | 299 | 30.5   | 3.78      | 10    | 29.9    |
| qwen3:4b                  | 2     | 335 | 34.0   | 1.18      | 10    | 33.5    |
| qwen3:4b                  | 3     | 292 | 29.0   | 3.58      | 10    | 29.2    |
| smollm2:135m              | 1     | 71  | 7.0    | 0.32      | 10    | 7.10    |
| smollm2:135m              | 2     | 58  | 7.0    | 0.46      | 8     | 7.25    |
| smollm2:135m              | 3     | 54  | 7.0    | 1.25      | 7     | 7.71    |


## Results from Shapiro-Wilk Test

1. P-Values for compound score and all criteria scores are lower than <0.05 and indicate that the underlying distribution is not normal.
2. Thus non-parametric statistical tests shall be applied.

| Criteria         | W Statistic | P-Value                |
|------------------|-------------|------------------------|
| score_criteria1  | 0.8015      | 3.64e-10               |
| score_criteria2  | 0.7434      | 8.56e-12               |
| score_criteria3  | 0.6838      | 3.21e-13               |
| score_criteria4  | 0.8245      | 1.97e-09               |
| score_criteria5  | 0.7574      | 1.99e-11               |
| score_criteria6  | 0.7105      | 1.31e-12               |
| score_criteria7  | 0.7379      | 6.21e-12               |
| compound_score   | 0.8034      | 4.18e-10               |

## Results Mann-Whitney U Test
1. P-Value below 0.01 for compound_score and criteria 1 and 4.
2. P-Value greater than 0.05 but below 0.10 for criteria 6.
4. P-Value greater than 0.1 for criteria 2,3,5,7.

| Criteria         | U Statistic | P-Value    |
|------------------|-------------|------------|
| score_criteria1  | 1597.50000  | 0.00287    |
| score_criteria2  | 1407.00000  | 0.11657    |
| score_criteria3  | 1281.00000  | 0.52187    |
| score_criteria4  | 1728.50000  | 0.00008    |
| score_criteria5  | 1394.50000  | 0.13999    |
| score_criteria6  | 1448.00000  | 0.05494    |
| score_criteria7  | 1384.00000  | 0.15138    |
| compound_score   | 1562.00000  | 0.00997    |


## Results Rank Biserial Correlation
1. Small to moderate rank biseral correlation. The treatment groupd tended to outperform the control group in 30.17% of the cases beyond what would be expected by chance.
2. All criterias had a positive rank biserial correlation and are thus favorable.
3. Criteria 4 has the highest rbc value of 0.4404 and criteria 3 the lowest rbc value of 0.0675.
4. Low(er) p-values from the Mann-Whitney U test do correlate with higher RBC-Values.


| Criteria         | Rank Biserial Correlation |
|------------------|--------------------------|
| score_criteria1  | 0.3313                   |
| score_criteria2  | 0.1725                   |
| score_criteria3  | 0.0675                   |
| score_criteria4  | 0.4404                   |
| score_criteria5  | 0.1621                   |
| score_criteria6  | 0.2067                   |
| score_criteria7  | 0.1533                   |
| compound_score   | 0.3017                   |

## Results of Cohens'D applied to compound score
### Cohen's D Effect Size for Compound Score
1. The group with the treatment has a 0.606 standard deviation higher compound score.

| Criteria        | Cohen's D |
|-----------------|-----------|
| compound_score  | 0.606     |

## Results Human vs M-Prometheus Evaluation Grade Comparison Pearson- and Spearman- Correlation
- 25/296 (8.45%) tested. Responses selected with two different random seeds.
1. HIgh correlation values for both pearson and spearman. Pearson correlation (0.80, p = 0.00031) and spearman correlation (0.73, p < 0.00194)
2. Only criteria 5 has a pearson and spearman p-value above .05.

| Criteria         | Pearson Correlation | Pearson P-Value      | Spearman Correlation | Spearman P-Value      |
|------------------|--------------------|----------------------|----------------------|-----------------------|
| score_criteria1  | 0.7245             | 0.0000422            | 0.7142               | 0.0000607             |
| score_criteria2  | 0.7211             | 0.0000476            | 0.7222               | 0.0000458             |
| score_criteria3  | 0.4514             | 0.02353              | 0.4406               | 0.02748               |
| score_criteria4  | 0.5733             | 0.00274              | 0.5380               | 0.00554               |
| score_criteria5  | 0.5871             | 0.00203              | 0.4961               | 0.01167               |
| score_criteria6  | 0.7459             | 0.0000187            | 0.6517               | 0.000417              |
| score_criteria7  | 0.6803             | 0.000183             | 0.6480               | 0.000461              |
| compound_score   | 0.7724             | 0.00000608           | 0.6821               | 0.000173              |

## Pairwise Agreement
1. For the compound score and all criterias there is a moderate to high agreement. https://doi.org/10.2307%2F2529310

| Criteria         | Agreement Percentage | Cohen's Kappa |
|------------------|---------------------|---------------|
| score_criteria1  | 64.67               | 0.610         |
| score_criteria2  | 68.00               | 0.652         |
| score_criteria3  | 53.00               | 0.474         |
| score_criteria4  | 64.33               | 0.608         |
| score_criteria5  | 57.33               | 0.527         |
| score_criteria6  | 60.33               | 0.557         |
| score_criteria7  | 59.33               | 0.535         |
| compound_score   | 72.33               | 0.707         |

## Cronbach's alpha
Cronbach's alpha summing the seven criterias is 0.93!