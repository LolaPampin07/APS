# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from numpy.fft import fft

# %% Sintetizacion de funciones


N = 1000
fs = N
df = fs / N #resolucion espectral = [[1/(s*muestras)]
ts = 1 / fs
ff = (N/4)*df #eje en frecuencia ==> frecuencia * resolucion espectral

def sen(ff, nn, amp=1, dc=0, ph=0, fs=2):
    N = np.arange(nn)
    t = N / fs
    x = dc + amp * np.sin(2 * np.pi * ff * t + ph)
    return t, x

t1, x1 = sen(ff=(N / 4) * df, nn=N, fs=fs)
t2, x2 = sen(ff=((N / 4) + 1) * df, nn=N, fs=fs)
t3, x3 = sen(ff=((N / 4) + 1/2) * df, nn=N, fs=fs)

plt.figure()
plt.plot(x1)
# FFTs
X1 = fft(x1)
X1abs = np.abs(X1)
X1ang = np.angle(X1)

X2 = fft(x2)
X2abs = np.abs(X2)
X2ang = np.angle(X2)

X3 = fft(x3)
X3abs = np.abs(X3)
X3ang = np.angle(X3)


# fig, axes = plt.subplots(nrows=4, ncols=1)
# axes[0].plot(t1, x1, 'x')
# axes[1].plot(t2, x, 'x')
# axes[3].plot(t3, x3, 'x')


#me armo mi eje x

Ff=np.arange(N)*df #mi eje x en hz


plt.figure()
plt.plot(Ff, 20*np.log10(X1abs), 'x', label='X N/4 abs en dB')
plt.plot(Ff, 20*np.log10(X2abs), 'o', label='X2 N/4+1 abs en dB')
plt.plot(Ff, 20*np.log10(X3abs), '+', label='X3 N/4+0.5 abs en dB')
plt.xlim([0, fs/2])


#si mi n no es entero ==> la energia se dispersa por todo el espectro
#rango dinamico --> ratio entre el valor mas grande y mas chicos del sistema (suele estar en dB) ==> el log expande el rango dinamico



plt.title('FFT')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud [dB]')
plt.legend()

plt.show()

# %% PARSEVAL -->sumatoria de |x[n]|**2=1/N * sumatoria|X(w)|**2 --> calculo de energias en ambos dominios (tiempo y frecuencia)

tt, xx = sen(ff,N, np.sqrt(2), dc=0, ph=0, fs=fs) #sinusoidal con varianza unitaria ==> amp=A**(1/2)

#identificar var(x)=1
varianza = np.var(xx)
print(varianza)

X = fft(xx)

absX = np.abs(X)

# lado espectral 

a = np.sum((absX**2) * (1/N))
print(a)

# lado temporal 

b = np.sum(np.abs(xx)**2)
print(b)

# %% ZEROPADING 

df = fs / (10*N) #resolucion espectral = [[1/(s*muestras)]
Ffp=np.arange(10*N)*df #mi eje x en hz
#tiempo
z= np.zeros(9*N)

x1z=np.concat((x1,z))

plt.figure()
plt.plot(x1z,'o', label='zero padding')

#el grafico tiene frecuencia muy alta ==> me da puntos porque no esta interpolado

#padding en frecuencia

X1z=fft(x1z)
X1zabs=np.abs(X1z)

plt.figure()
plt.plot(Ffp,20*np.log10(X1zabs),'o', label='zero padding')
plt.plot(Ff,20*np.log10(X1abs),'x', label='transformada sin padding')
plt.legend()
#hago el padding --> y ahi transformo

# %% SNR

noise_std = 0.5 # Es el desvio estandar del ruido

# Ruido Blanco Gaussiano
ruido = np.random.normal(0, noise_std, size=t1.shape)

# Señal con ruido
senoidal_ruido = x1+ ruido

# Grafico
plt.figure()
plt.xlim(0,0.05)
plt.plot(t1, x1, color='black', label = 'Senoidal pura')
#plt.xlim(0,max(t1))
plt.plot(t1, senoidal_ruido, color='orange', label = 'Senoidal con ruido')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.title('Señal senoidal con ruido blanco')
plt.legend()
plt.tight_layout()
plt.show()

# %% VENTANAS --> blackman harris, hanning, flattop
#Hacer la ventana y Generar un grafico similar al holton 
#x_BH = x1 * ventana_BH

from numpy.fft import fft, fftshift
N=31

ventana_rectangular = np.ones(N)

ventana_BH = signal.windows.blackmanharris(N)

ventana_Hamming = signal.windows.hamming(N)

ventana_Hann = signal.windows.hann(N)

ventana_FT = signal.windows.flattop(N)

#Blackman Harris
plt.figure()
A = fft(ventana_BH, 2**14) / (len(ventana_BH)/2.0)
B = fft(ventana_Hamming, 2**14) / (len(ventana_Hamming)/2.0)
C = fft(ventana_Hann, 2**14) / (len(ventana_Hann)/2.0)
D = fft(ventana_rectangular, 2**14) / (len(ventana_rectangular)/2.0)
E = fft(ventana_FT, 2**14) / (len(ventana_FT)/2.0)
# %%
freq = np.linspace(-np.pi, np.pi, 2**14)


responseBH = 20 * np.log10(np.abs(fftshift(A / abs(A).max())))
responseHamming = 20 * np.log10(np.abs(fftshift(B / abs(B).max())))
responseHann = 20 * np.log10(np.abs(fftshift(C / abs(C).max())))
responseRect = 20 * np.log10(np.abs(fftshift(D / abs(D).max())))
responseFT = 20 * np.log10(np.abs(fftshift(E / abs(E).max())))

plt.plot(freq, responseBH,color="red", label = 'Blackman Harris')
plt.plot(freq, responseHamming, color="green", label = 'Hamming')
plt.plot(freq, responseHann, color="orange", label = 'Hann')
plt.plot(freq, responseRect,  label = 'Rectangular')
plt.plot(freq, responseFT, color="brown",  label = 'Flattop')
plt.legend()
plt.axis([-np.pi, np.pi, -80, 0])
ticks = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
labels = [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$']
plt.xticks(ticks, labels)
plt.title("Ventanas")
plt.ylabel("|W_N(w)| [dB]")
plt.xlabel("Frecuencia")
#

