# Public Dataset with reference answer - obersvations (https://journals.sagepub.com/doi/full/10.2466/11.IT.3.1)
## Error analyis
1. 295/300 responses processed successfully. 5 Responses of smolllm2:135M are missing.

## Analysing Sum, Mean and Standard Deviation of Score Criteria and Compound_Score

1. The compound score and all criteria scores have higher mean values with treatment than without.
2. The compound score and all criteria scores, except criteria 4 and 7, have lower standard deviation with treatment than without.

## Results from Shapiro-Wilk Test

1. P-Values for compound score and all criteria scores are lower than <0.05 and indicate that the underlying distribution is not normal.
2. Thus non-parametric statistical tests shall be applied.

| Criteria         | W Value   | P-Value    |
|------------------|----------|------------|
| score_criteria1  | 0.9103   | 0.00000544 |
| score_criteria2  | 0.8859   | 0.00000041 |
| score_criteria3  | 0.8776   | 0.00000018 |
| score_criteria4  | 0.8932   | 0.00000085 |
| score_criteria5  | 0.9028   | 0.00000235 |
| score_criteria6  | 0.9023   | 0.00000222 |
| score_criteria7  | 0.8902   | 0.00000062 |
| compound_score   | 0.9492   | 0.00084    |


## Results Mann-Whitney U Test
1. Really low p-values for compound score and all criterias, except criteria 5.

| Criteria         | U Statistic | P-Value   |
|------------------|-------------|-----------|
| score_criteria1  | 1816.00000  | 0.00001   |
| score_criteria2  | 1524.50000  | 0.01735   |
| score_criteria3  | 1566.00000  | 0.00710   |
| score_criteria4  | 1702.00000  | 0.00020   |
| score_criteria5  | 1435.50000  | 0.08672   |
| score_criteria6  | 1562.00000  | 0.00829   |
| score_criteria7  | 1555.00000  | 0.00949   |
| compound_score   | 1580.00000  | 0.00687   |

## Results Rank Biserial Correlation
1. Small to moderate rank biseral correlation. The treatment groupd tended to outperform the control group in 31.66% of the cases beyond what would be expected by chance.
2. All criterias had a positive rank biserial correlation and are thus favorable.
3. Criteria 1 has the highest rbc value of 0.513 and criteria 5 the lowest rbc value of 0.27.
4. Low(er) p-values from the Mann-Whitney U test do correlate with higher RBC-Values.

| Criteria         | Rank Biserial Correlation |
|------------------|--------------------------|
| score_criteria1  | 0.51333                  |
| score_criteria2  | 0.27042                  |
| score_criteria3  | 0.30500                  |
| score_criteria4  | 0.41833                  |
| score_criteria5  | 0.19625                  |
| score_criteria6  | 0.30167                  |
| score_criteria7  | 0.29583                  |
| compound_score   | 0.31667                  |

## Results of Cohens'D applied to compound score
### Cohen's D Effect Size for Compound Score
1. The group with the treatment has a 0.569 standard deviation higher compound score.

| Criteria        | Cohen's D |
|-----------------|-----------|
| compound_score  | 0.787     |

## Results Human vs M-Prometheus Evaluation Grade Comparison Pearson- and Spearman- Correlation
- 25/295 (8.47%) tested. Responses selected with two different random seeds.

| Criteria         | Pearson Correlation | Pearson P-Value      | Spearman Correlation | Spearman P-Value      |
|------------------|--------------------|----------------------|---------------------|-----------------------|
| score_criteria1  | 0.743              | 2.13e-05             | 0.725               | 4.09e-05              |
| score_criteria2  | 0.631              | 7.11e-04             | 0.646               | 4.85e-04              |
| score_criteria3  | 0.408              | 4.30e-02             | 0.396               | 4.98e-02              |
| score_criteria4  | 0.705              | 8.27e-05             | 0.678               | 1.98e-04              |
| score_criteria5  | 0.424              | 3.47e-02             | 0.431               | 3.16e-02              |
| score_criteria6  | 0.822              | 4.80e-07             | 0.787               | 3.03e-06              |
| score_criteria7  | 0.771              | 6.35e-06             | 0.755               | 1.27e-05              |
| compound_score   | 0.815              | 7.19e-07             | 0.733               | 3.06e-05              |


## Pairwise Agreement
1. For the compound score and all criterias there is a moderate to high agreement. https://doi.org/10.2307%2F2529310

| Criteria         | Agreement Percentage | Cohen's Kappa |
|------------------|---------------------|---------------|
| score_criteria1  | 64.0                | 0.605         |
| score_criteria2  | 66.0                | 0.631         |
| score_criteria3  | 52.33               | 0.478         |
| score_criteria4  | 63.33               | 0.596         |
| score_criteria5  | 52.33               | 0.476         |
| score_criteria6  | 70.33               | 0.671         |
| score_criteria7  | 65.0                | 0.606         |
| compound_score   | 72.67               | 0.711         |

## Cronbach's alpha
Cronbach's alpha is 0.94