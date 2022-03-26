from zhizhen import version as Version
import zipfile
from os import unlink
from os.path import isfile

f = ''
def Install(name,author,email,introduce,version,icon,library):
    if isfile(icon):
        name_ = ('name:'+str(name)+'\n').encode('GB18030')
        author_ = ('author:'+str(author)+'\n').encode('utf-16le')
        email_ = ('email:'+str(email)+'\n').encode('utf-8')
        introduce_ = ('introduce:'+str(introduce)+'\n').encode('utf-16be')
        version_ = ('version:'+str(version)+'\n').encode('GB18030')
        icon_ = ('icon:ICONPATH\n').encode('GBK')
        Version_ = str(Version).encode('utf-16be')
        open('SETTING','wb').write(name_+author_+email_+introduce_+version_+icon_+Version_)
        icon_r = open(icon,'rb').read()
        open('ICONPATH','wb').write(icon_r)
        open('LIBRARY','w').write(library)
        f = zipfile.ZipFile(str(name)+'-'+str(version)+'.zes','w',0)
        f.write("SETTING")
        unlink('SETTING')
        f.write("ICONPATH")
        unlink('ICONPATH')
        f.write("LIBRARY")
        unlink('LIBRARY')
        f.write('file.zip','FILE')
    else:
        raise SystemExit('Error:Icon file does not exist')