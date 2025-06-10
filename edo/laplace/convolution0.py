from __future__ import division
from sympy import *
import math
import numpy
def x1(t,x): return math.sin(x*x) + math.cos(t*t)

h=1/5
t=0
T=[t]
x=1
X=[x]

print(t,x)
xth=x+h*x1(t,x)

while(t <= 3):
    x=xth
    X.append(xth)
    t=t+h
    T.append(t)
    print(t,x)
    xth=x+h*x1(t,x)

import matplotlib.pyplot as plt
C=numpy.convolve(T,X)
I=list(range(len(C)))
print(C)
print(len(C),len(I))

plt.subplot(1, 2, 1)
plt.plot(I, C, linestyle='none',marker='o',mfc='none')
plt.xlabel('t')
plt.ylabel('X(t)*g(t)')

plt.subplot(1, 2, 2)
plt.plot(T, X,linestyle='none',marker='o',mfc='none')
plt.xlabel('t')
plt.ylabel('x(t)')

plt.show()
