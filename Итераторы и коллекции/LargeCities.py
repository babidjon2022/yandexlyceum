import sys

lst = list(
    map(lambda x: (x.split()[0], int(x.split()[2])),
        sys.stdin.read().split('\n')))
dct = dict()
for i in lst:
    begin = i[1] // 1000 - i[1] // 1000 % 100
    end = begin + 100
    interval = f'{begin} - {end}'
    if interval not in dct:
        dct[interval] = [i[0]]
    else:
        dct[interval].append(i[0])
for i in sorted(dct.keys(), key=lambda x: int(x.split()[0])):
    print(f'{i}:', end=' ')
    print(*sorted(dct[i]), sep=', ')
