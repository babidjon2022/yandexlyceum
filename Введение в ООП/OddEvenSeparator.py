class OddEvenSeparator():

    def __init__(self):
        self.oddlist = list()
        self.evenlist = list()

    def odd(self):
        return self.oddlist

    def even(self):
        return self.evenlist

    def add_number(self, n):
        if n % 2 == 0:
            self.evenlist.append(n)
            return None
        self.oddlist.append(n)
