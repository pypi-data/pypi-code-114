import numpy as np
from sympy import factorint,root,expand

class Period:# Gaussian periods
    @classmethod
    def init(cls,p):# p must be prime
        n = p-1

        g = 2 # generator mod p
        f = factorint(n)
        while True:
            for q in f:
                if pow(g, n//q, p)==1: break
            else:
                break
            g+=1

        i = np.empty(p, dtype=np.int)
        x = np.empty(n, dtype=np.int)
        a = 1
        for j in range(n):
            x[j] = a
            i[a] = j
            a *= g
            a %= p

        cls.p = p
        cls.x = x
        cls.index = i
        cls.factor = f

    @classmethod
    def SetDim(cls,e):# e must divide p-1
        p = cls.p
        x = cls.x
        i = cls.index
        n = p-1
        f = n//e

        # multiplication table
        w = np.zeros((e,e), dtype=np.int)
        for j in range(e):
            for k in range(j,n,e):
                l = (1 + x[k])%p
                if l: w[j,i[l]%e] += 1
                else: w[j] -= f

        w = [np.roll(w,j,(0,1)) for j in range(e)]
        cls.w = np.asarray(w)

    @classmethod
    def save_context(cls):
        if not hasattr(cls, 'p'): return
        context = {'p':cls.p, 'x':cls.x,
                   'index':cls.index,
                   'factor':cls.factor}
        if hasattr(cls, 'context'):
            cls.context.append(context)
        else:
            cls.context = [context]

    @classmethod
    def restore_context(cls):
        if(not hasattr(cls, 'context') or
           len(cls.context)==0): return
        context = cls.context.pop()
        cls.p = context['p']
        cls.x = context['x']
        cls.index = context['index']
        cls.factor = context['factor']

    def __init__(self, c):
        self.c = c

    def __mul__(self, p):
        c = np.dot(self.c, np.dot(p.c, self.w))
        return Period(c)

    def __pow__(self, n):
        m = (1<<(n.bit_length() - 1))>>1
        p = self
        while m:
            p *= p
            if n&m: p *= self
            m >>= 1
        return p

class Ring:# ring of cyclotomic polynomial
    def __init__(self, c):# symbolic representation
        self.c = c # by array of coefficients

    def __add__(self, a):
        if isinstance(a, Ring):
            return Ring(self.c + a.c)
        elif a==0:
            return self
        else:# never occurs
            c = self.c.copy()
            c[0] += a
            return Ring(c)

    def __mul__(self, a):
        if isinstance(a, Ring):
            n = len(self.c)
            t = np.convolve(self.c, a.c)
            c = t[:n]
            c[:-1] += t[n:] - c[-1]
            c[-1] = 0 # normalize
            return Ring(c)
        else:
            return Ring(a*self.c)

    def __rmul__(self, a):
        return Ring(a*self.c)

def cyclo_(p, recur=True):
    """ solve cyclotomic equation by radicals
    return p-th roots of unity (except 1)
           [exp(2pi ij/p) for j=1,2,...,p-1]
    p must be prime
    if recur is True, q-th roots of unity (q<p) are
      recursively replaced by radical expressions
    """
    if p==2: return -1
    if recur: Period.save_context()
    Period.init(p)
    n = 1
    y = np.zeros(p-1, dtype='object')
    y[0] = -1
    for p in list(Period.factor)[::-1]:
        r = np.eye(p, dtype=np.int64)
        r = [Ring(x) for x in r]
        if recur: w = cyclo_(p)
        else: w = [root(1,p,i) for i in range(1,p)]
        w = np.insert(w,0,1)
        i = np.outer(np.r_[:p], np.r_[:p])%p
        w,z = w[i],w[-i]
        for _ in range(Period.factor[p]):
            m = n*p
            Period.SetDim(m)
            v = np.zeros(m, dtype='object')
            v[::n] = r
            u = (Period(v)**p).c
            u = [x.c for x in np.r_[u[:n], u[-n:]]]
            # DFT (a.k.a. Lagrange resolvent)
            u = np.dot(u, w[:,1:])
            for k in range(n):
                t = np.dot(y[:n], u[:n])
                y[k+n:m:n] = [root(x,p,0) for x in t]
                # inverse DFT
                v[k::n] = np.dot(z, y[k:m:n])/p
                # cyclic permutation of periods
                u = np.roll(u, 1, axis=0)

            n = m
            y[:n] = [expand(x) for x in v]

    y = y[Period.index[1:]]
    if recur: Period.restore_context()
    return y

def cyclo(n, recur=True):
    """ solve cyclotomic equation by radicals
    return n-th roots of unity (except 1)
           [exp(2pi ij/n) for j=1,2,...,n-1]
    if recur is True, q-th roots of unity (q<n) are
      recursively replaced by radical expressions
    """
    if n<2:
        raise RuntimeError("n<2 in cyclo")

    f = factorint(n)
    z = np.empty(n, dtype='object')
    j = n
    for p in f:
        k,m = n//p,n
        z[k::k] = cyclo_(p, recur)
        for _ in range(1,f[p]):
            l = k//p
            a = np.r_[k:n:k][:,np.newaxis]
            b = np.r_[l:k:l]
            z[b] = [root(x,p,0) for x in z[k:m:k]]
            z[a+b] = z[a]*z[b]
            k,m = l,k

        if j<n:
            a = np.r_[j:n:j][:,np.newaxis]
            b = np.r_[k:n:k]
            z[(a+b)%n] = z[a]*z[b]

        j = j*k//n

    return z[1:]
