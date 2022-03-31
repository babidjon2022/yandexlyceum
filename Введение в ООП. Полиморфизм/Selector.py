class Selector:

    def __init__(self, values):
        self.evens = list(filter(lambda x: x % 2 == 0, values))
        self.odds = [i for i in values if i not in self.evens]

    def get_odds(self):
        return self.odds

    def get_evens(self):
        return self.evens
