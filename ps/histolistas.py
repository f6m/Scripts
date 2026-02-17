import matplotlib.pyplot as plt
import numpy as np
#datos
vals = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# frecuencias
frec = [1,2,3,12,11,15,18,10,12,4,5,3,1,2,1]
# lista de frecuencias relativas
frecrel = [x / 100 for x in frec]
# bar plot
plt.bar(vals, frecrel, width=1, align='center', edgecolor='blue')
plt.xlabel('Intervalos de clase')
plt.ylabel('Frecuencias')
