import numpy as np
from scipy.interpolate import CubicSpline
import pylab


def Runge(x):
    return 1/1+25*x**2

x = np.linspace(1,5,50)
y = Runge(4.3)

xx = np.linspace(1,5)
cs = CubicSpline(x,y,bc_type='natural')
yy = cs(xx)
yR = Runge(xx)

pylab.scatter(x,y,c='k',marker='o')
pylab.plot(xx,yy,c='k',ls='- -', label='Spline')
pylab.plot(xx,yR,c='k',label='Runge')
pylab.grid()
pylab.xlabel('x')
pylab.ylabel('f(x)')
pylab.legend()