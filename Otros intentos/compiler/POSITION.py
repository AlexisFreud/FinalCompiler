class Position:
    def __init__(self, index, line_number, col_number):
        self.index = index
        self.line_number = line_number
        self.col_number = col_number

    def advance(self, current_char=None):
        self.index += 1
        self.col_number += 1
        if current_char == "\n":
            self.line_number += 1
            self.col_number = 0
        return self

    def copy(self):
        return Position(self.index, self.line_number, self.col_number)