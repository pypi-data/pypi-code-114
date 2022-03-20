import requests

def dork(args):
	google_url = f"https://www.google.com/search?q={args.query}&hl=en"
	api = f"https://api.hackertarget.com/pagelinks?q={google_url}"
	response = requests.get(api).text
	return response