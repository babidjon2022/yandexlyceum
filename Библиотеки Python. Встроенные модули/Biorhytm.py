from math import sin, pi
import datetime


def biorhytm(p, t):
    return sin((2 * pi * t) / p) * 100


deltadate = (-(datetime.date(*map(int, reversed(input().split('.')))) -
               datetime.date(*map(int, reversed(input().split('.')))))).days
print(*map(lambda x: round(x, ndigits=2), map(lambda x: biorhytm(x, t=deltadate),
                                              (23, 28, 33))), sep='\n')
