import sys
import random
names = sys.stdin.read().split('\n')


def names_random(names):
    names1 = names.copy()
    random.shuffle(names1)
    return names1


names1 = names_random(names)
while any(map(lambda x: x[0] == x[1], zip(names, names1))):
    names = names_random(names)
for i in range(len(names)):
    print(f'{names[i]} - {names1[i]}')
