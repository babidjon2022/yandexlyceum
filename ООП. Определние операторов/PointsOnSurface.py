class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, cl2):
        return self.x == cl2.x and self.y == cl2.y

    def __ne__(self, cl2):
        return self.x != cl2.x or self.y != cl2.y
