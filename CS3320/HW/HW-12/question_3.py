from numpy import array
from scipy import integrate
x=array([0, 4, 6, 8, 12, 16, 20])
rho=array([4.00, 3.95, 3.89, 3.80, 3.60, 3.41, 3.30])
area=array([100, 103, 106, 110, 120, 133, 150])
xCm=100*x
rhoAreaInKg = rho*area/1000
massTrap=integrate.trapezoid(rhoAreaInKg,xCm)
massSimp=integrate.simpson(rhoAreaInKg,xCm)
percentDiff = (abs(massTrap-massSimp)/massSimp)*100
print(f"Trapezoidal method: {massTrap}")
print(f"Simpson method: {massSimp}")
print(f"The percent difference is {percentDiff}")
