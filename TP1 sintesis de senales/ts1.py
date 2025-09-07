# -*- coding: utf-8 -*-

#Librerias
import ts1funciones as ts1
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 

#Invocacion de funciones
N=100
frecADC=40000
t1=11
t0=1
#------------------------------------Ejercicio 1---------------------------------------------------------------

#a) Una señal sinusoidal de 2KHz.
tta,fa=ts1.mi_funcion_sen(1,0,2000,0,N,frecADC)

#b) Misma señal amplificada y desfazada en π/2.
ttb,fb=ts1.mi_funcion_sen(2,0,2000,np.pi/2,N,frecADC)

#c) Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia.
ttc,fc=ts1.mi_funcion_item_C(1,0,2000,0,N,frecADC)

#d) Señal anterior recortada al 75% de su potencia (energia) 
ttd,fd=ts1.mi_funcion_item_D(1,0,2000,0,N,frecADC)

#e) Una señal cuadrada de 4KHz.
tte,fe=ts1.mi_funcion_cuadrada(0, 4000, 0, N, frecADC = frecADC)

#f) Un pulso rectangular de 10ms. --> NO HAY FRECUENCIA UN SOLO 
ff=ts1.mi_funcion_pulso(t0,t1,N,1)

#g) En cada caso indique tiempo entre muestras, número de muestras y potencia.
ts=1/frecADC
ts1.mi_funcion_item_G(N, ts, fa)
ts1.mi_funcion_item_G(N, ts, fb)
ts1.mi_funcion_item_G(N, ts, fc)
ts1.mi_funcion_item_G(N, ts, fd)
ts1.mi_funcion_item_G(N, ts, fe)
ts1.mi_funcion_item_G(N, t1-t0, ff)


# Graficos item 1

plt.figure()
plt.subplot(2,3,1)
plt.title('item 1a')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tta, fa,'o-', color ='c')

plt.subplot(2,3,2)
plt.title('Item 1b')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttb,fb,'o-', color ='m')

plt.subplot(2,3,3)
plt.title('Item 1c')
plt.plot(ttc,fc,'o-', color ='violet')

plt.subplot(2,3,4)
plt.title('Item 1d')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ttd,fd,'o-', color= 'orange')

plt.subplot(2,3,5)
plt.title('Item 1e')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(tte,fe,'o-', color ='green')

plt.subplot(2,3,6)
plt.title('Item 1f')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [V]')
plt.plot(ff,'o-', color = 'y')

plt.show()
plt.legend()


# %%2) Verificar ortogonalidad entre la primera señal y las demás. 
#b
ts1.mi_funcion_ortogonalidad(fa, fb)
#c
ts1.mi_funcion_ortogonalidad(fa, fc)
#d
ts1.mi_funcion_ortogonalidad(fa, fd)
#e
ts1.mi_funcion_ortogonalidad(fa, fe)
#f
ts1.mi_funcion_ortogonalidad(fa, ff)
#------------------------------------Ejercicio 3---------------------------------------------------------------
"""3) Graficar la autocorrelación de la primera señal y la correlación entre ésta y las demás.
    scipy tiene funcion de autocorrelacion --> obtener la serie de autocorrelacion
"""

raa= signal.correlate(fa, fa)

rab=signal.correlate(fa, fb)


rac=signal.correlate(fa, fc)


rad=signal.correlate(fa, fd)


rae=signal.correlate(fa, fe)


raf=signal.correlate(fa, ff)

eje = np.arange(-len(fa) + 1, len(fa))

plt.figure()
plt.subplot(2,3,1)
plt.title('autocorrelacion item a')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje,raa/max(raa),'o-', color='r')

plt.subplot(2,3,2)
plt.title('correlacion cruzada item a y b')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje,rab/max(rab),'o-', color = 'y')

plt.subplot(2,3,3)
plt.title('correlacion cruzada item a y c')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje, rac/max(rac),'o-', color='c')

plt.subplot(2,3,4)
plt.title('correlacion cruzada item a y d')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje, rad/max(rad),'o-', color='g')

plt.subplot(2,3,5)
plt.title('correlacion cruzada item a y e')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje, rae/max(rae),'o-',color ='b')

plt.subplot(2,3,6)
plt.title('correlacion cruzada item a y f')
plt.xlabel('# unidades de desplazamiento')
plt.plot(eje, raf/max(raf),'o-', color='m')

plt.show()
plt.legend()

#------------------------------------Ejercicio 4---------------------------------------------------------------
"""4) Dada la siguiente propiedad trigonométrica: --> hay una funcion en numpy para comprobar autocorrelacion

2⋅ sin(α)⋅ sin(β) = cos(α-β)-cos(α+β) --> reemplazar por omega t, graficar en ambos casos y demostrar la igualdad

Demostrar la igualdad
Mostrar que la igualdad se cumple con señales sinusoidales, considerando α=ω⋅t, el doble de β (Use la frecuencia que desee).
"""
ts1.mi_funcion_propTrigo(np.pi,2*(np.pi)) #llamo a la funcion y le paso 2 frecuencias en rad/s



#-------------------------------------BONUS----------------------------------------------------------

ts1.mi_funcion_bonus()


