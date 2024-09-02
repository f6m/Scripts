from sympy import *
R=Symbol('R')
x=Symbol('x')
def y(x): 
  return x*sqrt(2*log(x)+R)
print(simplify(diff(y(x),x)))
print(simplify((x**2+y(x)**2)/(x*y(x))))
#>(R + 2*log(x) + 1)/sqrt(R + 2*log(x))
#>(R + 2*log(x) + 1)/sqrt(R + 2*log(x))
