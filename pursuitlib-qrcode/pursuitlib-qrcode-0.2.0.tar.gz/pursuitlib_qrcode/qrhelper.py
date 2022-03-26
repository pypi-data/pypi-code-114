import os

import qrcode
from qrcode.image.base import BaseImage

from pursuitlib import color

DEFAULT_QR_COLOR = "#FFFFFF"


def create_qrcode(data: str, qr_color: str = DEFAULT_QR_COLOR) -> BaseImage:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    fill = "#FFFFFF" if color.is_dark(qr_color) else "#000000"
    return qr.make_image(fill_color=fill, back_color=qr_color).get_image()


def save_qrcode(path: str, data: str, qr_color: str = DEFAULT_QR_COLOR):
    path_dir = os.path.dirname(path)
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)

    img = create_qrcode(data, qr_color)
    img.save(path)
