# -*- coding: utf-8 -*-

""" En esta tarea semanal analizaremos un fenómeno muy particular que se da al calcular la DFT, el efecto de desparramo espectral.  

Luego, haremos el siguiente experimento:

Senoidal de frecuencia f0=k0∗fS/N=k0.Δf
potencia normalizada, es decir energía (o varianza) unitaria
Se pide:

a) Sea k0
 

N4
 
N4+0.25
 
N4+0.5
 
Notar que a cada senoidal se le agrega una pequeña desintonía respecto a  Δf
. Graficar las tres densidades espectrales de potencia (PDS's) y discutir cuál es el efecto de dicha desintonía en el espectro visualizado.

b) Verificar la potencia unitaria de cada PSD, puede usar la identidad de Parseval. En base a la teoría estudiada. Discuta la razón por la cual una señal senoidal tiene un espectro tan diferente respecto a otra de muy pocos Hertz de diferencia. 

c) Repetir el experimento mediante la técnica de zero padding. Dicha técnica consiste en agregar ceros al final de la señal para aumentar Δf
 de forma ficticia. Probar agregando un vector de 9*N ceros al final. Discuta los resultados obtenidos.

Bonus
💎 Calcule la respuesta en frecuencia de los sistemas LTI de la TS2.
"""
# %% Declaraciones
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import wave
from numpy.fft import fft
# Variables
N=1000
mbw=N/4 #mitad de banda digital
k0= [mbw, mbw + 0.25, mbw + 1/2]
fs=N
df = fs / N #resolucion espectral = [[1/(s*muestras)]
f0=np.dot(k0,df)
# %%Generacion de Senoidales
def sen(ff, nn, amp=np.sqrt(2), dc=0, ph=0, fs=2):
    N = np.arange(nn)
    t = N / fs
    x = dc + amp * np.sin(2 * np.pi * ff * t + ph)
    return t, x


t1, x1 = sen(ff=f0[0], nn=N, fs=fs)
t2, x2 = sen(ff=f0[1], nn=N, fs=fs)
t3, x3 = sen(ff=f0[2], nn=N, fs=fs)


#Graficos senoidales
# plt.figure()
# plt.title('Señales sinusoidales')
# plt.xlabel('Tiempo [s]')
# plt.ylabel('Amplitud')
# plt.plot(t1,x1,'x',label='Frecuencia'+str(f0[0]))
# plt.plot(t2,x2,'x',label='Frecuencia'+str(f0[1]))
# plt.plot(t3,x3,'o',label='Frecuencia'+str(f0[2]))
# plt.legend()
# plt.grid()
# plt.show()

# %%Calculo FFTs

#calculo la transformada, su modulo y su argumento
X1 = fft(x1)
X1abs = np.abs(X1)
X1ang = np.angle(X1)

X2 = fft(x2)
X2abs = np.abs(X2)
X2ang = np.angle(X2)

X3 = fft(x3)
X3abs = np.abs(X3)
X3ang = np.angle(X3)


Ff=np.arange(N)*df #mi eje x en hz
plt.figure()
plt.plot(Ff, 20*np.log10(X1abs), 'x', label='|X1| f= '+str(f0[0]))
plt.plot(Ff, 20*np.log10(X2abs), 'o', label='|X2| f= '+str(f0[1]))
plt.plot(Ff, 20*np.log10(X3abs), '+', label='|X3| f= '+str(f0[2]))
plt.xlim([0, fs/2])
plt.title('FFT')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid()
plt.legend()

# %% Parseval

#identificar var(x)=1

#identificar var(x)=1
varianza1 = np.var(x1)
varianza2 = np.var(x2)
varianza3 = np.var(x3)

print ('VARIANZAS UNITARIAS: ')
print('VAR(x1) = ' + str(varianza1))
print('VAR(x2)= ' + str(varianza2))
print('VAR(x3)= ' + str(varianza3)+'\n')

# lado espectral 

pot_x1_esp = np.sum((X1abs**2) * (1/N))
pot_x2_esp = np.sum((X2abs**2) * (1/N))
pot_x3_esp= np.sum((X3abs**2) * (1/N))

print('ENERGIAS CALCULADA POR LADO ESPECTRAL')
print('E(x1) = ' + str(pot_x1_esp))
print('E(x2)= ' + str(pot_x1_esp))
print('E(x3)= ' + str(pot_x1_esp)+'\n')

# lado temporal 

pot_x1_temp = np.sum(np.abs(x1)**2)
pot_x2_temp  = np.sum(np.abs(x2)**2)
pot_x3_temp  = np.sum(np.abs(x3)**2)

print('ENERGIAS CALCULADA POR LADO TEMPORAL')
print('E(x1) = ' + str(pot_x1_temp))
print('E(x2)= ' + str(pot_x2_temp))
print('E(x3)= ' + str(pot_x3_temp)+'\n')

# %% ZEROPADING 

df = fs / (10*N) 
Ffp=np.arange(10*N)*df #mi eje x en hz


z= np.zeros(9*N) #tiempo

x1z=np.concat((x1,z))
x2z=np.concat((x2,z))
x3z=np.concat((x3,z))

plt.figure(figsize=(20,10))
plt.title('zeropadding')
plt.plot(x1z,'o', label='x1')
plt.plot(x2z,'o', label='x2')
plt.plot(x3z,'o', label='x3')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

#el grafico tiene frecuencia muy alta ==> me da puntos porque no esta interpolado

#padding en frecuencia

X1z=fft(x1z)
X1zabs=np.abs(X1z)

X2z=fft(x2z)
X2zabs=np.abs(X2z)

X3z=fft(x3z)
X3zabs=np.abs(X3z)


plt.figure(figsize=(20,20))
plt.subplot(3,1,1)
plt.plot(Ffp,20*np.log10(X1zabs),'o', label='|X1| zero padding')
plt.plot(Ff,20*np.log10(X1abs),'x', label='|X1| sin padding')
plt.legend()
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid()

plt.subplot(3,1,2)
plt.plot(Ffp,20*np.log10(X2zabs),'o', label='|X2| zero padding')
plt.plot(Ff,20*np.log10(X2abs),'x', label='|X2| sin padding')
plt.legend()
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid()

plt.subplot(3,1,3)
plt.plot(Ffp,20*np.log10(X3zabs),'o', label='|X3| zero padding')
plt.plot(Ff,20*np.log10(X3abs),'x', label='|X3| sin padding')
plt.legend()
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid()












