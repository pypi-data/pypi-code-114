import requests

def generate(api_key):
    try: 
        r = requests.get('http://kinggen.com/api/v2/generate', params={'key': api_key}).text()
        return r
    except:
        return "Error"