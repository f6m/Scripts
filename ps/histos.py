from pandas import *
from numpy import *
from matplotlib.pyplot import *
#El archivo debe estar en el contenido del collab sample_data
df = read_csv('/content/B2018-2025dia.csv')
close=df['Close'] #solo la columna Close del archivo csv
print(close.head(5))
histo=histogram(close)
print(histo)
hist(close, bins='auto')  # arguments are passed to np.histogram
title("Histograma con 'auto' bins")
show()
#Como lo construye?
stem(close)
