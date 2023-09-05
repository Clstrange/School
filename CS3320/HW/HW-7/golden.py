from math import sin, sqrt
import sys
eps = sys.float_info.epsilon

def func(x):
    return (x**4 + 2*x**3 + 8*x*2 + 5*x)

def golden(func, left, right, tol):
    num = (sqrt(5)-1)/2
    xl = left
    xu = right
    d = num*(xu-xl)
    x1 = xl + d ; f1 = func(x1)
    x2 = xu - d ; f2 = func(x2)
    i = 0

    while i < 1:
        i += 1
        if f1 < f2:
            xopt = x1
            xl = x2
            x2 = x1
            f2 = f1
            x1 = xl + (xu - x2)
            f1 = func(x1)
        elif f1 > f2:
            xopt = x2
            xu = x1
            x1 = x2
            f1 = f2
            x2 = xu - (x1-xl)
            f2 = func(x2)
        if xopt != 0:
            if (1-num)*(xu-xl)/abs(xopt)<=tol:
                break
    return (xopt, func(xopt), i+1)
    
print(golden(func, -1, 0, eps))