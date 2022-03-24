#coding=utf-8

import time
import sys
import datetime
from razo.langpack import pack

rooting=False
sudoroot=False
nowsudo=False
try:
    if sys.argv[1]=='-root':
        rooting=True
except IndexError as inddde:
    rooting=False
liense=pack[0]
def setting():
    print(pack[1])
    print(liense)
    a=input(pack[2])
    if a=='n':
        print(pack[3])
        time.sleep(5)
        sys.exit(0)
    with open('settings.py','w') as c:
        c.write('#coding=utf-8\n')
    a=input(pack[4])
    with open('settings.py','a') as c:
        c.write("rootpass={}\n".format(a.encode()))
    a=input(pack[5])
    with open('settings.py','a') as c:
        c.write("username='{}'\n".format(a))
    
def showinfo():
    listget=pack[13]
    timer=datetime.datetime.now()
    weekday=listget[timer.weekday()]
    print(timer.strftime(pack[14])+' {}'.format(weekday) )
    tdo=[]
    try:
        with open('razo_ver.txt') as res:
            a=res.read().split(' ')
    except FileNotFoundError as ee:
        with open('razo_ver.txt','w') as res:
            res.write('2022.55.0.0b3 tkinter_6b3')
    print('Razo {0}({1}).'.format(a[0],a[1]))
    print(pack[6])
    print(pack[7])


h=pack[8]




try:
    import settings
    d=settings.rootpass
    username=settings.username
except ImportError as e:
    setting()
    
def sc():
    global sudoroot
    if not sudoroot:
        a=input(pack[9])
        import settings
        if a==settings.rootpass.decode():
            sudoroot=True
            return True
        else:
            print(pack[18])
            return False
    else:
        return True
    
def wai(a):
    global rooting
    global sudoroot
    global nowsudo
    if a=='help':
        print(h)
    elif a=='su':
        a=input(pack[9])
        import settings
        if a==settings.rootpass.decode():
            rooting=True
        else:
            time.sleep(2)
            print(pack[10])
    elif a=='shutdown':
        if rooting:
            yes=input(pack[11])
            if yes=='y':
                print(pack[12])
                time.sleep(5)
                sys.exit(0)
        else:
            print(pack[15])
    elif a=='info':
        showinfo()
    elif a=='setting':
        if rooting:
            setting()
            rooting=False
        else:
            print(pack[15])
    elif a=='time':
        listget=pack[13]
        timer=datetime.datetime.now()
        weekday=listget[timer.weekday()]
        print(timer.strftime(pack[14])+' {}'.format(weekday) )
        #The line between usually and sudo.
    elif a=='sudo help':
        if sc():
            nowsudo=True
        print(h)
        nowsudo=False
    elif a=='sudo su':
        if sc():
            nowsudo=True
        a=input('Please enter root password:')
        import settings
        if a==settings.rootpass:
            rooting=True
        else:
            time.sleep(2)
            print('su:Sorry')
        nowsudo=False
    elif a=='sudo shutdown':
        if sc():
            nowsudo=True
        if nowsudo:
            yes=input(pack[11])
            if yes=='y':
                print(pack[12])
                time.sleep(5)
                sys.exit(0)
        else:
            print(pack[15])
    elif a=='sudo info':
        if sc():
            nowsudo=True
        showinfo()
        nowsudo=False
    elif a=='sudo setting':
        if sc():
            nowsudo=True
        if nowsudo:
            setting()
            rooting=False
            sudoroot=False
            nowsudo=False
        else:
            print(pack[15])
    elif a=='sudo time':
        if sc():
            nowsudo=True
        listget=pack[13]
        timer=datetime.datetime.now()
        weekday=listget[timer.weekday()]
        print(timer.strftime(pack[14])+' {}'.format(weekday) )
        nowsudo=False
    else:
        try:
            exec('import '+a)
        except (ImportError,SyntaxError) as exc:
            try:
                if sc():
                    nowsudo=True
                exec('import '+a[5:])
                nowsudo=False
            except (ImportError,SyntaxError) as exc:
                print(pack[16].format(a))
    

showinfo()
time.sleep(2)
import settings
print(pack[17].format(settings.username))

while True:
    if rooting:
        a=input('[root]>>>')
    else:
        a=input('[user]>>>')
    wai(a)
