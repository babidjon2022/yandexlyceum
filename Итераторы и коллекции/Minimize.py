import sys
import functools
print(str(functools.reduce(lambda x, y: x if x < y else y, sys.stdin.read().split('\n'))))
