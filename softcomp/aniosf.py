from pandas import *
from numpy import *
from matplotlib.pyplot import * 
from seaborn import *
import re 
import scipy.stats as stats

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

##Análiis estadístico de la distribución de años de fundacion
##de las empresas e instituciones mexicanas

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

print("Valor mínimo:",min(ff))
print("Valor máximo:",max(ff))
print("Media:",mean(ff))
print("Mediana:",median(ff))
print("Moda:",argmax(bincount(ff)))
print("Desviación Estándar (division por n-1):",std(ff,ddof=1))

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

# Ajustamos una densidad de Weibull_min a los datos para obtener los parametros
shape, loc, scale = stats.weibull_min.fit(ff,floc=0)

print(shape,loc,scale)
# Generamos x-axis puntos entre el minimo y un valor cerca del maximo
x = linspace(1960,2030, 1000)

# Calculamos PDF
pdf_values = stats.weibull_min.pdf(x,c=shape,scale=scale,loc=loc)

# Generamos el plot
figure(figsize=(8, 5))
plot(x, pdf_values, color='orange', linewidth=3,
label=f'Weibull PDF (shape={shape:.2f}, scale={scale:0.2f}, loc={loc})')
fill_between(x, 0, pdf_values, color='blue', alpha=0.1) # Fills area under curve
histplot(ff,stat="density",binwidth=3,label=f'Frecuencias relativas de los años de fundación')

# Colocamos etiquetas y mostramos
title('Ajuste de distribución Weibull')
xlabel('Año de fundación (instituciones mexicanas)')
ylabel('Función de densidad, Frecuencias relativas')
legend()
show()
