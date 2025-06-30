from sympy import *
s,t = symbols('s,t')
from numpy import inf
def u(t): return cos(-t)

#Derivación
print(diff(u(t),t,2))
#Integral definida
print(simplify(integrate(u(t),(t,0,1))))
#Integral indefinida
print(simplify(integrate(u(t),t)))
#Integral impropia
print(simplify(integrate(u(t),(t,0,inf))))
