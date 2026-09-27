# Results

This folder is intended for compact machine-readable result files such as CSV summaries.

## Main PapSwin-MatchNet fixed-split result

| Metric | Value |
|---|---:|
| Accuracy | 0.9753 |
| Balanced Accuracy | 0.9754 |
| Macro Precision | 0.9754 |
| Macro Recall | 0.9754 |
| Macro F1 | 0.9752 |
| Weighted F1 | 0.9751 |
| MCC | 0.9692 |
| Cohen's Kappa | 0.9691 |
| Macro ROC-AUC | 0.9987 |
| Macro PR-AUC | 0.9955 |
| Brier Score | 0.0471 |
| Calibrated ECE | 0.0201 |

## Recommended files to add after final reruns

- `main_test_metrics.csv`
- `baseline_comparison.csv`
- `ablation_results.csv`
- `five_fold_cv.csv`
- `multi_seed_results.csv`
- `robustness_results.csv`
- `paired_statistical_tests.csv`

Do not commit temporary outputs, checkpoints, or stale result files from earlier experimental configurations.
