class Table:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols
