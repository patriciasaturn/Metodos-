import numpy as np
def gauss_jordan1(a, b):
    n = len(b)
    c = np.concatenate([a, b], axis=1)
    for e in range(n):
        t = c[e, e]
        for j in range(e, n + 1):
            c[e, j] = c[e, j] / t
        for i in range(n):
            if i != e:
                t = c[i, e]
                for j in range(e, n + 1):
                    c[i, j] = c[i, j] - t * c[e, j]
    x = c[:, n]
    return x

def gauss_jordan2(a,b):
    n = len(b)
    c = np.concatenate([a, b], axis=1)
    for e in range(n):
        c[e,e:] = c[e, e:]/c[e, e]
        for i in range(n):
            if i != e:
                c[i, e:] =c[i, e:] -c[i, e]* c[e, e:]
    x = c[:, n]
    return x


def Inversa(a, b):
    n = len(b)
    I= np.identity(n)
    c = np.concatenate([a, b], axis=1)
    c = np.concatenate([c, I], axis=1)

    for e in range(n):
        t = c[e, e]
        for j in range(e, 2* n + 1):
            c[e, j] = c[e, j] / t
        for i in range(n):
            if i != e:
                t = c[i, e]
                for j in range(e, 2 *n + 1):
                    c[i, j] = c[i, j] - t * c[e, j]
    Inv=c[:,n + 1:]
    return Inv

def gauss1(a,b):
    n = len(b)
    c = np.concatenate([a, b], axis=1)
    for e in range(n):
        t = c[e, e]
        for j in range(e, n + 1):
            c[e, j] = c[e, j] / t
        for i in range(e,n):
            if i != e:
                t = c[i, e]
                for j in range(e, n + 1):
                    c[i, j] = c[i, j] - t * c[e, j]
        x=np.zeros([n,1])
        x[n-1]=c[n-1,n]
        for i in range(n-2,-1,-1):
            s=0
            for j in range(i + 1,n):
             s=s + c[i,j]*x[j]
            x[i]=c[i,n]-s
    return x
def jacobi(a,b,x):
    n=len(x)
    t=x.copy()
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s + a [i,j]* t[j]
        x[i]=(b[i] -s) / a[i,i]
    return x
def jacobim(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=jacobi(a,b,x)
        d=np.linalg.norm(np.array(x)-np.array(t))
        if d<e:
            return[x,k]
        else:
            t=x.copy()
    return[[],m]
def gausseidel(a,b,x):
    n=len(x)
    for i in range(n):
        s=0
        for j in range(n):
            if i != j:
                s = s + a[i, j] * x[j]
        x[i] = (b[i] - s) / a[i, i]
    return x
def gaussseidelm(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=gausseidel(a,b,x)
        d=np.linalg.norm(np.array(x)-np.array(t))
        if d<e:
            return[x,k]
        else:
            t=x.copy()
    return[[],m]
