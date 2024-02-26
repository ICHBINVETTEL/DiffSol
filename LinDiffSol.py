import numpy as np
from matplotlib import pyplot as plt
from scipy import *
from math import *
from sympy import *

x,y = symbols('x y')
def P(x):
    p = input("Enter the function P: ")
    p1 = sympify(p)
    return(p1)

def Q(x):
    q = input("Enter the function Q: ")
    q1 = sympify(q)
    return(q1)

def int(x):
    I = integrate(P(x),x)
    I1 = exp(I)
    IF = sympify(I1)
    y = integrate(IF*Q(x))/IF
    return(y)
int(x)
