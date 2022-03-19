from pprint import pprint
import yaml

from rucaptcha import RucaptchaApi


def main(**kwargs):
    with open("var/config.yml") as inp:
        config = yaml.safe_load(inp)
    api_key = config["rucaptcha_api_key"]
    api = RucaptchaApi(api_key)
    with open("data/captcha.jpg", "rb") as inp:
        data = inp.read()
    res = api.process_task_image(data)
    # res = api.process_task_text("один + два")
    print(res)
