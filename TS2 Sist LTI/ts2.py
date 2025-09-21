# -*- coding: utf-8 -*-


"""
2) Hallar la respuesta al impulso y la salida correspondiente a una señal de 
entrada senoidal en los sistemas definidos mediante las siguientes ecuaciones en diferencias:

y[n]=x[n]+3⋅x[n−10]
y[n]=x[n]+3⋅y[n−10]


Bonus

5) Discretizar la siguiente ecuación diferencial correspondiente al modelo de Windkessel que describe la dinámica presión-flujo del sistema sanguíneo:

C⋅dPdt+1R⋅P=Q

Considere valores típicos de Compliance y Resistencia vascular
"""
# %% Librerias


import ts1funciones2 as ts1
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import signal
from scipy.signal import lfilter, unit_impulse

# %% Declaracion de variables

N=100
frecADC=40000
t1=11
t0=1
n=2 #
# %% Calculo de funciones


def mi_funcion_y1 (x):

    y=np.zeros(N) #primero me armo mi array solucion y lo inicializo en 0
    
    for n in range(2,len(x)):
#tanto mi entrada como mi salida es causal ==> para todo subindice <0 mi array vale 0
                
        #implementacion del zero padding --> puedo demorar mi array --> analizo cuantos 0 tengo que poner antes // puedo arrancar mi solucion a partir de indice positivo

        y[n] = (3e-2 * x[n] + 5e-2 * x[n-1] + 3e-2 * x[n-2] + 1.5 *y[n-1] - 0.5 * y[n-2])
    return y

#Invoco las funciones del tp anterior
#a) Una señal sinusoidal de 2KHz.
tta,fa=ts1.mi_funcion_sen(1,0,2000,0,N,frecADC)

y1=mi_funcion_y1(fa)

#b) Misma señal amplificada y desfazada en π/2.
ttb,fb=ts1.mi_funcion_sen(2,0,2000,np.pi/2,N,frecADC)

y2=mi_funcion_y1(fb)

#c) Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia.
ttc,fc=ts1.mi_funcion_item_C(1,0,2000,0,N,frecADC)

y3=mi_funcion_y1(fc)

#d) Señal anterior recortada al 75% de su potencia (energia) 
ttd,fd=ts1.mi_funcion_item_D(1,0,2000,0,N,frecADC)

y4=mi_funcion_y1(fd)

#e) Una señal cuadrada de 4KHz.
tte,fe=ts1.mi_funcion_cuadrada(0, 4000, 0, N, frecADC = frecADC)

y5=mi_funcion_y1(fe)

#f) Un pulso rectangular de 10ms. --> NO HAY FRECUENCIA UN SOLO 
ff=ts1.mi_funcion_pulso(t0,t1,N,1)
y6=mi_funcion_y1(ff)

# %% Graficos item 1


plt.figure()
plt.subplot(2,3,1)
plt.title('item 1a')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tta, fa,'x-', color ='b', label='entrada')
plt.plot(tta, y1,'o-', color ='c', label='salida')
plt.legend()


plt.subplot(2,3,2)
plt.title('Item 1b')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttb,fb,'x-', color ='b', label='entrada')
plt.plot(ttb,y2,'o-', color ='m', label='salida')
plt.legend()

plt.subplot(2,3,3)
plt.title('Item 1c')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttc,fc,'x-', color ='b', label='entrada')
plt.plot(ttc,y3,'o-', color ='violet', label='salida')
plt.legend()

plt.subplot(2,3,4)
plt.title('Item 1d')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttd,fd,'x-', color= 'b', label='entrada')
plt.plot(ttd,y4,'o-', color= 'orange', label='salida')
plt.legend()

plt.subplot(2,3,5)
plt.title('Item 1e')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tte,fe,'x-', color ='green', label='entrada')
plt.plot(tte,y5,'o-', color ='green', label='salida')
plt.legend()

plt.subplot(2,3,6)
plt.title('Item 1f')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ff,'x-', color = 'b', label='entrada')
plt.plot(y6,'o-', color = 'y', label='salida')
plt.legend()
# %% Item 1b calculo de funciones
#Hallar la respuesta al impulso

def mi_funcion_resp_imp (a,b, item):

    d = unit_impulse(3*N)
    h = lfilter(b, a, d)
    
    #grafico la respuesta al impulso
    plt.figure()
    plt.scatter(np.arange(0,3*N,1),h)
    plt.title('respuesta al impuso h')
    plt.legend()
    plt.show()
    
    return h

b= [0.03, 0.05, 0.03]      # Coeficientes de entrada (x)
a = [1.0, -1.5, 0.5]        # Coeficientes de salida (y)

h=mi_funcion_resp_imp(a,b, 'item 1b')
yy1=np.convolve(fa, h)

yy2=np.convolve(fb, h)

yy3=np.convolve(fc, h)

yy4=np.convolve(fd, h)

yy5=np.convolve(fe, h)

yy6=np.convolve(ff, h)

# %% Graficos item 1b

t_conv1 = np.arange(len(yy1)) / frecADC
t_conv2 = np.arange(len(yy2)) / frecADC
t_conv3 = np.arange(len(yy3)) / frecADC
t_conv4 = np.arange(len(yy4)) / frecADC
t_conv5 = np.arange(len(yy5)) / frecADC
dt = 1/frecADC
t = np.arange(len(fa)) * dt


#grafico mi salida
plt.figure(figsize=(20,20))
plt.subplot(2,3,1)
plt.title('item 1a')
plt.xlabel('Tiempo [s]')
plt.xlim(0,max (tta))
plt.ylabel('Amplitud')
plt.plot(t_conv1,yy1,'o:', color ='g', label='salida por convolucion')
plt.plot(tta,fa,'x-', color = 'y', label='entrada')
plt.plot(tta, y1,'x-', color ='b', label='salida metodo directo')
plt.legend()

plt.subplot(2,3,2)
plt.title('Item 1b')
plt.xlabel('Tiempo [s]')
plt.xlim(0,max (ttb))
plt.ylabel('Amplitud')
plt.plot(t_conv2, yy2,'o:', color ='g', label='salida por convolucion')
plt.plot(ttb,fb,'x-', color = 'y', label='entrada')
plt.plot(ttb,y2,'x-', color ='b', label='salida metodo directo')
plt.legend()

plt.subplot(2,3,3)
plt.title('Item 1c')
plt.xlabel('Tiempo [s]')
plt.xlim(0,max (ttc))
plt.ylabel('Amplitud')
plt.plot(t_conv3,yy3,'o:', color ='g', label='salida por convolucion')
plt.plot(ttc,fc,'x-', color = 'y', label='entrada')
plt.plot(ttc,y3,'x-', color ='b', label='salida metodo directo')
plt.legend()

plt.subplot(2,3,4)
plt.title('Item 1d')
plt.xlabel('Tiempo [s]')
plt.xlim(0,max (ttd))
plt.ylabel('Amplitud')
plt.plot(t_conv4,yy4,'o:', color= 'y', label='salida por convolucion')
plt.plot(ttd,fd,'x-', color = 'g', label='entrada')
plt.plot(ttd,y4,'x-', color= 'b', label='salida metodo directo')
plt.legend()

plt.subplot(2,3,5)
plt.title('Item 1e')
plt.xlabel('Tiempo [s]')
plt.xlim(0,max (tte))
plt.ylabel('Amplitud')
plt.plot(t_conv5,yy5,'o:', color ='y', label='salida por convolucion')
plt.plot(tte,fe,'x-', color = 'g', label='entrada ')
plt.plot(tte,y5,'x-', color ='b', label='salida metodo directo')
plt.legend()

plt.subplot(2,3,6)
plt.title('Item 1f')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.plot(yy6,'o:', color = 'y', label='salida por convolucion')
plt.plot(ff,'x-', color = 'g', label='entrada')
plt.plot(y6,'o-', color = 'b', label='salida metodo directo')
plt.legend()

# %% Item 2

"""
y[n]=x[n]+3⋅x[n−10]
y[n]=x[n]+3⋅y[n−10]
"""


#calculo mi fun a traves de la resp al impulso
b = [1,0,0,0,0,0,0,0,0,0,3]     
a = [1.0]        
h=mi_funcion_resp_imp(a,b, 'item 2a')


y2a = np.convolve(fa, h)
t_conv2a = np.arange(len(y2a)) / frecADC


#grafico item 2a
plt.figure()
plt.title('item 2a')
plt.xlabel('Tiempo [s]')
plt.xlim(0, max(tta))
plt.ylabel('Amplitud')
plt.plot(t_conv2a,y2a,'o:', color ='c', label='salida')
plt.plot(tta,fa,'x-', color = 'b', label='entrada')
plt.legend()


#item 2b
b = [1.0]      # Coeficientes de entrada (x)
a = [1,0,0,0,0,0,0,0,0,0,-3]        # Coeficientes de salida (y)

h=mi_funcion_resp_imp(a,b, 'item 2b')

y2b = np.convolve(fa, h)
t_conv2b = np.arange(len(y2b)) / frecADC

#grafico item 2b
plt.figure()
plt.title('item 2a')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
#plt.xlim(0, max(tta))
plt.plot(t_conv2,y2b,'o:', color ='c', label='salida')
plt.plot(tta,fa,'x-', color = 'b', label='entrada')
plt.legend()

