#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:45:05 2025

@author: victoria24
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.io.wavfile import write

#%% ECG
fs_ecg = 1000 # Hz

# Cargo la señal
ecg_one_lead = np.load('ecg_sin_ruido.npy')
#.shape devuelve tuplas
N = ecg_one_lead.shape[0] #solo el elemento 0


plt.figure(figsize=(8, 6))
plt.subplot(2,1,1)
plt.title("ECG sin ruido")
plt.grid(True)
plt.plot(ecg_one_lead)

#PARAMETROS WELCH

cant_promedios = 30 #cambia mucho la forma, cuanto mas chico mas varianza
nperseg = N // cant_promedios
nfft = 2 * nperseg
win = "hamming"

# Welch: devuelve f (vector de frecuencias) y Pxx
#si le especifico frecuencia de muestreo  me devuelve f
#nfft mejora resolucion espectral

f, Pxx = sig.welch(ecg_one_lead, fs=fs_ecg, window = win, nperseg=nperseg, nfft=nfft)

#Gráfico de la PSD - normal
plt.subplot(2,1,2)
plt.plot(f, Pxx)
plt.title("Densidad Espectral de Potencia (Welch)")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)
plt.xlim([0, 50]) #como es pasabajos, limito
plt.tight_layout()
plt.show()


#%% PPG

fs_ppg = 400 # Hz
ppg = np.load('ppg_sin_ruido.npy')

N_ppg = ppg.shape[0] 

plt.figure(figsize=(8, 6))
plt.subplot(2,1,1)
plt.title("PPG")
plt.grid(True)
plt.plot(ppg)

#PARAMETROS WELCH

cant_promedios_ppg = 20 #cambia mucho la forma, cuanto mas chico mas varianza
nperseg_ppg = N // cant_promedios_ppg
nfft_ppg = 2 * nperseg_ppg
win_ppg = "hamming"

f_ppg, Pxx_ppg = sig.welch(ppg, fs=fs_ppg, window = win_ppg, nperseg=nperseg_ppg, nfft=nfft_ppg)

#Gráfico de la PSD - PPG
plt.subplot(2,1,2)
plt.plot(f_ppg, Pxx_ppg)
plt.title("Densidad Espectral de Potencia (Welch)")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)
plt.tight_layout()
plt.xlim([0, 30]) #como es pasabajos, limito
plt.show()

#%%
# Cargar el archivo CSV como un array de NumPy

#fs_audio, wav_data = sio.wavfile.read('la cucaracha.wav')
#fs_audio, wav_data = sio.wavfile.read('prueba psd.wav')
fs_audio, wav_data = sio.wavfile.read('silbido.wav')

N_audio = wav_data.shape[0] 

plt.figure(figsize=(8, 6))
plt.subplot(2,1,1)
plt.title("Audio")
plt.grid(True)
plt.plot(wav_data)

# import sounddevice as sd
# sd.play(wav_data, fs_audio)

#PARAMETROS WELCH

cant_promedios_audio = 30 #cambia mucho la forma, cuanto mas chico mas varianza
nperseg_audio = N // cant_promedios_audio
nfft_audio = 1 * nperseg_audio
win_audio = "hamming"

f_audio, Pxx_audio = sig.welch(wav_data, fs=fs_audio, window = win_audio, nperseg=nperseg_audio, nfft=nfft_audio)

#Gráfico de la PSD - Audio
plt.subplot(2,1,2)
plt.plot(f_audio, Pxx_audio)
plt.title("Densidad Espectral de Potencia (Welch)")
plt.xlabel("Frecuencia [Hz]")
plt.grid(True)
plt.tight_layout()
plt.show()

# %% BLACKMAN TUKEY

# M = 2000 # M<N/5 - M tamaño de la ventana - dejar afuera lags autocorr

# # Autocorrelación completa (sec_corr_ecg)
# sec_corr_ecg = correlate(ecg_one_lead, ecg_one_lead, mode = 'full')

# # El índice de inicio y fin:
# start_idx = N - M - 1 # N-1 (centro) - M
# end_idx = N + M       # N-1 (centro) + M + 1 (regla de Python)

# r_x_hat_M = sec_corr_ecg[start_idx : end_idx] 

# %%

#ANCHO DE BANDA ECG
#area total cumsum, ultimo elemento
#PLantear proporcion de esa area para calcular ancho de banda

porcentaje = 0.99

pot_acum = np.cumsum(Pxx)
pot_acum_norm = pot_acum / pot_acum[-1]  # normaizo, estoy accediendo a la ultima pos del vector cumsum que es el total

# Encuentro el índice donde la potencia supera el 99%
index_bw = np.where(pot_acum_norm >= porcentaje)[0][0]

#np.where devuelve tupla de arrays, uno opr cada dimension
#Primer [0] → extrae el array de índices de la tupla que devuelve np.where.
#Segundo [0] → toma el primer elemento de ese array.

# Frecuencia correspondiente
freq_bw = f[index_bw]
print(freq_bw)

#%%
#ANCHO DE BANDA PPG
porcentaje_ppg = 0.99

pot_acum_ppg = np.cumsum(Pxx_ppg)
pot_acum_norm_ppg = pot_acum_ppg / pot_acum_ppg[-1]  # normaizo, estoy accediendo a la ultima pos del vector cumsum que es el total

# Encuentro el índice donde la potencia supera el 99%
index_bw_ppg = np.where(pot_acum_norm_ppg >= porcentaje_ppg)[0][0]

#np.where devuelve tupla de arrays, uno opr cada dimension
#Primer [0] → extrae el array de índices de la tupla que devuelve np.where.
#Segundo [0] → toma el primer elemento de ese array.

# Frecuencia correspondiente
freq_bw_ppg = f_ppg[index_bw_ppg]
print(freq_bw_ppg)


#%%

pot_acum_audio = np.cumsum(Pxx_audio)
pot_acum_norm_audio = pot_acum_audio / pot_acum_audio[-1]  # normaizo, estoy accediendo a la ultima pos del vector cumsum que es el total

# Encuentro el índice donde la potencia supera el 99%
index_inf_bw_audio = np.where(pot_acum_norm_audio >= 0.01)[0][0]
index_bw_audio = np.where(pot_acum_norm_audio >= porcentaje)[0][0]

#np.where devuelve tupla de arrays, uno opr cada dimension
#Primer [0] → extrae el array de índices de la tupla que devuelve np.where.
#Segundo [0] → toma el primer elemento de ese array.

# Frecuencia correspondiente
freq_inf_bw_audio = f_audio[index_inf_bw_audio]
freq_bw_audio = f_audio[index_bw_audio]
print("frecuencia cota inferior ancho banda audio", freq_inf_bw_audio)
print("frecuencia cota superior ancho banda audio", freq_bw_audio)
