import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import pathlib


def with_line ( poster, y=0, size=1, color=(0,0,0)):
    
    y *= poster.shape[0]
    size *= math.floor(poster.shape[0] / 300)
    inset = math.floor(poster.shape[1] * 0.3)
    
    y = math.floor(y)
    size = math.floor(size)
    
    poster[y:y+size,inset:-inset] = color