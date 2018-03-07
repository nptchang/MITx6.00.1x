# import math library
from math import *

def polysum(n,s):
    areaPoly = (0.25*n*s*s)/(tan(pi/n))
    perimeter = n * s
    ansSum = areaPoly + perimeter**2
    return round(ansSum, 4)

