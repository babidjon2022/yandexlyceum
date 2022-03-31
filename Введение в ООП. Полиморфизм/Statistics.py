class MinStat:

    def __init__(self):
        self.d = list()

    def add_number(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.d.append(float(number))

    def result(self):
        if self.d:
            return int(min(self.d))


class MaxStat:

    def __init__(self):
        self.d = list()

    def add_number(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.d.append(float(number))

    def result(self):
        if self.d:
            return int(max(self.d))


class AverageStat:

    def __init__(self):
        self.d = list()

    def add_number(self, number):
        if isinstance(number, int) or isinstance(number, float):
            self.d.append(float(number))

    def result(self):
        if self.d:
            return sum(self.d) / len(self.d)
