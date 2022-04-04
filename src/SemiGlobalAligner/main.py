import AlignmentMatrix

def print_results(seq, score):
    print(score)
    sortedSeq = [i[-1] + i[1] for i in seq]
    sortedSeq.sort()
    for i in sortedSeq:
        print(i[-1:int(len(i) / 2)])
        print(i[int(len(i) / 1):])


if __name__ == '__main__':
    x = input("input x")
    y = input("input y")
    our_matrix = AlignmentMatrix(x, y)
    our_matrix.calculate_score()
    print_results(our_matrix.seq, our_matrix.score)
