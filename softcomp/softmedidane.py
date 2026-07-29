from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

#Para contar el servicio de software a la medida en empresas nacionales y extranjeras
ne=DataFrame(f[['proposito','Nacional']])
filtro_n = ne[ne['Nacional'] == 'N']
filtroc_n= filtro_n['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)
filtro_e = ne[ne['Nacional'] == 'E']
filtroc_e= filtro_e['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)

sn=[filtroc_n.sum()/len(filtro_n),1]
se=[filtroc_e.sum()/len(filtro_e),1]

laben=['Empresas e Instituciones \n Nacionales con servicios \n de software a la medida',
       'Empresas e Instituciones \n Nacionales sin servicios \n de software a la medida']
myexplode = [0.1, 0]
colors = color_palette('pastel')
pie(sn, labels = laben, colors=colors, explode = myexplode,autopct='%.0f%%')
show()
labeln=['Empresas Extranjeras \n con servicios de \n software a la medida',
        'Empresas Extranjeras \n sin servicios de \n software a la medida']
pie(se, labels = labeln, colors=colors, explode = myexplode,autopct='%.0f%%')

show()

