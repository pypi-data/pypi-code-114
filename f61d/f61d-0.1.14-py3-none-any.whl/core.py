from tqdm import *
from time import sleep
from random import randint,choice
from os import system,urandom
from termcolor import colored
import f61d.LOGO as LOGO
from f61d.__version__ import *


__version__ == __VERSION__
print(colored(LOGO.randlogo(),choice(['red','yellow','green'])))
print(colored("Welcome to F61D. Use Help() for help.",'green'))

help_cont = {}
help_cont[0] = 'Help     : See this help page'
help_cont[1] = 'fuckStar : One Button to fuck Satellite'
help_cont[2] = 'lifeGame : Play the Life Game'
help_cont[3] = 'paint    : Draw a Bing Dwen Dwen'
help_cont[4] = 'b64tofile: Decode base64 to a file'
help_cont[5] = 'prove    : Prove your self. Only support:\n                  sha256(XXXX + abcdef) = aaabbb...'
help_cont[6] = 'Nim      : An interesting turtle game.'
help_cont[7] = 'getLogo  : Print the "F61D" LOGO.'
help_cont[8] - 'yinyang  : Draw the TaiJi.'


def Help(page=1,lines = 5):
    maxPage = int((0.5+len(help_cont))/lines)+1
    if (page - 1) * lines >= len(help_cont):
        print(f'Page Error, check the number : [{1},{maxPage}]')
        return
    print(f"{'=-'*14}= H E L P {'=-'*14}=\n")
    for i in range(lines):
        try:
            n = i+lines*(page-1)
            ll = colored(f"{help_cont[n]}",'green')
            print(f'   {n} - '+ll)
        except:break
    print(f"\n{'=-'*14} page({page}/{maxPage}) {'-='*14}")
    if page < maxPage:print(colored(f'\t\t\thelp({page+1}) for next page','green'))


def fuckStar():
    print(' - 欢迎使用一键日卫星功能')
    print(' - 请输入要日的卫星编号(可在官网查询):',end='')
    num = input()
    while num == '':
        num = input('请重新输入：')

    bar = trange(randint(1000,2000))
    for i in bar:
        bar.set_description('Hacking:',hex(urandom(4))[2:])
        for _ in range(66666):
            a = 1
            b = 1
            a,b = b,1
    for i in range(3):
        print('.',end='')
        sleep(0.4)
    if randint(1,100) > 80 or num == 'CHY':
        for i in range(3):
            print(colored('.','green'),end='')
            sleep(0.4)
        print(colored('\n日卫星成功.','green'))    
    else:
        print(colored('\n日卫星失败，请重新尝试','red'))
    
def lifeGame():
    from f61d.lifeGame import game
    game()
    
def paint():
    from f61d.bingdwendwen import draw
    draw()
    
def b64tofile():
    '''
    Encode/Decode a file by Base64
    '''
    menu = '''
please choose mode (1/2):
    - 1. encode
        Base64 encode a file
    - 2. decode
        Base64 decode a file
'''
    mode = input(menu)
    f1 = input('input file name:')
    f2 = input('Output file name:')
    while mode not in ['1','2']:
        mode = input('Please choose mode (1/2):')
    f = open(f1,'rb').read()
    from base64 import b64decode,b64encode
    if mode == '1':
        df = b64decode(f)
    elif mode == '2':
        df = b64encode(f)
    with open(f2,'wb') as ff:
        ff.write(df)


def Nim():
    from f61d.nim import game
    game()


def prove(cont):
    '''
    Only the format is supported
    sha256(XXXX + {a}) = {b}
    '''
    from itertools import product
    import re
    from string import ascii_letters,digits
    from hashlib import sha256

    
    cont = cont.replace(' ','')
    #print(cont)
    p = re.compile('sha256(.*?)=(.*)')
    #print(p.findall(cont)[0])
    r = p.findall(cont)[0]
    L = len(r[0].split('+')[0])-1
    a = r[0].split('+')[1][:-1]
    b = r[1]
    print(f"Proving:\n\tsha256({'X'*L} + {a}) = {b}\n")
    s = list(product(ascii_letters+digits,repeat=L))
    bar = tqdm(s)
    ss = lambda d:sha256(d.encode()).hexdigest()
    for i in bar:
        S = ''.join(i)
        bar.set_description(f"trying: {S}")
        if ss(S+a) == b:
            print('Find ,',S)
            return S

    
def getLogo():
    print(colored(LOGO.randlogo(),choice(['red','yellow','green'])))
    

def yinyang():
    import f61d.yinyang
    f61d.yinyang.main()
    
    
def main():
    help()
    fuckStar()
    #r = prove('sha256(XXX + O3) = a289ace0c0301fba709365606da60acf11d793869a7c76083cef6c1ac6ff1396')
    #print(r)

if __name__ == '__main__':
    main()
