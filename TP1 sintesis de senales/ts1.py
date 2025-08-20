# -*- coding: utf-8 -*-
"""
2) Verificar ortogonalidad entre la primera señal y las demás. 
    --> multiplicar matricialmente fila por columna --> producto interno =0 HAY UNA FUNCION EN PYTHON QUE LO HACE SOLO!!

3) Graficar la autocorrelación de la primera señal y la correlación entre ésta y las demás.
    scipy tiene funcion de autocorrelacion --> obtener la serie de autocorrelacion

4) Dada la siguiente propiedad trigonométrica: --> hay una funcion en numpy para comprobar autocorrelacion

2⋅ sin(α)⋅ sin(β) = cos(α-β)-cos(α+β) --> reemplazar por omega t, graficar en ambos casos y demostrar la igualdad

Demostrar la igualdad
Mostrar que la igualdad se cumple con señales sinosoidales, considerando α=ω⋅t, el doble de β (Use la frecuencia que desee).


Bonus
4) Graficar la temperatura del procesador de tu computadora en tiempo real.

Suponiendo distancia entre muestras constante
Considerando el tiempo de la muestra tomada
5) Bajar un wav de freesoung.org, graficarlo y calcular la energía"""

#def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):


import ts1funciones as ts1
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 

#Invocacion de funciones

#a) Una señal sinusoidal de 2KHz.
ts1.mi_funcion_sen(1,0,2000,0,100,40000)

#b) Misma señal amplificada y desfazada en π/2.
ts1.mi_funcion_sen(2,0,2000,np.pi/2,100,40000)

#c) Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia. --> reemplazo A con la funcion que modula
ts1.mi_funcion_item_C(1,0,2000,0,100,40000)

#d) Señal anterior recortada al 75% de su potencia (energia) 
ts1.mi_funcion_item_D(1,0,2000,0,100,40000)

#e) Una señal cuadrada de 4KHz.
ts1.mi_funcion_cuadrada(0, 4000, 0, N = 100, frecADC = 40000)

#f) Un pulso rectangular de 10ms. --> NO HAY FRECUENCIA UN SOLO 


#g) En cada caso indique tiempo entre muestras, número de muestras y potencia.

plt.show()



