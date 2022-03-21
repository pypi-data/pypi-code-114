from myHttp import http
from mySecrets import *
import os
from .others import *
from time import sleep
from _thread import start_new_thread
import platform

LOGIN_URL='https://www.dropbox.com/oauth2/authorize?client_id=vikgbifjv4zi29n&token_access_type=offline&response_type=code'
POST='POST'
GET='GET'
LOGIN_AUTHORIZATION='Basic dmlrZ2JpZmp2NHppMjluOnhrY3IzN3gycnlwYjhiYg=='
TOKEN_URL='https://api.dropbox.com/oauth2/token'
TOKEN_HEADER={
    'Content-Type':'application/x-www-form-urlencoded',
    'Authorization':LOGIN_AUTHORIZATION
}
FILE_NAME='.refresh_token_dropbox_jtc_mxTIPBpWbIxrLvZr5CCYpRwfY7DLrQRTxYlxxBWWrg3.txt'
PD2='ejBBcjkRe6kUdmhzd6gMcPwMpCkVcjoNoCcUdP9Cd3gVpm4Mc69AczwQcCcOdSpAozwUp30Mp6pxcSpCpmoVd='


lastRefreshTime=0
access_token=''
password=''
refresh_token=''
isValid=False
path=os.path.expanduser('~')
isWindows=((platform.platform().find('indows'))>=0)
slash={True:'\\',False:'/'}


def getAccessToken():
    if(isValid==False):
        return -9
    cnt=0
    while(isValid==True and access_token=='' and cnt<500):
        cnt=cnt+1
        sleep(0.02)
    if(access_token=='' and isValid==False):
        return -9
    if(access_token=='' and isValid==True):
        return -1
    return access_token



def getTokenByAuthorizationCode(authorization_code:str):
    # 失败: 400, 成功: 200
    body='code='+authorization_code+'&grant_type=authorization_code'
    r=http(TOKEN_URL,Method=POST,Header=TOKEN_HEADER,Body=body)
    return r

def getTokenByRefreshToken(refresh_token:str):
    # 失败: 400, 成功: 200
    body='refresh_token='+refresh_token+'&grant_type=refresh_token'
    r=http(TOKEN_URL,Method=POST,Header=TOKEN_HEADER,Body=body)
    return r





def keep():
    global isValid,access_token,lastRefreshTime
    while True:
        if(isValid==False or refresh_token=='' or getTime()-lastRefreshTime<=2*60*60*1000):
            sleep(1)
            continue
        r=getTokenByRefreshToken(refresh_token)
        if(r['status']<0):
            sleep(2)
            continue
        if(r['code']==400):
            isValid=False
            continue
        lastRefreshTime=getTime()
        access_token=r['text']['access_token']




try:
    tmp2=tmp1
except:
    tmp1=10
    start_new_thread(keep,())





def setPassword():
    global password,refresh_token,isValid
    if(password!=''):
        print('已经设置过密码, 请勿重新设置')
        return
    password=getHash(input('请输入密码: '))+PD2
    if(refresh_token!='' and isValid==True):
        flag=True
        try:
            f=open(path+slash[isWindows]+FILE_NAME,'w')
            f.write(encrypt(refresh_token,password))
            f.close()
        except:
            flag=False
            print('写入文件失败, Dropbox 仅在本次运行时可直接使用, 下次运行时需重新登陆')
        if(flag):
            print('已成功将账号信息写入文件')
        return
    try:
        f=open(path+slash[isWindows]+FILE_NAME,'r')
        text=f.readline()
        f.close()
    except:
        return
    try:
        text=decrypt(text,password)
    except:
        print('密码错误, 获取本地账户信息失败')
        return
    refresh_token=text
    isValid=True
    print('成功获取本地账户信息')



def tmptest():
    print(refresh_token)
    print(access_token)






def setAccount():
    global isValid,refresh_token,access_token
    print('请在浏览器中打开以下链接, 登陆, 然后复制之后的访问码')
    print(LOGIN_URL)
    auth_code=input('请输入访问码: ')
    r=getTokenByAuthorizationCode(auth_code)
    if(r['status']<0):
        print('无网络或网络超时, 请检查网络后重试')
        return
    if(r['code']==400):
        print('访问码错误')
        return
    access_token=r['text']['access_token']
    refresh_token=r['text']['refresh_token']
    isValid=True
    if(password==''):
        print('暂未设置密码, 无法将账号信息写入文件, Dropbox 仅在本次运行时可直接使用, 下次运行时需重新登陆')
        return
    try:
        f=open(path+slash[isWindows]+FILE_NAME,'w')
        f.write(encrypt(refresh_token,password))
        f.close()
    except:
        print('写入文件失败, Dropbox 仅在本次运行时可直接使用, 下次运行时需重新登陆')
        return
    print('已成功将账号信息写入文件')


