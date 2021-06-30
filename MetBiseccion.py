#METODO DE LA BISECCIÓN
import numpy as np
import matplotlib.pyplot as plt
from math import*
def f(x):
    return x+cos(x)

def biseccion(a,b,tol):
    m=a
    c=b
    k=0

    if(f(a)*f(b)>0):
        print("\nLa función no cambia de signo")
        print()

    while(abs(m-c)>tol):
        m=c
        c=(a+b)/2
        if(f(a)*f(c)<0):
            b=c
        if(f(c)*f(b)<0):
            a=c

        print("El intervalo es: [",a,"",b,"]")
        k=k+1

        print()
    print("El resultado de la raiz es: ")
    print("x",k,"=",c,"aproximacion resultante de la raiz")
biseccion(-2,0,10**(-4))