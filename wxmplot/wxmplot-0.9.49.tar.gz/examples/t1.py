from os import path
from tifffile import imread
import numpy as np
import wxmplot.interactive as wi

thisdir, _ = path.split(__file__)
imgdata =  imread(path.join(thisdir, 'ceo2.tiff'))

print(imgdata.shape)

mask = np.zeros(imgdata.shape, dtype=int)
mask[840:880, 950:1020] = 1

imd = wi.get_image_window(win=1)

imd.display(imgdata, contrast_level=0.1, colormap='coolwarm')
imd.panel.add_highlight_area(mask)
