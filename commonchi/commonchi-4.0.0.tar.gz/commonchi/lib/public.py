
# cxx增加
import datetime
import xlrd
import os
from time import sleep
import time
from commonchi.lib.utility import *


def get_shijianchuo_p():
    nowtime = datetime.datetime.now()
    # 格式化当前时间,获取时间戳
    strtime = datetime.datetime.strftime(nowtime, "%Y/%m/%d %H:%M:%S")
    return strtime


#读取Excel表格中passed数量   2022.1.22修改
def num_pa(file_path,num_result):
    global p
    try:
        book = xlrd.open_workbook(file_path, 'rb')  # 打开Excel
        sheet = book.sheet_by_index(0)  # 获取第几个sheet页数据
        p=0
        for i in range(1, sheet.nrows):  # sheet.nrows获取列表中的每一行
            #获取32行值
            z=sheet.cell_value(i, num_result)  # 文件类型2
            if z=='PASS':
                p=p+1
        return p
    except:
        pass


#获取行数
def gain_excel_nrows( num_table,file_path):
    #filepath = 'D:\\Interface_automation\\ussm\\test\\file\\data.xls'
    # module_path = os.path.abspath('..')  # 获取上一级目录
    # #filepath = module_path + '/file/data.xls'
    # filepath = module_path + file_path
    date = xlrd.open_workbook(file_path, "r")
    table = date.sheets()[num_table]  # 打开第几张表
    num_rows = table.nrows  # 获取表的行数
    return num_rows


#判断文件夹是否存在，不存在，则新建
def determine_directory(path):
    #path='D:\Interface_automation\API\\report\\aagc'
    os.path.exists(path)
    try:
        os.mkdir(path)
        sleep(1)
    except:
        pass
    sleep(1)

def bj():
    m_path = os.path.abspath(os.path.join(os.getcwd(), "."))  # 获取本级目录
    # print(m_path)
    return m_path

def lj():
    m_path = os.path.abspath(os.path.join(os.getcwd(), ".."))  # 获取上级目录
    # print(m_path)
    return m_path

def sj():
    m_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # 获取上两级目录
    # print(m_path)
    return m_path

def html_time():
    html_time_1 = time.strftime("_%Y-%m-%d-%H-%M-%S", time.localtime())
    return html_time_1

def time1():
    time_11 = time.strftime("%Y/%m/%d", time.localtime())
    return time_11

def report_p(product_name):
    # report_pa = report_path() + product_name + "\excelReport\\"
    report_pa=os.path.join(report_path() + product_name, "excelReport")
    return report_pa

def TARGET_FILE_dir(product_name):
    TARGET_FILE_d = report_path() + product_name +  "\excelReport"
    return TARGET_FILE_d

def TARGET_FILE(product_name,source_file):
    TARGET_F = os.path.join(report_p(product_name), product_name + html_time() + source_file)
    # TARGET_F=os.path.join(report_path() + product_name, "excelReport", product_name + html_time + source_file)
    return TARGET_F

def SOURCE_FILE(source_file):
    SOURCE_FILE = os.path.join(bj(), source_file)
    return SOURCE_FILE

def TEST_CONFIG():
    TEST_CONF= os.path.join(bj(), "config.ini")
    return TEST_CONF


def html_file(product_name):
    html_fi=report_path() + product_name + '\\' + product_name + html_time() + ".html"
    return html_fi

def html_FILE_dir(product_name):
    html_FILE_d=report_path() + product_name
    # print(html_FILE_d)
    return html_FILE_d


# bj()
# lj()
# sj()