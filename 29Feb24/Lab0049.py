##Map 2
# map is created whenever we have list of items
# list, set, tuple, dictionary

import math

def cbrt(num):
    return math.cbrt(num)


mylist = [27,125,64]
cubrt = list(map(cbrt,mylist))
print(cubrt)
