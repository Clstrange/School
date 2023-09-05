import sys
from math import *
def func(x):
    return x * cos(x) + sin(x)

def zero(a,b,f):
    i = 0
    eps = sys.float_info.epsilon
    while True:
        while True:
            i += 1
            c = ((f(b)*a) - (f(a)*b)) / (f(b) - f(a))
            if c <= a:
                c = a + eps * abs(a)
            elif c >= b:
                c = b - eps * abs(b)
            elif c == a or c == b:
                break
            if abs(f(c)) < ulp(0):
                return c
            d = (f(a) * (a - c)) / (f(a) - f(c))
            if d <= a or d >= b:
                break
            funcD = func(d)
            if abs(funcD) <= ulp(0):
                return d
            if f(a)*(d)>0:
                a=d
                funcA = f(d)
            else:
                b = d
                funcB = f(d)
        c = (a+b)/2

    return(a,b,i)


        
print(zero(2,3,func))
        


