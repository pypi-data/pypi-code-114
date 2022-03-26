# reference: P. Schneider, J. Ehlers and E. E. Falco
#   "Gravitational Lenses" section 8.3

import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import dblquad

class BinaryLens:
    """ gravitational lensing by binary star """
    def __init__(self, q, d, phi=0):
        """
        q = binary mass ratio m1/m2
        d = binary separation / Einstein radius rE
          rE = (4GM/c^2 d_L(d_S-d_L)/d_L)^{1/2}
          d_L,d_S = distances to lens and source
        phi = angle between x-axis and binary axis / radian
        """
        m = np.r_[1,q]/(1+q)
        z = np.r_[-m[1],m[0]]*d*np.exp(1j*phi)
        u = np.dot(m[::-1], z)
        p = np.prod([Polynomial([-z,1]) for z in z])
        q = Polynomial([-u,1])
        self.m = m # mass / total mass
        self.z = z # lens position (origin is at center of mass)
        self.u = u
        self.pp = p*p
        self.pq = p*q
        self.qq = q*q
        self.mag = np.vectorize(self.mag)

    def map(self,z):
        """ mapping from lens plane to source plane
        z = point on lens plane (complex number)
        return w = point on source plane (complex number)
        ray from w through z is deflected to observer
        """
        u = np.expand_dims(z,-1) # vectorize
        return z - np.dot(1/np.conj(u - self.z), self.m)

    def det_invmap(self,z):
        """ magnification factor of image at z
            (including sign of image parity)
        z = point on lens plane (complex number)
        return det(jacobian of inverse lens mapping)
        """
        z = np.expand_dims(z,-1) # vectorize
        J = np.abs(np.dot(1/np.conj(z - self.z)**2, self.m))**2
        return 1/(1-J)

    def crit(self,N=100):
        """ critical curve on lens plane
        return z = points on lens plane (complex number)
                   at which magnification diverge
        z.shape = (N,4)
        """
        p = [Polynomial([-z,1])**2 for z in self.z]
        h = np.dot(p, self.m[::-1])
        z = [(self.pp - h).roots()]
        for c in np.exp(1j*np.linspace(0, 2*np.pi, N))[1:]:
            z.append(sort((c*self.pp - h).roots(), z[-1]))

        return np.asarray(z)

    def caustic(self,N=100):
        """ critical curve on source plane
        return w = points on source plane (complex number)
                   at which magnification diverge
        w.shape = (N,4)
        """
        z = self.critical_curve(N)
        return self.map(z)

    def image(self,w):
        """ inverse of lens mapping
        w = source position (complex number)
        assume w is scalar or 1d-array
        return z = image position (complex number)
        if w is scalar, z.shape = (number of images,)
        if w is 1d-array, z.shape = (len(w), 5)
          if the number of images is less than 5,
          z is padded with nan in shape (len(w),5)
        """
        if not np.isscalar(w):# vectorize
            z = self.image(w[0])
            if len(w)==1: return z
            z = [pad(z,5)]
            for w in w[1:]:
                z.append(pad_sort(self.image(w), z[-1]))
            return np.asarray(z)

        f = np.conj(np.prod(w - self.z))*self.pp
        f += np.conj(2*w - np.sum(self.z))*self.pq + self.qq
        f *= Polynomial([-w,1])
        f -= np.conj(w - self.u)*self.pp + self.pq
        z = f.roots()
        return z[np.isclose(w, self.map(z))]

    def mag(self, w, r=0, atol=1e-3, rtol=1e-3):
        """ magnification factor of source at w
        w = source position (complex number)
        r = source radius of disk shape
        return mu = magnification factor
          (sum of |det_invmap| over all images)
        if r>0, mu is averaged over finite source size
          assuming uniform brightness over disk
        atol = tolerance for absolute error in averaging
        rtol = tolerance for relative error in averaging
          atol and rtol are used only if r>0
        w is vectorized so that mu.shape = w.shape
        (w can be array of any shape)
        """
        if r>0:# average over disk
            r2 = r**2
            return dblquad(# very slow
                lambda x,y: self.mag(w+x+1j*y),
                -r,r,
                lambda x: -np.sqrt(r2-x*x),
                lambda x:  np.sqrt(r2-x*x),
                epsabs=atol, epsrel=rtol)[0]/np.pi/r2

        z = self.image(w)
        return np.sum(np.abs(self.det_invmap(z)))


def sort(v,u):# used in BinaryLens.crit
    for i in range(len(v)-1):
        d = np.abs(v[i:] - u[i])
        j = np.argmin(d) + i
        if i!=j: v[i],v[j] = v[j],v[i]
    return v

def pad(v, n, a=np.nan):# used in BinaryLens.image
    if len(v)<n: v = np.r_[v, [a]*(n - len(v))]
    return v

def pad_sort(v, u, a=np.nan):# used in BinaryLens.image
    v = v.tolist()
    f = np.isfinite(u)
    w = np.full(len(u), a, dtype=np.complex)
    ind = np.flatnonzero(f).tolist()
    if len(v) >= len(f):
        for k in ind:
            d = np.abs(v - u[k])
            j = np.argmin(d)
            w[k] = v.pop(j)
        if len(v)==0: return w
        j = np.flatnonzero(np.logical_not(f))
        for i,t in enumerate(v):
            w[j[i]] = t
    else:
        for t in v:
            d = np.abs(u[ind] - t)
            j = np.argmin(d)
            w[ind.pop(j)] = t
    return w
