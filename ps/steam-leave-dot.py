#pip install stemgraphic matplotlib pandas
#pip install "dask[dataframe]<2025.1.0"

import matplotlib.pyplot as plt
import numpy as np
from stemgraphic import stem_graphic


x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

# datos = [16, 25, 47, 56, 23, 45, 19, 25, 32, 44, 45, 55, 37, 62]

# Generar y mostrar el diagrama de tallo y hojas
fig, ax = stem_graphic(y,scale=1)

# Mostrar el gráfico tallo-hoja
plt.show()

# Mostrar el gráfico tallo-punto
plt.stem(x, y)
plt.show()
