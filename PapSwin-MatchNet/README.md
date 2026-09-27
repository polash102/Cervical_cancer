# PapSwin-MatchNet

**PapSwin-MatchNet: A Dual-Expert CNN–Transformer Network with Spatial Correspondence and Adaptive Routing for Cervical Cell Classification**

This repository contains the experimental notebook, figures, dataset-access instructions, and result documentation for PapSwin-MatchNet, a five-class cervical-cell classification framework based on a ConvNeXt-Atto local morphology expert and a compact partial Swin-Tiny global context expert.

> **Research use only.** This project is intended for research, demonstration, and educational use and is not a clinical diagnostic system.

## Overview

PapSwin-MatchNet combines:

- **ConvNeXt-Atto** for local morphological feature extraction.
- **Partial Swin-Tiny** for broader contextual representation.
- **BSCM** (Bidirectional Spatial Correspondence Matching) for local-global feature alignment and bidirectional cross-attention.
- **MCCR** (Match-Conditioned Class Router) for reliability-, agreement-, and disagreement-aware adaptive routing.
- **Grad-CAM++ and SmoothGrad** for qualitative visual explanation.

## Main Test Results

| Metric | PapSwin-MatchNet |
|---|---:|
| Accuracy | 97.53% |
| Macro F1 | 0.9752 |
| MCC | 0.9692 |
| Macro ROC-AUC | 0.9987 |
| Parameters | 8.65 M |
| Single-view GFLOPs | 2.9057 |

The main evaluation used a stratified **80:10:10** split of the 4,049-image SIPaKMeD single-cell dataset.

## Repository Structure

```text
Cervical_cancer/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── PapSwin_MatchNet.ipynb
├── scripts/
│   └── download_dataset.py
├── data/
│   └── README.md
├── figures/
│   ├── overall_methodology.jpg
│   ├── preprocessing_comparison.png
│   ├── confusion_matrix.png
│   ├── explainability.jpg
│   └── web_app.png
└── results/
    └── README.md
```

## Methodology

![Overall methodology](figures/overall_methodology.jpg)

The pipeline includes dataset integrity checking, preprocessing, stratified partitioning, training augmentation, baseline benchmarking, PapSwin-MatchNet training, statistical evaluation, explainability, and browser-based deployment.

## Dataset

The experiments use the publicly available **SIPaKMeD** single-cell cervical cytology dataset through the Kaggle dataset **Single Cell Conventional Pap Smear Images**.

- Total images: **4,049**
- Number of classes: **5**
- Dyskeratotic: **813**
- Koilocytotic: **825**
- Metaplastic: **793**
- Parabasal: **787**
- Superficial-Intermediate: **831**

The dataset is **not redistributed in this repository**. See [`data/README.md`](data/README.md) for download instructions.

## Preprocessing

Each image is processed using:

1. Resize to **224 × 224**
2. **3 × 3 median filtering**
3. RGB to **CIELAB**
4. CLAHE on the luminance channel with clip limit **2.0** and grid **8 × 8**
5. Mild unsharp masking with Gaussian sigma **1.0**
6. Min-max intensity normalization
7. ImageNet channel normalization before model input

![Preprocessing comparison](figures/preprocessing_comparison.png)

## Training Augmentation

Training-only augmentation uses:

- Rotation: **±15°**
- Zoom: **0.9–1.1**
- Horizontal flip: **p = 0.5**
- Vertical flip: **p = 0.5**
- Brightness: **0.9–1.1**
- Contrast: **0.9–1.1**

No training augmentation is applied to validation or test images.

## Notebook

The complete experimental notebook is available at:

[`notebooks/PapSwin_MatchNet.ipynb`](notebooks/PapSwin_MatchNet.ipynb)

The notebook includes data preparation, integrity checking, preprocessing, augmentation, baseline experiments, PapSwin-MatchNet training, evaluation, ablation, statistical analysis, cross-validation, robustness analysis, reproducibility experiments, and explanation generation.

## Installation

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

For GPU training, install a PyTorch build compatible with your CUDA environment.

## Download the Dataset

After installing the requirements:

```bash
python scripts/download_dataset.py
```

The script uses KaggleHub to obtain:

```text
mohaliy2016/papsinglecell
```

You can also download the dataset manually from Kaggle and keep the extracted data outside version control.

## Example Results

### Confusion Matrix

![PapSwin-MatchNet confusion matrix](figures/confusion_matrix.png)

### Explainability

![Grad-CAM++ and SmoothGrad explanations](figures/explainability.jpg)

### Web Application

![PapSwin-MatchNet web application](figures/web_app.png)

## Reproducibility Notes

- Primary random seed: **42**
- Input resolution: **224 × 224**
- Batch size: **16**
- Maximum epochs: **30**
- Early stopping patience: **5**
- Optimizer: **AdamW**
- Initial backbone learning rate: **2e-4**
- Initial head/fusion learning rate: **2e-3**
- Weight decay: **1e-3**
- Label smoothing: **0.02**
- EMA decay: **0.995**

The notebook should be treated as the authoritative implementation. Before a final archival release, regenerate any result tables that depend on recently modified experimental code.

## Results

See [`results/README.md`](results/README.md) for the current result summary and guidance for adding CSV outputs from the experiments.

## Citation

If you use this work, please cite the associated PapSwin-MatchNet manuscript once the final bibliographic information is available.

## License

No license has been selected in this repository template. Add an appropriate open-source license only after confirming the intended code and data-sharing terms.
