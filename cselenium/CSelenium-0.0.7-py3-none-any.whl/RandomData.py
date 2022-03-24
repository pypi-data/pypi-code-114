'''

    随机数据类

作者: LX
当前版本: 0.0.1
编写时间: 2022.3.24
修改时间: 2022.3.24
'''
import os
import time
import datetime
import random
import base64
import hmac


class RandomData:

    # 数字,字母
    NUMBER = 1
    LETTER = 2

    def __init__(RandomData):
        pass

    # 返回一个整型随机时间
    @staticmethod
    def randomTimeInt(start_time: int = 1, end_time: int = 3) -> int:
        '''
            返回一个整型随机时间
        :param start_time: 开始时间
        :param end_time: 结束时间
        :return: int
        '''
        return int(random.uniform(start_time, end_time))

    # 返回一个随机浮点型时间
    @staticmethod
    def randomTimeFloat(start_time: float = 0.2, end_time: float = 0.7) -> float:
        '''
            返回一个随机浮点型时间
        :param start_time:开始时间
        :param end_time:结束时间
        :return:float
        '''
        return random.uniform(start_time, end_time)

    # 返回一个随机名称
    @staticmethod
    def randomName(len_: int = 6,is_first_upper:bool=False,is_upper:bool=False)->str:
        '''
            返回一个随机名称
        :param len_: 字符长度
        :param is_first_upper: 是否首字母大小
        :param is_upper: 全大小
        :return: str
        '''
        name = []
        for n in range(len_):
            name.append(chr(int(random.uniform(97, 122))))

        name = "".join(name)
        if is_upper:
            name = name.upper()
        elif is_first_upper:
            name = name.capitalize()

        return name

    # 返回随机字符串数字
    @staticmethod
    def randomNumber(len_: int = 10)->str:
        '''
            返回随机字符串数字
        :param len_: 字符长度
        :return: 
        '''
        phone = []
        for n in range(len_):
            phone.append(str(int(random.uniform(1, 10))))
        return "".join(phone)

    # 返回随机IP地址
    @staticmethod
    def randomAddr()->str:
        '''
            返回随机IP地址
        :return: str
        '''
        addr = "{}.{}.{}.{}".format(random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255)
                                    )
        return addr

    # 返回随机端口号
    @staticmethod
    def randomPort() -> str:
        '''
            返回随机端口号
        :return: str
        '''
        return str(random.randint(8000,9999))

    # 随机生日
    @staticmethod
    def randomBirthday(connector:str="/",order:bool=False)->str:
        '''
            随机生日
        :param connector:日期连接符号
        :param order: 排序 False为倒叙
        :return: str
        '''
        if order:
            bir = "{}{}{}{}{}".format(int(random.uniform(1970, datetime.datetime.now().year)), connector,
                                      random.randint(1, 12), connector,
                                      int(random.uniform(1, 28))
                                      )
        else:
            bir = "{}{}{}{}{}".format(int(random.uniform(1,28)),connector,
                                        random.randint(1,12),connector,
                                        int(random.uniform(1970,datetime.datetime.now().year)))

        return bir

    # 随机字母加数字
    @staticmethod
    def randomLetterNumber(l_len:int=2,n_len:int=5,order:bool=True)->str:
        '''
            返回随机字母加数字
        :param l_len: 字母长度
        :param n_len: 数字长度
        :param order: 字母与数字的顺序 True:字母在前,数字在后
        :return:str
        '''
        if order:
            return RandomData.randomName(l_len) + RandomData.randomNumber(n_len)
        else:
            return RandomData.randomNumber(n_len) + RandomData.randomName(l_len)

    # 随机邮箱
    @staticmethod
    def randomEmail(len_:int=9,suffix:str=None)->str:
        '''
            返回随机邮箱
        :param len_: 字符串长度
        :param suffix: 后缀
        :return: str
        '''
        suffix_list = ["@qq.com","@163.com","@comcast.net","@warwick.net",
                       "@sina.com","@sohu.com","@gmail.com","@live.com"]
        if suffix:
            return RandomData.randomNumber(len_)+suffix
        else:
            return RandomData.randomNumber(len_)+random.choice(suffix_list)

    # 随机性别
    @staticmethod
    def randomSex()->str:
        '''
            返回随机性别
        :return: str
        '''
        return random.choice(["男","女"])

    # 随机年龄
    @staticmethod
    def randomAge(is_real:bool = True)->str:
        '''
            随机年龄
        :param is_real: 年龄的真实性
        :return:
        '''
        if is_real:
            return str(random.randint(1,100))
        else:
            return str(random.randint(0,999))

    # 随机邮政编码
    @staticmethod
    def randomZipCode()->str:
        '''
            随机邮政编码
        :return: str
        '''
        return str(int(random.uniform(100000,300000)))

    # 随机token值
    @staticmethod
    def randomToken(key:str=None)->str:
        '''
            随机token值
        :param key: 字符串
        :return: 
        '''
        ts_str = str(time.time() + 3600)
        ts_byte = ts_str.encode("utf-8")
        if key:
            sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
        else:
            sha1_tshexstr = hmac.new(RandomData.randomName().encode("utf-8"), ts_byte, 'sha1').hexdigest()
        token = ts_str + ':' + sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8").replace("==","")

    # 随机密钥
    @staticmethod
    def randomKey() -> str:
        '''
            随机密钥
        :return: str
        '''
        return base64.b64encode(os.urandom(48)).decode()

    # 随机列表
    @staticmethod
    def randomList(len_:int=5,mode:int=1) -> list:
        '''
            随机列表
        :param len_: 列表长度
        :param mode: 数据的类型
        1:全数字
        2:全字母
        3:数字+字母
        :return:list
        '''
        if mode == RandomData.NUMBER:
            return [random.randint(0,999) for i in range(len_)]
        if mode == RandomData.LETTER:
            return [RandomData.randomName(random.randint(1,4)) for i in range(len_)]
        if mode == RandomData.NUMBER | RandomData.LETTER:
            return [random.choice([random.randint(0,999),RandomData.randomName(random.randint(1,4))]) for i in range(len_)]

    # 随机元祖
    @staticmethod
    def randomTuple(len_:int=5,mode:int=1) -> tuple:
        '''
            随机元祖
        :param len_: 列表长度
        :param mode: 数据的类型
        1:全数字
        2:全字母
        3:数字+字母
        :return:tuple
        '''
        return tuple(RandomData.randomList(len_,mode))

    # 随机集合
    @staticmethod
    def randomSet(len_:int=5,mode:int=1) -> set:
        '''
                随机集合
            :param len_: 列表长度
            :param mode: 数据的类型
            1:全数字
            2:全字母
            3:数字+字母
            :return:set
        '''
        return set(RandomData.randomList(len_,mode))

    # 随机字典
    @staticmethod
    def randomDict(len_:int=5,mode:int=1) -> dict:
        '''
                随机字典
            :param len_: 列表长度
            :param mode: 数据的类型
            1:全数字
            2:全字母
            3:数字+字母
            :return:dict
        '''
        if mode == RandomData.NUMBER:
            return { RandomData.randomName(1):random.randint(1,999) for v in range(len_)}
        if mode == RandomData.LETTER:
            return { RandomData.randomName(1):RandomData.randomName(random.randint(1,4)) for v in range(len_)}
        if mode == RandomData.NUMBER | RandomData.LETTER:
            return {RandomData.randomName(1): random.choice([random.randint(0,999),RandomData.randomName(random.randint(1,4))]) for v in range(len_)}


if __name__ == '__main__':
    r = RandomData()
    print(r.randomDict(mode=1))