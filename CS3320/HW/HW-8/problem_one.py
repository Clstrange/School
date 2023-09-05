from numpy import linalg, matrix
a = matrix('0,-7,5; 0, 4, 7;, 4, -3, 7')
b = matrix('50;-30;-40')

solved = linalg.solve(a,b)

print(solved)