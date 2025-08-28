# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 20:58:40 2025

@author: lolyy
"""

# -*- coding: utf-8 -*-


#-------------------AUTOCORRELACION--------------

import numpy as np
import matplotlib.pyplot as plt
#import scipy.signal as sig #metodos/fucniones para diversos campos de la ciencia (signal = senales)
from numpy.fft import fft


N=1000
def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
       
    return tt,xx


tt,xx1= mi_funcion_sen(1,0,N/4,N,N)
xft1=fft(xx1)

tt,xx2= mi_funcion_sen(1,0,N/4+0.5,N,N)
xft2=fft(xx2)

tt,xx3= mi_funcion_sen(1,0,N/4+1,N,N)
xft3=fft(xx3)

plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.title('|x| N/4')
plt.plot(np.abs(xft1),'o:')
plt.subplot(1,3,2)
plt.plot(np.abs(xft2),'o:')
plt.title('|x| N/4+0.5')
plt.subplot(1,3,3)
plt.plot(np.abs(xft3),'o:')
plt.title('|x| N/4+1')

plt.show()


"""correlate --> 
modos: --> usamos el que viene por defecto
-full ==> correlacion completa
-valid ==> salida son aquellos elementos que no estan afectados por el 0 padding (solamente solapamiento completo entre senales)
-same ==> devuelve solamente n


metodo
-autp
-direct
-fft



CONVOLUCIONAR CON LA DELTA DEMORA LA SE;AL
"""


