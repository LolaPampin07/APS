# -*- coding: utf-8 -*-


#-------------------AUTOCORRELACION--------------

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig #metodos/fucniones para diversos campos de la ciencia (signal = senales)


N=8
"""
X=np.zeros(N)
X[:2]=1 #de la muestra 3 a la 5 vale 1
y=np.zeros(N)
y[5]=1
#plt.subplot()
#plt.plot(X)
#plt.stem(X)

Rxx= sig.correlate(X,y)
convxy=sig.convolve(X,y)


plt.figure(1)
plt.clf()
plt.plot(Rxx,'o:',label ='Rxx')
plt.plot(y,'x:',label='y')
plt.plot(X,'x:',label='X')
plt.plot(convxy,'o:',label='conv')
plt.show()

#plt.subplot()
#plt.stem(Rxx)
"""
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

#-------------------------------------
x=np.zeros(N)
y=np.zeros(4)
for i in len(x)-1:
    x[i]=4+3*np.sen(i*(np.pi/2))
for k in len(x-1)/2:
    y[k]=x[-k]

plt.plot(y,'x:',label='y')
plt.plot(x,'o:',label='x')











