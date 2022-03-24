from itertools import chain
import random
dct = tuple(map(str, chain(range(2, 10), map(chr, chain(range(65, 73), range(74, 79),
                                                        range(80, 91), range(
                                                            97, 108),
                                                        range(109, 111), range(112, 123))))))


def generate_password(m):
    possibleletters = list(dct)
    stroke = str()
    for _ in range(m):
        letter = random.choice(possibleletters)
        possibleletters.remove(letter)
        stroke += letter
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
