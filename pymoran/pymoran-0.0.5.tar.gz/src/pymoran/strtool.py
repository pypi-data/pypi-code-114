
import random
import hashlib
import binascii
import os
from unittest import result
from pymoran.timetool import TimeClass


class StrClass:
    def __init__(self) -> None:
        pass

    def random_num(self, length: int):
        '''
        创建纯数字随机字符串
        :param length 生成的字符串长度
        return {str} 生成的随机字符串
        '''
        result = ''
        pool = '0123456789'
        pool_len = len(pool)-1
        for i in range(length):
            result += pool[random.randint(0, pool_len)]
        return result

    def random_str(self, length: int):
        '''
        创建包含大小写字母和数字的随机字符串
        :param length 生成的字符串长度
        return {str} 生成的随机字符串
        '''
        result = ''
        pool = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        pool_len = len(pool)-1
        for i in range(length):
            result += pool[random.randint(0, pool_len)]
        return result

    def custom_random_str(self, pool: str, length: int):
        '''
        创建自定义范围的随机字符串
        :param pool 自定义字符串范围
        :param length 生成的字符串长度
        return {str} 生成的随机字符串
        '''
        result = ''
        pool_len = len(pool)-1
        for i in range(length):
            result += pool[random.randint(0, pool_len)]
        return result

    def hash_md5(self, enstr):
        """
        字符串md5加密
        :param enstr 需要加密的字符串
        return {str} 加密后的字符串
        """
        md = hashlib.md5()
        md.update(bytes(enstr, encoding='utf-8'))
        result = md.hexdigest()
        return result

    def hash_sha1(self, enstr):
        """
        字符串sha1加密
        :param enstr 需要加密的字符串
        return {str} 加密后的字符串
        """
        sha = hashlib.sha1()
        sha.update(bytes(enstr, encoding='utf-8'))
        result = sha.hexdigest()
        return result

    def password(self, pwd: str, salt: str):
        """
        根据原密码加盐获取新的加密密码
        :param pwd 原密码
        :param salt 盐值，盐值长度必须大于4
        return {str} 加密后的密码
        """
        salt1 = salt[0:4]
        salt2 = salt[4:]
        pwd = salt1+pwd+salt2
        return self.hash_md5(pwd)

    def access_token(self, uniqueid: str):
        """
        生成唯一access_token
        :param pwdStr 原密码
        :param salt 盐值，盐值长度必须大于4
        """
        timeclass = TimeClass()
        result = str(uniqueid)+str(timeclass.timestamp())
        result = self.hash_md5(result)
        result = result + str(binascii.b2a_base64(os.urandom(108))[:-1])
        result = result.replace('\'', '')
        result = result.replace('/', '')
        return result


if __name__ == '__main__':
    strclass = StrClass()
    print(strclass.access_token('11'))

    # def creat_ordernum():
    #     ordernum = time.time()*1000000
    #     ordernum = int(ordernum)
    #     ranNum = random.randint(10, 99)
    #     return str(ordernum)+str(ranNum)
