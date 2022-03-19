import json

with open("prof.json", "r") as json_file:
    a = json.load(json_file)


def fun_dop():
    return a["Age"]
