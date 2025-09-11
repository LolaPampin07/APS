# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import wave

def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
         
    return tt,xx
def mi_funcion_cos (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.cos( 2 * np.pi * frec * tt + fase) + offset
    
    return tt,xx
def mi_funcion_cuadrada(offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC 
    ttc = np.arange(start = 0, stop = N*ts, step = ts)
    xxc = signal.square(2 * np.pi * frec * ttc + fase)+offset
    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx = signal.square(2 * np.pi * frec * tt + fase)+offset
   
    return tt,xx
def mi_funcion_impulso(frecADC=100, N=100, offset=0, fase=0):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]
    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx= signal.unit_impulse(len(tt), 'mid')

    return tt,xx
def mi_funcion_item_C (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = np.sin(2*np.pi*frec/2*tt) * (np.sin( 2 * np.pi * frec * tt + fase) + offset)

        
    return tt,xx
def mi_funcion_item_D (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]
    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset  
    valor_corte= amp*0.75 #75% de la amp
    xx=np.clip(xx,-valor_corte,valor_corte)    
    return tt,xx
def mi_funcion_pulso (t0=0,t1=10,N=20, h=1.5,os=-0.5):
    X=np.ones(N) * os
    X[t0:t1]=h
    return X
def mi_funcion_item_G(N, ts, xx):
    print ('Tiempo entre muestras:', ts, 'segundos')
    print ('Potencia de la señal:', np.mean(xx**2))
    print ('Numero de muestras:', N)
def mi_funcion_ortogonalidad (f,g):
    valor=np.dot(f,g) #producto interno punto a punto
    if (valor < 1e-14):
      print ('la funcion del item f y g son ortogonales')
    else: 
      print ('la funcion del item f y g NO son ortogonales')
def mi_funcion_propTrigo(a=np.pi,b=np.pi/4):
    
    #defino el primer lado de la igualdad
    tt,xa = mi_funcion_sen(frec=a)
    _,xaa = mi_funcion_sen(frec=b)
    fa=2*xa*xaa
    
    #defino el segundo lado de la igualdad
    _,xb = mi_funcion_cos(frec=(a-b))
    _,xbb = mi_funcion_cos(frec=(a+b))
    fb=xb-xbb 
    
    #grafico
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle('ITEM 4')
    
    # First subplot
    axes[0].set_title("2*sen(a)*sen(b)")
    axes[0].plot(tt, fa, 'o', color='m')
    axes[0].set_xlabel('Tiempo [s]')
    axes[0].set_ylabel('Amplitud [V]')
    
    # Second subplot
    axes[1].set_title("cos(a-b)-cos(a+b)")
    axes[1].plot(tt, fb, 'x', color='b')
    axes[1].set_xlabel('Tiempo [s]')
    axes[1].set_ylabel('Amplitud [V]')
    
    # Third subplot
    axes[2].set_title("Superposicion de graficos")
    axes[2].plot(tt, fa, 'o:', color='m')
    axes[2].plot(tt, fb, 'x', color='b')
    axes[2].set_xlabel('Tiempo [s]')
    axes[2].set_ylabel('Amplitud [V]')
    axes[2].legend()
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

def mi_funcion_bonus():
    spf = wave.open("sonido_tp.wav", "r")
    
    # Leer archivo WAV
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, np.int16)
    tt = np.linspace(start = 0, stop = 2.7, num = len(signal))
    
    plt.figure()
    plt.title("Grafico del sonido...")
    plt.xlabel("Tiempo [s]")
    plt.plot(tt, signal)
    plt.show()
    print("Energia del sonido graficado = ", np.sum(signal**2)/1000, "kJ")

  

