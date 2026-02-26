from numpy import *
from scipy import stats
vel = [99,86,87,88,111,86,103,87,94,78,77,85,86]

media = mean(vel)
mediana = median(vel)
moda = stats.mode(vel)
q = quantile(vel,[0,0.25,0.5,0.75,1])
p = percentile(vel,.5)
print("media:",media)
print("mediana:",mediana)
print("moda:",moda[0])
print("cuartiles:",q)
print("percentil 50:",p)
