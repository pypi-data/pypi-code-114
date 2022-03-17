from math import sqrt, ceil, pi
import numpy as np
import itertools
import numpy.matlib
from numpy.random import RandomState, SeedSequence, MT19937, Generator


np.seterr(divide='raise')
numpy.seterr('raise')

class ICA:
    def __init__(self, K, N_RANDOM_INITS = 10, RAND_SEED = 1):
        self.K = K
        self.N_RANDOM_INITS = N_RANDOM_INITS
        self.RAND_SEED = RAND_SEED
        self.rng = Generator(MT19937(RAND_SEED))
        self.Q = None
        self.W_ica = None

    def histogram(self,x):
        minx=x.min()
        maxx=x.max()
        delta=(maxx-minx)/(len(x)-1)
        ncell=ceil(sqrt(len(x)))
        descriptor=[minx-delta/2,maxx+delta/2,ncell]
        lower,upper,ncell = descriptor
        y=np.round( (x-lower)/(upper-lower)*ncell + 1/2 ).astype(int)
        result = np.bincount(y)

        return result[1:],descriptor



    def random_rotation_matrix(self,N):
        pairs = np.flipud(list(itertools.combinations(np.arange(N),2)))
        n_pairs = pairs.shape[0]
        th = self.rng.random(n_pairs)*2*pi
        order = self.rng.permutation(n_pairs)
        rotMat = np.eye(N)
        for i,o in zip(th,order):
            x = np.eye(N)
            pair = pairs[o,:]
            x[np.ix_(pair,pair)] = [[np.cos(i),-np.sin(i)],[np.sin(i),np.cos(i)]]
            rotMat = x@rotMat
        return rotMat

    def entropy(self,x):
        h,descriptor = self.histogram(x)
        lowerbound = descriptor[0]
        upperbound = descriptor[1]
        ncell = descriptor[2]

        logf = np.log(h,out=np.zeros_like(h,dtype=float),where=(h!=0))
        count = h.sum()
        h_logf = h*logf
        estimate = -(h_logf.sum())
        sigma = (h_logf*logf).sum()
        
        estimate /= count
        sigma = np.sqrt((sigma/count-estimate**2)/(count-1))
        estimate += np.log(count) + np.log((upperbound-lowerbound)/ncell)
        nbias = -(ncell-1)/(2*count)

        estimate -= nbias
        nbias = 0

        base = np.exp(1)
        estimate /= np.log(base)
        nbias /= np.log(base)
        sigma /= np.log(base)

        return estimate,nbias,sigma,descriptor

    def maximize_negentropy_via_rotation(self,Wpca):
        n_random_initializations = self.N_RANDOM_INITS
        gaussEntropy = np.log(sqrt(2*pi*np.exp(1)))
        max_iter = 1000
        resolution = 61 # must be odd

        n = Wpca.shape[0]
        pairs = np.flipud(list(itertools.combinations(np.arange(n),2)))
        n_pairs = len(pairs)

        th = np.linspace(-pi/4,pi/4,resolution)
        negentropy_all_initializations = np.full(n_random_initializations, np.nan)
        Wica_all_initializations = np.full((*Wpca.shape,n_random_initializations),np.nan)
        negentropy_vs_rotation_all_initializations = np.full((len(th),n_pairs,n_random_initializations), np.nan)  

        for z in range(n_random_initializations):
            rotMat = self.random_rotation_matrix(n)
            Wica_all_initializations[:,:,z] = rotMat@Wpca
            negentropy = np.full(max_iter,np.nan)

            x =  np.array([gaussEntropy - self.entropy(Wpca[j,:])[0] for j in range(n)])
            negentropy[0] = x.mean()

            q = 0
            pairs_for_next_iteration = np.arange(n_pairs)
            negentropy_vs_rotation_all_initializations[:,:,z] = np.full((len(th),n_pairs),np.nan)
            while q<max_iter:
                q += 1
                
                rot = np.full(n_pairs,np.nan)

                pairs_to_check = self.rng.permutation(np.unique(pairs_for_next_iteration))
                pairs_for_next_iteration = []
                for i in pairs_to_check:
                    for j,t in enumerate(th):
                        rotMat = np.array([[np.cos(t),-np.sin(t)],
                                            [np.sin(t),np.cos(t)]])
                        Vrot = rotMat@Wica_all_initializations[np.array([pairs[i,0],pairs[i,1]]),:,z]
                        x = gaussEntropy - np.array([self.entropy(Vrot[0,:])[0], self.entropy(Vrot[1,:])[0]])
                        negentropy_vs_rotation_all_initializations[j,i,z] = x.mean()
                    rot_i = negentropy_vs_rotation_all_initializations[:,i,z].argmax()
                    rot[i] = rot_i # np.nan is float, so any int is coerced to float
                    rotMat = np.array([[np.cos(th[rot_i]), -np.sin(th[rot_i])], 
                                        [np.sin(th[rot_i]), np.cos(th[rot_i])]])  
                    Wica_all_initializations[np.array([pairs[i,0],pairs[i,1]]),:,z] = rotMat@Wica_all_initializations[np.array([pairs[i,0],pairs[i,1]]),:,z]

                    if rot_i != (resolution+1)/2 -1:
                        pairs_for_next_iteration = np.append(pairs_for_next_iteration,np.where(np.any(pairs[i,0] == pairs,axis=1) | np.any(pairs[i,1] == pairs,axis=1))).astype(int)
                x = np.array([gaussEntropy - self.entropy(Wica_all_initializations[j,:,z])[0] for j in range(n)])
                negentropy[q] = x.mean()
                if len(pairs_for_next_iteration)==0:
                    break

            
            negentropy_all_initializations[z] = negentropy[q]
        xi = np.argmax(negentropy_all_initializations)
        Wica_best = Wica_all_initializations[:,:,xi]
        #negentropy_vs_rotation_best_initialization = negentropy_vs_rotation_all_initializations[:,:,xi]; 
        #negentropy_best = negentropy_all_initializations[xi]

        return Wica_best, Wica_all_initializations, negentropy_all_initializations, negentropy_vs_rotation_all_initializations

    def nonparametric_ica(self,X):
        K = self.K
        M,N = X.shape
        X_zero_mean_rows = X - X.mean(axis=1,keepdims=True)
        U,S,V = np.linalg.svd(X_zero_mean_rows,full_matrices=False)
        V = V.T # consistent w/ Matlab
        Rpca = U[:,range(K)] @ np.diag(S[range(K)])
        Wpca = V[:,range(K)].T
        W, W_alliterations, negentropy_alliterations,_ = self.maximize_negentropy_via_rotation(Wpca)
        R = X_zero_mean_rows@np.linalg.pinv(W)
        R = R / np.sqrt((R**2).mean(axis=0,keepdims=True))
        W = np.linalg.pinv(R)@X
        R = R * numpy.matlib.repmat(np.sign(W.mean(axis=1,keepdims=True)).T,M,1)
        W = W * numpy.matlib.repmat(np.sign(W.mean(axis=1,keepdims=True)),1,N)
        return R, W, negentropy_alliterations, W_alliterations

    def fit(self,X):
        self.mixing,self.sources, self.negentropy_vs_rotation_all_initializations, self.negentropy_vs_rotation_all_initializations = self.nonparametric_ica(X)

    def fit_transform(self,X,R = None):
        self.fit(X)
        if R is None:
            return self.mixing
        else:
            return R@self.mixing, self.sources
        







