from sympy import *
x=Symbol('x')
m=Symbol('m')
#y'+y^2=2/x^2
#u'+2u/x=1
def y(x): return (1/(m/(x*x)+(x/3)))-1/x
simplify(diff(y(x),x)+y(x)*y(x)
