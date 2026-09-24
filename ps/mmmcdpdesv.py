from numpy import *
from scipy import stats
import matplotlib.pyplot as plt
import random
def prV(s): print("\033[92m {}\033[00m".format(s))

r = random.sample(range(100),70)
print(r)
histo, bins = histogram(r,bins=10)
print(histo,bins)
plt.hist(r,bins=10)
plt.show()
indexh = argmax(histo)
print(indexh)
moda = (bins[indexh]+bins[indexh+1])/2

media = mean(r)
mediana = median(r)
#moda = stats.mode(r)
mediarecortada = stats.trim_mean(r,0.1)
q = quantile(r,[0,0.25,0.5,0.75,1])
p = percentile(r,.04)
prV("Medidas de tendencia central (de la muestra)")
print("media:",media)
print("mediana:",mediana)
print("moda:",moda)
print("media recortada:",mediarecortada)
print("cuartiles:",q)
print("percentil p4:",p)
prV("Medidas de variabilidad (de la muestra)")
print("Rango:",max(r)-min(r))
print("Varianza:",var(r))
print("Desviación estándar:",std(r))
