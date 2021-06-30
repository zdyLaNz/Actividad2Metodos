#METODO DE NEWTON

import numpy as np
from math import*

fx=lambda x: x+cos(x) #funcion
dfx = lambda x: 1-sin(x) #derivada de la función
x0 = 0
tol = 10**(-4) #tolerancia
'''En este caso
xn vendria ha ser x sub i+1 (x_i+1)'''
xi=x0
tramo =abs(2*tol)
while not (tramo<=tol): #el tramo no puede ser igual a la tolerancia
    xn=xi-fx(xi)/dfx(xi)
    tramo = abs(xn-xi)
    xi=xn
print()
print("\tel valor de la raiz es:  ",xn)
print("\tEl error es:  ",tramo)