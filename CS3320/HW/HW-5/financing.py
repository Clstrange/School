
import numpy as np

def myfunc(x):
    return 71991 * ((x*(1+x)**84)/(((1+x)**84)-1)) - 1000

def false(func,xl,xu,maxit=20): 
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
    return xm*1200

def main():
    print(false(myfunc, .03, .09, 1000))
if __name__ == "__main__":
    main()