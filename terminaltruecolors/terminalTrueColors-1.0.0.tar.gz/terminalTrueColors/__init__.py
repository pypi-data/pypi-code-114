from colorsys import hls_to_rgb
from pyfiglet import figlet_format
from sys import stdout


class rgb:
	def __init__(self, r,g,b):
		self.r = r
		self.g = g
		self.b = b
	def __str__(self):
		return "\x1b[38;2;{0};{1};{2}m██rgb({0},{1},{2})\x1b[0m".format(self.r, self.g, self.b) 
	def __getitem__(self, key):
		return [self.r, self.g, self.b][key]

class hsl:
	def __init__(self, h,s,l):
		self.h = h
		self.s = s
		self.l = l
	def __str__(self):
		ret = hls_to_rgb(self.h/360, self.l/100, self.s/100)
		return "\x1b[38;2;{0};{1};{2}m██hsl({3},{4},{5})\x1b[0m".format(round(ret[0]*255), round(ret[1]*255), round(ret[2]*255), self.h, self.s, self.l)
	def __getitem__(self, key):
		return [self.h, self.s, self.l][key]
	def rgb(self):
		ret = hls_to_rgb(self.h/360, self.l/100, self.s/100)
		return rgb(round(ret[0]*255), round(ret[1]*255), round(ret[2]*255))


def cadd(color, value):
	end = "\x1b[0m"
	if isinstance(color, rgb):
		code = "\x1b[38;2;{};{};{}m".format(color.r, color.g, color.b)
		
	elif isinstance(color, hsl):
		ret = hls_to_rgb(color.h/360, color.l/100, color.s/100)
		code = "\x1b[38;2;{0};{1};{2}m".format(round(ret[0]*255), round(ret[1]*255), round(ret[2]*255))
	
	else:
		raise Exception('ClassError: Unacceptable color class, please use rgb or hsl class')

	return code + value + end

def cprint(color, value, end="\n"):
	
	print(cadd(color, value), end=end)
	stdout.flush()

def cgradprint(c,c2,value,end='\n'):

	if not((isinstance(c, rgb) or isinstance(c2, rgb)) or  (isinstance(c, hsl) or isinstance(c2, hsl))):
		raise Exception('ClassError: Unacceptable color class, please use rgb or hsl class')

	lenght = len(value)
	diff0 = c2[0] - c[0]
	diff1 = c2[1] - c[1]
	diff2 = c2[2] - c[2]

	if isinstance(c, hsl) and isinstance(c2, hsl):
		
		for i in range(lenght):
			tempColor = hsl(
				round((i*(diff0/(lenght-1)))+c.h),  
				round((i*(diff1/(lenght-1)))+c.s),   
				round((i*(diff2/(lenght-1)))+c.l)
			)
			cprint(tempColor, value[i], end='')

	elif isinstance(c, rgb) and isinstance(c2, rgb):
		for i in range(lenght):
			tempColor = rgb(
				round((i*(diff0/(lenght-1)))+c.r),  
				round((i*(diff1/(lenght-1)))+c.g),   
				round((i*(diff2/(lenght-1)))+c.b)
			)
			cprint(tempColor, value[i], end='')
	else:
		raise Exception('IncompatibleCLasses: Please use either rgb or hsl, not both')
	
	print("",end=end)
		
def divider(value, porcentage):
	
	lenght = list(get_terminal_size())[0]
	ret=""
	for i in range(round((lenght*porcentage)/100)):
		ret+=value
	return ret

def csys(color, symbol, message="", end='\n'):
	print(cadd(color,symbol+" ") + message, end=end)
	stdout.flush()

def banner(text,tab='    ',font='big',minus=-2):
	banner = figlet_format(text,font=font)
	val=""
	total=[]
	for i in banner:
		val+=i
		if i =="\n":
			total.append(val)
			val=""
	val=""
	for i in total[:minus]:
		val += (tab+i)
	return val[:-1]

def header(colorPallete, divider, banner, author, version, name):

	val=""
	total=[]
	for i in banner:
		val+=i
		if i =="\n":
			total.append(val)
			val=""
	ret=""
	for i in range(len(total[0])+6):
		ret+=divider



	print("")
	print(ret) 

	cgradprint(colorPallete[0], colorPallete[1], banner)


	cprint(colorPallete[2],"      [→] ",end='')
	print("Coded by ", end='')
	cprint(colorPallete[3], author)

	cprint(colorPallete[2],"      [→] ",end='')
	print("Version ", end='')
	cprint(colorPallete[4], str(version))

	csys(colorPallete[2], "      [→]", name)
	print(ret)
	print("")
	

symbols = ["[+]", "[x]", "[~]", "[¬]", "[-]", "[=]", "[≡]", "[!]", "[?]", "[→]", "[<]", "[>]", "[OK]"]
types = ["─", "═","░", "▒", "▓", "█", "-",  "=",  "≡",  "≡", "¯", "#"]
colors={
	"red":hsl(0.0, 100, 50),
	"orange":hsl(22.5, 100, 50),
	"yellow":hsl(60, 100, 50),
	"lightGreen":hsl(90, 100, 50),
	"green":hsl(120, 100, 50),
	"darkGreen":hsl(120, 100, 25),
	"lightBlue":hsl(180, 100, 50),
	"blue":hsl(210, 100, 50),
	"darkBlue":hsl(240, 100, 50),
	"purple":hsl(270, 100, 50),
	"pink":hsl(315, 100, 50),
	"black":hsl(0, 0, 0),
	"darkGrey":hsl(0, 0, 25),
	"grey":hsl(0, 0, 50),
	"lightGrey":hsl(0, 0, 75),
	"white":hsl(0, 0, 100),	
}

def main():

	from os import get_terminal_size

	colorPallete = [
		colors["red"],
		colors["purple"],
		colors["orange"],
		colors["orange"],
		colors["orange"]
	]

	header(colorPallete, "─", banner("TTS",minus=-2), "Azcué", 1.0, "Terminal True Colors")
	print(rgb(203,228,165))
	print(hsl(84,54,77))
	print()
	

	cprint(colors["blue"], "Este texto es azul - ", end='')
	cprint(colors["darkBlue"], "Este texto es azul fuerte")
	print()


	consoleWidth = list(get_terminal_size())[0]

	for i in range(consoleWidth):
		color = hsl(i*(360/consoleWidth),100,50)
		cprint(color, "-", end='')
	print("")


	value = "This is printed in rainbows"
	lenght = len(value)

	for i in range(lenght):
		color = hsl(i*(360/lenght),100,50)
		cprint(color, value[i], end='')
	print("")



	print()
	for key in colors.keys():
		cprint(colors[key], "██"+ key )

	print()
	for i in range(361):
		cprint(hsl(i,100,50), "█"+ str(i), end='')
	print();print()
"""
	while True:
		value =""
		for i in range(list(get_terminal_size())[0]):
			value+="█"
		color = hsl(round((cos(time())+1)*180),100,50)
		cprint(color, value)
"""



if __name__ == '__main__':
	main()

	
