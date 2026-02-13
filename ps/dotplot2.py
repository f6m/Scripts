import matplotlib.pyplot as plt
#from numpy import *
from collections import Counter
#data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]
data = [5,8,3,7,1,5,3,2,3,3,8,5] #array de datos

sdup=list(set(data))
histo=list(Counter(data))

print(sdup)
print(histo)

plt.stem(sdup,histo)
#plt.scatter(sdup,histo)
plt.show()
