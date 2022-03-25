import sys

lst = list(
    map(lambda i: (int(i.split()[0]), ' '.join(i.split()[1:])),
        sys.stdin.read().split('\n')))
dct = dict()
for i in lst:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
can_spend = dict()
for i in dct:
    if dct[i] != 1:
        can_spend[i] = dct[i] - 1
print(sum(map(lambda x: x[0] * can_spend[x], can_spend)))
