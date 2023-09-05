import numpy as np

A = [[15, -3, -1], [-3, 18, -6], [-4,-1, 12]]
b = [4000,1200,2350]
inverse_A = np.linalg.inv(A)
print(inverse_A)