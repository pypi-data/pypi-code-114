import importlib, postify, cv2, math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def crop_width (poster, new_width = 50):
    
    amount = poster.shape[1] - new_width
    
    left = amount // 2
    right = amount // 2
    
    if left + right < amount:
        left += 1
       
    new_img = np.zeros((poster.shape[0], new_width, 3))
    new_img[:,0:new_width] = poster[:,left:-right]
    
    return new_img

def crop_width_ratio (poster, new_ratio = 1):
    
    amount = math.floor(poster.shape[1] * new_ratio)
    return crop_width(poster, amount)

def pad_with_color (poster, pad = 0, color = (0,0,0)):
    
    new_img = np.zeros((poster.shape[0] + pad*2, poster.shape[1] + pad*2, 3))
    new_img[:,:] += color
    new_img[pad:-pad, pad:-pad] = poster
    
    return new_img


def pad_bottom_with_color (poster, pad = 0, color = (0,0,0)):
    
    new_img = np.zeros((poster.shape[0] + pad, poster.shape[1], 3))
    new_img[:,:] += color
    new_img[:-pad] = poster
    
    return new_img

def pad_with_color_percent (poster, pad = 0, color = (0,0,0)):
    
    amount = math.floor(poster.shape[1] * pad)
    return pad_with_color(poster, pad=amount, color=color)


def pad_bottom_with_color_percent (poster, pad = 0, color = (0,0,0)):
    
    amount = math.floor(poster.shape[1] * pad)
    return pad_bottom_with_color(poster, pad=amount, color=color)
    