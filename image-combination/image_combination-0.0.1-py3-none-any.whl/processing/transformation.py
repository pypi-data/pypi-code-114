from skimage.transform import resize

def resize_image(image, heigth, width):
    image_resized = resize(image, (heigth, width), anti_aliasing=True)
    return image_resized