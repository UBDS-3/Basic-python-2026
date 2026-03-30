# DNA Translation and Pairwise Alignment

This project provides two core bioinformatics utilities:

1. Translate a DNA coding sequence into a protein sequence
2. Compute pairwise identity scores between protein sequences using global alignment

A notebook demonstrates the full workflow:

- read DNA sequences from `data/raw/*.fasta`
- translate them into proteins
- save translated proteins to `data/processed/translated_proteins.fasta`
- compute pairwise identity scores
- save the score table to `outputs/tables/identity_scores.csv`
- plot identity scores and save the figure to `outputs/figures/identity_scores_scatter.png`

## Project Structure

```text
.
├── .gitignore
├── README.md
├── data
│   ├── processed
│   └── raw
├── notebooks
├── outputs
│   ├── figures
│   └── tables
├── requirements.txt
├── setup.py
├── src
└── tests
```

## Installation

```bash
pip install -r requirements.txt
pip install -e .
```

## Example input

Place a FASTA file in `data/raw/`, for example `data/raw/example_dna.fasta`:

```fasta
>seq1
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
>seq2
ATGGCCATTGTTATGGGCCGCTGAAAGGGCGCCCGATAG
>seq3
ATGGCCTTTGTAATGGGTCGCTGAAAGGGTGCCCGATAG
```

## Running

Open the notebook in `notebooks/dna_translation_alignment.ipynb` and run all cells.

## Testing

```bash
pytest
```
