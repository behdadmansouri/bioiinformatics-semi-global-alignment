from src.SemiGlobalAligner import AlignmentMatrix

def test_calculate_score():
    assert False

def test_calculate_seq():
    assert False

def test_print_results():
    assert False

def test_case_0():
    our_matrix = AlignmentMatrix.AlignmentMatrix("HEAGAWGHE", "PAWHEA")
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    assert our_matrix.seq == ""
    assert our_matrix.score == 0
    our_matrix.print_results()

def test_case_1():
    our_matrix = AlignmentMatrix.AlignmentMatrix("AAAAA", "AA")
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    our_matrix.print_results()