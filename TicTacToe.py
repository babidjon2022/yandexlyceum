import itertools


class TicTacToeBoard():

    def __init__(self):
        self.map = [['-' for _ in range(3)] for _ in range(3)]
        self.X_0_cycle = itertools.cycle(('X', '0'))
        self.game_end = False

    def new_game(self):
        self.__init__()
    
    def get_field(self):
        return self.map

    def check_field(self):
        if any(
                map(lambda y: all(map(lambda x: x == 'X', self.map[y])),
                    range(3))):
            return 'X'
        if any(
                map(lambda y: all(map(lambda x: x == '0', self.map[y])),
                    range(3))):
            return '0'
        if all(map(lambda x: self.map[x][x] == 'X', range(3))) or all(
                map(lambda x: self.map[x][2 - x] == 'X', range(3))):
            return 'X'
        if all(map(lambda x: self.map[x][x] == '0', range(3))) or all(
                map(lambda x: self.map[x][2 - x] == '0', range(3))):
            return '0'
        if any(
                map(
                    lambda y: all(
                        map(lambda x: self.map[x][y] == 'X', range(3))),
                    range(3))):
            return 'X'
        if any(
                map(
                    lambda y: all(
                        map(lambda x: self.map[x][y] == '0', range(3))),
                    range(3))):
            return '0'
        if all(map(lambda x: x != '-', itertools.chain(*self.map))):
            return 'D'
        return None

    def make_move(self, row, col):
        if self.game_end:
            return 'Игра уже завершена'
        row -= 1
        col -= 1
        self.player = next(self.X_0_cycle)
        if self.map[row][col] == '-':
            self.map[row][col] = self.player
        else:
            self.player = next(self.X_0_cycle)
            return f'Клетка {row + 1}, {col + 1} уже занята'
        result = self.check_field()
        if result == 'X':
            self.game_end = True
            return 'Победил игрок X'
        if result == '0':
            self.game_end = True
            return 'Победил игрок 0'
        if result == 'D':
            self.game_end = True
            return 'Ничья'
        if result is None:
            return 'Продолжаем играть'
board = TicTacToeBoard()
board.new_game()
