#METODO DE LA SECANTE
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

def f(x):
    return np.cos(x)+x



def secante (f,x0,x1,N=100,emax=1e-10):
    for k in range (N):
       fp =(f(x1)-f(x0))/(x1-x0)
       x=x1-f(x1)/fp
       e=abs((x-x1)/x)
       if e<emax:
           break

       x0=x1
       x1=x
       print(x)

secante (f,-2,0)