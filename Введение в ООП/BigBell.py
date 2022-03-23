class BigBell():

    def __init__(self):
        self.x1 = 'ding'
        self.x2 = 'dong'

    def sound(self):
        print(self.x1)
        self.x1, self.x2 = self.x2, self.x1
