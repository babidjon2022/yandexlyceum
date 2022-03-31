class Rectangle:

    def __init__(self, x, y, w, h):
        x1 = x + w
        y1 = y + h
        self.rect = [(x, y), (x1, y1)]

    def intersection(self, rect):
        rect = rect.rect
        xrange3 = sorted(
            set(range(self.rect[0][0], self.rect[1][0] + 1))
            & set(range(rect[0][0], rect[1][0] + 1)))
        yrange3 = sorted(
            set(range(self.rect[0][1], self.rect[1][1] + 1))
            & set(range(rect[0][1], rect[1][1] + 1)))
        if xrange3 and yrange3 and xrange3[-1] - xrange3[0] and yrange3[
                -1] - yrange3[0]:
            return Rectangle(xrange3[0], yrange3[0], xrange3[-1] - xrange3[0],
                             yrange3[-1] - yrange3[0])

    def get_x(self):
        return self.rect[0][0]

    def get_y(self):
        return self.rect[0][1]

    def get_w(self):
        return self.rect[1][0] - self.rect[0][0]

    def get_h(self):
        return self.rect[1][1] - self.rect[0][1]
