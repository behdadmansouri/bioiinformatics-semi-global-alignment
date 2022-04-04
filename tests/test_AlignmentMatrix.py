from src.SemiGlobalAligner import AlignmentMatrix

def test_pam_reference():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    print(our_matrix.PAM250['A']['C'])

def test_score_PAW():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 20

def test_score_AA():
    our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 4

def test_seq_PAW():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    assert our_matrix.seq == [('---PAW-HEA', 'HEAGAWGHE-')]
    our_matrix.print_results()
    # PAWHEA
    # HEAGAWGHE
    # [[ 0.  0.  0.  0.  0.  0.  0.]
    #  [ 0.  0. -1. -3.  6.  1. -1.]
    #  [ 0. -1.  0. -8. -2. 10.  1.]
    #  [ 0.  1.  1. -6. -9.  1. 12.]
    #  [ 0.  0.  2. -6. -8. -8.  3.]
    #  [ 0.  1.  2. -4. -7. -8. -6.]
    #  [ 0. -6. -5. 19. 10.  1. -8.]
    #  [ 0.  0. -5. 10. 17. 10.  2.]
    #  [ 0.  0. -1.  1. 16. 18.  9.]
    #  [ 0. -1.  0. -8.  7. 20. 18.]]
    # 20
    # ('---PAW-HEA', 'HEAGAWGHE-')
    #
    # ('-----PAWHEA', 'HEAGAWG-HE-')
    #
    # ('---PAW-HEA', 'HEAGAWGHE-')

def test_seq_AA():
    our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('AAAAA', '--AA-'), ('AAAAA', '-AA--'), ('AAAAA', 'AA---'), ('AAAAA', '---AA')}
    our_matrix.print_results()
    # AAAAA
    # AA
    # [[0. 0. 0. 0. 0. 0.]
    #  [0. 2. 2. 2. 2. 2.]
    #  [0. 2. 4. 4. 4. 4.]]
    # 4
    # AAAAA
    # ---AA
    # AAAAA
    # --AA-
    # AAAAA
    # -AA--
    # AAAAA
    # AA---
