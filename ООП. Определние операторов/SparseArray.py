class SparseArray:

    def __init__(self):
        self.array = dict()

    def __setitem__(self, key, value):
        self.array[key] = value

    def __getitem__(self, key):
        if key in self.array:
            return self.array[key]
        return 0
