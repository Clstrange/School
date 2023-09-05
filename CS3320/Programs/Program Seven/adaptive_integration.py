import math

def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

def adaptive_simpson(f, a, b, tol, whole_area):
    c = (a + b) / 2
    left_area = simpson(f, a, c)
    right_area = simpson(f, c, b)
    approx_area = left_area + right_area
    
    if abs(approx_area - whole_area) <= 15 * tol:
        return approx_area + (approx_area - whole_area) / 15
    
    return adaptive_simpson(f, a, c, tol / 2, left_area) + adaptive_simpson(f, c, b, tol / 2, right_area)

def area(f, a, b, tol=5.0e-6):
    whole_area = simpson(f, a, b)
    return adaptive_simpson(f, a, b, tol, whole_area)

def f(x):
    return math.exp(x**2)

def f2(x):
    return (math.sin(x)) / x

def f3(x):
    return x

print(area(f, -1, 1, tol=5.0e-6))

print(area(f2, -1, 10, tol=5.0e-6))
