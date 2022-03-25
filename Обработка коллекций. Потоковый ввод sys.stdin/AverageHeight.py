import sys
s = sys.stdin.read()
if s:
    s = list(map(lambda x: int(x), s.split('\n')))
    print(sum(s) / len(s))
else:
    print('-1')
