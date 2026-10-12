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

anios = f['Nacional']
df = DataFrame(anios)
numne = df["Nacional"].value_counts()
yy=[numne[0],numne[1]]


labels = ["Empresas de Software Nacionales", "Empresas de Software Extranjeras"]
fig = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
fig.add_trace(Pie(labels=labels, values=yy, name="Cantidades de la muestra"),
              1, 1)
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(title_text="Instituciones de Software en México (muestra)",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='', x=sum(fig.get_subplot(1, 1).x) / 2, y=0.5,
                      font_size=20, showarrow=False, xanchor="center")])
fig.show()
