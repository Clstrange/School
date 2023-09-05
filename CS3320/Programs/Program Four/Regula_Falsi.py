import sys
import numpy as np
eps = sys.float_info.epsilon
def myfunc(xIn):
    fVal = (3+xIn*(-10+xIn*(12+xIn*(-6+xIn))))
    return fVal
def myfunc2(xIn):
    fVal = (-9+xIn*(15+xIn*(-7+xIn)))
    return fVal

def regula_falsi(xLower, xUpper, func): 
    """ 
    Uses the Regula_Falsi method to estimate a root of func(x). 
    Input: 
        func = name of the function 
        xLower = lower guess 
        xUpper = upper guess 
    Output: 

        root: a root of the function in [xLower, xUpper] if one is found
        flag: indicating whether a root is found
        number of iterations: number of iterations used to find the root if a root was found
    """
    root = None
    flag = None
    iter_count = 0
    value = None

    if func(xLower) * func(xUpper) >= 0:
        flag = -1
        return (root, flag, iter_count, value)
    elif func(xLower) == 0:
        root = xLower
        flag = 0
        iter_count = 0
        value = myfunc(root)
        return (root, flag, iter_count, value)
    elif func(xUpper) == 0:
        root = xUpper
        flag = 0
        iter_count = 0
        value = myfunc(root)
        return (root, flag, iter_count)

    maxit = 100000
    root = 100
    print(eps)
    while (abs(func(root)) > eps):
        iter_count += 1
        previous_root = root
        root = xUpper - func(xUpper)*(xUpper-xLower)/(func(xUpper)-func(xLower))
        if func(root)*func(xLower)<0:
            xUpper = root 
        else: 
            xLower = root
        if root == np.nextafter(previous_root, root):
            print("test")
            break
        if iter_count == maxit:
            print("test_one")
            break

    flag = 0
    value = func(root)
    return (root, flag, iter_count, value)


def main():
    print(regula_falsi(0,1.5,myfunc2))
if __name__ == "__main__":
    main()