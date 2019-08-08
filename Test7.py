from numpy import *
from Lineal import *

a=array([[5,-3,1],[2,4,-1],[2,-3,8]], float)
b=array([[5],[6],[4]], float)
x=array([[1],[1],[1]], float)
x=gausseidel(a,b,x,0.0001,20);print(x)
print()
x=gausseidel(a,b,x,0.0001,20);print(x)
print()
x=gausseidel(a,b,x,0.0001,20);print(x)
print()
x=gausseidel(a,b,x,0.0001,20);print(x)
print()
x=gausseidel(a,b,x,0.0001,20);print(x)
print()
