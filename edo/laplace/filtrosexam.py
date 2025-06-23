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

#Diseño del filtro de pase alto
bb, aa = butter(order, normal_cutoff, btype='highpass')

#Diseño del frltro de pase banda
bbb, aaa = butter(order,[0.1, 0.5],'bandpass')


# Datos muestra
t = np.linspace(0, 1, 100)  # 1000 puntos equiespaciados en [0,1]
data = np.sin(2*np.pi*150*t) + np.random.rand(100)  # Señal con ruido aleatorio

# Aplicamos los filtros
filtered_data = filtfilt(b, a, data)
filtered_data1 = filtfilt(bb, aa, data)
filtered_data2 = filtfilt(bbb, aaa, data)

# Plot la señal con ruido y la señal filtrada
plt.figure(figsize=(10, 6))

plt.plot(t, data, label='Señal original x(t)')
plt.plot(t, filtered_data, label='Señal filtrada filtro pase bajo')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Ejemplo de un filtrado con un pase bajo')
plt.legend()
plt.grid(True)

plt.show()

# Plot la señal con ruido y la señal filtrada filtro alto
plt.figure(figsize=(10, 6))

plt.plot(t, data, label='Señal original x(t)')
plt.plot(t, filtered_data1, label='Señal filtrada filtro pase alto')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Ejemplo de un filtrado con un pase alto')
plt.legend()
plt.grid(True)

plt.show()


# Plot la señal con ruido y la señal filtrada filtro pase banda
plt.figure(figsize=(10, 6))

plt.plot(t, data, label='Señal original x(t)')
plt.plot(t, filtered_data2, label='Señal filtrada filtro pase banda')

plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Ejemplo de un filtrado con un pase banda')
plt.legend()
plt.grid(True)
