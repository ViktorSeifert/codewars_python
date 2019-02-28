COLUMNS = [chr(i) for i in range(ord("A"), ord("G") + 1)]
ROWS = range(7)
DUMMY_VALUE = "Draw"


class Board(object):
    def __init__(self):
        self.columns = {}
        for c in COLUMNS:
            self.columns[c] = []

    def apply_move(self, move):
        column, color = move.split("_")
        self.columns[column].append(color)

    def __repr__(self):
        result = []
        for c in COLUMNS:
            r = c + ": "
            for i in self.columns[c]:
                r += "{:10}".format(i)
            result.append(r)

        return "\n".join(result)

    def winner(self):
        for c in COLUMNS:
            color, length = longest_sequence(self.column_seq(c))
            if length >= 4 and color != DUMMY_VALUE:
                return color

            for r in ROWS:
                color, length = longest_sequence(self.right_diagonal_seq(c, r))
                if length >= 4 and color != DUMMY_VALUE:
                    return color

                color, length = longest_sequence(self.left_diagonal_seq(c, r))
                if length >= 4 and color != DUMMY_VALUE:
                    return color

        for r in ROWS:
            color, length = longest_sequence(self.row_seq(r))
            if length >= 4 and color != DUMMY_VALUE:
                return color

        return "Draw"

    def column_seq(self, column):
        return self.columns[column]

    def row_seq(self, row):
        for c in COLUMNS:
            if row < len(self.columns[c]):
                yield self.columns[c][row]
            else:
                yield DUMMY_VALUE

    def right_diagonal_seq(self, column, row):
        column_index = COLUMNS.index(column)

        while row in ROWS and column_index < len(COLUMNS):
            current_column = self.columns[COLUMNS[column_index]]
            if row < len(current_column):
                yield current_column[row]
            else:
                yield DUMMY_VALUE
            column_index += 1
            row += 1

    def left_diagonal_seq(self, column, row):
        column_index = COLUMNS.index(column)

        while row in ROWS and column_index >= 0:
            current_column = self.columns[COLUMNS[column_index]]
            if row < len(current_column):
                yield current_column[row]
            else:
                yield DUMMY_VALUE
            column_index -= 1
            row += 1


def longest_sequence(color_seq):
    seqs = {}
    current_color = DUMMY_VALUE
    current_count = 0

    for color_element in color_seq:
        if color_element == current_color:
            current_count += 1
        else:
            current_count = 1
            current_color = color_element

        seqs[current_count] = color_element

    if len(seqs.keys()) == 0:
        return DUMMY_VALUE, 0

    count = max(seqs.keys())

    return seqs[count], count


def who_is_winner(pieces_position_list):
    board = Board()
    for p in pieces_position_list:
        board.apply_move(p)
        current_winner = board.winner()
        if current_winner != "Draw":
            return current_winner

    return board.winner()


print(who_is_winner([
    'B_Red', 'C_Yellow', 'G_Red', 'B_Yellow', 'A_Red', 'A_Yellow', 'C_Red', 'E_Yellow', 'D_Red', 'D_Yellow',
     'E_Red', 'E_Yellow', 'G_Red', 'A_Yellow', 'A_Red', 'F_Yellow', 'G_Red', 'C_Yellow', 'D_Red', 'A_Yellow',
     'B_Red', 'G_Yellow', 'F_Red', 'D_Yellow', 'A_Red'
]))
