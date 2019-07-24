import numpy as np
def biseccion(a ,b,f,error):
    while abs(b - a) / 2 > error:
        c=( a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        if  f(b) * f(c) < 0:
            a = c
        return c
def f(x):
    return x-np.sin(x)
print(biseccion(-1,2,f,0.0001))
input()



def biseccion(a ,b,f,error):
    while abs(b - a) / 2 > error:
        c=( a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        if  f(b) * f(c) < 0:
            a = c
        return c
def f(x):
    return x-np.sin(x)
print(biseccion(-1,2,f,0.0001))
input()
