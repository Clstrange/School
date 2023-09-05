import numpy as np
import math
def myfunc(x):
    return x**3 - x**2 + (- 17) *x - 15

def bisect1(func,xl,xu,rootType,maxit=20): 
    """ 
    Uses the bisection method to estimate a root of func(x). 
    The method is iterated maxit (default = 20) times. 
    Input: 
        func = name of the function 
        xl = lower guess 
        xu = upper guess 
    Output: 
        xm = root estimate 
        or 
        error message if initial guesses do not bracket solution 
    """
    xm = (xl+xu)/2
    if rootType == "ubr":
        xu = xm
    else:
        xl = xm

    for i in range(maxit-1): 
        xm = (xl+xu)/2
        if func(xm)*func(xl)>0: 
            xl = xm 
        else: 
            xu = xm 
    return xm


def main():
    print(bisect1(myfunc, 0, 1, "lbr", 3))
if __name__ == "__main__":
    main()