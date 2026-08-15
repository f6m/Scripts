from numpy import *
from pandas import  *
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# El archivo debe estar en el contenido del collab sample_data
f = read_csv('/content/datosregresionsimple.csv',encoding='latin-1')

# Definimos los datos de las variables independientes
X = f['egresadossupmx']
Y = f['anioempnummx']

print("Coeficiente de correlacion:",corrcoef(f['anioempnummx'],f['egresadossupmx']))

# Entrenamos el modelo con una particion 80% de los datos
# para entrenacion y 20% para testear  
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

XX_train = X_train.values.reshape(-1, 1)

modeloregr = linear_model.LinearRegression()
modeloregr.fit(XX_train, Y_train)

#Observamos las constantes
print("Constante interseccion en el origen:", modeloregr.intercept_)
print("Constantes pendientes:", modeloregr.coef_)

XX_test = X_test.values.reshape(-1, 1)

#prediciones
y_predict = modeloregr.predict(XX_test)
print(Y_test)
print(y_predict)

# Calculamos SSE sum square error del la particion 
# a predecir
sse = sum((Y_test - y_predict) ** 2)
print("SSE:", sse)
print("SSE1:", modeloregr.score(XX_test,Y_test))
r2=modeloregr.score(X.values.reshape(-1,1),Y)
print("SSE2:",r2)

#### para la grafica
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

### visualizacion ####
x = X
y = Y

plt.scatter(x, y, color="blue", label="Datos actuales")
plt.plot(X, modeloregr.predict(X.values.reshape(-1,1)), color="red")
plt.xlabel("Taza de egresados nivel superior (%)")
plt.ylabel("Numero de empresas de software \n mexicanas (% año)")
plt.title('Regresión lineal - Recta de mejor ajuste \n $R^2 = %.2f$' %r2, fontsize=10)
plt.legend()
plt.show()
