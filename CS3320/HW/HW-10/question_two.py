import numpy as np
import math
W = np.log(np.array([1, 2, 3, 4]))
A = np.log(np.array([6, 2, 1, 1]))
lFit = np.polyfit(W, A, 1)
a=math.exp(lFit[1])
b=lFit[0]
A95 = a*math.pow(95,b)
print(f"a={a}, b={b}, A95={A95}")