
from math import cos, log,sin



x0 = 0.5
x1 = 0.7853981635
def func(x):
    return cos(x) - x
# def secant_method():
#     for i in range(2):
#         dfunc = (func(x1)-func(x0))/(x1-x0)
#         x0 = x1
#         x1 = x1 - (func(x1)/dfunc)

# def newton_method(x1):
#     for i in range(2):
#         x1 = x1 - (func(x1)/(-sin(x1)-1))
#         print(x1)

def iterative_method(x):
    for i in range(2):

        z = ((log(x)) + (x**2) + x - 3)
        x = z
        print(x)

iterative_method(1)