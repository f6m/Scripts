from sympy import *
s,t = symbols('s,t')
#O bien definimos una funcion como el producto para la convolucion
#entre f(t)=e^{-3t} y g(t)=e^{-7t}
def u(s): return exp(-3*(t - s))*exp(-7*s)
#o definimos las funciones por separado
def f(t): return exp(-3*t)
def g(t): return exp(-7*t)

print(integrate(u(s),(s,0,t)))
print(integrate(f(t-s)*g(s),(s,0,t)))
