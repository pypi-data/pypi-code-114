import time
import os
import rich

try:
    os.mkdir("logs")
except:
    pass

file = open(f"./logs/{int(time.time())}.log","w")
def _log(msg,level = 0,f = "Main Thread"):
    global file
    if level == 0:
        l = "INFO"
        q = ""
    elif level == 1:
        l = "WARN"
        q = "[yellow]"
    elif level == 2:
        l = "ERROR"
        q = "[red]"
    t = time.strftime("%H:%M:%S",time.localtime(time.time()))
    lo = f"[{t}][{f} / {l}] {msg}"
    rich.print(f"{q}{lo}")
    file.write(f"{lo}\n")
def close():
    global file
    file.close()
