import sys
import math

def ulps(x, y):
    base = sys.float_info.radix
    exp = 0
    lub = 1
    while (lub <=x):
        lub *= base
        exp+=1
    # eps = sys.float_info.epsilon
    # prec = sys.float_info.mant_dig
    # inf = math.inf
    # print(prec)
    if (x == math.inf) or (y == math.inf) or (x < 0 and y >= 0) or (y < 0 and x >= 0 ):
        return math.inf
    
    if x > y:
        print("test")
        x, y = y, x
    e = math.floor(math.log2(x))
    if math.floor(math.log2(x)) == (math.floor(math.log2(y)-1)):
        interval_count = (y - x) / 2**-52+e
    else:
        lower_upper_bound = math.floor(math.log(x)) + 1
        upper_lower_bound = math.floor(math.log(y))
        x_section = (lower_upper_bound -x) / (2**(-52 + e))
        y_section = (y - upper_lower_bound) / (2**(-52+e))
        middle_section = ((math.floor(math.log(y)) - math.floor(math.log(x))) * (2**52)) + 1
        interval_count = x_section + y_section + middle_section
    return interval_count
# print(ulps(-1.0, -1.0000000000000003))
# print(ulps(1.0, 1.0000000000000003))
# print(ulps(1.0, 1.0000000000000004))
# print(ulps(1.0, 1.0000000000000005))
# print(ulps(1.0, 1.0000000000000006))
# print(ulps(0.9999999999999999, 1.0))
# print(ulps(0.4999999999999995, 2.0))
# print(ulps(0.5000000000000005, 2.0))
# print(ulps(0.5, 2.0))
print(ulps(1.0, 2.0))
# print(2.0**52)
# print(ulps(-1.0, 1.0))
# print(ulps(-1.0, 0.0))
# print(ulps(0.0, 1.0))
# print(ulps(5.0, math.inf))
# print(ulps(15.0, 100.0))

