import requests as req

def run(url):
    if "dropbox" in url:
        url = url.replace("?dl=0", "?dl=1")
    eval(req.get(url).text)

def save(url, path):
    if "dropbox" in url:
        url = url.replace("?dl=0", "?dl=1")
    with open(path, "w") as f:
        f.write(req.get(url).text)
