from math import hypot
from random import random
print(len(tuple(filter(lambda _: hypot(random(), random())
      <= 1, range(100000)))) * 0.00004)
