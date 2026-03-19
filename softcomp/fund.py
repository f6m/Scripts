from pandas import *
from numpy import *
from matplotlib.pyplot import *
import seaborn as sns

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')
anios=f['fundacion'] #solo la columna indicada
# print(anios)
df = DataFrame(anios, columns=["fundacion"])
ax=sns.histplot(data=df,x="fundacion",stat="density",kde=True,cumulative=True,binwidth=3)
# Colocamos las etiquetas
ax.set_xlabel("Años", fontsize=12)
ax.set_ylabel("Frecuencia relativa acumulada", fontsize=12)
show()
