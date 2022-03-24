from itertools import chain
import random
digits = tuple(map(str, range(2, 10)))
upperletters = tuple(map(chr, chain(range(65, 73), range(74, 79), range(80, 91))))
lowerletters = tuple(map(chr, chain(range(97, 108), range(109, 111), range(112, 122))))
allsymbols = digits + upperletters + lowerletters


def generate_password(m):
    stroke = str()
    dindex, uindex, lindex = random.sample(range(m), k=3)
    for _ in range(m):
        if _ == dindex:
            stroke += random.choice(tuple(digits))
            continue
        if _ == uindex:
            stroke += random.choice(tuple(upperletters))
            continue
        if _ == lindex:
            stroke += random.choice(tuple(lowerletters))
            continue
        stroke += random.choice(allsymbols)
    return stroke


def main(n, m):
    passwordlist = list()
    k = 0
    while True:
        password = generate_password(m)
        if password in passwordlist:
            continue
        passwordlist.append(password)
        k += 1
        if k == n:
            break
    return passwordlist
