def get_value(cl, index):
    if index in cl.dct:
        return cl.dct[index]
    return 0


class Polynomial:

    def __init__(self, coefficients):
        self.dct = {x[0]: x[1] for x in enumerate(coefficients)}

    def __getitem__(self, index):
        return self.dct[index]

    def __add__(self, cl2):
        newlst = list()
        for i in set(self.dct.keys()) | set(cl2.dct.keys()):
            newlst.append(get_value(self, i) + get_value(cl2, i))
        return Polynomial(newlst)

    def __call__(self, x):
        return sum(map(lambda y: self.dct[y] * x**y, self.dct))
