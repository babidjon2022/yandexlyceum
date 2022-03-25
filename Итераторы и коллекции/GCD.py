import sys
import functools
import math

print(
    int(
        functools.reduce(
            lambda x, y: math.gcd(x, y),
            list(map(lambda x: int(x),
                     sys.stdin.read().split('\n'))))))
