class Button():

    def __init__(self):
        self.k = 0

    def click(self):
        self.k += 1

    def click_count(self):
        return self.k

    def reset(self):
        self.k = 0
