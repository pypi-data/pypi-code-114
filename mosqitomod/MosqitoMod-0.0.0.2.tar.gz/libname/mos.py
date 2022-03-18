import random
import math
import time
import os
from os.path import exists
import keyboard
import replit

def on_run():
  print('The Mos Module was made by MosqitoTorpedo')

def pause(s):
  time.sleep(s)

def rndint(x,y):
  rand = random.randint(x, y)
  return rand


def read(file):   
  file_exists = exists(file)
  if file_exists == False:
    print('ACTION_FAILED; invalid file name or path; ERR_CODE=1001')
  else:
    rfile = open(file)
    content = rfile.read()
    rfile.close()
    return content

def clear():
  replit.clear()

def edit(file,newContent):
  if not 'mos.py' in file:
    efile = open(file, "w")
    efile.write(newContent)
    efile = open(file)
    content = efile.read()
    efile.close()
    return content
  else:
    print('ACTION_RESTRICTED; can not edit mos.py for risk of damaging module; ERR_CODE=0110')

def errsrch(ERR_CODE):
  if '0110' in ERR_CODE:
    print('Error code 0110 means you tried to edit an undeitable file')
  elif '1001' in ERR_CODE:
    print('Error code 1001 means that you tried to read an invalid file, check the stated file directory and try again')
  elif '4040' in ERR_CODE:
    print('Error code 4040 means that you have tried to use the helpFunc command but entered an invalid funtion; check to make sure you entered the correct funtion and dont include the parenthese or variables')
  elif '8604' in ERR_CODE:
    print('Error code 8604 means that you tried to use the error search funtion but inputed an invalid error code')
  else:
    print('ACTION_FAILED; Invalid ERR_CODE; ERR_CODE=8604')

def help():
  print("""Mos Module Help Page

mos.pause([time_in_seconds]) - Pauses the program for set ammount of time in seconds
        
mos.rndint(x, y) - Generates a random integer (whole number) between x and y; y must be greater that x
        
mos.read(file) - Reads the file inputed; if your file is embeded in folders you must start the path with the first folder until you get to the file you want to read
      
mos.edit(file,new_file_content) - Edits the file with whatever you put; if your file is embeded in folders you must start the path with the first folder until you get to the file you want to edit

mos.errsrch(ERR_CODE) - Show the meaning of the inputed error code
        
mos.help() - shows this list
        
mos.clear() - Clears the console

mos.helpFunc(funtion) - Show a more in depth explination of the inputed function
        
        """)

def helpFunc(func):
  if 'pause' in func:
    print('This pauses the program and prevents anything from happening until the time is up.\nProper usage would be:\nmos.pause(seconds_to_pause)')
  if 'rndint' in func:
    print('This generates a random number between x and y; y must be greater than x, otherwise you will recieve an error\nProper usage would be:\nmos.rndint(x, y)')
  if 'read' in func:
    print("This reads the file that you have inputed; if you have the file inside of a folder you must include the full path to the file in the command\nProper usage would be:\nmos.read('folder/folder/text.txt')")
  if 'edit' in func:
    print("This edit the inputed file to whatever you set it to be; WARNING: USING THIS COMMAND WILL REPLACE ALL PREVIOUS DATA IN THE FILE\nProper usage would be:\nmos.edit('folder/folder/text.txt','example')")
  elif 'errsrch' in func:
    print("This will show you the meaning of the error code you inputed;anytime you recive an error you will see a line that says 'ERR_CODE=xxxx' when using the errsrch command you would put those four digits into the parentheses\nProper usage would be:\nmos.errsrch('ERR_CODE')")
  elif 'help' in func:
    print('This will show a page with all commands and what they do\nProper usage would be:\nmos.help()')
  elif 'helpFunc' in func:
    print("This will show you a more indepth help result to than the help page\nProper usage would be\nmos.helpFunc('funtion')")
  elif 'clear' in func:
    print('This will clear the console\nProper usage would be:\nmos.clear()')
  elif 'errsrch' in func:
    print("This will allow you to search the error codes that you recieve when using the Mos Module\nProper usage would be:\nmos.errsrch('error code')")
  else:
    print('ACTION_FAILED; invalid funtion; ERR_CODE=4040')