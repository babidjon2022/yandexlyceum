import sys
print(any(map(lambda z: 0 in z, list(map(lambda x: list(map(int, x.split())),
                                         sys.stdin.read().split('\n'))))))
