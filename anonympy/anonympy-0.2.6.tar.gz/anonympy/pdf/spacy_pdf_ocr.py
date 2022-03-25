import PIL
import spacy
import easyocr
import numpy as np
from PIL import ImageDraw, Image
from pdf2image import convert_from_path
from utils import find_emails, find_persons_GPE
# from IPython.display import display, Image


reader = easyocr.Reader(['en'])
image = convert_from_path('test.pdf', poppler_path = r"C:\Users\shakhansho.sabzaliev\Downloads\Release-22.01.0-0\poppler-22.01.0\Library\bin")[0] # 1 page PDF
bounds = reader.readtext(np.array(image))

# display(image)
# print(bounds[3][0])

text = '' 

for i in range(len(bounds)):
	text += bounds[i][1] + '\n'

# print(text)

nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
found = []

find_emails(doc, found)
find_persons_GPE(doc, found)

bbox = []

def find_coordinates(pii_objects: list, bounds: list, bbox: list) -> None:
	for obj in pii_objects:
		for i in range(len(bounds)):
			if type(obj) == str:
				if obj.strip() in bounds[i][1].strip():
					bbox.append(bounds[i][0])	
			else:
				if obj.text.strip() in bounds[i][1].strip():
					bbox.append(bounds[i][0])

find_coordinates(found, bounds, bbox)

draw_black_box(bbox, image)

# image.show()

### Transformers 

from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

output = ner(text)

print(output)
