# -*- coding: utf-8 -*-



import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1000
fs=1000

# Función para generar señal senoidal
def mi_funcion_sen(amp=1, offset=0, frec=1, fase=0, N=100, fs=1000):
    ts = 1 / fs
    tt = np.arange(start=0, stop=N * ts, step=ts)
    xx = amp * np.sin(2 * np.pi * frec * tt + fase) + offset
    return tt, xx


tt, xx = mi_funcion_sen(1, 0, 1, 0, N, fs)

# Calcular DFT 
X = np.zeros(N, dtype=np.complex128) #inicializo el array X en ceros complejos

for k in range(N):
    for n in range(N):
        X[k] += xx[n] * np.exp(-1j * 2 * np.pi * k * n / N)

# Magnitud y fase de la DFT
X_mag = np.abs(X)
X_ph=np.angle(X)

# Graficar señal original
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(tt, xx, 'o--')
plt.title("Señal Senoidal")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")


# Graficar DFT

frecuencia = np.arange(N) * 2*np.pi/N

plt.subplot(1, 2, 2)
plt.plot(frecuencia, X_mag) #el grafico de dft debe estan en funcion de las frecencias
plt.title("Magnitud de la DFT")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X[k]|")
plt.xlim(-fs/2, fs / 2)

plt.tight_layout()
plt.show()

