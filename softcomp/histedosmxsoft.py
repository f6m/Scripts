from pandas import *
from numpy import *
from matplotlib.pyplot import *
from seaborn import *
import re
import scipy.stats as stats
from plotly import *

#El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/empresassoftwareACT1.csv',encoding='latin-1')

cedep=f['Cede principal'] #Para estudiar la distribucion en los estados
cp = DataFrame(cedep)
ags = cp["Cede principal"].str.contains("Aguascalientes")
bc = cp["Cede principal"].str.contains("Baja California")
bcs = cp["Cede principal"].str.contains("Baja California")
cch = cp["Cede principal"].str.contains("Campeche")
chi = cp["Cede principal"].str.contains("Chiapas")
chih = cp["Cede principal"].str.contains("Chihuahua")
cdmx = cp["Cede principal"].str.contains("Cdmx|Ciudad de México|Ciudad de Mexico")
co = cp["Cede principal"].str.contains("Coahuila")
col = cp["Cede principal"].str.contains("Colima")
du = cp['Cede principal'].str.contains("Durango")
gto = cp['Cede principal'].str.contains("Guanajuato")
grr = cp['Cede principal'].str.contains("Guerrero")
hgo = cp["Cede principal"].str.contains("Hidalgo")
jal = cp["Cede principal"].str.contains("Jalisco")
edomex = cp["Cede principal"].str.contains("Edomex|Estado de Mexico")
mich = cp["Cede principal"].str.contains("Michoacan")
mo = cp["Cede principal"].str.contains("Morelos")
na = cp["Cede principal"].str.contains("Nayarit")
nl = cp["Cede principal"].str.contains("Nuevo Leon")
ox = cp["Cede principal"].str.contains("Oaxaca")
pue = cp["Cede principal"].str.contains("Puebla")
qro = cp["Cede principal"].str.contains("Queretaro")
qr = cp["Cede principal"].str.contains("Quintana Roo")
slp = cp["Cede principal"].str.contains("San Luis Potosi")
sin = cp["Cede principal"].str.contains("Sinaloa")
son = cp["Cede principal"].str.contains("Sonora")
tb = cp["Cede principal"].str.contains("Tabasco")
tam = cp["Cede principal"].str.contains("Tamaulipas")
tx = cp["Cede principal"].str.contains("Tlaxcala")
vera = cp["Cede principal"].str.contains("Veracruz")
yu = cp["Cede principal"].str.contains("Yucatan")
zac = cp["Cede principal"].str.contains("Zacatecas")

cn=[ags.sum(),bc.sum(),bcs.sum(),cch.sum(),chi.sum(),chih.sum(),cdmx.sum(),co.sum(),col.sum(),
    du.sum(),gto.sum(),grr.sum(),hgo.sum(),jal.sum(),edomex.sum(),mich.sum(),mo.sum(),
    na.sum(),nl.sum(),ox.sum(),pue.sum(),qro.sum(),qr.sum(),slp.sum(),sin.sum(),
    son.sum(),tb.sum(),tam.sum(),tx.sum(),vera.sum(),yu.sum(),zac.sum()]
print(len(cn))
print(sum(cn))
cc=['ags','bc','bcs','cch','chi','chh','cd','co','col',
    'du','gto','grr','hgo','jal','edx','mi','mo',
    'na','nl','ox','pue','qro','qr','sl','sn',
    'so','tb','tm','tx','ve','yu','za']
    
figure(figsize=(10, 6))
ax=barplot(x=cn/sum(cn),y=cc)
ax.bar_label(ax.containers[0],fmt='{:.2f}')
ax.set_xlabel("Cantidad relativa", fontsize=12)
ax.set_ylabel("Estados de México", fontsize=12)
#ax.axis("off")

#ax.bar_label(ax.containers[0])
show()
