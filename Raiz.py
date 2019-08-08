import numpy as np
def biseccion(a ,b,f,e):

    while b-a>=e:
        c=( a + b) / 2
        if f(c) == 0:
            return c
        else:
            if  f(a) * f(c) > 0:
                a = c
            else:
                b=c
    return c

