from pandas import *
from numpy import *
from matplotlib.pyplot import *
#El archivo debe estar en el contenido del collab sample_data
df = read_csv('/content/B2018-2025dia.csv')
close=df['Close'] #solo la columna Close del archivo csv
print(close.head(5))
histo=histogram(close,bins=10) #Datos a graficar 
print(histo)
hist(close, bins='auto')  # arguments are passed to np.histogram
title("Histograma con 'auto' bins") #bins = 20 para 20 bins
show()
#Como lo construye?
#stem(close) #Coloca puntos por los valores de close
stem(histo[0])
