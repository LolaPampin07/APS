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
import ts1funciones as ts1
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import signal
from scipy.signal import lfilter, unit_impulse

N=100
frecADC=40000
t1=11
t0=1


def mi_funcion_y1 (x):

    y=np.zeros(N) #primero me armo mi array solucion y lo inicializo en 0
    
    #tanto mi entrada como mi salida es causal ==> para todo subindice <0 mi array vale 0
    for n in range(len(x)):
        x_n   = x[n] if n >= 0 else 0
        x_n1  = x[n-1] if n-1 >= 0 else 0
        x_n2  = x[n-2] if n-2 >= 0 else 0
        y_n1  = y[n-1] if n-1 >= 0 else 0
        y_n2  = y[n-2] if n-2 >= 0 else 0

        y[n] = (3e-2 * x_n + 5e-2 * x_n1 + 3e-2 * x_n2 + 1.5 * y_n1 - 0.5 * y_n2)
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

## Graficos item 1

plt.figure()
plt.subplot(2,3,1)
plt.title('item 1a')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tta, y1,'o:', color ='c')

plt.subplot(2,3,2)
plt.title('Item 1b')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttb,y2,'o:', color ='m')

plt.subplot(2,3,3)
plt.title('Item 1c')
plt.plot(ttc,y3,'o:', color ='violet')

plt.subplot(2,3,4)
plt.title('Item 1d')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttd,y4,'o:', color= 'orange')

plt.subplot(2,3,5)
plt.title('Item 1e')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tte,y5,'o:', color ='green')

plt.subplot(2,3,6)
plt.title('Item 1f')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(y6,'o:', color = 'y')

plt.show()
plt.legend()

######################################################

#Hallar la respuesta al impulso

def mi_funcion_resp_imp (a,b):

    d = unit_impulse(N)
    h = lfilter(b, a, d)
    return h

b= [0.03, 0.05, 0.03]      # Coeficientes de entrada (x)
a = [1.0, -1.5, 0.5]        # Coeficientes de salida (y)

h=mi_funcion_resp_imp(a,b)
yy1=np.convolve(fa, h)

yy2=np.convolve(fb, h)

yy3=np.convolve(fc, h)

yy4=np.convolve(fd, h)

yy5=np.convolve(fe, h)

yy6=np.convolve(ff, h)


plt.figure()
plt.subplot(2,3,1)
plt.title('item 1a')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy1,'o:', color ='c')

plt.subplot(2,3,2)
plt.title('Item 1b')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy2,'o:', color ='m')

plt.subplot(2,3,3)
plt.title('Item 1c')
plt.plot(yy3,'o:', color ='violet')

plt.subplot(2,3,4)
plt.title('Item 1d')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy4,'o:', color= 'orange')

plt.subplot(2,3,5)
plt.title('Item 1e')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy5,'o:', color ='green')

plt.subplot(2,3,6)
plt.title('Item 1f')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy6,'o:', color = 'y')

plt.show()
plt.legend()


"""
y[n]=x[n]+3⋅x[n−10]
y[n]=x[n]+3⋅y[n−10]
"""

def mi_funcion_y2 (x):
    y=np.zeros(N) #primero me armo mi array solucion y lo inicializo en 0
    for n in range(len(x)): 
        x_n  = x[n-10] if n >= 10 else 0
        y[n] = x[n]+3*x_n
    return y

#calculo mi fun directamente
y2a =mi_funcion_y2(fa)


#calculo mi fun a traves de la resp al impulso
b = [1,0,0,0,0,0,0,0,0,0,3]     
a = [1.0]        
h=mi_funcion_resp_imp(a,b)
yy2a = np.convolve(y2a, h)

plt.figure()
plt.subplot(1,2,1)
plt.title('Calculo directo y2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(y2a,'o:', color = 'c')

plt.subplot(1,2,2)
plt.title('"Calculo por h"')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy2a,'o:', color = 'm')


def mi_funcion_y3 (x):
    y=np.zeros(N) #primero me armo mi array solucion y lo inicializo en 0  
    for n in range(len(x)):    
        y[n] = x[n]+y[n-10]
    return y

y2b=mi_funcion_y3(fa)

b = [1.0]      # Coeficientes de entrada (x)
a = [1,0,0,0,0,0,0,0,0,0,-3]        # Coeficientes de salida (y)

h=mi_funcion_resp_imp(a,b)
yy2b = np.convolve(y2b, h)

plt.figure()
plt.subplot(1,2,1)
plt.title('Calculo directo y2')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(y2b,'o:', color = 'c')

plt.subplot(1,2,2)
plt.title('"Calculo por h"')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(yy2b,'o:', color = 'm')

