# -*- coding: utf-8 -*-

#Librerias
import ts1funciones as ts1
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 

#Invocacion de funciones
N=100
#------------------------------------Ejercicio 1---------------------------------------------------------------

#a) Una señal sinusoidal de 2KHz.
_,fa=ts1.mi_funcion_sen(1,0,2000,0,N,40000)

#b) Misma señal amplificada y desfazada en π/2.
_,fb=ts1.mi_funcion_sen(2,0,2000,np.pi/2,N,40000)

#c) Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia. --> reemplazo A con la funcion que modula
_,fc=ts1.mi_funcion_item_C(1,0,2000,0,N,40000)

#d) Señal anterior recortada al 75% de su potencia (energia) 
_,fd=ts1.mi_funcion_item_D(1,0,2000,0,N,40000)

#e) Una señal cuadrada de 4KHz.
_,fe=ts1.mi_funcion_cuadrada(0, 4000, 0, N, frecADC = 40000)

#f) Un pulso rectangular de 10ms. --> NO HAY FRECUENCIA UN SOLO 
ff=ts1.mi_funcion_pulso(1,11,N,1)

#g) En cada caso indique tiempo entre muestras, número de muestras y potencia.


#------------------------------------Ejercicio 2---------------------------------------------------------------
"""2) Verificar ortogonalidad entre la primera señal y las demás. """
#b
if (ts1.mi_funcion_ortogonalidad(fa, fb)):
    print ('la funcion del item a y la del item b son ortogonales')
else:
    print('la funcion del item a y la del item b NO son ortogonales')
#c
if (ts1.mi_funcion_ortogonalidad(fa, fc)):
    print ('la funcion del item a y la del item c son ortogonales')
else:
    print('la funcion del item a y la del item c NO son ortogonales')
#d
if (ts1.mi_funcion_ortogonalidad(fa, fd)):
    print ('la funcion del item a y la del item d son ortogonales')
else:
    print('la funcion del item a y la del item d NO son ortogonales')
#e
if (ts1.mi_funcion_ortogonalidad(fa, fe)):
    print ('la funcion del item a y la del item e son ortogonales')
else:
    print('la funcion del item a y la del item e NO son ortogonales')
#f
if (ts1.mi_funcion_ortogonalidad(fa, ff)):
    print ('la funcion del item a y la del item f son ortogonales')
else:
    print('la funcion del item a y la del item f NO son ortogonales')

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


plt.figure()
plt.subplot(2,3,1)
plt.title('autocorrelacion item a')
plt.plot(raa,'o:')

plt.subplot(2,3,2)
plt.title('correlacion cruzada item a y b')
plt.plot(rab,'o:')

plt.subplot(2,3,3)
plt.title('correlacion cruzada item a y c')
plt.plot(rac,'o:')

plt.subplot(2,3,4)
plt.title('correlacion cruzada item a y d')
plt.plot(rad,'o:')

plt.subplot(2,3,5)
plt.title('correlacion cruzada item a y e')
plt.plot(rae,'o:')

plt.subplot(2,3,6)
plt.title('correlacion cruzada item a y f')
plt.plot(raf,'o:')

plt.show()
plt.legend()

#------------------------------------Ejercicio 4---------------------------------------------------------------
"""4) Dada la siguiente propiedad trigonométrica: --> hay una funcion en numpy para comprobar autocorrelacion

2⋅ sin(α)⋅ sin(β) = cos(α-β)-cos(α+β) --> reemplazar por omega t, graficar en ambos casos y demostrar la igualdad

Demostrar la igualdad
Mostrar que la igualdad se cumple con señales sinusoidales, considerando α=ω⋅t, el doble de β (Use la frecuencia que desee).
"""
a=np.pi
b=2*a
ts1.mi_funcion_propTrigo(a,b) #llamo a la funcion y le paso 2 frecuencias en rad/s



#--------------------------------------------------------------------------------------------------------------




