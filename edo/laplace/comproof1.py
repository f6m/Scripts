from sympy import *
t,s=symbols('t,s')
def y(t): return (1/10)*(cos(3*t)+(1/3)*sin(3*t)
-11*exp(3*t)*cos(sqrt(6)*t)-(8/sqrt(6))*exp(3*t)*sin(sqrt(6)*t))

print(simplify(diff(y(t),t,2)-6*diff(y(t),t,1)+15*y(t)))

f=(-s**3+2*s**2-9*s+24)/(s**2+9)*(s**2-6*s+15)
print(apart(f))

#8.88178419700125e-16*sqrt(6)*exp(3*t)*sin(sqrt(6)*t) + 2.0*sin(3*t) - 
#2.22044604925031e-16*cos(3*t)
