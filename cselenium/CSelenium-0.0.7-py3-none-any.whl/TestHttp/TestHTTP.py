'''

    测试网址

'''

import socket
import time
import random
import ctypes
import re
import sys

# 通过地址去获取值
a = 100
addr = id(a)
g = ctypes.cast(addr,ctypes.py_object).value
# print(g)

def t():
    pass

class A:
    pass

'''
数字
字符串
类
...
'''
NUMBER_BYTE = sys.getsizeof(1)
STRING_BYTE = sys.getsizeof("")
FUNCTION_BYTE = sys.getsizeof(t)

# print(sys.getsizeof(A))
# print(sys.getsizeof(t))

'''
1G=1024MB
1MB=1024KB
1KB=1024B
'''


'''
    读取网页
'''

# 获取变量名
def createVarName()->str:
    # a-z,A-Z
    AZ = [chr(c) for c in range(65, 91)]
    AZ.extend([chr(c) for c in range(97, 122)])
    # 已时间作为名称
    return random.choice(AZ) + str(int(time.time()))


# 数据容器
class DataContainer:
    def __init__(self,html_text):
        self.__html_text = html_text

    @property
    def data(self)->str:
        return self.__html_text


# 存放动态创建的变量名二维表
class DynamicVariableTable:
    '''
        [{"var":变量地址,"变量名称":变量名称,"size":占用内存大小},{"var":变量地址,"变量名称":变量名称,"size":占用内存大小},...]
        变量地址 -> []
    '''
    def __init__(self):
        self.__dynamic_table = list()
        self.__index_pos = -1  # 当前下标位置

    @property
    def i(self)->int:
        return self.__index_pos

    # 添加变量
    def addVar(self,var_id,var_name,size):
        self.__dynamic_table.append({"var_id": var_id,"name":var_name, "size": size})
        self.next()

    # 給size赋值
    def addSizeValue(self,value):
        self.getValue(self.i)["size"] += value

    def table(self) -> list:
        return self.__dynamic_table

    def getValue(self, index):
        return self.__dynamic_table[index]

    def var(self,index) -> str:
        return self.getValue(index)["var"]

    def size(self,index) -> int:
        return self.getValue(index)["size"]

    def __getitem__(self, item):
        if isinstance(item,int):
            return self.table()[item]
        elif isinstance(item,str):
            for e in self.table():
                if e["name"] == item:
                    return e

    # 返回当前下标所指向的数据
    def ing(self):
        return self.__dynamic_table[self.__index_pos]

    # 将下标往下移动(永久性操作)
    def next(self):
        if self.__index_pos+1 < len(self.__dynamic_table):
            self.__index_pos += 1

    # 将下标往上移动(永久性操作)
    def up(self):
        if self.__index_pos - 1 > 0:
            self.__dynamic_table -= 1

    # 动态读取变量
    def dynamicGetVar(self):
        # 从地址上获取值
        return ctypes.cast(self.ing()["var_id"], ctypes.py_object).value

    # 从地址上获取数据
    def getIdData(self,id_addr:int):
        return ctypes.cast(id_addr, ctypes.py_object).value

    # 添加内容
    def dynamicAddVarValue(self, value,size):
        self.dynamicGetVar().append(DataContainer(value))
        self.ing()["size"] += size


# 动态创建变量
class DynamicCreateVar:
    public = 0
    protect = 1
    private = 2

    def __init__(self):
        self.__dynamic_table = DynamicVariableTable()

    # 头
    def _header(self) -> str:
        return "_" + self.__class__.__name__

    # 动态创建变量
    def dynamicCreateVar(self, var_name, value):
        '''
        少使用默认值,这里如果使用了默认值,那么它生成的id永远是一样的

        :param key: 变量名
        :param value: 所创建的容器
        :return:
        '''
        number = var_name.count("_")
        var_id = None
        # 公用,保护变量的创建
        if number == DynamicCreateVar.public or number == DynamicCreateVar.protect:
            self.__dict__[var_name] = value
            var_id = id(self.__dict__[var_name])

        # 私有变量的创建
        if number == DynamicCreateVar.private:
            self.__dict__[self._header() + var_name] = value
            var_id = id(self.__dict__[self._header() + var_name])
        return var_id


class DynamicVar:
    def __init__(self):
        # 每个列表变量最多存15个G网页大小,超过15G自动创建新的变量
        self.__max_var_memory_G = 15
        self.__size = 0
        # 容器个数
        self.__container_number = 0
        # 动态创建变量
        self.__dynamic_create_Var = DynamicCreateVar()
        # 存放动态创建的变量名二维表 [{"var":变量名,"size":占用内存大小}]
        self.__dynamic_table = DynamicVariableTable()

    # 设置最大内存
    def setMaxMemory(self,max_number):
        '''

        :param max_number:
            这个参数可以数字,也可以是字符串
            如果是数字默认单位是:G
            字符串穿参方法例如:1G, 2MB, 4kb
        :return:
        '''
        if isinstance(max_number,int):
            if max_number < 1:
                self.__max_var_memory_G = 4
            else:
                self.__max_var_memory_G = max_number

        if isinstance(max_number,str):
            number = float(re.findall(r"^[0-9]+", max_number)[0])
            unit = re.findall(r"[A-Z]+$", max_number, re.I)[0]
            if unit == "G" or unit == "g":
                self.__max_var_memory_G = number
            elif unit == "MB" or unit == "mb":
                self.__max_var_memory_G = round(number/1024,6)
            elif unit == "KB" or unit == "kb":
                self.__max_var_memory_G = round(number/1024/1024,6)

    # 容量增加
    def containerADD(self):
        self.__container_number += 1

    # 容量减少
    def containerReduce(self):
        self.__container_number -= 1

    # 容器个数
    def containerNumber(self)->int:
        return self.__container_number

    # 设置单位显示模式
    def setUnitMode(self,mode:str="G"):
        pass

    @property
    def maxG(self)->int:
        # print("kb=",self.__max_var_memory_G*self.MB)
        return self.__max_var_memory_G

    @property
    def size(self) -> int:
        return self.__size

    @property
    def KB(self):
        return 1024

    @property
    def G(self) -> int:
        return 1024 * self.MB

    @property
    def MB(self) -> int:
        return self.KB * self.KB

    # 添加数据
    def AddData(self,data):
        '''
            当存的数据超过所设置最大内存时,自动扩展
        :param data:
        :return:
        '''
        # print(sys.getsizeof(data))
        name = createVarName()
        if not self.__dynamic_table.table() \
            or self.__dynamic_table.ing()["size"] > self.maxG*self.MB:
            # 存对象地址
            self.__dynamic_table.addVar(self.__dynamic_create_Var.dynamicCreateVar(name,list()),
                                        name,0)
            self.containerADD()
        # elif self.__dynamic_table.ing()["size"] > self.maxG*self.MB:
        #     self.__dynamic_table.addVar(self.__dynamic_create_Var.dynamicCreateVar(name,list()),
        #                                 name, 0)
        #     self.containerADD()
        # print("size:{} G:{}".format(self.__dynamic_table.ing()["size"], self.maxG))
        '''
            这里减去45,
            在python中一个对象占用的字节大约在45左右,减去45是为了防止过多占用内存
        '''
        size = sys.getsizeof(data)-45
        self.__dynamic_table.dynamicAddVarValue(data,size)

    # 当前容器中的数据
    def dataIng(self)->None:
        # print(self.__dynamic_table.table())
        # print(self.__dynamic_table.ing())
        # print(self.__dynamic_table.dynamicGetVar())
        for i in self.__dynamic_table.dynamicGetVar():
            print(i.data)

    # 显示所有数据
    def all(self,is_show_id:bool=False,separator:str="\n")->None:
        '''

        :param is_show_id: 是否显示每条数据所对应的id
        :param separator: 每条数据之间的分隔符号,默认"\n"
        :return: None
        '''
        # print(self.__dynamic_table.table())
        # var_id = [i["var_id"] for i in self.__dynamic_table.table()]
        # print(var_id)
        try:
            var_id = [i["var_id"] for i in self.__dynamic_table.table()]

            for id in var_id:
                if is_show_id:
                    print("--------[id={}]--------".format(id))
                for data_ in self.__dynamic_table.getIdData(id):
                    print(data_.data,end=separator)
        except Exception as e:
            pass

    # 返回文本信息
    def text(self) -> str:
        '''
            返回字符串形式的数据
        :return:
        '''
        _text = ""
        var_id = [i["var_id"] for i in self.__dynamic_table.table()]

        for id_ in var_id:
            for data in self.__dynamic_table.getIdData(id_):
                _text += data.text
        return _text

# print(sys.getsizeof("abc"))
rrr= ["dasd","21312","kodad","joasd","dhalsdhals"]
a = DynamicVar()
a.setMaxMemory("10kb")
print("maxG=",a.maxG)
for i in rrr:
    a.AddData(i)
# a.AddData("abc")
a.dataIng()
# a.all()
# print(a.text())
# print(a.containerNumber())


# class ReadHtml:
#     def __init__(self,html_path:str="web/index.html"):
#         self.__dy = DynamicVar()
#         self.__dy.setMaxMemory("1024kb")
#
#     def readHTML(self,html_path:str="web/index.html"):
#         with open(html_path,"r") as f:
#             while 1:
#                 data = f.readline(1024)
#                 if data:
#                     self.__dy.AddData(data)
#                 else:
#                     break
#     def html(self)->str:
#
#         print(self.__dy.all())
#         print(self.__dy.containerNumber())
#         return ""
        # return self.__dy.text()

# rh = ReadHtml()
# rh.readHTML("/Applications/Python 3.8/save/CSelenium/src/Cselenium/TestReport/HtmlTestReport.html")
# print(rh.html())


# HTML_TEXT = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Test</title>
# </head>
# <body>
#     <h1>Hello World</h1>
# </body>
# </html>
# '''
#
# # ip地址,端口号
# HOST = "127.0.0.0"
# POST = 8888
#
# IP = (HOST, POST)
# # 监听数量
# NUMBER = 4
#
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(("127.0.0.1",8888))
# s.listen(NUMBER)
#
# print("服务器启动[本机名:{}]".format(socket.gethostname()))
# while True:
#     con, addr = s.accept()
#     data = con.recv(1024)
#     print("data:",data)
#     while 1:
#         content = HTML_TEXT.encode("utf-8")
#         header = "HTTP/1.1 200 OK\r\n"
#         empty = "\r\n"
#         response = (header + empty).encode('utf-8')
#         con.send(response)
#         con.send(content)
#         break
#     print(addr)
#     con.close()
# s.close()





# -------
# import socket
# import threading
#
# html='''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>测试</title>
# </head>
# <body>
#     <h2>hell world</h2>
# </body>
# </html>
# '''
#
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(("127.0.0.1",8888))
# server.listen(4)
#
# data= True
# print("服务器启动[本机名:{}]".format(socket.gethostname()))
# def cc(conn:socket.socket,addr:tuple):
#     print(addr)
#     print("------")
#     print(conn.getsockname())
#     print(conn.getpeername())
#     # print(socket.getnameinfo(addr))
#
#     while True:
#         try:
#             data = conn.recv(1024)
#             if data:
#                 print("数据",data.decode())
#                 if data.decode()=="q":
#                     print("退")
#                     break
#                 # print("数据:",data.decode())
#                 # content = html.encode("utf-8")
#                 # header = "HTTP/1.1 200 OK\r\n"
#                 # empty = "\r\n"
#                 # response = (header + empty).encode('utf-8')
#                 # conn.send(response)
#                 # conn.send(content)
#                 # break
#         # except ConnectionResetError as e:
#         except Exception as e:
#             print("关闭正在",e)
#             break
#     print("{}退出".format(addr))
#     conn.close()
#
#
# while True:
#     conn, addr = server.accept()
#
#     # print(conn,addr)
#     t= threading.Thread(target=cc,args=(conn,addr,))
#     t.start()
#
# server.close()