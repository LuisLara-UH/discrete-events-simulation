import random as rnd
import math

def uniform(a, b):
    U = rnd.random()

    return a + ((b - a)*U)

def exponential(h):
    U = rnd.random()
    
    return -1 * (math.log(U, 10) / h)