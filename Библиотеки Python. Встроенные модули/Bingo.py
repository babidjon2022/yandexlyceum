import random


def make_bingo():
    d = list(map(lambda _: list(), range(5)))
    allnumbers = set()
    k = 0
    for i in range(5):
        for j in range(5):
            if i == j == 2:
                d[i].append(0)
                continue
            k = random.randint(1, 76)
            while k in allnumbers:
                k = random.randint(1, 76)
            d[i].append(k)
            allnumbers.add(k)
    return tuple(map(tuple, d))
