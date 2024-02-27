import numpy as np
from matplotlib import pyplot as plt
from scipy import *
from math import *
from sympy import *

a = float(input("Enter the co-eff a: "))
b = float(input("Enter the co-eff b: "))
c = float(input("Enter the co-eff c: "))
coeff_mat = np.array([[a],[b],[c]])
print(coeff_mat)

x,y,C1,C2 = symbols('x y C1 C2')
D = b**2 - 4*a*c
r1 = (-b + sqrt(D))/(2*a)
r2 = (-b - sqrt(D))/(2*a)
soln_mat = np.array([[r1],[r2]])
def soln():
    if(r1!=r2 and D>=0):
        y = sympify(C1*exp(r1*x) + C2*exp(r2*x))
        return(y)
    if(r1==r2 and D>=0):
        y = sympify(C1*exp(r1*x) + C2*x*exp(r2*x))
        return(y)
    if(D<0):
        alpha = (r1+r2)/2
        beta = (r1-r2)/2j
        y = exp(alpha*x)*(C1*cos(beta*x) + C2*sin(beta*x))
        return(y)
soln()

K = soln()
def func_plot():
    plot(K.subs({C1: 1,C2: 2}),(x,-10,10),xlabel='x',ylabel='y',title='Soln.')

func_plot()
