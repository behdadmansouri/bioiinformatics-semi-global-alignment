import AlignmentMatrix

if __name__ == '__main__':
    x = input("input x\n")
    y = input("input y\n")
    our_matrix = AlignmentMatrix.AlignmentMatrix(x, y)
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    our_matrix.print_results()
