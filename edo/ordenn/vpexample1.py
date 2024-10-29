from sympy import * 
x=Symbol('x')
A=Matrix([[x**((1+sqrt(5))/2),x**((1-sqrt(5))/2)],
[((1+sqrt(5))/2)*x**((-1+sqrt(5))/2),((1-sqrt(5))/2)*x**((-1-sqrt(5))/2)]])
b=Matrix([0,1/x])
C=simplify(A.inv()*b)
c1=integrate(C[0],x)
c2=integrate(C[1],x)
print(c1)
print(c2)
yp=simplify(c1*x**((1+sqrt(5))/2)+c2*x**((1-sqrt(5))/2))
print(yp)
print(diff(yp,x,2)-yp)
