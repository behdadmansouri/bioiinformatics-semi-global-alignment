from src.SemiGlobalAligner import AlignmentMatrix

def test_pam_reference():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    print(our_matrix.PAM250['A']['C'])

def test_seq_PAW():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 20
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
    assert our_matrix.score == 4
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


def test_seq_students_1():
    our_matrix = AlignmentMatrix.AlignmentMatrix("ACTATATTATATATA", "ACTATATATATATA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 97
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {(' ACGTACGTACGTCCCCC---CCCC', ' ----ACTGACGTCCCCCWWWWCCC'),
                                   (' ACGTACGTACGTCCCCC--C-CCC', ' ----ACTGACGTCCCCCWWWWCCC'),
                                   (' ACGTACGTACGTCCCCC-C--CCC', ' ----ACTGACGTCCCCCWWWWCCC'),
                                   (' ACGTACGTACGTCCCCCC---CCC', ' ----ACTGACGTCCCCCWWWWCCC')}
    our_matrix.print_results()

def test_seq_students_2():
    our_matrix = AlignmentMatrix.AlignmentMatrix("ACGTACGTACGTCCCCCCCCC", "ACTGACGTCCCCCWWWWCCC")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 35
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('ACTATATTATATATA', 'ACTATA-TATATATA'), ('ACTATATTATATATA', 'ACTATAT-ATATATA')}
    our_matrix.print_results()

def test_seq_students_3():
    our_matrix = AlignmentMatrix.AlignmentMatrix("ACTATATTATA", "ACTATATATA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 30
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('ACTATATTATA', 'ACTATATATA-')}
    our_matrix.print_results()

def test_seq_students_4():
    our_matrix = AlignmentMatrix.AlignmentMatrix("GTCCCCCCCCC", "GTCCCCCWWWWCCC")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 69
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('GTCCCCC---CCCC', 'GTCCCCCWWWWCCC'), ('GTCCCCC--C-CCC', 'GTCCCCCWWWWCCC'), (
        'GTCCCCC-C--CCC', 'GTCCCCCWWWWCCC'), ('GTCCCCCC---CCC', 'GTCCCCCWWWWCCC')}
    our_matrix.print_results()


def test_seq_students_5():
    our_matrix = AlignmentMatrix.AlignmentMatrix("ACGTWWW", "ACGTCCC")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 10
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('-----ACGTWWW', 'ACGTCCC-----')}
    our_matrix.print_results()


def test_seq_students_6():
    our_matrix = AlignmentMatrix.AlignmentMatrix("ACGTGGG", "ACGTCCC")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 13
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('ACGTGGG', 'ACGTCCC')}
    our_matrix.print_results()

def test_seq_students_7():
    our_matrix = AlignmentMatrix.AlignmentMatrix("WWWTGCA", "CCTGCA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 10
    our_matrix.calculate_seq()
    assert set(our_matrix.seq) == {('WWWTGCA----', '-----CCTGCA'), ('WWWTGCA---', '----CCTGCA')}
    our_matrix.print_results()
