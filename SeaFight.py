def search_ship(d, row, col):
    ship = [(row, col)]
    direction = None
    for _ in range(1):
        if row - 1 in range(10) and row + 1 in range(10) and col - 1 in range(
                10) and col + 1 in range(10):
            if d[row - 1][col] == 'x' or d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x' or d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if row - 1 not in range(10) and col - 1 not in range(10):
            if d[row + 1][col] != 'x' and d[row][col + 1] != 'x':
                break
            if d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if row - 1 not in range(10) and col + 1 not in range(10):
            if d[row + 1][col] != 'x' and d[row][col - 1] != 'x':
                break
            if d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x':
                direction = 'hor'
                break
        if row + 1 not in range(10) and col - 1 not in range(10):
            if d[row - 1][col] != 'x' and d[row][col + 1] != 'x':
                break
            if d[row - 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if row + 1 not in range(10) and col + 1 not in range(10):
            if d[row - 1][col] != 'x' and d[row][col - 1] != 'x':
                break
            if d[row - 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x':
                direction = 'hor'
                break
        if row - 1 not in range(10):
            if d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x' or d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if row + 1 not in range(10):
            if d[row - 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x' or d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if col - 1 not in range(10):
            if d[row - 1][col] == 'x' or d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col + 1] == 'x':
                direction = 'hor'
                break
        if col + 1 not in range(10):
            if d[row - 1][col] == 'x' or d[row + 1][col] == 'x':
                direction = 'ver'
                break
            if d[row][col - 1] == 'x':
                direction = 'hor'
                break
    if direction is not None:
        if direction == 'ver':
            for i in range(row - 1, -1, -1):
                if d[i][col] == 'x':
                    ship.append((i, col))
                else:
                    break
            for i in range(row + 1, 10):
                if d[i][col] == 'x':
                    ship.append((i, col))
                else:
                    break
        if direction == 'hor':
            for i in range(col - 1, -1, -1):
                if d[row][i] == 'x':
                    ship.append((row, i))
                else:
                    break
            for i in range(col + 1, 10):
                if d[row][i] == 'x':
                    ship.append((row, i))
                else:
                    break
    around_ship = list()
    for row1, col1 in ship:
        if row1 - 1 in range(10):
            around_ship.append((row1 - 1, col1))
        if row1 + 1 in range(10):
            around_ship.append((row1 + 1, col1))
        if col1 - 1 in range(10):
            around_ship.append((row1, col1 - 1))
        if col1 + 1 in range(10):
            around_ship.append((row1, col1 + 1))
        if row1 - 1 in range(10) and col1 - 1 in range(10):
            around_ship.append((row - 1, col - 1))
        if row1 - 1 in range(10) and col1 + 1 in range(10):
            around_ship.append((row - 1, col + 1))
        if row1 + 1 in range(10) and col1 - 1 in range(10):
            around_ship.append((row + 1, col - 1))
        if row1 + 1 in range(10) and col1 + 1 in range(10):
            around_ship.append((row + 1, col + 1))
    return around_ship


class SeaMap():

    def __init__(self):
        self.matrix = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.matrix[row][col] = '*'
            return None
        if result == 'hit':
            self.matrix[row][col] = 'x'
            return None
        if result == 'sink':
            self.matrix[row][col] = 'x'
            for x, y in search_ship(self.matrix, row, col):
                self.matrix[x][y] = '*'

    def cell(self, row, col):
        return self.matrix[row][col]
