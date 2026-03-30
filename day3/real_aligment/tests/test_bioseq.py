from src.bioseq import pairwise_identity_score, translate_dna_sequence


def test_translate_dna_sequence():
    dna = "ATGGCC"
    protein = translate_dna_sequence(dna)
    assert protein == "MA"


def test_pairwise_identity_score_identical():
    seq_a = "MART"
    seq_b = "MART"
    assert pairwise_identity_score(seq_a, seq_b) == 100.0


def test_pairwise_identity_score_different():
    seq_a = "MAAA"
    seq_b = "MATA"
    score = pairwise_identity_score(seq_a, seq_b)
    assert score == 75.0
