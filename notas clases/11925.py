# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 20:11:26 2025

@author: lolyy
"""
# %% LIBRERIAS


import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
import scipy.signal as sp

# %% FUNCIONES DE GENERACION

def gen_señal (fs, N, amp, frec, fase, v_medio, SNR):
    
    t_final = N * 1/fs
    tt = np.arange (0, t_final, 1/fs)
    
    frec_rand = np.random.uniform (-2, 2)
    frec_omega = frec/4 + frec_rand * (frec/N)
    
    ruido = np.zeros (N)
    for k in np.arange (0, N, 1):
        pot_snr = amp**2 / (2*10**(SNR/10))                                 
        ruido[k] = np.random.normal (0, pot_snr)
    
    x = amp * np.sin (frec_omega * tt) + ruido
    
    return tt, x

def eje_temporal (N, fs):
    
    Ts = 1/fs
    t_final = N * Ts
    tt = np.arange (0, t_final, Ts)
    return tt

def func_senoidal (tt, frec, amp, fase = 0, v_medio = 0):
    
    xx = amp * np.sin (2 * np.pi * frec * tt + fase) + v_medio # tt es un vector, por ende la función sin se evalúa para cada punto del mismo
    # xx tendrá la misma dimensión que tt
    return xx

def pot_ruido (a,snr):
    pr= a**2 / (2*10**(snr/10))  
    return pr

# %% SNR 10

# SNR en dB
SNR_10 = 10 
SNR_3=3

amp_0 = np.sqrt(2) # amplitud
N = 1000
fs = 1000
df = (fs / N) # Hz, resolución espectral

R=200#parametro para las cantidad de realizaciones

fr=np.random.uniform(-2,2,R)#esto es un vector de parametros --> tengo q salir de mi senoidal ==> armar una matriz de senoidales
Omega0=np.pi/2 #fs/4
Omega1=Omega0+fr*np.pi*2/N

nn = np.arange (N) # vector adimensional de muestras
ff = np.arange (N) * df # vector en frecuencia al escalar las muestras por la resolución espectral
tt = eje_temporal (N = N, fs = fs)
t_matriz=np.tile(tt.reshape(N,1),R)
fr_matriz=np.tile(Omega1.reshape(R,1),N).reshape(N,R)

s_1 = amp_0 * np.sin (2 * np.pi*df* fr_matriz* t_matriz) #matriz NxR de senoidales con frecuencias aleatorias
#func_senoidal (tt = tt, amp = amp_0, frec = )

X_matriz=(1/N)*fft(s_1,1)
plt.figure()

plt.plot (ff, 10*np.log10(10*(np.abs(X_matriz)**2)), color='orange', label='X_1')


pr10=pot_ruido(amp_0,SNR_10)  
pr3=pot_ruido(amp_0,SNR_3) 
#print (f"Potencia de SNR {pot_snr:3.1f}")   
                     
ruido10 = np.random.normal (0, np.sqrt(pr10), N)
var_ruido10 = np.var (ruido10)

ruido3 = np.random.normal (0, np.sqrt(pr3), N)
var_ruido3 = np.var (ruido3)


print (f"Potencia de ruido -> {var_ruido10:3.3f}")
print (f"Potencia de ruido -> {var_ruido3:3.3f}")


x_1 = s_1 + ruido10 # modelo de señal

R =(1/N)* fft (ruido10)
S_1 =(1/N)* fft (s_1)
X_1ruido = (1/N)*fft (x_1)
# print (np.var(x_1))


plt.plot (ff, 10*np.log10(2*(np.abs(X_1ruido)**2)), color='orange', label='X_1')
#plt.plot (ff, 20*np.log10(np.abs(S_1)), color='black', label='S_1')
#plt.plot (ff, 10*np.log10(np.abs(R)), label='Ruido')
plt.xlim((0,fs/2))
plt.grid (True)
plt.legend ()
plt.show ()

# %%Calibrar --> marcar mi 0
"""
normalizo por 1/N + mi cte de calibracion

cte de calibracion=lo que se reparte mi enegria ==> trato de equilibrarlo

potencia=area que encierra la densidad
potencia del ruido --> distribuida en todo el espectro (=0.1W)--> 
potencia de la senal la mido en la delta --> funcion distribucion: concentra la energia
"""
