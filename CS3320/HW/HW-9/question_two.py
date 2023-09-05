from math import sqrt


A = [[8,2,-10,],[-9,1,3],[15,-1,6]]
n = 3
sumation = 0
for i in range(n):
    for j in range(n):
        sumation += A[i][j]**2

A2 = sqrt(sumation)
print(A2)