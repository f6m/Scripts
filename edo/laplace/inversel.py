from sympy import *
s,t=symbols('s,t')
p=Symbol('p')
inverse_laplace_transform(
-exp(-s*pi)/((s**2+1)*(s+1)),s,t)
-2*(exp(-t + pi) - sin(t) + cos(t))*
Heaviside(t - pi)/((1 - I)**2*(1 + I)**2)
