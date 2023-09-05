import sys
from math import *
def func(x):
    return (x*cos(x)) + (sin(x))

def zero(a,b,f):
    i = 0
    eps = sys.float_info.epsilon

    while True:
        i +=1
        
        #step 1
        if a == b:
            break
        c = ((f(b)*a) - (f(a)*b)) / (f(b) - f(a))

        if abs(f(c)) <= ulp(0):
            break
        
        if a == c:
            break
        #step 2a
        if b == c:
            break
        if f(a) * f(c) > 0:
            d = (f(a) * (a - c)) / (f(a) - f(c))
        #step 2b
        elif f(a) * f(c) < 0:
            d = (f(b) * (b - c)) / (f(b) - f(c))

        #step 2c
        if d <=a or d>=b:
            d = (a + b) / 2 #???

        if abs(f(d)) <= ulp(0):
            break
        
        #step 2d
        if c < d:
            a = c
            b = d
        else:
            a = d
            b = c
    return((a+b)/2,i)


        
print(zero(4,5,func))
        


