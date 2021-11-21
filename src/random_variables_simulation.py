import random as rnd
import math

def uniform(a, b):
    U = rnd.random()

    return int(a + ((b - a)*U))

def exponential(h):
    U = rnd.random()
    
    return int(-1 * (math.log(U) * h))