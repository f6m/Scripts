from sympy import *
s,t = symbols('s,t')
a = Symbol('a')

#Funciones/señales
def c(t): return a
def e(t): return exp(a*t)*2
def p(t): return exp(t-a) * Heaviside(t-a)
def sh(t): return sinh(a*t)
def ch(t): return cosh(a*t)
def sn(t): return sin(a*t)
def cn(t): return cos(a*t)
def u(t): return t**(202)
def r(t): return diff(u(t),t)

print("L[a]=",laplace_transform(c(t),t,s))
print("L[e^(a*t)*2]=",laplace_transform(e(t),t,s))
print("L[e^(t-a)*U(t-a)]=",laplace_transform(p(t),t,s))
print("L[sinh(a*t)]=",laplace_transform(sh(t),t,s))
print("L[cosh(a*t)]=",laplace_transform(ch(t),t,s))
print("L[sin(a*t)]=",laplace_transform(sn(t),t,s))
print("L[cos(a*t)]=",laplace_transform(cn(t),t,s))
print("L[t^202]=",laplace_transform(u(t),t,s))
print("L[d(t^202)/dt]=",laplace_transform(r(t),t,s))
