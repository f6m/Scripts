from sympy import *
t,s=symbols('t,s')
f=(-3*s**2+10*s-4)/((s-1)*(s-2)**2)
g=1/((s**2)*(s+1)**2)
print(apart(f))
print(apart(g))
def y(t): return 3*exp(t)-6*exp(2*t)+4*t*exp(2*t)
print(simplify(diff(y(t),t,2)-3*diff(y(t),t,1)+2*y(t)))
#3/(s - 1) - 6/(s - 2) + 4/(s - 2)**2
#4*exp(2*t)
