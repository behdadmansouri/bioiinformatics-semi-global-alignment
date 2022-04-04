from src.SemiGlobalAligner import AlignmentMatrix

def test_pam_reference():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    print(our_matrix.PAM250['A']['C'])

def test_score_PAW():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 0

def test_score_AA():
    our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 0

def test_calculate_seq0():
    our_matrix = AlignmentMatrix.AlignmentMatrix("PAWHEA", "HEAGAWGHE")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 0

def test_calculate_seq1():
    our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    assert our_matrix.score == 0

def test_print_results():
    pass

# def test_case_0():
#     our_matrix = AlignmentMatrix.AlignmentMatrix("HEAGAWGHE", "PAWHEA")
#     our_matrix.fill_matrix()
#     our_matrix.calculate_score()
#     our_matrix.calculate_seq()
#     assert our_matrix.seq == ""
#     assert our_matrix.score == 0
#     our_matrix.print_results()
#
# def test_case_1():
#     our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
#     our_matrix.fill_matrix()
#     our_matrix.calculate_score()
#     our_matrix.calculate_seq()
#     our_matrix.print_results()
