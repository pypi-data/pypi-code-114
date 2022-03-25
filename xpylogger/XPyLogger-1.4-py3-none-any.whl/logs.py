import time
import os
import rich

file = None
def init(file_enable = True,file_name = int(time.time()),dir_name = "logs"):
    global file
    try:
        if file_enable:
            os.mkdir(dir_name)
    except:
        pass
    if file_enable:
        file = open(f"./{dir_name}/{file_name}.log","w")
    else:
        file = False

def _log(msg,level = 0,f = "Main Thread"):
    global file
    if file == None:
        _init()   

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
    if file != False:
        file.write(f"{lo}\n")
def close():
    global file
    if file != False:
        file.close()
    file = None
