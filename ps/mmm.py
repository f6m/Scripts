from numpy import *
from scipy import stats
vel = [99,86,87,88,111,86,103,87,94,78,77,85,86]

media = mean(vel)
mediana = median(vel)
moda = stats.mode(vel)
print("media:",media)
print("mediana:",mediana)
print("moda:",moda[0])
