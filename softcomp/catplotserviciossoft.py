from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

propo=f['proposito'] #Para estudiar la distribucion de servicios / propositos de empresa
pro = DataFrame(propo)
wb = pro["proposito"].str.contains('Marketing digital|marketing digital',flags=re.IGNORECASE)
dw = pro["proposito"].str.contains('desarrollo web|Web|web|UX|ux|UI|ui|diseño|Diseño',flags=re.IGNORECASE)
me = pro["proposito"].str.contains('medida|fábrica|Medida',flags=re.IGNORECASE)
mo = pro["proposito"].str.contains('apps|APPS|mobiles|móvil|mobil',flags=re.IGNORECASE)
ia = pro["proposito"].str.contains('IA|ia|Inteligencia Artificial|inteligencia artificial',flags=re.IGNORECASE)
co = pro["proposito"].str.contains('Consultoria|consultoria|Asesoria|asesoria|TI|ti|ciberseguridad|educacion',flags=re.IGNORECASE)
ec = pro["proposito"].str.contains('ecommerce|comercio electronico|comercio digital',flags=re.IGNORECASE)
go = pro["proposito"].str.contains('gobiernomx|gobierno mx',flags=re.IGNORECASE)
#sa = pro["proposito"].str.contains('salud|industria de la medicina|salud',flags=re.IGNORECASE)
da = pro["proposito"].str.contains('analitica datos|datos|Datos|analisis datos',flags=re.IGNORECASE)
#fa = pro["proposito"].str.contains('administracion|administracion empresa|contabilidad empresa|facturacion electronica|contabilidad electronica',flags=re.IGNORECASE)
nu = pro["proposito"].str.contains('nube',flags=re.IGNORECASE)
lpso = pro["proposito"].str.contains('lenguajes de programacion|sistemas operativos',flags=re.IGNORECASE)
sos = pro["proposito"].str.contains('software sistema|software propio',flags=re.IGNORECASE)
#cons = pro['proposito'].str.contains('construccion|industria de la construccion',flags=re.IGNORECASE)
sia = pro["proposito"].str.contains('software codigoia',flags=re.IGNORECASE)
#ed = pro["proposito"].str.contains('centro educativo publico',flags=re.IGNORECASE)
subrec = pro["proposito"].str.contains('subcontratacion|nearshore|reclutamiento|staffing|staff augmentation|aumento de personal',flags=re.IGNORECASE)

propn=[wb.sum(),dw.sum(),me.sum(),mo.sum(),ia.sum(),
    co.sum(),ec.sum(),go.sum(),da.sum(),nu.sum(),
    lpso.sum(),sos.sum(),sia.sum(),subrec.sum()]
print(len(propn))
print(sum(propn))
propd=['Marketing digital','Desarrollo web','Software a la medida','Desarrollo móvil','Inteligencia Artificial',
       'Consultoría','Comercio eletrónico','Servicio al Gobierno de México','Anális de datos','Servicios en la nube',
       'Lenguajes Sistemas Operativos','Software como productdo propio','Software con código IA','Reclutamiento subcontratación']
#ax=barplot(y=propn/sum(propn),x=propd)
dataf = DataFrame({'Servicios de Software': propd, 'Cantidad relativa': propn/sum(propn)})
#ax=catplot(data=dataf,y="Cantidad relativa", hue="class", kind="count",palette="pastel", edgecolor=".6",
#)
ax=catplot(x="Cantidad relativa",hue="Servicios de Software",data=dataf,kind="bar")
# 2. Iterate through axes and add bar labels
for axe in ax.axes.flat:
  for container in axe.containers:
    axe.bar_label(container, fmt="%.2f")

from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

propo=f['proposito'] #Para estudiar la distribucion de servicios / propositos de empresa
pro = DataFrame(propo)
wb = pro["proposito"].str.contains('Marketing digital|marketing digital',flags=re.IGNORECASE)
dw = pro["proposito"].str.contains('desarrollo web|Web|web|UX|ux|UI|ui|diseño|Diseño',flags=re.IGNORECASE)
me = pro["proposito"].str.contains('medida|fábrica|Medida',flags=re.IGNORECASE)
mo = pro["proposito"].str.contains('apps|APPS|mobiles|móvil|mobil',flags=re.IGNORECASE)
ia = pro["proposito"].str.contains('IA|ia|Inteligencia Artificial|inteligencia artificial',flags=re.IGNORECASE)
co = pro["proposito"].str.contains('Consultoria|consultoria|Asesoria|asesoria|TI|ti|ciberseguridad|educacion',flags=re.IGNORECASE)
ec = pro["proposito"].str.contains('ecommerce|comercio electronico|comercio digital',flags=re.IGNORECASE)
go = pro["proposito"].str.contains('gobiernomx|gobierno mx',flags=re.IGNORECASE)
#sa = pro["proposito"].str.contains('salud|industria de la medicina|salud',flags=re.IGNORECASE)
da = pro["proposito"].str.contains('analitica datos|datos|Datos|analisis datos',flags=re.IGNORECASE)
#fa = pro["proposito"].str.contains('administracion|administracion empresa|contabilidad empresa|facturacion electronica|contabilidad electronica',flags=re.IGNORECASE)
nu = pro["proposito"].str.contains('nube',flags=re.IGNORECASE)
lpso = pro["proposito"].str.contains('lenguajes de programacion|sistemas operativos',flags=re.IGNORECASE)
sos = pro["proposito"].str.contains('software sistema|software propio',flags=re.IGNORECASE)
#cons = pro['proposito'].str.contains('construccion|industria de la construccion',flags=re.IGNORECASE)
sia = pro["proposito"].str.contains('software codigoia',flags=re.IGNORECASE)
#ed = pro["proposito"].str.contains('centro educativo publico',flags=re.IGNORECASE)
subrec = pro["proposito"].str.contains('subcontratacion|nearshore|reclutamiento|staffing|staff augmentation|aumento de personal',flags=re.IGNORECASE)

propn=[wb.sum(),dw.sum(),me.sum(),mo.sum(),ia.sum(),
    co.sum(),ec.sum(),go.sum(),da.sum(),nu.sum(),
    lpso.sum(),sos.sum(),sia.sum(),subrec.sum()]
print(len(propn))
print(sum(propn))
propd=['Marketing digital','Desarrollo web','Software a la medida','Desarrollo móvil','Inteligencia Artificial',
       'Consultoría','Comercio eletrónico','Servicio al Gobierno de México','Anális de datos','Servicios en la nube',
       'Lenguajes Sistemas Operativos','Software como productdo propio','Software con código IA','Reclutamiento subcontratación']
#ax=barplot(y=propn/sum(propn),x=propd)
dataf = DataFrame({'Servicios de Software': propd, 'Cantidad relativa': propn/sum(propn)})
#ax=catplot(data=dataf,y="Cantidad relativa", hue="class", kind="count",palette="pastel", edgecolor=".6",
#)
ax=catplot(x="Cantidad relativa",hue="Servicios de Software",data=dataf,kind="bar")
# 2. Iterate through axes and add bar labels
for axe in ax.axes.flat:
  for container in axe.containers:
    axe.bar_label(container, fmt="%.2f")

#ax.bar_label(ax.containers[0],fmt='{:.2f}')
#ax.set_ylabel("Cantidad relativa", fontsize=12)

## Como tenemos las frecuencias podemos calcular la moda, mediana y media.
total = sum(propn)

# Frequencias acumuladas
cum_freq = cumsum(propn)

# Encontramos el indice para la mediana
# where regresa los indices,  donde cn es maximo para la moda y donde
#  cum_freq > total / 2 para la mediana
moda_ind  = propn.index(max(propn))
mediana_ind = where(cum_freq >= total / 2)[0][0]

# Obtebenis la mediana y la moda
print('Moda categorica:',propd[moda_ind])
print('Mediana categorica:',propd[mediana_ind])
