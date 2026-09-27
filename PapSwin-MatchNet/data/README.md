# Dataset Access

This project uses the public **Single Cell Conventional Pap Smear Images** dataset derived from SIPaKMeD.

## Kaggle identifier

```text
mohaliy2016/papsinglecell
```

## Recommended approach

Do **not** commit the raw dataset ZIP or extracted image folders to GitHub. Instead, download the dataset locally with the provided script:

```bash
python scripts/download_dataset.py
```

or download it directly from Kaggle.

Keeping the raw images outside the Git repository:

- avoids GitHub file-size limits,
- avoids duplicating a public dataset,
- keeps the repository lightweight,
- and avoids redistribution/licensing ambiguity.

The experiment uses 4,049 images from five classes:
Dyskeratotic, Koilocytotic, Metaplastic, Parabasal, and Superficial-Intermediate.
