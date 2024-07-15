from sympy import *
t=Symbol('t')
s=Symbol('s')
laplace_transform(Heaviside(t-1),t,s)
(exp(-s)/s, 0, True)
