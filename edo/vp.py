#Variacion de parametros made easy
#integrate puede no devolver solucion
from sympy import * 
x=Symbol('x')
A=Matrix([[1,exp(-x)],[0,-exp(-x)]])
def y(x): return exp(x)
b=Matrix([0,exp(x)+x])
C=A.inv()*b
print(simplify(C))
c1=integrate(C[0],x)
c2=integrate(C[1],x)
print(c1)
print(c2)
yp=simplify(c1+c2*exp(-x))
print(yp)
print(diff(yp,x,2)+diff(yp,x,1))
