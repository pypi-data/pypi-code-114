import json
from package_dan_pr3.dop import name
def showJs():
	with open("prof.json", "r") as json_file:
		a = json.load(json_file)
		print(a)
		name()


