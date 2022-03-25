import sys
import itertools
dct = map(lambda x: x.lower(), input().split())


def func1(s):
    s = s.split()
    for i in range(len(s)):
        if len(tuple(filter(lambda x: ''.join(x).lower() in dct and ''.join(x).lower() !=
                                      s[i].lower(),
                            itertools.permutations(s[i])))) >= 1:
            s[i] = s[i], True
        else:
            s[i] = s[i], False
    return list(map(lambda x: (x[0].lower(), x[1]), s))


def func2(s):
    for j1 in range(len(s)):
        if s[j1][1]:
            s[j1] = '#' * len(s[j1][0])
        else:
            s[j1] = s[j1][0]
    return ' '.join(s)


print(*map(func2, map(func1, sys.stdin.read().split('\n'))), sep='\n')
