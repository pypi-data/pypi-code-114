import json

def parse():
	with open('5.json') as json_file:
		data = json.load(json_file)
		print(data)
