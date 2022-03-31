class Table:

    def __init__(self, rows, cols):
        self.table = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.table[row][col]

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1

    def delete_col(self, col):
        for i in range(self.rows):
            self.table[i].pop(col)
        self.cols -= 1

    def add_row(self, row):
        self.table.insert(row, [0 for _ in range(self.cols)])
        self.rows += 1

    def add_col(self, col):
        for i in range(self.rows):
            self.table[i].insert(col, 0)
        self.cols += 1

    def set_value(self, row, col, value):
        self.table[row][col] = value
