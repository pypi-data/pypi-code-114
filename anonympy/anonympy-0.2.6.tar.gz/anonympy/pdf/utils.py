import re
import PIL 
from PIL import ImageDraw, Image


def draw_boxes(image, bounds, color='yellow', width=2):
	draw = ImageDraw.Draw(image)
	for bound in bounds:
		p0, p1, p2, p3 = bound[0]
		draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
	return image	


# def find_emails(doc, lst: list) -> None:
# 	for ent in doc:
# 		if ent.like_email:
# 			lst.append(ent)


# def find_persons_GPE(doc, lst: list) -> None:
#      for ent in doc.ents:
#      	if ent.label_ == 'PERSON' or ent.label_ == 'GPE':
#      		lst.append(ent.text)


def find_coordinates(pii_objects: list, bounds: list, bbox: list) -> None:
	for obj in pii_objects:
		for i in range(len(bounds)):
			if (obj.strip() in bounds[i][1].strip()) and (len(obj.strip()) > 3 and len(bounds[i][1].strip()) > 3):
				bbox.append(bounds[i][0])

def draw_black_box(bbox: list, image) -> None:
	draw = ImageDraw.Draw(image)
	for box in bbox:
		p0, p1, p2, p3 = box
		draw.rectangle([*p0, *p2], fill ="black", outline ="black")


def find_emails(text: str, lst: list) -> None:
	match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
	lst += match


# from spacy import displacy

# displacy.render(doc, jupyter=True, style='ent')


# image_list = [im_2, im_3, im_4]
# im_1 = image_1.convert('RGB')
# im_1.save(r'C:\Users\Ron\Desktop\Test\my_images.pdf', save_all=True, append_images=image_list)