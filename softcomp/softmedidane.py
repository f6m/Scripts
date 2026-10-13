from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *
from plotly.graph_objects import Pie
from plotly.subplots import make_subplots
from plotly.io import write_image


#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

#Para contar el servicio de software a la medida en empresas nacionales y extranjeras
ne=DataFrame(f[['proposito','Nacional']])
filtro_n = ne[ne['Nacional'] == 'N']
filtroc_n= filtro_n['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)
filtro_e = ne[ne['Nacional'] == 'E']
filtroc_e= filtro_e['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)

sn=filtroc_n.sum()
snc=len(filtro_n)-sn

se=filtroc_e.sum()
sec=len(filtro_e)-se

#labels=['Empresas e Instituciones \n Nacionales con servicios \n de software a la medida',
 #      'Empresas e Instituciones \n Nacionales sin servicios \n de software a la medida']

labels = ["Con servicio de software a la medida", 
          "Sin servicio de software a la medida"]
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(Pie(labels=labels, values=[sn,snc], name="Muestra1"),
              1, 1)
fig.add_trace(Pie(labels=labels, values=[se,sec], name="Muestra2"),
              1, 2)
fig.update_traces(hole=.5, hoverinfo="label+percent+name")

fig.update_layout(title_text="Instituciones con servicios de software a la medida (en la muestra)",
    # Add annotations in the center of the donut pies.
annotations=[dict(text='Nacionales', x=sum(fig.get_subplot(1, 1).x) / 2, y=0.5,
                      font_size=12, showarrow=False, xanchor="center"),
             dict(text='Extranjeras', x=sum(fig.get_subplot(1, 2).x) / 2, y=0.5,
                      font_size=12, showarrow=False, xanchor="center")])
fig.show()
