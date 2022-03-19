import json
from package1 import fun_dop

with open("prof.json", "r") as json_file:
	a = json.load(json_file)


def fun1():
	return  "My name is " + a['Name']+"\nAge is "+fun_dop()


