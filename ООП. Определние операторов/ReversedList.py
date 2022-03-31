class ReversedList:

    def __init__(self, lst):
        self.lst = lst[::-1]

    def __getitem__(self, index):
        return self.lst[index]

    def __len__(self):
        return len(self.lst)
