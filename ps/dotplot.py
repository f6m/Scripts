import matplotlib.pyplot as plt
#from numpy import *
#data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27]
#histo=histogram(data,bins='auto')
data  = [5,8,3,7,1,5,3,2,3,3,8,5]

pos = [] 
keys = {} 

#frequencies
for num in data:
   if num not in keys:
     keys[num] = 1
     pos.append(1)
   else:
     keys[num] += 1
     pos.append(keys[num])

print(pos)
#print(histo[0])
#print(histo[1])
#[1, 1, 1, 1, 1, 2, 2, 1, 3, 4, 2, 3]
#reducir = set(histo[1][:5])
#print(reducir)
plt.scatter(data,pos)
plt.show()
