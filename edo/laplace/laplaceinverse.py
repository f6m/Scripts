from sympy import *
s,t = symbols('s,t')
def u(t): return exp(-(t - 2))*Heaviside(t-2)
def F(s): return exp(-2*s) * s/(s*s+1)
laplace_transform(u(t),t,s)
inverse_laplace_transform(F(s),s,t)
