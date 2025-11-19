#https://github.com/EmmaWolman/lab11-EW-CG
# Partner 1: Emma Wolman
# Partner 2: Connor Gionet

import math

def square_root(a):
    if a < 0:
        raise ValueError("must be non-negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b<=0 or b == 1:
        raise ValueError
    return math.log(a,b)

def log(a, b):
    return logarithm(a, b)

def exp(a,b):
    return a**b






