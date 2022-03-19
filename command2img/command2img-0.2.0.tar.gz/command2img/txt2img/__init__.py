from os.path import join, realpath, dirname
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = join(dirname(__file__), "fonts")
FONT_FACE_MESLO = join(FONT_PATH, "meslo.ttf")
FONT_FACE_FIRA = join(FONT_PATH, "FiraCode-Regular.ttf")


def Txt2img(
    text: str,
    margin=10,
    font_face=FONT_FACE_MESLO,
    font_size=28,
    font_encoding="unic",
    backgroud=(255, 255, 255),
    text_fill=(0, 0, 0),
) -> Image:

    font = ImageFont.truetype(font=font_face, size=font_size, encoding=font_encoding)
    w, h = font.getsize_multiline(text)
    img = Image.new("RGB", (w + margin * 2, h - 40 + margin * 2), backgroud)

    ImageDraw.Draw(img).text((margin, margin - 10), text, fill=text_fill, font=font)
    return img
