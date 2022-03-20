import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def open_file ( path ):
    return cv2.imread(path) / 255

def create_blank ( width = 100, height = 0, ratio = 0, color=(1,1,1) ):
    
    # Load via width and ratio
    if ratio > 0:
        height = math.floor(width * (1/ratio))
    
    # Load via width and height
    if width > 0 and height > 0:
        img = np.zeros((height,width,3))
        img[:,:] = color
        return img
    
    raise Exception("Must provide either a (width, height) or a (width, ratio) to form blank image")


def save (poster, path):

    # Save as output
    _ = np.uint8(poster*255)
    img = Image.fromarray(_, 'RGB')
    img.save(path)

def show ( poster, size = 5):

    # Show in NOTEBOOK if needed
    plt.figure(figsize=(size, size), dpi=80)
    plt.imshow(poster, interpolation='nearest')
    plt.show()