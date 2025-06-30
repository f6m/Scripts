from sympy import * 
x=Symbol('x')

#Ecuacion diferencial: y^{(2)}+y^{(1)}=x+e^x
#Funciones del conjunto fundamental de soluciones
def y1(x): return 1
def y2(x): return exp(-x)

#Colocamos la matriz de Wronski y la funcion de entrada
A=Matrix([[y1(x),y2(x)],[diff(y1(x),x),diff(y2(x),x)]])
b=Matrix([0,exp(x)+x])

#Calculamos la inversa de la matriz de Wronski para resolver 
#el sistema de ecuaciones
C=A.inv()*b
print(simplify(C))

#Integramos las soluciones del sistema de ecuaciones
c1=integrate(C[0],x)
c2=integrate(C[1],x)
print(c1)
print(c2)

#Construimos la solucion particular a partir de las integrales
yp=simplify(c1+c2*exp(-x))
print(yp)

#Comprobamos la solucion
print(diff(yp,x,2)+diff(yp,x,1))
