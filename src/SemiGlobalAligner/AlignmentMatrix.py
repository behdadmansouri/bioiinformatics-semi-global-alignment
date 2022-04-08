class AlignmentMatrix:
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

    def __init__(self, first_string, second_string, alignment):
        """
        initializes the matrix.
        :param first_string: The first string to be aligned
        :param second_string: The second string to be aligned
        :param alignment: The alignment type. "local", "global" or "semi-global"
        """
        self.A = first_string
        self.B = second_string
        self.alignment = alignment
        self.traceback_matrix = [[False for _ in range(len(first_string) + 1)]
                                 for _ in range(len(second_string) + 1)]
        self.matrix = [[0 for _ in range(len(first_string) + 1)]
                       for _ in range(len(second_string) + 1)]
        # alignment score
        self.score = 0
        self.start = []
        self.sequences = []

    def fill_matrix(self):
        """
        classic feedforward. Find the maximum of a left gap, an up gap, and the match from up-left. Put it in the matrix
        If the alignment is global, fill the first row with gaps instead of zeros
        """
        if self.alignment == "global":
            for i in range(0, len(self.B) + 1):
                j = 0
                self.matrix[i][j] = i * self.GAP_PENALTY

            for j in range(0, len(self.A) + 1):
                i = 0
                self.matrix[i][j] = j * self.GAP_PENALTY
        for j in range(1, len(self.A) + 1):
            for i in range(1, len(self.B) + 1):
                first_word = self.A[j - 1]
                second_word = self.B[i - 1]
                gamma = self.matrix[i - 1][j - 1] + self.PAM250[first_word][second_word]
                s = [self.matrix[i][j - 1] + self.GAP_PENALTY,
                     self.matrix[i - 1][j] + self.GAP_PENALTY,
                     gamma]
                self.matrix[i][j] = max(s)

    def print_colored_matrix(self):
        """
        Prints the matrix with given strings on the top and the left
        Also the colorama library is imported here, so we'd color the matrix items which are in the traceback
        """
        from colorama import Fore
        print("\n\t\t", end="")
        print("\t".join(self.A))
        for j in range(len(self.matrix)):
            print((self.B + " ")[j - 1], end="  ")
            for i in range(len(self.matrix[j])):
                if self.traceback_matrix[j][i]:
                    print(Fore.RED + str(self.matrix[j][i]) + Fore.WHITE, end="\t")
                else:
                    print(str(self.matrix[j][i]), end="\t")
            print("")

    def calculate_score_find_start_positions(self):
        """
        global only finds scores (head is always the last matrix entry)
        local and semi-global not only calculate scores, but they also finds various heads.
        :return: nothing. Just breaks out if local or global scores are found
        """
        if self.alignment == "global":
            self.start = [(len(self.B), len(self.A))]
            return
        if self.alignment == "local":
            for i in range(1, len(self.B) + 1):
                for j in range(1, len(self.A) + 1):
                    if self.matrix[i][j] == self.score and (i, j) not in self.start:
                        self.start.append((i, j))
                    if self.matrix[i][j] > self.score:
                        self.score = self.matrix[i][j]
                        self.start = [(i, j)]
            return

        for i in range(1, len(self.B) + 1):
            j = len(self.A)
            if self.matrix[i][j] == self.score and (i, j) not in self.start:
                self.start.append((i, j))
            if self.matrix[i][j] > self.score:
                self.score = self.matrix[i][j]
                self.start = [(i, j)]

        for j in reversed(range(1, len(self.A) + 1)):
            i = len(self.B)
            if self.matrix[i][j] == self.score and (i, j) not in self.start:
                self.start.append((i, j))
            if self.matrix[i][j] > self.score:
                self.score = self.matrix[i][j]
                self.start = [(i, j)]

    def calculate_seq(self):
        """
        We have a filled matrix, and we're going to trace back two (or more) tuples of strings to find alignments.
        """
        for start in self.start:
            A, B = self.A, self.B
            j, i = start
            trace_A, trace_B = "", ""

            # final offsets
            for _ in range(len(self.A) - i):
                trace_A, trace_B, A = self.gap(A, trace_A, trace_B)
            for _ in range(len(self.B) - j):
                trace_B, trace_A, B = self.gap(B, trace_B, trace_A)

            # run our recursive function
            self.traceback(start, trace_A, trace_B, A, B)

    def traceback(self, start, trace_A, trace_B, A, B):
        """

        :param start: the current matrix item that we're finding our way back from
        :param trace_A: the traced first string, so far
        :param trace_B: the traced second string, so far
        :param A: the remainder of the first string
        :param B: the remainder of the second string
        :return: nothing. Just breaks out if we reach an end point
        """
        j, i = start

        # if the end is reached
        if i == 0 or j == 0 or (self.alignment == "local" and self.matrix[j][i] == 0):
            # initial offsets
            for _ in range(i):
                trace_A, trace_B, A = self.gap(A, trace_A, trace_B)
            for _ in range(j):
                trace_B, trace_A, B = self.gap(B, trace_B, trace_A)
            # invert the tracebacks and add them to self.seq
            self.sequences.append((trace_A[::-1], trace_B[::-1]))
            return

        this = self.matrix[j][i]
        up_left = self.matrix[j - 1][i - 1]
        up_left_cost = self.PAM250[B[-1]][A[-1]]
        j_gap = self.matrix[j - 1][i]
        i_gap = self.matrix[j][i - 1]

        # determine direction and run our recursive function
        if this == up_left + up_left_cost:
            self.traceback_matrix[j][i] = True
            self.traceback((j - 1, i - 1), trace_A + A[-1], trace_B + B[-1], A[:-1], B[:-1])
        if this == j_gap + self.GAP_PENALTY:
            self.traceback_matrix[j][i] = True
            self.traceback((j - 1, i), trace_A + "-", trace_B + B[-1], A, B[:-1])
        if this == i_gap + self.GAP_PENALTY:
            self.traceback_matrix[j][i] = True
            self.traceback((j, i - 1), trace_A + A[-1], trace_B + "-", A[:-1], B)

    def gap(self, string_loss, trace_loss, trace_hyphen):
        """
        calculates a gap
        the only thing making this function a method is checking the matrix alignment
        :param string_loss: the initial string that will have a letter dropped (for the gap)
        :param trace_loss: the traceback string that will have a letter dropped (for the gap)
        :param trace_hyphen: the traceback string that will be getting a hyphen (for the gap)
        :return: the state. Every parameter will be returned.
        """
        if self.alignment != "local":
            trace_hyphen += "-"
            trace_loss += string_loss[-1]
        string_loss = string_loss[:-1]
        return trace_loss, trace_hyphen, string_loss

    def print_results(self):
        """
        prints the score and the alignment tuples
        """
        print(self.score)
        for i in self.sequences:
            print(i[0])
            print(i[1])


def calculate_alignment(x, y, alignment):
    """
    does everything, except printing the matrix. it only prints the score and the final alignments
    :param x: first input string
    :param y: second input string
    :param alignment: "global", "local" or "semi-global
    :return: our matrix object, meant to be examined / used for printing the colored matrix
    """
    our_matrix = AlignmentMatrix(x, y, alignment)
    our_matrix.fill_matrix()
    our_matrix.calculate_score_find_start_positions()
    our_matrix.calculate_seq()
    # the only printing this function does
    our_matrix.print_results()
    return our_matrix


if __name__ == '__main__':
    # matrix_for_printing = calculate_alignment(input(), input(), "global")
    # matrix_for_printing = calculate_alignment(input(), input(), "local")
    matrix_for_printing = calculate_alignment(input(), input(), "semi-global")
    # matrix_for_printing.print_colored_matrix()
