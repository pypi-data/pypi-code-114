import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def with_borders_pixels ( poster, margin = 0, width = 0, color = (0,1,0)):
    
    # Validate values
    if width <= 0:
        raise Exception("Must provide a width for border")
    
    # Apply border
    if margin > 0:
        poster[margin:-margin,margin:margin+width] = color
        poster[margin:margin+width,margin:-margin] = color
        poster[margin:-margin,-margin-width:-margin] = color
        poster[-margin-width:-margin,margin:-margin] = color
    else:
        poster_size = poster.shape
        poster[0:width,  :] = color
        poster[poster_size[0]-width:poster_size[0],:] = color
        poster[:,0:width] = color
        poster[:,poster_size[1]-width:poster_size[1]] = color
    
def with_borders_percent ( poster, margin = 0, width = 0, color = (0,1,0)):
    
    if width + margin > 0.5:
        raise Exception("Width + Margin can not be >0.5")
        
    poster_size = poster.shape
    
    margin = math.floor(margin * poster_size[0])
    width = math.floor(width * poster_size[0])
    
    with_borders_pixels(poster, margin=margin, width=width, color=color)

# Chins and Heads

def with_chin_pixels ( poster, size = 0, color = (0,1,0)):
    
    # Validate values
    if size <= 0:
        raise Exception("Must provide a size for chin")
    
    poster_size = poster.shape
    poster[poster_size[0]-size:poster_size[0], :] = color
    
def with_head_pixels ( poster, size = 0, color = (0,1,0)):
    
    # Validate values
    if size <= 0:
        raise Exception("Must provide a size for head")
    
    poster_size = poster.shape
    poster[0:size, :] = color
     
def with_chin_percent ( poster, size = 0, color = (0,1,0)):
        
    poster_size = poster.shape
    size = math.floor(size * poster_size[0])
    with_chin_pixels(poster, size=size, color=color)
    
def with_head_percent ( poster, size = 0, color = (0,1,0)):
        
    poster_size = poster.shape
    size = math.floor(size * poster_size[0])
    with_head_pixels(poster, size=size, color=color)