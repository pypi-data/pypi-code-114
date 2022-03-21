from json import dumps,loads
from .authorize import getAccessToken
from .others import *
from myHttp import http
from .exceptions import *


'''
需要功能:
    1. 删除 (文件和文件夹) =
    2. 新建文件夹 =
    3. 复制   必须添加目标文件名或文件夹名 =
    4. 移动   必须添加目标文件名或文件夹名 =
    5. 查看文件夹内容 =
    6. 下载文件 =
    7. 上传
    8. 重命名   只能通过移动实现 =
    9. 下载文件夹 =
'''

POST='POST'

'''
返回值:
-1 ~ -8: 同 myHttp
-9: 登陆无效
-2x: 文件(夹)名不合法
-10: 文件(夹)不存在
-15: 类型错误（e.g. ls 传入文件, download 传入文件夹)
-11 ~ -13: 命名冲突: -11: 与末端文件名相同, -12: 与文件夹名相同, -13: 与前面的文件名相同
-18: 复制或移动时 source 包含 target
-25: 读取本地文件失败
10: 写入文件失败
'''


def ls(folder:str):
    # -20: 文件名不合法, -15: 是文件, -10: 文件夹不存在
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(folder)==0 or folder[0]!='/'):
        raise InputError('Folder name must start with "/".')
    if(folder=='/'):
        folder=''
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'path':folder}
    body=dumps(body)
    url='https://api.dropboxapi.com/2/files/list_folder'
    r=http(url,Method=POST,Header=header,Body=body)
    # print(r)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']!=200):
        if(str(r['text']).find('malformed_path')>=0):
            return -20 # 文件夹名非法
        if(r['text']['error']['path']['.tag']=='not_found'):
            return -10 # 文件夹不存在
        return -15 # 是文件
    result={}
    for i in r['text']['entries']:
        result[i['name']]=i['.tag']
    return result
    
    




def mkdir(path:str):
    # 前面不存在的所有文件夹都会被创建
    # -11: 与末端文件名相同, -12: 与文件夹名相同, -13: 与前面的文件名相同, -20: 文件名不合法
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(path)<=1 or path[0]!='/' or path[-1]=='/'):
        raise InputError('Folder name must start with "/", can\'t end with "/", and root folder is not supported.')
    url='https://api.dropboxapi.com/2/files/create_folder_v2'
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'path':path}
    body=dumps(body)
    r=http(url,Method=POST,Header=header,Body=body)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']==200):
        return 0
    if(str(r['text']).find('malformed_path')>=0):
        return -20
    tag=r['text']['error']['path']['conflict']['.tag']
    dic={'file':-11,'folder':-12,'file_ancestor':-13}
    return dic[tag]



def rm(target:str):
    # -10: 不存在, -20: 文件夹名不合法
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(target)<=1 or target[0]!='/' or target[-1]=='/'):
        raise InputError('Folder of file name must start with "/", can\'t end with "/", and root folder is not supported.')
    url='https://api.dropboxapi.com/2/files/delete_v2'
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'path':target}
    body=dumps(body)
    r=http(url,Method=POST,Header=header,Body=body)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']==200):
        return 0
    if(str(r['text']).find('malformed_path')>=0):
        return -20
    return -10
    

def cp(source:str,target:str):
    # 必须添加目标文件名或文件夹名
    # -21: source 格式不合法, -22: target 格式不合法
    # -10: 不存在, -11: 与末端文件名相同, -12: 与文件夹名相同, -13: 与前面的文件名相同 -18: source 包含 target
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(target)<=1 or target[0]!='/' or target[-1]=='/'):
        raise InputError('Folder or file name must start with "/", can\'t end with "/", and root folder is not supported.')
    if(len(source)<=1 or source[0]!='/' or source[-1]=='/'):
        raise InputError('Folder or file name must start with "/", can\'t end with "/", and root folder is not supported.')
    if(source==target):
        raise InputError('Souce and target can\'t be the same.')
    url='https://api.dropboxapi.com/2/files/copy_v2'
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'from_path':source,'to_path':target}
    body=dumps(body)
    r=http(url,Method=POST,Header=header,Body=body)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']==200):
        return 0
    if(str(r['text']).find('malformed_path')>=0):
        if(str(r['text']).find('from_lookup')>=0):
            return -21
        return -22
    if(str(r['text']).find('not_found')>=0):
        return -10
    if(str(r['text']).find('duplicated_or_nested_paths')>=0):
        return -18
    tag=r['text']['error']['to']['conflict']['.tag']
    dic={'file':-11,'folder':-12,'file_ancestor':-13}
    return dic[tag]




def mv(source:str,target:str):
    # 必须添加目标文件名或文件夹名
    # -21: source 格式不合法, -22: target 格式不合法
    # -10: 不存在, -11: 与末端文件名相同, -12: 与文件夹名相同, -13: 与前面的文件名相同, -18: source 包含 target
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(target)<=1 or target[0]!='/' or target[-1]=='/'):
        raise InputError('Folder or file name must start with "/", can\'t end with "/", and root folder is not supported.')
    if(len(source)<=1 or source[0]!='/' or source[-1]=='/'):
        raise InputError('Folder or file name must start with "/", can\'t end with "/", and root folder is not supported.')
    if(source==target):
        raise InputError('Souce and target can\'t be the same.')
    url='https://api.dropboxapi.com/2/files/move_v2'
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'from_path':source,'to_path':target}
    body=dumps(body)
    r=http(url,Method=POST,Header=header,Body=body)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']==200):
        return 0
    if(str(r['text']).find('malformed_path')>=0):
        if(str(r['text']).find('from_lookup')>=0):
            return -21
        return -22
    if(str(r['text']).find('not_found')>=0):
        return -10
    if(str(r['text']).find('duplicated_or_nested_paths')>=0):
        return -18
    tag=r['text']['error']['to']['conflict']['.tag']
    dic={'file':-11,'folder':-12,'file_ancestor':-13}
    return dic[tag]




def rename(prev:str,new:str):
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(new==''):
        raise InputError('The length of new name must be larger than 0.')
    if(new.find('/')>=0):
        raise InputError('New name can\'t contain "/".')
    if(len(prev)<=1 or prev[0]!='/' or prev[-1]=='/'):
        raise InputError('Folder or file name must start with "/", can\'t end with "/", and root folder is not supported.')
    loc=prev.rfind('/')
    if(prev[loc+1:]==new):
        raise InputError('The previous name can\'t be same with new name.')
    newPath=prev[:loc+1]+new
    return mv(prev,newPath)




def download(path:str,LocalPath=None):
    # LocalPath 为 None 时, 返回二进制字符串, 为 True 时写入文件, 如果文件写入失败, 则返回二进制字符串
    # 返回值: [status, content]
    # -15: 是文件夹, -10: 不存在, -20: 文件名格式不合法, 10: 写入文件失败
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return [access_token,None]
    if(len(path)<=1 or path[0]!='/' or path[-1]=='/'):
        raise InputError('File name must start with "/", can\'t end with "/", and root folder is not supported.')
    url='https://content.dropboxapi.com/2/files/download'
    header={
        'Authorization':'Bearer '+access_token,
        'Dropbox-API-Arg':dumps({'path':path})
    }
    r=http(url,Method=POST,Header=header,Retry=False,Decode=False)
    #print(r)
    if(r['status']<=-1):
        return [r['status'],None]
    if(r['code']==401):
        return [-9,None]
    if(r['code']!=200):
        if(str(r['text']).find('malformed_path')>=0):
            return [-20,None]
        if(str(r['text']).find('not_found')>=0):
            return [-10,None]
        return [-15,None]
    # 以下是成功的情况
    if(LocalPath==None):
        return [0,r['text']]
    try:
        f=open(LocalPath,'wb')
        f.write(r['text'])
        f.close()
    except:
        return [10,r['text']]
    return [0,None]



def downloadFolder(path,localPath):
    # 返回值: [status, content], 写入文件失败时 content 为二进制字符串, 写入成功时为 None
    # -15: 是文件夹, -10: 不存在, -20: 文件夹名格式不合法, 10: 写入文件失败
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return [access_token,None]
    if(len(path)<=1 or path[0]!='/'):
        raise InputError('Folder name must start with "/" and root folder is not supported.')
    url='https://content.dropboxapi.com/2/files/download_zip'
    header={
        'Authorization':'Bearer '+access_token,
        'Dropbox-API-Arg':dumps({'path':path})
    }
    r=http(url,Method=POST,Header=header,Retry=False,Decode=False)
    # print(r)
    if(r['status']<=-1):
        return [r['status'],None]
    if(r['code']==401):
        return [-9,None]
    if(r['code']!=200):
        if(str(r['text']).find('Invalid path: INVALID_PATH')>=0):
            return [-20,None]
        if(str(r['text']).find('not_found')>=0):
            return [-10,None]
        return [-15,None]
    try:
        f=open(localPath,'wb')
        f.write(r['text'])
        f.close()
    except:
        return [10,r['text']]
    return [0,None]



def upload(path:str,file,Timeout=1000):
    # Timeout 单位为 s
    # file 为本地文件路径(字符串)或二进制字符串
    # 如果是二进制字符串, 直接上传, 如果是本地文件路径, 打开读取内容后上传
    # -30: 读取文件失败, -20: 文件名格式不合法
    if(type(file)!=type('') and type(file)!=type(b'')):
        raise InputError('The parameter file must be str or bytes.')
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(path)<=1 or path[0]!='/' or path[-1]=='/'):
        raise InputError('File name must start with "/", can\'t end with "/", and root folder is not supported.')
    if(type(file)==type('')):
        try:
            f=open(file,'rb')
            text=f.read()
            f.close()
        except:
            return -25
        file=text
    url='https://content.dropboxapi.com/2/files/upload'
    header={
        'Authorization':'Bearer '+access_token,
        'Dropbox-API-Arg':dumps({'path':path}),
        'Content-Type':'application/octet-stream'
    }
    timeout=1000*Timeout
    r=http(url,Method=POST,Header=header,Retry=False,Decode=False,Body=file,Timeout=timeout)
    # print(r)
    if(r['status']<=-1):
        return [r['status'],None]
    if(r['code']==401):
        return [-9,None]
    if(r['code']==200):
        return 0
    if(str(r['text']).find('malformed_path')>=0):
        return -20
    s=r['text'].decode('utf-8')
    s=loads(s)
    tag=s['error']['reason']['conflict']['.tag']
    dic={'file':-11,'folder':-12,'file_ancestor':-13}
    return dic[tag]


def ls_l(folder:str):
    # -20: 文件名不合法, -15: 是文件, -10: 文件夹不存在
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(folder)==0 or folder[0]!='/'):
        raise InputError('Folder name must start with "/".')
    if(folder=='/'):
        folder=''
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    body={'path':folder}
    body=dumps(body)
    url='https://api.dropboxapi.com/2/files/list_folder'
    r=http(url,Method=POST,Header=header,Body=body)
    # print(dumps(r['text']))
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']!=200):
        if(str(r['text']).find('malformed_path')>=0):
            return -20 # 文件夹名非法
        if(r['text']['error']['path']['.tag']=='not_found'):
            return -10 # 文件夹不存在
        return -15 # 是文件
    result={}
    for i in r['text']['entries']:
        if(i['.tag']=='folder'):
            result[i['name']]=[]
        else:
            result[i['name']]=[i['size'],toUnix(i['client_modified']),toUnix(i['server_modified'])]
    return result



def getFileProperty(file:str):
    # -20: 文件名不合法, -15: 是文件夹, -10: 文件夹不存在
    access_token=getAccessToken()
    if(type(access_token)==type(0)):
        return access_token
    if(len(file)<=1 or file[0]!='/' or file[-1]=='/'):
        raise InputError('Folder name must start with "/", can\'t end with "/", and root folder is not supported.')
    header={
        'Content-Type':'application/json',
        'Authorization':'Bearer '+access_token
    }
    url='https://api.dropboxapi.com/2/files/get_metadata'
    body={'path':file}
    body=dumps(body)
    r=http(url,Method=POST,Header=header,Body=body)
    if(r['status']<=-1):
        return r['status']
    if(r['code']==401):
        return -9
    if(r['code']!=200):
        if(str(r['text']).find('not_found')>=0):
            return -10
        return -20
    if(r['text']['.tag']!='file'):
        return -15
    return [r['text']['size'],toUnix(r['text']['client_modified']),toUnix(r['text']['server_modified'])]

def search():
    pass



