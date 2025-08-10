# -*- coding: utf-8 -*-

"""programar una función que genere señales senoidales y que permita parametrizar:

la amplitud máxima de la senoidal (volts)
su valor medio (volts)
la frecuencia (Hz)
la fase (radianes)
la cantidad de muestras digitalizada por el ADC (# muestras)
la frecuencia de muestreo del ADC.
es decir que la función que uds armen debería admitir se llamada de la siguiente manera

tt, xx = mi_funcion_sen( vmax = 1, dc = 0, ff = 1, ph=0, nn = N, frec = frec)
"""

# Importacion de librerias
import numpy as np
import matplotlib.pyplot as plt
 
# Definicion de la funcion
def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    
    return tt, xx

# Creacion de variables
amp=2 # [Volt]
offset = 1 # Valor medio en Volts
frec = 5 # Frecuencia en Hz
fase= np.pi/4 # Fase en radianes
N= 1000 # Cantidad de muestras
frecADC= 1000 #frecuencia de muestreo del ADC [Hz]

#Llamo a la funcion
tt, xx = mi_funcion_sen(amp, offset,frec, fase, N, frecADC)

# Grafico
plt.xlabel('Tiempo [s]')
plt.ylabel('sen [V]')
plt.plot( tt, xx, 'o--')

