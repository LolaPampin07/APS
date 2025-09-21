# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 18:48:46 2025

@author: lolyy
"""
# %%LIBRERIAS


import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
from scipy.signal import windows

# Modelo de señal, modelo asitivo
# x(k) = a0 * sen(omega1 * n) + na(n) = S de la cajita de modelo aditivo
# a0 = raiz de 2
# Cuando a una senoidal la contamino con una señal aleatoria que tiene una distribucion normal y pontencia sigma n al cuadrado
# --> x no es mas una se;al pura, es una señal a ruido
# señal a ruido es la relacion entre ...
# Para obtener sigma cuadrado lo despejo de de la formula de SNRdB = -10*log(sigma^2), el valor de SNRdB es un valor que nos dan

# %% VARIABLES
N = 1000
fs = N
df = fs/N # Resolucion temporal
a0 = np.sqrt(2)
realizaciones = 200 # Sirve para parametrizar la cantidad de realizaciones de sampling, de muestras que vamos a tomar de la frecuencia
omega_0 = np.pi / 2 # fs/4
fr = np.random.uniform(-2,2,realizaciones)
omega_1 = omega_0 + fr * 2 * np.pi / N
SNR = 10 # En dB
amplitud_0 = np.sqrt(2) # En Volts
nn = np.arange(N) # Vector dimensional de muestras
ff = np.arange(N) # Vector en frecuencia al escalar las muestras por la resolucion espectral

# %% FUNCION SENOIDAL
def mi_funcion_sen(frecuencia, nn, amplitud = 1, offset = 0, fase = 0, fs = 2): # Si lo igualo a algo es opcional, entonces si no le paso nada el programa me lo hace cero
     # Los obligatorios van al principio del parentesis y los opcionales al final    

    N = np.arange(nn)
    
    t = N / fs

    x = amplitud * np.sin(2 * np.pi * frecuencia * t + fase) + offset

    return t, x


k0 = (N / 4)
t1,s1 = mi_funcion_sen(frecuencia = k0 * df, nn = N, fs = fs, amplitud = amplitud_0) # Funcion senoidal de mitad de banda digital

# %% Calculo las potencias para ver que machean

pot_ruido = amplitud_0*2 / (2*10*(SNR/10))
print(f"Potencia del SNR -> {pot_ruido:.3f}")
ruido = np.random.normal(0, np.sqrt(pot_ruido), N) # Vector
var_ruido = np.var(ruido)
print(f"Potencia de ruido -> {var_ruido:.3f}")

x1 = s1 + ruido  # Modelo de señal --> señal limpia + ruido

# %% CALCULO LAS DFT
S1 = (1/N)*fft(s1)
# modulo_S1 = np.abs(S1)**2

RUIDO = (1/N)*fft(ruido)
# modulo_R = np.abs(R)**2

# Calculo la FFT
X1 = (1/N)*fft(x1) # Multiplico por 1/N para calibrarlo --> llevar el piso de ruido a cero
# modulo_X1 = np.abs(X1)**2

# %% GRAFICO
plt.figure()  # Tamaño de la figura (ancho, alto)
# plt.clf --> me borra los graficos cuando tengo muchos y los voy cerrando

# Grafico X1 en db
# plt.subplot(1,3,1)

plt.title("Densidades espectrales de potencia (PDS) en db")

# plt.title("Modulo de la DFFT con frecuencia = (N/4)")

plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.xlim([0, fs/2]) # En este caso fs = N, pero pongo fs para saber que va eso y no va siempre N
# plt.plot(ff, np.log10(np.abs(S1)**2) * 10, label = 'S1') # En este caso es un db de tension
# plt.plot(ff, np.log10(np.abs(R)**2) * 10, label = 'Ruido')
plt.plot(ff, np.log10(2*np.abs(X1)**2) * 10, label = 'X1')  # Densidad espectral de potencia
plt.legend()

plt.show()

# En ruido es poco entonces se "tapa", no me juega en la suma
# Estar 250dB por debajo, es estar 25 ordenes de potencia por debajo
# Todo el piso de ruido es tapado por la energia, al ser esta tan tan grande (casi infinitamente mas grande), lo tapa al ruido.

# %% Vamos a hacer una funcion seno para poder pasarle matrices

t = np.arange(N).reshape(-1,1) / fs # reshape para que las columnas sean tiempo
t_mat = np.tile(t, (1, realizaciones)) # (1000, 200)


# Repetir fr en filas (mismo valor de frecuencias por columna)
frecuencias = (k0 + fr) * df # en Hz
f_mat = np.tile(frecuencias, (N, 1))  # (1000, 200)


# Matriz de senoidales
s_mat = amplitud_0 * np.sin(2 * np.pi * f_mat * t_mat) # (1000, 200)

# RUIDO
pot_ruido = amplitud_0*2 / (2 * 10*(SNR / 10))
ruido_mat = np.random.normal(0, np.sqrt(pot_ruido), size = (N, realizaciones))  # (1000, 1)

x_ruido = s_mat + ruido_mat #matriz de sinusoidales + ruidos

# %%senales ventaneadas


x_vent_fla= x_ruido * (windows.flattop(N).reshape(-1,1))
x_vent_BM= x_ruido * (windows.blackman(N).reshape(-1,1))
x_vent_R= x_ruido * (windows.boxcar(N).reshape(-1,1))
x_vent_H= x_ruido * (windows.hamming(N).reshape(-1,1))

# Calculo la FFT normalizada a lo largo del eje del tiempo (filas)
X_mat_ft = (1/N) * fft(x_vent_fla, axis=0)
X_mat_BM = (1/N) * fft(x_vent_BM, axis=0)
X_mat_R = (1/N) * fft(x_vent_R, axis=0)
X_mat_H = (1/N) * fft(x_vent_H, axis=0)


#graficos de transformada de senales ventanadas con ruido
plt.figure()
plt.subplot(4,1,1)
plt.title('FLATOP')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_ft)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(4,1,2)
plt.title('BLACKMAN')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_BM)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(4,1,3)
plt.title('RECTANGULAR')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_R)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.subplot(4,1,4)
plt.title('HAMMING')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PDS [db]')
plt.plot(ff, np.log10(2*np.abs(X_mat_H)**2) * 10)  # Densidad espectral de potencia
plt.xlim([0, fs/2])

plt.show()

# %% Estimador de energia

trans=0.35
b=10

estimador_a_FT_10= 10*np.log10(2*(np.abs(X_mat_ft[N//4,:])**2))
estimador_a_BM_10= 10*np.log10(2*(np.abs(X_mat_BM[N//4,:])**2))
estimador_a_R_10= 10*np.log10(2*(np.abs(X_mat_R[N//4,:])**2))
estimador_a_H_10= 10*np.log10(2*(np.abs(X_mat_H[N//4,:])**2))


plt.figure()
plt.hist(estimador_a_FT_10,label='Flatop',alpha=trans,bins=b)
plt.hist(estimador_a_BM_10,label='Blackman',alpha=trans,bins=b)
plt.hist(estimador_a_R_10,label='Rectangular',alpha=trans,bins=b)
plt.hist(estimador_a_H_10,label='Hamming',alpha=trans,bins=b)
plt.legend()
plt.show()



# %%Estimador de frecuencia

estimador_omega_10=max(np.angle(X_mat_ft[N//4,:]))







