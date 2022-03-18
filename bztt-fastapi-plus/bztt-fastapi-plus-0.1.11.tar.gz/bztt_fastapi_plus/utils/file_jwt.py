# 基于jwt实现的用户校验
import jwt
from jwt import exceptions
import time

class FileJwtConfig(object):
    """
    RedisConfig Redis配置类
    :version: 1.2
    :date: 2020-02-11
    """

    SECRET_KEY = ""
    
# 定义签名密钥，用于校验jwt的有效、合法性
class file_jwt():
    
    def __init__(self, config: FileJwtConfig = None):
        if config:
            self.SECRET_KEY = FileJwtConfig.SECRET_KEY
        else:
            self.SECRET_KEY = "123"

    def create_token(self,name):
        '''基于jwt创建token的函数'''
        SECRET_KEY = self.SECRET_KEY
        headers = {
            "alg": "HS256",
            "typ": "JWT"
        }
        exp = int(time.time() + 3600)
        payload = name
        payload["exp"] = exp
        token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm='HS256', headers=headers).encode('utf-8').decode('utf-8')
        # 返回生成的token
        return token

    def validate_token(self,token):
        '''校验token的函数，校验通过则返回解码信息'''
        SECRET_KEY = self.SECRET_KEY
        payload = None
        msg = None
        try:
            payload = jwt.decode(token, SECRET_KEY,  algorithms='HS256')
            # jwt有效、合法性校验
        except exceptions.ExpiredSignatureError:
            msg = 'token已失效'
        except jwt.DecodeError as e:
            msg = 'token认证失败'
        except jwt.InvalidTokenError:
            msg = '非法的token'
        return (payload, msg)

    def validate_token_log(self,token):
        '''校验token的函数，校验通过则返回解码信息'''
        SECRET_KEY = self.SECRET_KEY
        #options = {"verify_signature": False}  #,options=options
        payload = None
        msg = None

        payload = jwt.decode(token, SECRET_KEY,  algorithms='HS256')
        return (payload, msg)
        

