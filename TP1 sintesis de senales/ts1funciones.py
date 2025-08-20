# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    # Grafico
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt, xx
def mi_funcion_cuadrada(offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC 
    ttc = np.arange(start = 0, stop = N*ts, step = ts)
    xxc = signal.square(2 * np.pi * frec * ttc + fase)+offset
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( ttc, xxc, 'o--')

    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx = signal.square(2 * np.pi * frec * tt + fase)+offset
    
    plt.plot(tt, xx)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje[V]") 
    return tt,xx
def mi_funcion_impulso(frecADC=100, N=100, offset=0, fase=0):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx= signal.unit_impulse(len(tt), 'mid')
    
    plt.plot(tt, xx,color='k')
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje[V]")
    return tt, xx
def mi_funcion_item_C (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = np.sin(2*np.pi*frec/2*tt) * (np.sin( 2 * np.pi * frec * tt + fase) + offset)
    # Grafico
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt, xx
def mi_funcion_item_D (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]
    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    
    
    valor_corte= amp*0.75 #75% de la amp
    
    xx=np.clip(xx,-valor_corte,valor_corte)
    
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')
    # Grafico
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt, xx


  
  

