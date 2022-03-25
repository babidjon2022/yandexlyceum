import sys
s = list(map(lambda x: x.lstrip(), sys.stdin.read().split('\n')))
d = dict()
for i in range(len(s)):
    if s[i] and s[i][0] == '#':
        d[f'Line {i + 1}'] = s[i][s[i].index('#') + 1:].lstrip()
for i in d:
    print(f'{i}: {d[i]}')
