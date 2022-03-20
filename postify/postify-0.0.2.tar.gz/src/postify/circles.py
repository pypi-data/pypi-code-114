import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

# Circles

def _grid_2D (width, height):
    
    x = np.linspace(0, width-1, width)
    y = np.linspace(0, height-1, height)

    xv, yv = np.meshgrid(x, y)
    
    return np.stack([xv,yv]).T

def with_circle_pixels ( poster, inside = None, outside = None, radius = 0):
    
    # Validate values
    if radius <= 0:
        raise Exception("Must provide a radius for circle")
        
    if not inside and not outside:
        raise Exception("Must provide a color for either the inside or outside")
        
    # Calculate points pos
    center_x = poster.shape[0]//2
    center_y = poster.shape[1]//2
    
    # Distances
    mesh = _grid_2D (poster.shape[0], poster.shape[1])
    mesh[:,:,0] = mesh[:,:,0] - center_x
    mesh[:,:,1] = mesh[:,:,1] - center_y
    mesh[:,:,0] = mesh[:,:,0]**2 + mesh[:,:,1]**2
    mesh[:,:,0] = mesh[:,:,0] - radius ** 2

    if inside:
        poster[ mesh[:,:,0] < 0 ] = inside
    if outside:
        poster[ mesh[:,:,0] > 0 ] = outside
        
def with_circle_precent ( poster, inside = None, outside = None, radius = 0):
        
    poster_size = poster.shape
    radius = math.floor(radius * poster_size[0])
    with_circle_pixels(poster, inside=inside, outside=outside, radius=radius)
    