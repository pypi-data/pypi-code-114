import re
import PIL
import easyocr
import numpy as np
from PIL import ImageDraw,Image
from transformers import pipeline
from pdf2image import convert_from_path
from utils import *


reader = easyocr.Reader(['en'])
image = convert_from_path('test.pdf', poppler_path = r"C:\Users\shakhansho.sabzaliev\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")[0] # 1 page PDF
bounds = reader.readtext(np.array(image))


text = '' 
for i in range(len(bounds)):
	text += bounds[i][1] + '\n'

ner = pipeline("ner", grouped_entities=True)
bert = ner(text)


bbox, matches = [], []

find_emails(text, matches) # find matches and apend them to the list

# Find names, organizations' names, locations & addresses
for obj in bert:
    group = obj['entity_group']
    word = obj['word']
    if group in ['PER', 'ORG', 'LOC']:
    	matches.append(word)

find_coordinates(matches, bounds, bbox)

draw_black_box(bbox, image)

image.save(r'D:\Git Repos\open-data-anonymizer\anonympy\pdf\out.pdf')