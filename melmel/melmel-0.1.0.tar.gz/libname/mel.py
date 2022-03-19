import random
import math
import time
import os
import datetime
import colorama
from colorama import Fore, Back, Style


def on_run():
  print('mel.py was made by Melonpod using replit\n')

def melhelp():
  print('Functions;')
  y = help1()
  for x in y:
    print(x)

def help1():
  fileEdit = ' - "fileEdit"\n    | replaces what is in the specified file with the text you provide\n'
  helpFunc = ' - "helpFunc"\n    | gives you informaiton on the specified function\n'
  clearConsole = ' - "clearConsole"\n   | clears the console\n'
  game = ' - "Game"\n   | plays a game in the console with little comstimzation\n where all you can do is move around\n'
  wait = ' - "wait"\n   | waits the set amount of ticks (20 ticks = 1 second)\n'
  rand = ' - "rand"\n    | returns a random whole number between the two inputs "a" and "to_b"\n'
  file = ' - "file"\n    | returns the name and location\n'
  split = ' - "split"\n    | splits the inputed text into separate letters and prints them on the console. I am trying to get it to return the splited values\n'
  nput = ' - "nput"\n    | retrves the most recent user input from the console. "mel.nput('')" you can put text into the parenthisess and it will print the text and only detect the input that comes directly after that text\n'

  return helpFunc, clearConsole, wait, game, fileEdit, nput, split, file, rand

def helpFunc(function): 
  fun = help1()
  for x in fun:
    if x == 'help':
      print('explains how all functions work')
    else:
      if str(function) in x:
        print('')
        print(x)
        return 
  print('\n"'+function+'" is not a valid function, make sure you have the correct spelling and capitalization')
      
def clearConsole():
  #clears the console
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
    os.system(command)

def repeat(until,code):
  while until:
    exec(code)

def game(player):
  print('press "enter" to start the \'Game\'')
  loop = 0
  posX = 0
  posY = 0
  timesRun = 0
  debug = False
  while loop == 0:
    put = input()
    if 'd' in put:
        posX = posX + 1
    else:
        if 'a' in put:
            posX = posX - 1
        else:
            if 'w' in put:
                posY = posY + 1
            else:
                if 's' in put:
                    posY = posY - 1
                else:
                  if put == 'q':
                    clearConsole()
                    return
                  else:
                    if put == 'f3':
                      if debug == True:
                        debug = False
                      else:
                        if debug == False:
                          debug = True                            
    
    if posY > 16:
        posY = 16
    if posY < 0:
        posY = 0
    if posX < 0:
        posX = 0
    if posX > (13 - math.ceil(int((len(player)) / 3))):
        posX = int(13 - math.ceil(int((len(player)) / 3)))
    
    clearConsole()
    #debug screen
    if debug == True:
        print('X: ' + str(posX) + ' Y: ' + str(posY))
        print('player icon (' + player + ')')
        print('player length:',len(player))
        print('times input ran:',timesRun)
        print('Current running file name:',__file__,'')
        print('positon single intiger code:',(posX * 100) + (posY))
    #debug screen end
    print('I========================================I')
    if posY < 16:
        times = 15 - posY
        while times > 0 :
            print('I                                        I')
            times = times - 1
    if posY < 16:
        print('I                                        I')
    print('I' + ' ' * (3 * posX) + player + ' ' * ((3 * (13 - posX)) - (len(player) - 1)) + 'I')
    if posY > 0:
        times = posY - 1
        while times > 0:
            print('I                                        I')
            times = times - 1
    if posY > 0:
        print('I                                        I')
    print('I========================================I')
    time.sleep(0.1)
    timesRun = timesRun + 1



def wait(ticks):
  time.sleep(ticks / 20)

def rand(a,to_b):
  return random.randint(a,to_b)
  
class split:
  def lines(str):
		return str.splitlines()
		
  def char(str):
    text = []
    for i in str:
      text.append(i)
      return text
			

def nput(text_potinal=''):
  return input(text_potinal)

class file:
  def get():
    return __file__

	
  def edit(file,what_in_file):
    if not 'mel.py' in file:
      my_file = open(file, "w")
      my_file.write(what_in_file)
      my_file = open(file)
      content = my_file.read()
      my_file.close()
      return content
    else:
      print('Error; you can not edit mel.py because of risk of breaking module')

  def read(file):
    my_file = open(file)
    content = my_file.read()
    my_file.close()
    return content



class credit:
	def __init__(self):
		print("""
Credits:
	Main Coders:
		Melonpod
	
	Modules:
		random
		math
		time
		os
		keyboard
		datetime
		colorama
					""")



class color:
	def reset():
		print(Style.RESET_ALL)
		print ("\033[A\033[A")
	
	def dim():
		print(Style.DIM)
		print ("\033[A\033[A")
		
	def red():
		print(Fore.RED)
		print ("\033[A\033[A")

	def blue():
		print(Fore.BLUE)
		print ("\033[A\033[A")

	def green():
		print(Fore.GREEN)
		print ("\033[A\033[A")

	def yellow():
		print(Fore.YELLOW)
		print ("\033[A\033[A")

	def magenta():
		print(Fore.MAGENTA)
		print ("\033[A\033[A")

	def black():
		print(Fore.BLACK)
		print ("\033[A\033[A")
	
	def white():
		print(Fore.WHITE)
		print ("\033[A\033[A")
	
	def cyan():
		print(Fore.CYAN)
		print ("\033[A\033[A")
	
	
		
	class back:
		def red():
			print(Back.RED)
			print ("\033[A\033[A")

		def blue():
			print(Back.BLUE)
			print ("\033[A\033[A")

		def green():
			print(Back.GREEN)
			print ("\033[A\033[A")

		def yellow():
			print(Back.YELLOW)
			print ("\033[A\033[A")

		def magenta():
			print(Back.MAGENTA)
			print ("\033[A\033[A")

		def black():
			print(Back.BLACK)
			print ("\033[A\033[A")
	
		def white():
			print(Back.WHITE)
			print ("\033[A\033[A")
	
		def cyan():
			print(Back.CYAN)
			print ("\033[A\033[A")


class lem:
	def compress(curfile,to):
                print('This Function is currently undinished and the way files get compressed WILL change as this gets developed')
		if to.endswith('.lem'):
			if curfile.endswith('.py'):
				com = '{LANG="Python"}'
			code = file.read(curfile).splitlines()
			for i in code:
				if '#' in i or i == '':
					pass
				else:
					if 'print' in i:
						i = i.replace('print','Ⓟ℃ж')
					else:
						if 'import ' in i:
							i = i.replace('import ','☢☏♫')
					com += '\n' + i

			file.edit(to,com)
			color.green()
			print(f'ERROR: file "{curfile}" has been sucsseccefuly compressed into {to}')
			color.reset()
			
		else:
			color.red()
			print('ERROR: you can only compess files into a ".lem" file')
			color.reset()
	def expand(curfile,to):
		if curfile.endswith('.lem'):
			code = file.read(curfile).splitlines()
			if code[0] == '{LANG="Python"}' and not to.endswith('.py'):
				color.red()
				print('ERROR: you can only expand a python file into a ".py" file')
				color.reset()
				return
			exp = ''
			for i in code:
				if i == '{LANG="Python"}':
					pass
				else:
					if 'Ⓟ℃ж' in i:
						i = i.replace('Ⓟ℃ж','print')
					else:
						if '☢☏♫' in i:
							i = i.replace('☢☏♫','import ')
					exp += '\n' + i

			file.edit(to,exp)
				
			color.green()
			print(f'SUCCSESS: file "{curfile}" has been sucsseccefuly expanded into {to}')
			color.reset()
				

class mel:
	def config():
		#opens a config menu in the console
		#menu
		length = 40

		content = []
		if content == []:
			content.append('No config appends found')
		
		print('|'+'='*(length - 2) + '|')
		for i in range(len(content)):
			print('|' + content[i] + ' ' * ((length - 2) - len(content[i])) + '|')
		
		print('|'+'='*(length - 2) + '|')




class inner:
	def error(message):
		color.red()
		print('ERROR:',message)
		color.reset()
	def succ(message):
		color.green()
		print('SUCCESS: '+message)
		color.reset()
