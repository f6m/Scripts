from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

#Para estudiar la distribucion de industrias
propo=f['proposito'] 
pro = DataFrame(propo)
go = pro["proposito"].str.contains('gobiernomx|gobierno mx',flags=re.IGNORECASE)
sa = pro["proposito"].str.contains('salud|industria de la medicina|salud',flags=re.IGNORECASE)
fa = pro["proposito"].str.contains('administracion|administracion empresa|contabilidad empresa|facturacion electronica|contabilidad electronica',flags=re.IGNORECASE)
cons = pro['proposito'].str.contains('construccion|industria de la construccion',flags=re.IGNORECASE)
ed = pro["proposito"].str.contains('centro educativo publico',flags=re.IGNORECASE)

propn=[go.sum(),sa.sum(),fa.sum(),cons.sum(),ed.sum()]
print(len(propn))
print(sum(propn))
propd=['Servicio al Gobierno de México','Industria de la salud','Administracion de la empresa',
       'Industrias de la construccion','Centro educativo']
#ax=barplot(y=propn/sum(propn),x=propd)
dataf = DataFrame({'Industrias de Software': propd, 'Cantidad relativa': propn/sum(propn)})
#ax=catplot(data=dataf,y="Cantidad relativa", hue="class", kind="count",palette="pastel", edgecolor=".6",
#)
ax=catplot(x="Cantidad relativa",hue="Industrias de Software",data=dataf,kind="bar")
# 2. Iterate through axes and add bar labels
for axe in ax.axes.flat:
  for container in axe.containers:
    axe.bar_label(container, fmt="%.2f")
