import numpy

a = numpy.matrix('0,-3,7; 1,2,-1; 5,-2,0')
b = numpy.matrix('4;0;3')

determinant = numpy.linalg.det(a)
print(determinant)