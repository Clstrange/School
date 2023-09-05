import numpy as np
import math
y = np.log(np.array([800, 985, 1490, 1950,2850, 3600]))
RHS=np.matmul(np.vstack((np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]), np.power(np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]),0))).transpose().transpose(),y)
lFit =np.matmul(np.linalg.inv(np.matmul(np.vstack((np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]), np.power(np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]),0))).transpose().transpose(),np.vstack((np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]), np.power(np.array([0.4, 0.8, 1.2, 1.6, 2, 2.3]),0))).transpose())),RHS)
a=math.exp(lFit[1])
b=lFit[0]
y2 = a*math.exp(b*2)
print(f"a={a}, b={b}, y(2)={y2}")

