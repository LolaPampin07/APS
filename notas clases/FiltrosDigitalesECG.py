# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 16:38:17 2025

@author: JGL
"""

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Thu Oct 23 19:28:37 2025

@author: milenawaichnan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io as sio

#filtro normalizado -> todas las singularidades en el circulo unitario?
#--- Plantilla de diseño ---

fs = 1000
wp = [0.8, 35] #freq de corte/paso (rad/s)
ws = [0.1, 40] #freq de stop/detenida (rad/s)

#si alpha_p es =3 -> max atenuacion, butter

alpha_p = 1/2 #atenuacion de corte/paso, alfa_max, perdida en banda de paso 
alpha_s = 40/2 #atenuacion de stop/detenida, alfa_min, minima atenuacion requerida en banda de paso 

#Aprox de modulo

#
#
#f_aprox = 'ellip'
#

#Aprox fase
#f_aprox = 'bessel'

# --- Diseño de filtro analogico ---
f_aprox = 'butter'
mi_sos_butter = signal.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output ='sos', fs=fs) #devuelve dos listas de coeficientes, b para P y a para Q
# f_aprox = 'cheby1'
# mi_sos_cheby1 = signal.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output ='sos', fs=fs) #devuelve dos listas de coeficientes, b para P y a para Q
# f_aprox = 'cheby2'
# mi_sos_cheby2 = signal.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output ='sos', fs=fs) #devuelve dos listas de coeficientes, b para P y a para Q
f_aprox = 'cauer'
mi_sos_cauer = signal.iirdesign(wp = wp, ws = ws, gpass = alpha_p, gstop = alpha_s, analog = False, ftype = f_aprox, output ='sos', fs=fs) #devuelve dos listas de coeficientes, b para P y a para Q

# %%
mi_sos = mi_sos_cauer

# --- Respuesta en frecuencia ---
w, h= signal.freqz_sos(mi_sos, worN = np.logspace(-2, 1.9, 1000), fs = fs) #calcula rta en frq del filtro, devuelve w y vector de salida (h es numero complejo)

# --- Cálculo de fase y retardo de grupo ---

fase = np.unwrap(np.angle(h)) #unwrap hace grafico continuo

w_rad = w / (fs / 2) * np.pi
gd = -np.diff(fase) / np.diff(w_rad) #retardo de grupo [rad/rad]

# --- Polos y ceros ---

z, p, k = signal.sos2zpk(mi_sos) #ubicacion de polos y ceros, z=ubicacion de ceros(=0), p=ubicacion polos, k

# --- Gráficas ---
#plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(2,2,1)
plt.plot(w, 20*np.log10(abs(h)), label = f_aprox)
plt.title('Respuesta en Magnitud')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('|H(jω)| [dB]')
plt.grid(True, which='both', ls=':')

# Fase
plt.subplot(2,2,2)
plt.plot(w, fase, label = f_aprox)
plt.title('Fase')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('Fase [°]')
plt.grid(True, which='both', ls=':')

# Retardo de grupo
plt.subplot(2,2,3)
plt.plot(w[:-1], gd, label = f_aprox)
plt.title('Retardo de Grupo ')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which='both', ls=':')

# Diagrama de polos y ceros
plt.subplot(2,2,4)
plt.plot(np.real(p), np.imag(p), 'x', markersize=10, label=f'{f_aprox} Polos')
if len(z) > 0:
    plt.plot(np.real(z), np.imag(z), 'o', markersize=10, fillstyle='none', label=f'{f_aprox} Ceros')
plt.axhline(0, color='k', lw=0.5)
plt.axvline(0, color='k', lw=0.5)
plt.title('Diagrama de Polos y Ceros (plano z)')
plt.xlabel('σ [rad/s]')
plt.ylabel('jω [rad/s]')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


#%%

##################
# Lectura de ECG #
##################

fs_ecg = 1000 # Hz

##################
## ECG con ruido
##################

# para listar las variables que hay en el archivo
#io.whosmat('ECG_TP4.mat')
mat_struct = sio.loadmat('./ECG_TP4.mat')
ecg_one_lead = mat_struct['ecg_lead'].flatten()
N = len(ecg_one_lead)

ecg_filt_butt = signal.sosfiltfilt(mi_sos_butter, ecg_one_lead)
ecg_filt_cauer = signal.sosfiltfilt(mi_sos_cauer, ecg_one_lead)
# ecg_filt_cheb1 = signal.sosfiltfilt(mi_sos_cheby1, ecg_one_lead)
# ecg_filt_cheb2 = signal.sosfiltfilt(mi_sos_cheby2, ecg_one_lead)

plt.figure()

plt.plot(ecg_one_lead, label = 'ecg raw')
# plt.plot(ecg_filt_butt, label = 'butter')
plt.plot(ecg_filt_cauer, label = 'cauer')
#plt.plot(ecg_filt_cheb1, label = 'cheby1')
#plt.plot(ecg_filt_cheb2, label = 'cheby2')

plt.legend()

# hb_1 = mat_struct['heartbeat_pattern1']
# hb_2 = mat_struct['heartbeat_pattern2']

# plt.figure()
# plt.plot(ecg_one_lead[5000:12000])

# plt.figure()
# plt.plot(hb_1)

# plt.figure()
# plt.plot(hb_2)

##################
## ECG sin ruido
##################


#################################
# Regiones de interés sin ruido #
#################################

cant_muestras = len(ecg_one_lead)

regs_interes = (
        [4000, 5500], # muestras
        [10e3, 11e3], # muestras
        )
 
for ii in regs_interes:
   
    # intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
   
    plt.figure()
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ecg_filt_butt[zoom_region], label='Butterworth')
    #plt.plot(zoom_region, ECG_f_win[zoom_region + demora], label='FIR Window')
   
    plt.title('ECG sin ruido desde ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
   
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
           
    plt.show()
 
#################################
# Regiones de interés con ruido #
#################################
 
regs_interes = (
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        )
 
for ii in regs_interes:
   
    # intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
   
    plt.figure()
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ecg_filt_butt[zoom_region], label='Butterworth')
    # plt.plot(zoom_region, ECG_f_win[zoom_region + demora], label='FIR Window')
   
    plt.title('ECG con ruido desde ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
   
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
           
    plt.show()

# %% FIR

WD = [0.8,35] #FRECUENCIA DE CORTE/PASO [HZ]
WS=[0.1,40] #FRECUENCIA DE STOP/DETENIDA (HZ)

frecuencias=np.sort(np.concatenate(((0,.05,fs/2),wp,ws))) #hasta Nyquist pq asi lo require la documentacion de la funcion
cant_coef=1000 #con cant de coef par ==> 
retardo=(N-1)//2

deseado=[0,0,0,1,1,0,0] #comportamiento deseado en pasa banda

fir_win_rect=signal.firwin2(numtaps=cant_coef, freq=frecuencias,gain=deseado,fs=fs, window= 'boxcar',nfreqs=int((np.ceil(np.sqrt(cant_coef))*2)**2-1)) #me devuelve los coef b pq los a en FIR es siempre 1
## obtengo la respuesta al impulso del filtro --> coeficientes b!! 
#nfreqs=(np.ceil(np.sqrt(cant_coef))*2)**2-1 ==> p/ mejprar la grilla
#boxcar ==> alta capacidad de transicionar


#resp en frec filtro fir
w, h= signal.freqz(b= fir_win_rect, worN = np.logspace(-2, 1.9, 1000), fs = fs) #asume a=1 ==> todos los polos en el origen ==> CONDICION PARA QUE SEA FIR == QUE NO SEA RECURSIVO

# --- Cálculo de fase y retardo de grupo ---

fase = np.unwrap(np.angle(h)) #unwrap hace grafico continuo

w_rad = w / (fs / 2) * np.pi

# --- Polos y ceros ---

#z, p, k = signal.sos2zpk(signal.tf2sos(b=fir_win_rect,a=1)) #ubicacion de polos y ceros, z=ubicacion de ceros(=0), p=ubicacion polos, k

# --- Gráficas ---
plt.figure(figsize=(12,10))

# Magnitud
plt.subplot(2,2,1)
plt.plot(w, 20*np.log10(abs(h)), label = f_aprox)
plt.title('Respuesta en Magnitud')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('|H(jω)| [dB]')
plt.grid(True, which='both', ls=':')

# Fase
plt.subplot(2,2,2)
plt.plot(w, fase, label = f_aprox)
plt.title('Fase')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('Fase [°]')
plt.grid(True, which='both', ls=':')

# Retardo de grupo
plt.subplot(2,2,3)
plt.plot(w[:-1], gd, label = f_aprox)
plt.title('Retardo de Grupo ')
plt.xlabel('Pulsación angular [r/s]')
plt.ylabel('τg [# muestras]')
plt.grid(True, which='both', ls=':')

# Diagrama de polos y ceros
# plt.subplot(2,2,4)
# plt.plot(np.real(p), np.imag(p), 'x', markersize=10, label=f'{f_aprox} Polos')
# if len(z) > 0:
#     plt.plot(np.real(z), np.imag(z), 'o', markersize=10, fillstyle='none', label=f'{f_aprox} Ceros')
# plt.axhline(0, color='k', lw=0.5)
# plt.axvline(0, color='k', lw=0.5)
# plt.title('Diagrama de Polos y Ceros (plano z)')
# plt.xlabel('σ [rad/s]')
# plt.ylabel('jω [rad/s]')
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# %%DISENO DEL FILTRO

ecg_filt_win = signal.lfiter(b=fir_win_rect,a=1, x= ecg_one_lead)







