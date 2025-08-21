# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 21:24:12 2025

@author: lolyy
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
 
# Definicion de la funcion seno
def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts) #tambien puedo usar linespace
    

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    plt.plot(tt,xx,label='Funcion', linestyle='-',color='r') #Genero un grafico llamado 'funcion' con linea 'discontinua-punteada' de color 'rojo'
    plt.plot(tt,xx,label='Puntos',linestyle='',marker='o',color='y') #Genero un grafico llamado 'Puntos', sin linea de color amarillo
    plt.legend() #Muestra las leyendas de cada plot (en este caso seria: label='Funcion', label='Puntos')
    plt.tight_layout() #Ajusta las posiciones de los subplots para que no se superpongan
    plt.show() #Muestra los graficos
    
    return tt, xx


mi_funcion_sen(1,0,2,0,1000,1000)

 
    