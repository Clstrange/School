from numpy import polyfit, polyval
x=[0,1.8,5,6,8.2,9.2]
y=[2.6,16.415,5.375,3.5,2.015,2.54]
intPoly = polyfit(x,y,5)
print(intPoly)
print(polyval(intPoly, 3.5))