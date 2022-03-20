import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

def with_text ( poster, font="", text="", x=0, y=0, size=1, color=(0.004,0.004,0.004)):
    
    # Create layer
    image = Image.fromarray(np.uint8(poster)*255)
    #image = Image.new('RGB', (poster.shape[1], poster.shape[0]), (0,0,0))
    
    draw = ImageDraw.Draw(image)
    
    x *= poster.shape[1]
    y *= poster.shape[0]
    size *= math.floor(poster.shape[0] / 20)
    size = math.floor(size)
    
    # load font
    font = ImageFont.truetype(font, size)  

    # positioning
    w, h = draw.textsize(text, font=font)
    draw.text((x-w//2,y-h//2,0),text,(math.floor(color[0]*255),math.floor(color[1]*255),math.floor(color[2]*255)),font=font)
    
    i = np.array(image)
    poster[i != 0] = i[i!=0]/255
    
    poster[poster>1] = 1