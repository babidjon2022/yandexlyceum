import sys
d = list(map(lambda x: (x, sum(map(lambda y: ord(y.upper()) - ord('A') + 1, x))),
             sys.stdin.read().split('\n')))
d_dict = dict()
for i in d:
    if i[1] in d_dict:
        d_dict[i[1]].append(i[0])
    else:
        d_dict[i[1]] = [i[0]]
for i in sorted(d_dict.keys()):
    print(*sorted(d_dict[i]), sep='\n', end='\n')
