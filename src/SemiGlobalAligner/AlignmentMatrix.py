class AlignmentMatrix:
    GAP_HORIZONTAL = 2
    GAP_VERTICAL = 4
    MATCH = 1
    GAP_PENALTY = -9
    PAM250 = {
        'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0,
              'P': 1, 'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3},
        'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5,
              'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0},
        'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2,
              'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
        'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1,
              'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4},
        'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3,
              'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7},
        'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0,
              'P': 0, 'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5},
        'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2,
              'P': 0, 'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0},
        'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
              'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1},
        'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1,
              'P': -1, 'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4},
        'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3,
              'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1},
        'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2,
              'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2},
        'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2,
              'P': 0, 'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2},
        'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0,
              'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5},
        'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1,
              'P': 0, 'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
        'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0,
              'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4},
        'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1,
              'P': 1, 'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3},
        'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0,
              'P': 0, 'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3},
        'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2,
              'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2},
        'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4,
              'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0},
        'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2,
              'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}
    }

    def __init__(self, first_string, second_string):
        self.A_vertical = first_string

        self.traceback_matrix = [[0 for _ in range(len(first_string) + 1)]
                                 for _ in range(len(second_string) + 1)]
        self.B_horizontal = second_string
        self.matrix = [[0 for _ in range(len(first_string) + 1)]
                       for _ in range(len(second_string) + 1)]
        self.score = 0
        self.score_loc = []
        self.seq = []

    def fill_matrix(self):
        for j in range(1, len(self.A_vertical) + 1):
            for i in range(1, len(self.B_horizontal) + 1):
                first_word = self.A_vertical[j - 1]
                second_word = self.B_horizontal[i - 1]
                gamma = self.matrix[i - 1][j - 1] + self.PAM250[first_word][second_word]
                s = [self.matrix[i][j - 1] - 9,
                     self.matrix[i - 1][j] - 9,
                     gamma]
                self.matrix[i][j] = max(s)

    def print_traceback_matrix(self):
        print("\n\t\t", end="")
        print("\t".join(self.A_vertical))
        for i in range(len(self.traceback_matrix)):
            print((self.B_horizontal + " ")[i - 1], end="  ")
            print(*self.traceback_matrix[i], sep="\t")

    def print_matrix(self):
        from colorama import Fore
        print("\n\t\t", end="")
        print("\t".join(self.A_vertical))
        for j in range(len(self.matrix)):
            print((self.B_horizontal + " ")[j - 1], end="  ")
            for i in range(len(self.matrix[j])):
                if self.traceback_matrix[j][i]:
                    print(Fore.RED + str(self.matrix[j][i]) + Fore.WHITE, end="\t")
                else:
                    print(Fore.WHITE + str(self.matrix[j][i]), end="\t")
            print("")

    def calculate_score(self):
        for i in range(1, len(self.B_horizontal) + 1):
            j = len(self.A_vertical)
            if self.matrix[i][j] == self.score and (i, j) not in self.score_loc:
                self.score_loc.append((i, j))
            if self.matrix[i][j] > self.score:
                self.score = self.matrix[i][j]
                self.score_loc = [(i, j)]

        for j in reversed(range(1, len(self.A_vertical) + 1)):
            i = len(self.B_horizontal)
            if self.matrix[i][j] == self.score and (i, j) not in self.score_loc:
                self.score_loc.append((i, j))
            if self.matrix[i][j] > self.score:
                self.score = self.matrix[i][j]
                self.score_loc = [(i, j)]

    def calculate_seq(self):
        for head in self.score_loc:
            self.make_graph(head)

            A, B = self.A_vertical, self.B_horizontal
            j, i = head
            trace_A, trace_B = "", ""

            # final offsets
            for _ in range(len(self.A_vertical) - i):
                trace_A, trace_B, A = self.gap(A, trace_A, trace_B)
            for _ in range(len(self.B_horizontal) - j):
                trace_B, trace_A, B = self.gap(B, trace_B, trace_A)
            self.traverse_graph(head, trace_A, trace_B, A, B)

    def traverse_graph(self, head, trace_A, trace_B, A, B):
        j, i = head

        # middle part
        while i and j:
            up_left = self.matrix[j - 1][i - 1]
            this = self.matrix[j][i]
            up_left_cost = self.PAM250[B[-1]][A[-1]]

            if up_left == this - up_left_cost:
                A, B, trace_A, trace_B = self.fill(A, B, trace_A, trace_B)
                j -= 1
                i -= 1
            elif this == self.matrix[j - 1][i] - 9:
                trace_B, trace_A, B = self.gap(B, trace_B, trace_A)
                j -= 1
            else:
                trace_A, trace_B, A = self.gap(A, trace_A, trace_B)
                i -= 1

        # initial offsets
        for _ in range(i):
            trace_A, trace_B, A = self.gap(A, trace_A, trace_B)
        for _ in range(j):
            trace_B, trace_A, B = self.gap(B, trace_B, trace_A)

        self.seq.append((trace_A[::-1], trace_B[::-1]))
        # append the reverse sequences
        # self.seq = sorted(self.seq, key=len, reverse=True)


    @staticmethod
    def fill(reverse_A_first_i_horizontal, reverse_B_second_j_vertical, traceback_A_first_i_horizontal,
             traceback_B_second_j_vertical):
        traceback_B_second_j_vertical += reverse_B_second_j_vertical[-1]
        traceback_A_first_i_horizontal += reverse_A_first_i_horizontal[-1]
        reverse_B_second_j_vertical = reverse_B_second_j_vertical[:-1]
        reverse_A_first_i_horizontal = reverse_A_first_i_horizontal[:-1]
        return reverse_A_first_i_horizontal, reverse_B_second_j_vertical, \
               traceback_A_first_i_horizontal, traceback_B_second_j_vertical

    def make_graph(self, head):
        sequences = []
        j, i = head
        if (i == 0) or (j == 0) or self.traceback_matrix[j][i]:
            return

        A, B = self.A_vertical, self.B_horizontal

        up_left = self.matrix[j - 1][i - 1]
        this = self.matrix[j][i]
        up_left_cost = self.PAM250[B[j - 1]][A[i - 1]]

        if up_left == this - up_left_cost:
            self.traceback_matrix[j][i] += self.MATCH
            sequences.append(self.make_graph((j - 1, i - 1)))
        if this == self.matrix[j - 1][i] - 9:
            self.traceback_matrix[j][i] += self.GAP_HORIZONTAL
            sequences.append(self.make_graph((j - 1, i)))
        if this == self.matrix[j][i - 1] - 9:
            self.traceback_matrix[j][i] += self.GAP_VERTICAL
            sequences.append(self.make_graph((j, i - 1)))

    @staticmethod
    def gap(reverse_no_gap, traceback_no_gap, traceback_gap_haver):
        traceback_gap_haver += "-"
        traceback_no_gap += reverse_no_gap[-1]
        reverse_no_gap = reverse_no_gap[:-1]
        return traceback_no_gap, traceback_gap_haver, reverse_no_gap

    def print_results(self):
        print(self.score)
        for i in self.seq:
            print(i[0])
            print(i[1])


# transpose the matrix
# self.matrix = list(zip(*self.matrix))
if __name__ == '__main__':
    x = input()
    y = input()
    our_matrix = AlignmentMatrix(x, y)
    our_matrix.fill_matrix()
    our_matrix.calculate_score()
    our_matrix.calculate_seq()
    our_matrix.print_results()
