from zhizhen import version
import zipfile
from os import unlink

f = ''
def install(name,author,contact,introduce,version):
    global f
    begin = 'name:'+str(name)+'\nauthor:'+str(author)+'\ncontact:'+str(contact)+'\nintroduce:'+str(introduce)+'\nversion:'+str(version)
    open('SETTING','wb').write(begin.encode('gb2312'))
    f = zipfile.ZipFile(str(name)+'-'+str(version)+'.zes','w',0)
    f.write("SETTING")
    unlink('SETTING')
def pack(library):
    global f
    open('LIBRARY','w').write(library)
    f.write('file.zip')
    f.write('LIBRARY')
    f.close()
    unlink('LIBRARY')
def open(file):
    pass