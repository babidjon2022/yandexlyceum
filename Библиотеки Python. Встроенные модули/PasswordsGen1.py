import random
import itertools
dct = tuple(map(str, itertools.chain(map(chr, itertools.chain(range(65, 73),
                                                              range(74, 79),
                                                              range(80, 91),
                                                              range(97, 108),
                                                              range(109, 111),
                                                              range(112, 123))),
                                     range(2, 10))))


def generate_password(m):
    return ''.join(random.choice(dct) for _ in range(m))


def main(n, m):
    d = list()
    for _ in range(n):
        k = generate_password(m)
        while k in d:
            k = generate_password(m)
        d.append(k)
    return d
