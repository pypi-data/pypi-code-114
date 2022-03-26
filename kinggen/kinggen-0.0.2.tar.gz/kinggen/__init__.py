import requests

def generate(api_key):
    try: 
        r = requests.get(f'http://kinggen.com/api/v2/generate?key={api_key}')
        return r
    except:
        return "Error"