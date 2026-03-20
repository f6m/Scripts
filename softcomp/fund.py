from pandas import *
from numpy import *
from matplotlib.pyplot import *
import seaborn as sns

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')
anios=f['Nacional'] #solo la columna indicada
df = DataFrame(anios)
numne = df["Nacional"].value_counts()
yy=[numne[0],numne[1]]
xx=['Nacionales','Extrangeras']
ax=sns.barplot(y=yy,x=xx,palette=['skyblue','orange'])
ax.bar_label(ax.containers[1])
ax.set_ylabel("Cantidad", fontsize=12)
ax.bar_label(ax.containers[0])

show()

filterdf = df[df["Nacional"] == 'N']
print(filterdf)
ax=sns.histplot(filterdf,stat="density",kde=True,cumulative=False,binwidth=3)
# Colocamos las etiquetas
#ax.set_xlabel("Nacional o Extrangera", fontsize=12)
#ax.set_ylabel("Frecuencia relativa acumulada", fontsize=12)
#show()
