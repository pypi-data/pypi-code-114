import io

import requests

from . import settings


def captcha_solver(img, session=None, **kwargs):
    if isinstance(img, str):
        img = io.StringIO(img)

    if isinstance(img, bytes):
        img = io.BytesIO(img)

    if session is None:
        r = requests.post(settings.CAPTCHA_API, data=kwargs, files=dict(file=img))
    else:
        r = session.post(settings.CAPTCHA_API, data=kwargs, files=dict(file=img))

    return r.text.replace(' ', '')


__all__ = ('captcha_solver',)
