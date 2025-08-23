# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def mi_funcion_sen (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.sin( 2 * np.pi * frec * tt + fase) + offset
    # Grafico
    plt.figure()
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt,xx
def mi_funcion_cos (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = amp * np.cos( 2 * np.pi * frec * tt + fase) + offset
    # Grafico
    plt.figure()
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt,xx
def mi_funcion_cuadrada(offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC 
    ttc = np.arange(start = 0, stop = N*ts, step = ts)
    xxc = signal.square(2 * np.pi * frec * ttc + fase)+offset
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( ttc, xxc, 'o--')

    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx = signal.square(2 * np.pi * frec * tt + fase)+offset
    
    plt.figure()
    plt.plot(tt, xx)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje[V]") 
    return tt,xx
def mi_funcion_impulso(frecADC=100, N=100, offset=0, fase=0):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)
    xx= signal.unit_impulse(len(tt), 'mid')
    
    plt.figure()
    plt.plot(tt, xx,color='k')
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje[V]")
    return tt,xx
def mi_funcion_item_C (amp = 1, offset = 0, frec = 1, fase=0, N = 1000, frecADC = 1000):
    ts= 1/frecADC #tiempo al que se toma cada muestra [s]

    tt = np.arange(start = 0, stop = N*ts, step = ts)

    xx = np.sin(2*np.pi*frec/2*tt) * (np.sin( 2 * np.pi * frec * tt + fase) + offset)
    
    # Grafico
    plt.figure()
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt,xx
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
    plt.figure()
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot( tt, xx, 'o--')

    
    return tt,xx
def mi_funcion_pulso (t0=0,t1=10,N=20, h=1): #t0 es el tiempo donde comienza el pulso, t1 donde finaliza, N mi cantidad de muestras, h la altura de mi pulso
    
    X=np.zeros(N)
    X[t0:t1]=h
    
    plt.figure()
    plt.plot(X)
    plt.axis([-1,15,0,h+0.5])
    plt.xlabel('Tiempo [ms]')
    plt.ylabel('Voltaje [V]')
    plt.show()
    return X
def mi_funcion_ortogonalidad (f,g):
    valor=np.dot(f,g)
    if (valor == 0):
        return True
    else: 
        return False
def mi_funcion_propTrigo(a=np.pi,b=np.pi/4):
    
    #defino el primer lado de la igualdad
    _,xa = mi_funcion_sen(frec=a)
    _,xaa = mi_funcion_sen(frec=b)
    fa=2*xa*xaa
    
    #defino el segundo lado de la igualdad
    _,xb = mi_funcion_cos(frec=(a-b))
    _,xbb = mi_funcion_cos(frec=(a+b))
    fb=xb-xbb 
    
    #grafico
    plt.figure()
    plt.title('ITEM 4')
    plt.subplot(1,3,1)
    plt.plot(fa,'o:', label='primer lado de la igual')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    
    
    plt.subplot(1,3,2)
    plt.plot(fb,'o:', label='segundo lado de la igual')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    
    plt.subplot(1,3,3)
    plt.plot(fa,'o:', label='superposicion')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud [V]')
    plt.plot(fb,'o:')
       
    
  

