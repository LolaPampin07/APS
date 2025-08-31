# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#import scipy.signal as sig #metodos/fucniones para diversos campos de la ciencia (signal = senales)
from numpy.fft import fft
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


plt.figure(1)
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

# %%

# PARSEVAL

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

