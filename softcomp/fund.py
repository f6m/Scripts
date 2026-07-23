from pandas import *
from numpy import *
from matplotlib.pyplot import * 
from seaborn import *
import re 
import scipy.stats as stats

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

"""
#Para el histograma del numero de instituciones nacionales y extrangeras
anios=f['Nacional'] #Para estudiar las nacionales y extranjeras
df = DataFrame(anios)
numne = df["Nacional"].value_counts()
yy=[numne[0],numne[1]]
xx=['Nacionales','Extranjeras']
ax=sns.barplot(y=yy,x=xx,palette=['skyblue','orange'])
ax.bar_label(ax.containers[1])
ax.set_ylabel("Cantidad", fontsize=12)
ax.bar_label(ax.containers[0])
show()
"""
anios = f['Nacional']
df = DataFrame(anios)
numne = df["Nacional"].value_counts()
yy=[numne[0],numne[1]]
xx=['Empresas e \n Instituciones Nacionales','Empresas \n Extranjeras']
myexplode = [0.1, 0]
colors = color_palette('pastel')
pie(yy, labels = xx, colors=colors, explode = myexplode,autopct='%.0f%%')
show()

"""
cedep=f['Cede principal'] #Para estudiar la distribucion en los estados
cp = DataFrame(cedep)
cdmx = cp["Cede principal"].str.contains("Cdmx")
nl = cp["Cede principal"].str.contains("Nuevo Leon")
jal = cp["Cede principal"].str.contains("Jalisco")
qro = cp["Cede principal"].str.contains("Queretaro")
slp = cp["Cede principal"].str.contains("San Luis Potosi")
edomex = cp["Cede principal"].str.contains("Edomex")
vera = cp["Cede principal"].str.contains("Veracruz")
hgo = cp["Cede principal"].str.contains("Hidalgo")
bc = cp["Cede principal"].str.contains("Baja California")
co = cp["Cede principal"].str.contains("Coahuila")
chi = cp["Cede principal"].str.contains("Chiapas")
chih = cp["Cede principal"].str.contains("Chihuahua")
col = cp["Cede principal"].str.contains("Colima")
sin = cp["Cede principal"].str.contains("Sinaloa")
son = cp["Cede principal"].str.contains("Sonora")
tam = cp["Cede principal"].str.contains("Tamaulipas")
pue = cp["Cede principal"].str.contains("Puebla")

cn=[cdmx.sum(),nl.sum(),jal.sum(),qro.sum(),slp.sum(),edomex.sum(),
    vera.sum(),hgo.sum(),bc.sum(),co.sum(),chi.sum(),chih.sum(),
    col.sum(),sin.sum(),son.sum(),tam.sum(),pue.sum()]
print(len(cn))
print(sum(cn))
cc=['cd','nl','ja','qr','sl','ex','vz','hg','bc','co','ch','chi',
    'cl','sn','sr','tm','pb']
ax=sns.barplot(y=cn/sum(cn),x=cc)
ax.bar_label(ax.containers[0],fmt='{:.2f}')
ax.set_ylabel("Cantidad relativa", fontsize=12)
#ax.bar_label(ax.containers[0])
show()
"""

propo=f['proposito'] #Para estudiar la distribucion de servicios / propositos de empresa
pro = DataFrame(propo)
wb = pro["proposito"].str.contains('linea,Marketing digital|marketing digital',flags=re.IGNORECASE)
dw = pro["proposito"].str.contains('desarrollo web|Web|web|línea',flags=re.IGNORECASE)
me = pro["proposito"].str.contains('medida|fábrica|Medida',flags=re.IGNORECASE)
mo = pro["proposito"].str.contains('apps|APPS|mobiles|móvil|mobil',flags=re.IGNORECASE)
di = pro["proposito"].str.contains('UX|ux|UI|ui|diseño|Diseño',flags=re.IGNORECASE)
ia = pro["proposito"].str.contains('IA|ia|Inteligencia Artificial|inteligencia artificial',flags=re.IGNORECASE)
co = pro["proposito"].str.contains('Consultoria|consultoria|Asesoria|asesoria|TI|ti|ciberseguridad|educacion',flags=re.IGNORECASE)
ec = pro["proposito"].str.contains('ecommerce|comercio electronico|comercio digital',flags=re.IGNORECASE)
go = pro["proposito"].str.contains('gobiernomx|gobierno mx',flags=re.IGNORECASE)
sa = pro["proposito"].str.contains('salud|industria de la medicina|salud',flags=re.IGNORECASE)
da = pro["proposito"].str.contains('analitica datos|datos|Datos|analisis datos',flags=re.IGNORECASE)
fa = pro["proposito"].str.contains('administracion|administracion empresa|contabilidad empresa|facturacion electronica|contabilidad electronica',flags=re.IGNORECASE)
nu = pro["proposito"].str.contains('nube',flags=re.IGNORECASE)
lpso = pro["proposito"].str.contains('lenguajes de programacion|sistemas operativos',flags=re.IGNORECASE)
sos = pro["proposito"].str.contains('software sistema|software propio|construccion|industria de la construccion',flags=re.IGNORECASE)
sia = pro["proposito"].str.contains('software codigoia',flags=re.IGNORECASE)
ed = pro["proposito"].str.contains('centro educativo publico',flags=re.IGNORECASE)
subrec = pro["proposito"].str.contains('subcontratacion|nearshore|reclutamiento|staffing|staff augmentation|aumento de personal',flags=re.IGNORECASE)

propn=[wb.sum(),dw.sum(),me.sum(),mo.sum(),di.sum(),ia.sum(),
    co.sum(),ec.sum(),go.sum(),sa.sum(),da.sum(),fa.sum(),
    nu.sum(),lpso.sum(),sos.sum(),sia.sum(),
       ed.sum(),subrec.sum()]
print(len(propn))
print(sum(propn))
propd=['MK','WB','FB','APP','DIS','IA','AC','EC','G','S','D','AD','NU',
    'LSO','SS','CIA','ED','RS']
ax=barplot(y=propn/sum(propn),x=propd)
ax.bar_label(ax.containers[0],fmt='{:.2f}')
ax.set_ylabel("Cantidad relativa", fontsize=12)
#ax.bar_label(ax.containers[0])

#Para contar el servicio de software a la medida en empresas nacionales y extranjeras
ne=DataFrame(f[['proposito','Nacional']])
filtro_n = ne[ne['Nacional'] == 'N']
filtroc_n= filtro_n['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)
filtro_e = ne[ne['Nacional'] == 'E']
filtroc_e= filtro_e['proposito'].str.contains('desarrollo web|Web|web|línea|medida|fábrica|Medida|apps|APPS|mobiles|móvil|mobil|movil|lenguajes|sistemas operativos',flags=re.IGNORECASE)

sm=[filtroc_n.sum(),filtroc_e.sum()]
laben=['N','E']
ax=barplot(y=sm/sum(sm),x=laben)
ax.bar_label(ax.containers[0],fmt='{:.2f}')
ax.set_ylabel("Software a la medida", fontsize=12)
#ax.bar_label(ax.containers[0])
show()

#print(filtroc_n,filtroc_e)

##Para la distribución de años de fundacion

filterdf = f[f["Nacional"] == 'N']
ff=filterdf['fundacion']
print(len(ff))
figure(figsize=(8, 5))
ax=histplot(ff,stat="density",kde=False,cumulative=False,binwidth=3)
# Colocamos las etiquetas
#set_xlabel("Año de fundación (Nacionales)", fontsize=12)
#set_ylabel("Frecuencia relativa", fontsize=12)
xlabel("Año de fundación (Nacionales)", fontsize=12)
ylabel("Frecuencia relativa", fontsize=12)
show()

#Criterio para ajstar distribucion: gráfica P-P plot

# 1. Generamos los datos distribuidos Gamma distributed data (Shape a=3, Scale=2)
#np.random.seed(42)
#data = stats.gamma.rvs(a=3.0, scale=2.0, size=250)
#data = stats.lognorm.rvs(s=0.5,loc=0.7)

# 2. Ajustamos los datos para encontrar el parametro estimador de forma
# probplot requiere este parametro para calcular los cuantiles teoricos
#shape_est, loc_est, scale_est = stats.lognorm.fit(data)

# 3. Creamos el plot de probabilidad
#stats.probplot(data, dist=stats.gamma, sparams=(shape_est,), plot=ax)
#stats.probplot(ff,plot=plt,dist="lognorm",sparams=(shape_est,))
fig, ax = subplots(figsize=(8,5))
#stats.probplot(ff,dist="norm",plot=ax)
stats.probplot(ff, dist=stats.weibull_min, sparams=(266,), plot=ax)
ax.set_xlabel('Percentiles teóricos (Weibull Min)')
ax.set_ylabel('Años de fundación ordenados')
ax.set_title('Gráfica de Probabilidad')

#Ajustamos una densidad de Weibull_min a los datos para obtener los parametros
shape, loc, scale = stats.weibull_min.fit(ff,floc=0)

print(shape,loc,scale)
# 2. Generate x-axis data points
x = linspace(1960,2030, 1000)

# 3. Calculate the Probability Density Function (PDF)
pdf_values = stats.weibull_min.pdf(x,c=shape,scale=scale,loc=loc)

# 4. Generate the plot
figure(figsize=(8, 5))
plot(x, pdf_values, color='orange', linewidth=3,
label=f'Weibull PDF (shape={shape:.2f}, scale={scale:0.2f}, loc={loc})')
fill_between(x, 0, pdf_values, color='blue', alpha=0.1) # Fills area under curve
histplot(ff,stat="density",binwidth=3,label=f'Frecuencias relativas de los años de fundación')

# 5. Format labels and display
title('Ajuste de distribución Weibull')
xlabel('Año de fundación (instituciones mexicanas)')
ylabel('Función de densidad, Frecuencias relativas')
legend()
#grid(False, linestyle='--', alpha=0.7)
show()
