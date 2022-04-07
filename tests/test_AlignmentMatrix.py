from src.SemiGlobalAligner import AlignmentMatrix

def test_pam_reference():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE", "semi-global")
    print(our_matrix.PAM250['A']['C'])

def test_seq_PAW_reverse():
    our_matrix = AlignmentMatrix.calculate_alignment("HEAGAWGHE", "PAWHEA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 20
    assert our_matrix.sequences == [('HEAGAWGHE-', '---PAW-HEA')]

def test_seq_PAW():
    our_matrix = AlignmentMatrix.calculate_alignment("PAWHEA", "HEAGAWGHE", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 20
    assert our_matrix.sequences == [('---PAW-HEA', 'HEAGAWGHE-')]

def test_seq_AA():
    our_matrix = AlignmentMatrix.calculate_alignment("AAAAA", "AA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 4
    assert our_matrix.sequences == [('AAAAA', '---AA'), ('AAAAA', '--AA-'), ('AAAAA', '-AA--'), ('AAAAA', 'AA---')]

def test_seq_students_1():
    our_matrix = AlignmentMatrix.calculate_alignment("ACTATATTATATATA", "ACTATATATATATA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 35
    assert our_matrix.sequences == [('ACTATATTATATATA', 'ACTATA-TATATATA'), ('ACTATATTATATATA', 'ACTATAT-ATATATA')]

def test_seq_students_1_modified():
    our_matrix = AlignmentMatrix.calculate_alignment("ACTTATATATA", "ACTATATATA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 25
    assert our_matrix.sequences == [('ACTTATATATA', 'AC-TATATATA'), ('ACTTATATATA', 'ACT-ATATATA')]

def test_seq_students_2():
    our_matrix = AlignmentMatrix.calculate_alignment("ACGTACGTACGTCCCCCCCCC", "ACTGACGTCCCCCWWWWCCC", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 97
    assert our_matrix.sequences == [('ACGTACGTACGTCCCCC---CCCC', '----ACTGACGTCCCCCWWWWCCC'),
                                    ('ACGTACGTACGTCCCCC--C-CCC', '----ACTGACGTCCCCCWWWWCCC'),
                                    ('ACGTACGTACGTCCCCC-C--CCC', '----ACTGACGTCCCCCWWWWCCC'),
                                    ('ACGTACGTACGTCCCCCC---CCC', '----ACTGACGTCCCCCWWWWCCC')]

def test_seq_students_3():
    our_matrix = AlignmentMatrix.calculate_alignment("ACTATATTATA", "ACTATATATA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 30
    assert our_matrix.sequences == [('ACTATATTATA', 'ACTATATATA-')]

def test_seq_students_3_local():
    our_matrix = AlignmentMatrix.calculate_alignment("ACTATATTATA", "ACTATATATA", "local")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 30
    assert our_matrix.sequences == [('ACTATATTAT', 'ACTATATATA')]

def test_seq_students_4():
    our_matrix = AlignmentMatrix.calculate_alignment("GTCCCCCCCCC", "GTCCCCCWWWWCCC", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 69
    assert our_matrix.sequences == [('GTCCCCC---CCCC', 'GTCCCCCWWWWCCC'), ('GTCCCCC--C-CCC', 'GTCCCCCWWWWCCC'), (
        'GTCCCCC-C--CCC', 'GTCCCCCWWWWCCC'), ('GTCCCCCC---CCC', 'GTCCCCCWWWWCCC')]

def test_seq_students_4_local():
    our_matrix = AlignmentMatrix.calculate_alignment("GTCCCCCCCCC", "GTCCCCCWWWWCCC", "local")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 69
    assert our_matrix.sequences == [('GTCCCCC---CCCC', 'GTCCCCCWWWWCCC'), ('GTCCCCC--C-CCC', 'GTCCCCCWWWWCCC'), (
        'GTCCCCC-C--CCC', 'GTCCCCCWWWWCCC'), ('GTCCCCCC---CCC', 'GTCCCCCWWWWCCC')]

def test_seq_students_5():
    our_matrix = AlignmentMatrix.calculate_alignment("ACGTWWW", "ACGTCCC", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 10
    assert our_matrix.sequences == [('-----ACGTWWW', 'ACGTCCC-----')]

def test_seq_students_6():
    our_matrix = AlignmentMatrix.calculate_alignment("ACGTGGG", "ACGTCCC", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 13
    assert our_matrix.sequences == [('ACGTGGG', 'ACGTCCC')]

def test_seq_students_6_local():
    our_matrix = AlignmentMatrix.calculate_alignment("ACGTGGG", "ACGTCCC", "local")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 22
    assert our_matrix.sequences == [('ACGT', 'ACGT')]

def test_seq_students_7():
    our_matrix = AlignmentMatrix.calculate_alignment("WWWTGCA", "CCTGCA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 10
    assert our_matrix.sequences == [('WWWTGCA----', '-----CCTGCA'), ('WWWTGCA---', '----CCTGCA')]

def test_seq_students_7_global():
    our_matrix = AlignmentMatrix.calculate_alignment("WWWTGCA", "CCTGCA", "global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 0
    assert our_matrix.sequences == [('WWWTGCA', '-CCTGCA'), ('WWWTGCA', 'C-CTGCA'), ('WWWTGCA', 'CC-TGCA')]

def test_seq_students_7_local():
    our_matrix = AlignmentMatrix.calculate_alignment("WWWTGCA", "CCTGCA", "local")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 12
    assert our_matrix.sequences == [('C', 'C')]

def test_seq_student_8():
    our_matrix = AlignmentMatrix.calculate_alignment("CACGGTCCGAA", "AACTTCGAA", "semi-global")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 23
    assert our_matrix.sequences == [('--C-ACGGTCCGAA', 'AACTTCGAA-----'), ('--CA-CGGTCCGAA', 'AACTTCGAA-----')]

def test_seq_student_8_local():
    our_matrix = AlignmentMatrix.calculate_alignment("CACGGTCCGAA", "AACTTCGAA", "local")
    our_matrix.print_colored_matrix()
    assert our_matrix.score == 23
    assert our_matrix.sequences == [('C-ACGGT', 'CTTCGAA'), ('CA-CGGT', 'CTTCGAA')]
