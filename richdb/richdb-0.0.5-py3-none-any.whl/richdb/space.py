# -*- coding=utf-8 -*-
import os
import yaml
import logging
import re
import copy

from rich.console import Console
from rich.table import Table

from datetime import datetime
from common import common as c 
from functools import wraps
from runlog import log
from pathlib import Path
from threading import Thread, Lock
from vdict import vdict

logging.basicConfig(filename='log.txt', level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

MAX = 65536
FILE_NAME_LEN = len(str(MAX))
print(f"file_name_len is :{FILE_NAME_LEN}" )
DELETED = 0 # 0 not deleted 1 deleted
UPDATED = 0 # 0 no update found 1 updated
lock = Lock()

def smatch(dirname):
    prog =  re.compile('^s\d{%s}.\d{%s}$' %(FILE_NAME_LEN,FILE_NAME_LEN) )
    if prog.search(dirname):
        spaceline = dirname.strip('s').split('.')[0]
        spacerow = dirname.strip('s').split('.')[1]
        if int(spaceline) < FILE_NAME_LEN and int( spacerow)<FILE_NAME_LEN:
            return True
    return False

def dmatch(filename):
    prog =  re.compile('^d\d{%s}$' %FILE_NAME_LEN)
    if prog.search(filename):
        if int( filename.strip('d') ) < FILE_NAME_LEN:
            return True
    return False

def spacedir(i,j):
    return 's'+str(i+1).rjust(FILE_NAME_LEN,'0')+'.'+str(j+1).rjust(FILE_NAME_LEN,'0')

def datafilename(i):
    return 'd'+str(i+1).rjust(FILE_NAME_LEN,'0')

def readdata(filename):
    return { "name":"hello", "path":"/data/d/t/e", "detail":"s00001.00001"}

class Space:
    def __init__(self, sdir=""):
        self.__data =vdict(name='root') 
        self.__all_columns_in_yaml = {} 
        self.__latest_column = None 
        self.__path = Path(sdir)
        self.__dirty ={}

        self.__rows = 0
        self.__lines = 0

        self.init()
        if sdir != "":
            self.load()

    @log
    def init(self):
        pass
        
    @log
    def load(self):

        spath = self.__path
        syml = spath/"space.yaml"
        if not os.path.exists(syml):
            self.__data=[]
            return None

        with open(syml, "r", encoding="utf-8") as f:
            self.__all_columns_in_yaml= yaml.load(f)

        if self.__all_columns_in_yaml is not None and len(self.__all_columns_in_yaml) >0:
            self.__latest_column = self.__all_columns_in_yaml[max(self.__all_columns_in_yaml)] 

        print(f"column is : {self.__latest_column}" )

        space_count =0
        for i in self.__latest_column:
            if self.__latest_column[i] == 'space':
                space_count+=1

        print( self.__path )
        print( spath )
        for i in os.listdir(spath):
            if smatch( i ) and not os.path.isfile(i):
                print( f"space {i.strip('s').split('.')}") 
                k = int( i.strip('s').split('.')[0] )
                l = int( i.strip('s').split('.')[1] )
                s = Space(spath/i)
                self.__data[k][l] = s
            if dmatch( i ) and os.path.isfile(i):
                print( f"data {i.strip('d')}")
                #print(spacedir(i,j)) 

    def __getitem__(self, i):
        return self.__data[i]

    @log
    def __setitem__(self,i,value):
        print( f"i,  {i}")
        with lock:
            his = self.__data[i]
            self.__data[i]=value
            self.__dirty[i] = value

    def getdirty():
        return self.__dirty


    def getData(self):
        print( self.__latest_column)
        #print( self.__data)
        print( self.__dirty)

class Vision:
    def __init__(self, name):
        self.__root = Space()

class Universe:
    def __init__(self):
        self.__location ="" #ip or url for db
        self.__port=""
        self.__username=""
        self.__password=""
        self.__datadir="" #data dir
        self.__v = {'math':Vision("math")} #the vision you fucked by the world or the way you want to fuck the world

    def __getitem__(self, name):
        return self.__v.get(name)
        
    def show(self):
        print(self.__v.keys())

class DB:
    """
    DB() constructor function has only one argument.
    db = DB() current dir
    db = DB("C:/data/")
    """
    DBROOT = "DB314"
    DBSIZE = 16
    STARTDIR = "//"

    def __init__(self, *args, **argv):
        print( args)
        print( argv)
        file = "./" 
        self.__dbdir = None
        self.__db = {'D647':Universe()} 

        self.init()

        self.load()

    def __getitem__(self, name):
        return self.__db.get(name)

    def __setitem__(self, name):
        return None

    #init db info init D647 universe
    @log
    def init(self):
        if self.__dbdir is None:
            self.__dbdir = "./" 
        elif not os.path.exists(self.__dbdir):
            self.__dbdir = "./"

        dbpath =  os.path.join(self.__dbdir, self.DBROOT)
        dbyaml =  self.__dbdir+self.DBROOT +'/db.yaml'

        if not os.path.exists(dbpath): 
            os.mkdir( dbpath )

        if not os.path.exists(dbyaml):
            with open(dbyaml, 'a+', encoding='utf-8') as f:
                f.write( "datetime:" + str(datetime.now()) +'\n' )
                f.write( "    -DBROOT:" + dbpath +'\n') 
                f.write( "    -DBSIZE:" + str(self.DBSIZE) +'\n') 
                f.write( "    -ABSROOT:" + str(self.ABSROOT) +'\n') 

        print( dbyaml ) 
        with open(dbyaml) as f:
            print( yaml.load(f) )

        #for i in range( 2**16):
        #    print( 's'+'{:0>5d}'.format(i))
    #load data in harddisk
    def load(self):
        pass

    def save(self):
        with open(file):
            pass

print('s00001.00001', smatch('s00001.00001'))
print('s000001.00001', smatch('s000001.00001'))
print('sa0001.00001', smatch('sa0001.00001'))
print('s65536.00001', smatch('s65536.00001'))
print('s00001.65536', smatch('s00001.65536'))
print('s65536.65536', smatch('s65536.65536'))

print( dmatch('d00001'))
print( dmatch('d00004444'))
print( dmatch('d0000d'))
print( dmatch('d65536'))

a = Space(".")
b = Space()
print( b )
a[10] = vdict(name = "userinfo", _list = ['username',16,'s00010.00002'] )
a[11] = vdict(name ="userinfo", _list=['username', 16,'s00011.00002'] )

a[10][0] = 'uname'

a[10].print()
a[11].print()

table = Table(title = "userinfo")

a[10][2] = b
a[11][2] = b

b[0] = vdict(name="books", _list=['微积分', 'hello ', '新华社'] )
b[1] = vdict(name="books", _list=['微积分', 'hello ', '新华社'] )

table.add_column("nu", style="cyan", no_wrap=True)
table.add_column("username", style="cyan", no_wrap=True)
table.add_column("age", style="magenta")
table.add_column("books|subspace", justify = "right", style="green")

for i in range(20):
    t = a[i]
    table.add_row(str(i), *[str(i) for i in t])

console = Console()
console.print(table, justify="center")

print( "a[1][2]", a[1][2][0] )
print( "a[10][2]", a[10][2][0] )
#就问你beautiful 不 beautiful
#a[10][2]
#b = Space()
#print(f"a[10] is {a[10]}")
#print(f"a[10][0] is {a[10][0]}")
#a[10][0]='username'
#a[10][1]=16
#a[10][2]='s00010.00001'
#a[10][3]='s00010.00001'
#a[10] = ['username', 16, 's00010.00001']
#print( a[10])
#a.getData()
#c.test()

e = vdict(name="e", _list=[])
f = vdict(name="f", _list=[])
g = vdict(name="", _list=[])
l = vdict()

e.add_column('help', 'str')
e.add_column('info', 'str')
f.add_column('f1', 'str')
f.add_column('f2', 'str')

e.print()
f.print()
g.print()
l.print()
e[0] = 1
e[1] = 2

f[0] = 3
f[1] = 4

print( "e is :")
e.print()

print( "f is :")
f.print()

print( "g is :")
g.print()

print("e[0:1]", e[::-1])

for i in e:
    print( i )

#v = vdict()
#v = {'hello':0, 'kilo':1, 'name':2, 'win':3, 'harddisk':4}
#v[0] = 1
#v[1] = 2
#v[2] = 3
#v[3] = 4
#v[4] = 5

#print( v )

#print('v len is :', len(v) )

#print( v[0])
#print( v[1])
#print( v[2])
#print( v[3])
#print( v[4])

#for i in v:
#    print(i)
