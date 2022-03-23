# Copyright 2020 Jean-Marie Mirebeau, University Paris-Sud, CNRS, University Paris-Saclay
# Distributed WITHOUT ANY WARRANTY. Licensed under the Apache License, Version 2.0, see http://www.apache.org/licenses/LICENSE-2.0

"""
This module gathers a few helper functions for plotting data, that are used throughout the 
illustrative notebooks.
"""

from os import path
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from . import LinearParallel as lp


def SetTitle3D(ax,title):
	ax.text2D(0.5,0.95,title,transform=ax.transAxes,horizontalalignment='center')

def savefig(fig,fileName,dirName=None,ax=None,**kwargs):
	"""Save a figure:
	- in a given directory, possibly set in the properties of the function. 
	 Silently fails if dirName is None
	- with defaulted arguments, possibly set in the properties of the function
	"""
	# Choose the subplot to be saved 
	if ax is not None:
		kwargs['bbox_inches'] = ax.get_tightbbox(
			fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())

	# Set arguments to be passed
	for key,value in vars(savefig).items():
		if key not in kwargs and key!='dirName':
			kwargs[key]=value

	# Set directory
	if dirName is None: 
		if savefig.dirName is None: return 
		else: dirName=savefig.dirName

	# Save figure
	if path.isdir(dirName):
		fig.savefig(path.join(dirName,fileName),**kwargs) 
	else:
		print("savefig error: No such directory", dirName)
#		raise OSError(2, 'No such directory', dirName)

savefig.dirName = None
savefig.bbox_inches = 'tight'
savefig.pad_inches = 0
savefig.dpi = 300

def animation_curve(X,Y,**kwargs):
    """Animates a sequence of curves Y[0],Y[1],... with X as horizontal axis"""
    fig, ax = plt.subplots(); plt.close()
    ax.set_xlim(( X[0], X[-1]))
    ax.set_ylim(( np.min(Y), np.max(Y)))
    line, = ax.plot([], [])
    def func(i,Y): line.set_data(X,Y[i])
    kwargs.setdefault('interval',20)
    kwargs.setdefault('repeat',False)
    return animation.FuncAnimation(fig,func,fargs=(Y,),frames=len(Y),**kwargs)

def quiver(X,Y,U,V,subsampling=tuple(),**kwargs):
	"""
	Pyplot quiver with additional arg:
	- subsampling (tuple). Subsample X,Y,U,V
	"""
	where = tuple(slice(None,None,s) for s in subsampling)
	def f(Z): return Z.__getitem__(where)
	plt.quiver(f(X),f(Y),f(U),f(V),**kwargs)



def plotly_primal_dual_bodies(V):
    """    
    Output : facet indices, facet measures. 
    If an index appears several times, then the measures must be summed.
    """
    import scipy.spatial
    import plotly.graph_objects as go

    # Use a convex hull routine to triangulate the primal convex body
    primal_body = scipy.spatial.ConvexHull(V.T) 

    Vsize = V.shape[1]
    if primal_body.vertices.size!=Vsize:  # Then primal_body.vertices == np.arange(Xsize)
        raise ValueError("Non-convex primal body ! See",set(range(Vsize))-set(primal_body.vertices))

    # Use counter-clockwise orientation for all triangles
    S = primal_body.simplices.T
    N = primal_body.neighbors.T
    cw = np.sign(lp.det(V[:,S]))==-1 
    S[1,cw],S[2,cw] = S[2,cw],S[1,cw] 
    N[1,cw],N[2,cw] = N[2,cw],N[1,cw] 

    # --- Plotly primal mesh object
    x,y,z = V; i,j,k = S;
    primal_mesh = go.Mesh3d(x=x,y=y,z=z, i=i,j=j,k=k)
    # ---

    # --- Plotly primal edges object
    V0=V[:,S]; V1=V[:,np.roll(S,1,axis=0)];
    xe,ye,ze = np.moveaxis([V0,V1,np.full_like(V0,np.nan)],0,1)
    primal_edges = go.Scatter3d(x=xe.T.flat,y=ye.T.flat,z=ze.T.flat,mode='lines')
    # ---
    
    Sg = lp.solve_AV(lp.transpose(V[:,S]),np.ones(S.shape)) # The vertices of the dual convex body
    Ng = Sg[:,N] # Gradient of the neighbor cells
    
    # --- Plotly dual edges object
    xe,ye,ze = np.moveaxis(np.array([Sg[:,None]+0*Ng,Ng,np.full_like(Ng,np.nan)]),0,1)
    dual_edges = go.Scatter3d(x=xe.T.flat,y=ye.T.flat,z=ze.T.flat,mode='lines')
    # ---
    
    # Choose a reference simplex for each vertex, hence a reference point for each dual facet
    XS = np.full(Vsize,-1,S.dtype)
    XS[S] = np.arange(S.shape[1],dtype=S.dtype)[None]
        
    # --- Plotly dual mesh object, using triangulated faces
    x,y,z = Sg
    i = XS[S]; j=np.roll(N,-1,axis=0); k=np.tile(np.arange(Sg.shape[1]),(3,1))
    dual_mesh=go.Mesh3d(x=x,y=y,z=z, i=i.flat,j=j.flat,k=k.flat)
    # ---
    
    return (primal_mesh,primal_edges),(dual_mesh,dual_edges)