from itertools import combinations
from typing import Iterable

from Bio import pairwise2
from Bio.Seq import Seq


def translate_dna_sequence(dna_sequence: str, stop_at_stop_codon: bool = True) -> str:
    """
    Translate a DNA sequence into a protein sequence.
    """
    cleaned = dna_sequence.upper().replace("\n", "").replace(" ", "")
    return str(Seq(cleaned).translate(to_stop=stop_at_stop_codon))


def pairwise_identity_score(seq_a: str, seq_b: str) -> float:
    """
    Compute percent identity from a global alignment between two protein sequences.
    """
    alignments = pairwise2.align.globalxx(seq_a, seq_b)
    best_alignment = alignments[0]
    aligned_a, aligned_b = best_alignment.seqA, best_alignment.seqB

    matches = 0
    aligned_positions = 0

    for aa, bb in zip(aligned_a, aligned_b):
        if aa == "-" and bb == "-":
            continue
        aligned_positions += 1
        if aa == bb:
            matches += 1

    if aligned_positions == 0:
        return 0.0

    return matches / aligned_positions * 100.0


def all_pairwise_identity_scores(protein_records: Iterable[tuple[str, str]]) -> list[dict]:
    """
    Compute pairwise identity scores for a collection of named protein sequences.
    """
    results = []
    for (name_a, seq_a), (name_b, seq_b) in combinations(protein_records, 2):
        results.append(
            {
                "seq_a": name_a,
                "seq_b": name_b,
                "identity_score": pairwise_identity_score(seq_a, seq_b),
            }
        )
    return results
