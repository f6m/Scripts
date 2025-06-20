import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Paramettros del filtro
cutoff_freq = 100  # Frecuencia umbral in Hz
fs = 1000  # Taza para la muestera en Hz
order = 4  # Orden del filtro

# Diseño del filtro pase bajo 
nyq = 0.5 * fs
normal_cutoff = cutoff_freq / nyq
b, a = butter(order, normal_cutoff, btype='lowpass')

# Datos muestra
t = np.linspace(0, 1, 100)  # 1000 puntos equiespaciados en [0,1]
data = np.sin(2*np.pi*150*t) + np.random.rand(100)  # Señal con ruido aleatorio

# Aplicamos el filtro
filtered_data = filtfilt(b, a, data)

# Plot la señal con ruido y la señal filtrada
plt.figure(figsize=(10, 6))

plt.plot(t, data, label='Señal original x(t)')
plt.plot(t, filtered_data, label='Señal filtrada')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Ejemplo de un filtrado con un pase bajo')
plt.legend()
plt.grid(True)

plt.show()
