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
from scipy import signal
 
# Definicion de la funcion seno
def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    
    return tt, xx
n=0
# Definicon de la funcion para graficar
def graficar(x, y, ejex, ejey, titulo):
    plt.plot(x,y,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
    plt.plot(x,y,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
    plt.title(titulo) #Titulo del grafico
    plt.xlabel(ejex) #Titulo del eje
    plt.ylabel(ejey) #Titulo del eje 
    plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')
    plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
    plt.show() #Muestra los graficos
    

# Creacion de variables
amp=2 # [Volt]
offset = 1 # Valor medio en Volts
frec = 5 # Frecuencia en Hz
fase= np.pi/4 # Fase en radianes
N= 1000 # Cantidad de muestras
frecADC= 1000 #frecuencia de muestreo del ADC [Hz]

#Llamo a la funcion
tt, xx = mi_funcion_sen(amp, offset,frec, fase, N, frecADC)

graficar(tt, xx, 't [s]' , 'sen [V]', ' funcion inicial')


#--------------Bonus------------------------------------
"""Bonus:

Realizar los experimentos que se comentaron en clase. Siguiendo la notación de la función definida más arriba:
ff = 500 Hz
ff = 999 Hz
ff = 1001 Hz
ff = 2001 Hz
🤯 Implementar alguna otra señal propia de un generador de señales. """

tt1,xx1=mi_funcion_sen (amp = 1, offset = 0, frec = 500, fase=0, N = 1000, frecADC = 500000) #cambio la frecuencia del ADC para poder visualizar el grafico
graficar(tt1, xx1, 't[s]','sen [V]', 'frec 500Hz')

tt2,xx2=mi_funcion_sen (amp = 1, offset = 0, frec = 999, fase=0, N = 1000, frecADC = 1000)
graficar(tt2, xx2, 't[s]','sen [V]', 'frec 999 Hz')

tt3,xx3=mi_funcion_sen (amp = 1, offset = 0, frec = 1001, fase=0, N = 1000, frecADC = 1000)
graficar(tt3, xx3, 't[s]','sen [V]', 'frec 1001 Hz')

tt4,xx4=mi_funcion_sen (amp = 1, offset = 0, frec = 2001, fase=0, N = 1000, frecADC = 1000)
graficar(tt4, xx4, 't[s]','sen [V]', 'frec 2001 Hz')



def mi_funcion_cuadrada(frec=4, frecADC=100, N=100, offset=0, fase=0):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    ttc = np.arange(start = 0, stop = N*ts, step = ts)
    xxc = signal.square(2 * np.pi * frec * ttc + fase)+offset
    graficar(ttc,xxc,'t[s]','senal cuadrada [V]', 'funcion adicional')
    
mi_funcion_cuadrada()




