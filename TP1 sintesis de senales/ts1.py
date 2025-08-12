# -*- coding: utf-8 -*-
"""1) Sintetizar y graficar:

Una señal sinusoidal de 2KHz.
Misma señal amplificada y desfazada en π/2.
Misma señal modulada en amplitud por otra señal sinusoidal de la mitad de la frecuencia.
Señal anterior recortada al 75% de su potencia.
Una señal cuadrada de 4KHz.
Un pulso rectangular de 10ms.
En cada caso indique tiempo entre muestras, número de muestras y potencia.
2) Verificar ortogonalidad entre la primera señal y las demás.

3) Graficar la autocorrelación de la primera señal y la correlación entre ésta y las demás.

3) Dada la siguiente propiedad trigonométrica:

2⋅ sin(α)⋅ sin(β) = cos(α-β)-cos(α+β)

Demostrar la igualdad
Mostrar que la igualdad se cumple con señales sinosoidales, considerando α=ω⋅t, el doble de β (Use la frecuencia que desee).
Bonus
4) Graficar la temperatura del procesador de tu computadora en tiempo real.

Suponiendo distancia entre muestras constante
Considerando el tiempo de la muestra tomada
5) Bajar un wav de freesoung.org, graficarlo y calcular la energía"""
import ts1funciones as ts1
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 

#Invocacion de funciones
ts1.mi_funcion_sen(1, 0,2, 0)
ts1.mi_funcion_sen(3,0,2,np.pi/2)
ts1.mi_funcion_cuadrada()
ts1.mi_funcion_impulso()

plt.show()


