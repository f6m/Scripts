from numpy import *
from scipy import stats
def prV(s): print("\033[92m {}\033[00m".format(s))
vel = [1,2,3,1,1,3,4,5,2,2,4,7,5,6]

media = mean(vel)
mediana = median(vel)
moda = stats.mode(vel)
mediarecortada = stats.trim_mean(vel,0.1)
q = quantile(vel,[0,0.25,0.5,0.75,1])
p = percentile(vel,.5)
prV("Medidas de tendencia central (de la muestra)")
print("media:",media)
print("mediana:",mediana)
print("moda:",moda[0])
print("media recortada:",mediarecortada)
print("cuartiles:",q)
print("percentil 50:",p)
prV("Medidas de variabilidad (de la muestra)")
print("Rango:",max(vel)-min(vel))
print("Varianza:",var(vel))
print("Varianza:",std(vel))
