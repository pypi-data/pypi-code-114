from .logs import *

INFO = 0
WARN = 1
ERR = 2
SENDER_MAIN = "Main Thread"

def log(msg,level = INFO,sender = SENDER_MAIN):
    logs._log(msg,f = sender,level = level)

if __name__ == "__main__":
    log("Hello, XLOGGER!")
    close()
