import sys
print(len(tuple(filter(lambda x: x and x[0] == '#',
                       tuple(map(lambda x: x.lstrip(), sys.stdin.read().split('\n')))))))
