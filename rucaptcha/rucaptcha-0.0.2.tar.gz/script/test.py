from pprint import pprint

from rucaptcha import RucaptchaApi


def main(**kwargs):
    with open("var/rucaptcha.key") as inp:
        api_key = inp.read().strip()
    api = RucaptchaApi(api_key)
    with open("data/captcha.jpg", "rb") as inp:
        data = inp.read()
    res = api.process_task_image(data)
    # res = api.process_task_text("один + два")
    print(res)
