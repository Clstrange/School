import numpy as np
import math

def myfunc(x):
    return 2*x**3 - x - 7

def false(func,xl,xu,maxit): 
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

    for i in range(maxit): 
        xm = xl - func(xl)*((xu-xl)/(func(xu)-func(xl)))
        if func(xm)*func(xl)<0: 
            xl = xm 
        else: 
            xu = xm 
    return xm


def main():
    print(false(myfunc, 0, 4, 1))
if __name__ == "__main__":
    main()