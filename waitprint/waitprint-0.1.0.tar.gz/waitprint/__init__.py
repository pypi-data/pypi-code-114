__version__ = '0.1.0'

import time
import replit

def waitprint(value, timebetween):
  valuelist = ""
  num = 0
  for i in value:
    valuelist += value[num]
    print(valuelist)
    time.sleep(timebetween)
    num += 1
    if num < (len(value)):
      replit.clear()