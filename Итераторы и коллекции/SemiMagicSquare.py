import sys
s = list(map(lambda j: list(map(lambda i: int(i), j.split())), sys.stdin.read().split('\n')))
print('YES') if all(map(lambda x: sum(x) == sum(s[0]), s)) and \
                all(map(lambda x: sum(x) == sum(s[0]), zip(*s))) else print('NO')
