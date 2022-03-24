# coding=utf-8
'''

                mySelenium
作者：LX
开始时间: 2021.12.15
更新时间: 2022.2.15
简化原生selenium操作,以更简短的方式对元素定位
使代码看起来更加清晰.
特点：
    代码简洁,
    代码具有及联操作


author: LX
Start Time: 2021.12.15
UpdateTime: 2022.1.3
Simplify native Selenium operations to locate elements in a shorter manner
Make the code look cleaner.
characteristics:
    Clean code,
    Code has and associated operations
---------------------------------------------------------------
Directions for use
    # 初始化 Initialize
    cs = ChromeSelenium()
    # 打开网页 open Url
    cs.get(url)
    # 等待时间  Waiting time
    cs.wait(2)
    # 关闭网页  Close Url
    cs.quit()
'''

'''
    在mac系统关于鼠标系列的操作失效
    问题:
        发现拖拽到了鼠标所停留的位置，也不是实际设置位置
    原因大概是我所拖拽的元素其实本身不能拖拽，是点击这个元素拖拽生成了一个新的元素，拖拽的并非本身这个元素，而是新生成的这个元素
'''


import os
import sys
import time
import random
import types
import datetime
import copy
import inspect
import threading
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

if __name__ == '__main__':
    from CSLanguage.Language import Language
    from CSAbstract.CSeleniumABS import CSeleniumABS
    from CSError.Error import DriverError
else:
    from .CSLanguage.Language import Language
    from .CSAbstract.CSeleniumABS import CSeleniumABS
    from .CSError.Error import DriverError

Lan = Language.L
ERROR_OUT = sys.stderr
CommonError = (WebDriverException,TypeError,AttributeError)  # 自定义错误
'''
    谷歌selenium
'''

# 返回当前函数的名称,这个函数不能用于默认值,只能函数内部调用
def getCurrentFuncName():
    return inspect.stack()[1][3]


# 操作步骤类
class Steps:
    def __init__(self):
        '''
        {
            url:[操作步骤]
        }
        '''
        self.__step_list = {}  # type:{str:list}
        self.__language_list = ["Chinese", "English"]
        self.__language = "Chinese"

    # 设置语言
    def setLanguage(self, language: str = "Chinese"):
        self.__language = language

    def language(self) -> str:
        return self.__language

    # 判断网址是否存在
    # Determine if the url exists
    def isUrl(self, url: str):
        if url in self.__step_list:
            return True
        return False

    # 添加步骤
    # Add the driver
    def addStep(self, url: str, text: str):
        if not self.isUrl(url):
            self.__step_list[url] = list()
        self.__step_list[url].append(text)

    # 输出步骤/或者用于写日志
    # The output step
    def pintStep(self,io:str="out",path_file:str=""):
        '''

        :param io:
            out:输出到屏幕
            file:输出到文件
        :return:
        '''
        if io =="out":
            for k, v in self.__step_list.items():
                print(k, "--")
                for i in v:
                    print("         -->", i)
        if io == "file" and path_file:
            if not os.path.isfile(path_file):
                open(path_file,"w").close()
            with open(path_file,"a") as f:
                f.write("------------------------------"+datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')+"------------------------------\n")
                for k, v in self.__step_list.items():
                    f.write(k+"--"+"\n")
                    for i in v:
                        f.write("         -->"+i+"\n")

# 线程监视报错
# class MonitorErrorThread(threading.Thread):
#     def __init__(self,obj):
#         super(MonitorErrorThread, self).__init__(daemon=True)
#         self.__obj = obj
#         # 修改线程名称
#         self.setName(self.__class__.__name__ + "-" + self.name.split("-")[-1])
#
#         for i in range(5):
#             print("i=",i,obj)
#             time.sleep(1)




class ChromeSelenium(CSeleniumABS):
    # 模拟键盘的key 例如: ChromeSelenium.Key.BACKSPACE
    # The key of the simulated keyboard. example: ChromeSelenium.Key.BACKSPACE
    Key = Keys

    def __init__(self, url: str = None, is_interface: bool = True,
                 executable_path="chromedriver",
                 info_tracking: bool = False,log:[str,bool]="",ignore_err:bool=True,wait_time: float = 1.0,
                 driver: WebDriver = None):
        '''

        :param url: 网址
        :param is_interface:无界面
        :param info_tracking:信息追踪
        :param log: 日志文件,为True系统为日志文件命名,也可以自定义
        :param err_ignore:忽略错误.False时:调用方法报错直接忽略(大部分)
        :param executable_path:驱动路径
        :param wait_time: 等待时间
        :param driver: 支持将原生selenium驱动对象转换成ChromeSelenium对象
        url
        Waiting time
        Support for converting native Selenium driver objects into ChromeSelenium objects
        '''
        # 处理网页的显示通知(默认处理)
        prefs = {
            'profile.default_content_setting_values':{
                'notifications':2
            }
        }
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs',prefs)
        # 驱动 drive
        if driver:
            self.setDriver(driver)
        else:
            if is_interface:
                self.__drive = webdriver.Chrome(executable_path=executable_path)
            else:
                # 无界面
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                self.__drive = webdriver.Chrome(executable_path=executable_path,
                                                chrome_options=chrome_options)

        # 元素对象  The element object
        self.__ele = None  # type:WebElement
        # 历史url  Url history
        self.__his_url = []
        # 弹窗对象  alter object
        self.__alter_obj = None  # type:SwitchTo
        # 下标 index
        self.__index = -1
        # 追踪
        self.__tracking = info_tracking
        # 日志
        self.__log_file = ""
        # 忽略错误
        self.__err_ignore = ignore_err
        # 记录操作步骤类 Record the action step class
        self.__steps = Steps()
        if url:
            self.get(url, wait_time)
        # 为日志文件命名
        if log == True:
            self.__log_file = "CSelenium_"+self.currentTime+".log"
        elif log != "":
            self.__log_file = log+".log"

        # self.me = MonitorErrorThread(self.__drive)

    def newElement(self,by,value) -> WebElement:
        return copy.copy(self.driver.find_element(by, value))

    # 是否追踪输出
    def _trackingOut(self, out_st=None,err_st=None,err_info="",file_st=None) -> None:
        '''

        :param out_st: 标准输出
        :param err_st: 错误输出
        :param err_info: 错误输出的额外信息
        :param file_st: 输出在文件里的
        :return:
        '''
        if self.__tracking:
            if err_st:
                if err_info:
                    print("         -->", err_st,"--{}".format(err_info), file=ERROR_OUT)
                else:
                    print("         -->", err_st, file=ERROR_OUT)
            else:
                print("         -->", out_st)

            if file_st:
                self.__steps.addStep(self.currentUrl, file_st)
            elif out_st:
                self.__steps.addStep(self.currentUrl, out_st)
            elif err_st:
                self.__steps.addStep(self.currentUrl, err_st)

    def __isLog(self) ->bool:
        if self.__log_file:
            return True
        return False

    def getLogFilePath(self) -> str:
        return self.__log_file

    # 返回当前时间 Return current time
    @property
    def currentTime(self, connector="-") -> str:
        '''
        返回当前时间
        Return current time
        :connector: 连接符
        :return: str
        '''
        return datetime.datetime.now().strftime('%Y@%m@%d %H@%M@%S'.replace("@", connector))

    # 设置驱动 Set the drive
    def setDriver(self, driver: WebDriver):
        '''
        设置驱动
        :param driver: 支持将原生selenium驱动对象转换成ChromeSelenium对象
        :return: self
        Set the drive
        Support for converting native Selenium driver objects into ChromeSelenium objects
        '''
        self.__drive = driver
        return self

    # 设置文档元素 Setting document Elements
    def setElement(self, ele: [WebElement,list]):
        '''
        设置文档元素
        :param ele: 支持将原生selenium文档对象转换成ChromeSelenium文档对象
        :return: self
        Setting document Elements
        Support for converting native Selenium driver objects into ChromeSelenium objects
        '''
        self.__ele = ele
        return self

    # 返回原始驱动对象Returns the original driver object
    @property
    def driver(self) -> WebDriver:
        '''
        Returns the original driver object
        :return: selenium
        '''
        return self.__drive

    # 当前操作的url  Url of the current operation
    @property
    def currentUrl(self) -> str:
        '''
        当前操作的url
        :return: str
        Url of the current operation
        '''
        if self.allUrl():
            return self.allUrl()[-1]
        return ""

    # 返回当前使用的浏览器名称
    def getBrowserName(self) -> str:
        return self.driver.name

    # 打开网页  open Url
    def get(self, url: str = "", wait_time: float = 0.0):
        '''

        :param url: url
        :param wait_time: 等待时间
        :return: self
        url
        wait time
        '''
        # 记录
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, url)
        # self.__steps.addStep(self.currentUrl, st)
        try:
            self.__drive.get(url)
            if self.__tracking:
                print(st)
            self.__his_url.append(url)  # 加入url
        except CommonError:
            if self.__tracking:
                e = "--URL ERROR"
                print(st, e, file=ERROR_OUT)
                self.__steps.addStep(self.currentUrl, st + e)
            # 忽略错误
            if self.__err_ignore:
                raise ValueError("URL error")
        if wait_time:
            self.wait(wait_time)
        return self

    # 函数模版
    def _funcTemplate(self,func,
                      parameter=None,
                      st:str=None,
                      err_type=None,
                      err_info:str=""):
        try:
            # self.element().send_keys(*value)
            if parameter:
                func(parameter)
            else:
                func()
            self._trackingOut(st)
        except CommonError:
            self._trackingOut(err_st=st,err_info=err_info)
            if self.__err_ignore:
                raise err_type(err_info)
                # raise ValueError("Parameter error, support text or image path")

    # 返回关于语言设置的字典信息进行格式化
    def _getLan(self, func_name):
        return Lan[self.__steps.language()][func_name]

    # 输入键 Enter key
    def send_keys(self, *value):
        '''

        :param text: 文本/图片路径
        :return: self
        text
        '''
        # 记录步骤
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._funcTemplate(func=self.element().send_keys,
                           parameter=value,
                           st=st,
                           err_type=ValueError,
                           err_info="Parameter error, support text or image path")
        # try:
        #     self.element().send_keys(*value)
        #     self._trackingOut(st)
        # except CommonError:
        #     self._trackingOut(err_st=st,err_info="Parameter error, support text or image path")
        #     if self.__err_ignore:
        #         raise ValueError("Parameter error, support text or image path")
        return self

    # 点击 click
    def click(self):
        '''
        点击
        :return: self
        click
        '''
        # 记录步骤
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._funcTemplate(func=self.element().click,
                           parameter=None,
                           st=st,
                           err_type=TypeError,
                           err_info="Try using element location methods first,id(),xpath()...")
        # try:
        #     self.element().click()
        #     self._trackingOut(st)
        # except CommonError:
        #     self._trackingOut(err_st=st,err_info="Try using element location methods first,id(),xpath()...")
        #     if self.__err_ignore:
        #         # 尝试先使用元素定位方法,id(),xpath(),…
        #         raise TypeError("Try using element location methods first,id(),xpath()...")
        return self

    # 强制等待 Mandatory waiting
    def wait(self, wait_time: float = 1.0):
        '''
        强制等待
        :param wait_time: 时间
        :return:
        Mandatory waiting
        '''
        # 记录步骤
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, wait_time)
        self._trackingOut(st)
        time.sleep(wait_time)
        return self

    # 隐试等待
    def implicitly_wait(self, wait_time: float = 7.0):
        '''
        隐试等待
        :param wait_time: 时间
        :return: self
        implicit wait
        '''
        # 记录步骤
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, wait_time)
        try:
            self._funcTemplate(func=self.driver.implicitly_wait,
                               parameter=wait_time,
                               st=st,
                               err_type=DriverError,
                               err_info="No drive found")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self._trackingOut(st)
        # self.driver.implicitly_wait(wait_time)
        return self

    # def eleWait(self,max_wait_time:int=10):
    # WebDriverWait(self.__drive,max_wait_time).until()

    # 清除 clear
    def clear(self):
        '''
        清除
        :return: self
        clear
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._funcTemplate(func=self.element().clear,
                           parameter=None,
                           st=st,
                           err_type=TypeError,
                           err_info="Try using element location methods first,id(),xpath()...")

        # try:
        #     self.__ele.clear()
        #     self._trackingOut(st)
        # except CommonError:
        #     self._trackingOut(err_st=st, err_info="Try using element location methods first,id(),xpath()...")
        #     if self.__err_ignore:
        #         # 尝试先使用元素定位方法,id(),xpath(),…
        #         raise TypeError("Try using element location methods first,id(),xpath()...")
        return self

    # 获取元素文本 Get element text
    @property
    def text(self) -> str:
        '''
        获取元素文本
        :return: self
        Get element text
        '''
        t = self.element().text
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, t)
        self._trackingOut(st)
        return t

    @property
    def value(self):
        v = self.element().get_attribute("value")
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, v)
        self._trackingOut(st)
        return v

    @property
    def class_(self) -> str:
        v = self.element().get_attribute("class")
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, v)
        self._trackingOut(st)
        return v

    @property
    def name_(self) -> str:
        v = self.element().get_attribute("name")
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, v)
        self._trackingOut(st)
        return v

    # 提交submit
    def submit(self):
        '''
        提交
        :return: self
        submit
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._funcTemplate(func=self.element().submit,
                           parameter=None,
                           st=st,
                           err_type=TypeError,
                           err_info="Try using element location methods first,id(),xpath()...")
        # self.element().submit()
        # self._trackingOut(st)
        return self

    # 网页标题 page title
    @property
    def title(self) -> str:
        '''
        网页标题
        :return: str
         page title
        '''
        title_ = self.driver.title
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,title_)
        self._trackingOut(st)
        return title_

    # 窗口最大化 Window maximization
    def maxWin(self):
        '''
        窗口最大化
        :return: self
        Window maximization
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        try:
            self._funcTemplate(func=self.driver.maximize_window,
                               parameter=None,
                               st=st,
                               err_type=DriverError,
                               err_info="No drive found")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self._trackingOut(st)
        # self.driver.maximize_window()
        return self

    # 窗口最小化 Window minimization
    def minWin(self):
        '''
        窗口最小化
        :return: self
        Window minimization
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        try:
            self._funcTemplate(func=self.driver.minimize_window,
                               parameter=None,
                               st=st,
                               err_type=DriverError,
                               err_info="No drive found")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self.driver.minimize_window()
        # self._trackingOut(st)
        return self

    # 设置窗口大小 Setting window size
    def resizeWin(self, w: int, h: int):
        '''
        设置窗口大小
        :param w: 宽度
        :param h: 高度
        :return: self
        Setting window size
        Width
        height
        '''
        self.driver.set_window_size(w, h)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, w, h)
        self._trackingOut(st)
        return self

    # -------------处理内嵌框架-----------------
    # 处理内嵌框架 Processing framework
    def frame(self):
        '''
        处理内嵌框架
        :return: self
        Processing framework
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        try:
            self._funcTemplate(func=self.driver.switch_to.frame,
                               parameter=self.element(),
                               st=st,
                               err_type=TypeError,
                               err_info="Try using element location methods first,id(),xpath()...")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self.driver.switch_to.frame(self.element())
        # self._trackingOut(st)
        return self

    # 切换默认文档 Switching between default documents
    def defaultContent(self):
        '''
        切换默认文档
        :return: self
        Switching between default documents
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        try:
            self._funcTemplate(func=self.driver.switch_to.default_content,
                               parameter=None,
                               st=st,
                               err_type=TypeError,
                               err_info="Please use frame() first")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self.driver.switch_to.default_content()
        # self._trackingOut(st)
        return self

    # 切换到父框架(上一层) Switch to parent frame (previous layer)
    def parentFrame(self):
        '''
        切换到父框架(上一层)
        :return: self
        Switch to parent frame (previous layer)
        '''
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        try:
            self._funcTemplate(func=self.driver.switch_to.parent_frame,
                               parameter=None,
                               st=st,
                               err_type=TypeError,
                               err_info="Please use frame() first")
        except CommonError:
            raise DriverError("No drive found,driver={}".format(self.driver))
        # self.driver.switch_to.parent_frame()
        # self._trackingOut(st)
        return self

    # ------------处理弹窗-----------------
    # 处理弹窗 Handle the pop-up
    def alert(self):
        '''
        处理弹窗
        :return: self
        Handle the pop-up
        '''
        self.__alter_obj = self.driver.switch_to.alert  # type: SwitchTo
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 接收弹窗 Receive the pop-up
    def alertOK(self):
        '''
        接收弹窗
        :return: self
        Receive the pop-up
        '''
        if self.__alter_obj:
            self.__alter_obj.accept()
            # 接收完弹窗立刻清除
            self.__alter_obj = None
            st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
            self._trackingOut(st)
        return self

    # 取消弹窗 Cancel the popup window
    def alertNO(self):
        '''
        取消弹窗
        :return: self
        Cancel the popup window
        '''
        if self.__alter_obj:
            self.__alter_obj.dismiss()
            # 接收完弹窗立刻清除
            self.__alter_obj = None
            st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
            self._trackingOut(st)
        return self

    # -------------处理内嵌框架End-----------------

    # 获取弹窗文本 Gets popover text
    @property
    def alertText(self) -> str:
        '''
        获取弹窗文本
        :return: str
        Gets popover text
        '''
        if self.__alter_obj:
            st = '{} 获取alert弹窗文本:[{}]'.format(self.currentTime, self.__alter_obj.text)
            self.__steps.addStep(self.currentUrl, st)
            return self.__alter_obj.text

    # ------------处理弹窗End-----------------

    # 快照 snapshot
    def save_screenshot(self, image_name: str = None, path: str = None, suffix: str = "png"):
        '''
        快照
        :param image_name:图片名称
        :param path:路径
        :param suffix:后缀
        :return:
        snapshot
        '''

        temp = self.title + self.currentTime
        if path:
            if image_name:
                file = os.path.join(path, image_name + "." + suffix)
                self.__drive.get_screenshot_as_file(file)
            else:
                file = os.path.join(path, temp + "." + suffix)
                self.__drive.get_screenshot_as_file(file)
        else:
            if image_name:
                file = os.path.join(os.path.dirname(__file__), image_name + "." + suffix)
                self.__drive.get_screenshot_as_file(file)
            else:
                file = os.path.join(os.path.dirname(__file__), temp + "." + suffix)
                self.__drive.get_screenshot_as_file(file)

        # 记录步骤
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, file)
        self._trackingOut(st)
        return self

    # 模版 template
    def _posTemplate(self, by, value, text: str = None, wait_time: float = 0.0, is_press=False):
        '''

        :param by: 匹配方式
        :param value:值
        :param text: 输入文本
        :param wait_time: 等待时间
        :param is_press: 是否按下
        :return:
        '''
        self.setElement(self.driver.find_element(by, value))
        if text:
            self.element().send_keys(text)
        if is_press:
            self.element().click()
        if wait_time > 0.0:
            time.sleep(wait_time)

    # 多匹配
    def _posTemplates(self, by, value, wait_time: float = 0.0):
        self.setElement(self.driver.find_elements(by, value))
        if wait_time > 0.0:
            time.sleep(wait_time)

    # 返回当查找元素对象
    def element(self) -> WebElement:
        if isinstance(self.__ele,WebElement):
            return self.__ele
        else:
            raise TypeError("Return type error, try elements() method or NoneType or Try using element location methods first,id(),xpath()...")

    # 位置
    def location(self) -> dict:
        if isinstance(self.__ele, WebElement):
            return self.element().location
        else:
            raise TypeError("There are no element objects, element() is empty")

    # 返回元素对象列表
    def elements(self) -> list:
        if isinstance(self.__ele,list):
            return self.__ele
        else:
            raise TypeError("Return type error, try element() method or [] or Try using element location methods first,id(),xpath()...")

    # 检查元素到可见性
    @property
    def isElementDisplayed(self) -> bool:
        return self.element().is_displayed()

    # ----------------元素信息-------------
    # 返回元素属性值
    def getElementAttr(self, attribute, index: int = 0) -> str:
        value = ""
        if isinstance(self.element(), WebElement):
            value = self.element().get_attribute(attribute)
        if isinstance(self.elements(), list):
            value = self.elements()[index].get_attribute(attribute)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return value

    # 元素绝对位置
    def elementPos(self) -> dict:
        # value = self.element().location
        # 在随机时间内移动到当前元素位置
        js_code = """var r = arguments[0].getBoundingClientRect();
                                    return {top: (window.outerHeight - window.innerHeight) + Math.floor(r.top),
                                    left: Math.floor(r.left), elem_width: r.width, elem_height: r.height}"""
        res = self.driver.execute_script(js_code, self.element())
        x, y = res["left"] + res["elem_width"] // int(random.uniform(2, 6)), res["top"] + res["elem_height"] // 2
        value = {"x":x,"y":y}

        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return value

    # 元素绝对位置x
    def elementX(self) -> int:
        return self.elementPos()["x"]

    # 元素当绝对位置y
    def elementY(self) -> int:
        return self.elementPos()["y"]

    # 元素大小
    @property
    def elementSize(self) -> dict:
        return self.element().size

    # 元素宽度
    @property
    def elementWidth(self) -> int:
        return self.elementSize["width"]

    # 元素高度
    @property
    def elementHeight(self) -> int:
        return self.elementSize["height"]

    # ----------------元素信息End-------------

    # 多窗口切换
    def moreWin(self, i: int):
        win_handles = self.driver.window_handles
        # 定位到窗口
        self.driver.switch_to.window(win_handles[i])
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 切换到下一个窗口
    def nextWin(self):
        win_handles = self.driver.window_handles
        win_handles_len = len(win_handles)
        current_win = self.driver.current_window_handle
        index = win_handles.index(current_win)
        index += 1
        if index < win_handles_len:
            self.moreWin(index)
            st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,self.driver.title)
            self._trackingOut(st)
        return self

    # 切换到上一个窗口
    def onWin(self):
        win_handles = self.driver.window_handles
        current_win = self.driver.current_window_handle
        index = win_handles.index(current_win)
        index -= 1
        if index >= 0:
            self.moreWin(index)
            st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,self.driver.title)
            self._trackingOut(st)
        return self

    # ----------------查找元素操作--------------
    # id定位
    def id(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.ID,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # XPATH查找
    def xpath(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.XPATH,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # css查找
    def className(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.CLASS_NAME,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    def css(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.CSS_SELECTOR,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(), self.currentTime, value)
        self._trackingOut(st)
        return self

    # TAG_NAME查找
    def tagName(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.TAG_NAME,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # LINK_TEXT查找
    def linkText(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.LINK_TEXT,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # NAME查找
    def name(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.NAME,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # PARTIAL_LINK_TEXT查找
    def partialLineText(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self._posTemplate(by=By.PARTIAL_LINK_TEXT,
                          value=value,
                          text=text,
                          wait_time=wait_time,
                          is_press=is_press)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # XPATH查找 多匹配
    def xpaths(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.XPATH,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # css查找 多匹配
    def csss(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.CSS_SELECTOR,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # classNames查找 多匹配
    def classNames(self, value, wait_time: float):
        self._posTemplates(by=By.CLASS_NAME,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(), self.currentTime, value)
        self._trackingOut(st)
        return self

    # TAG_NAME查找 多匹配
    def tagNames(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.TAG_NAME,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # LINK_TEXT查找 多匹配
    def linkTexts(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.LINK_TEXT,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # NAME查找 多匹配
    def names(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.NAME,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # PARTIAL_LINK_TEXT查找 多匹配
    def partialLineTexts(self, value, wait_time: float = 0.0):
        self._posTemplates(by=By.PARTIAL_LINK_TEXT,
                           value=value,
                           wait_time=wait_time)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,value)
        self._trackingOut(st)
        return self

    # ----------------查找元素操作End---------------

    # 执行脚本
    def exec_script(self, js: str, *args):
        self.__drive.execute_script(js, *args)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,js)
        self._trackingOut(st)
        return self

    # 执行异步脚本
    def exec_async_script(self, js, *args):
        self.driver.execute_async_script(js, args)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime,js)
        self._trackingOut(st)
        return self

    # 网页源码
    def source(self, encoding=None) -> str:
        if encoding:
            return BeautifulSoup(self.driver.page_source, "html.parser").prettify(encoding)
        return BeautifulSoup(self.driver.page_source, "html.parser").prettify()

    # 浏览器后退
    def back(self):
        self.driver.back()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 浏览器前进
    def forward(self):
        self.driver.forward()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 刷新
    def refresh(self):
        self.driver.refresh()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # ------------鼠标操作--------------
    # 按住左键不放
    def mouseClick_and_hold(self):
        ActionChains(self.driver).click_and_hold(self.element()).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 在某个元素位置松开左键
    def mouseRelease(self):
        ActionChains(self.driver).release(self.element()).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 双击鼠标左键
    def mouseDoubleClick(self):
        ActionChains(self.driver).double_click(self.element()).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 点击鼠标右键
    def mouseRightClick(self):
        ActionChains(self.driver).context_click(self.element()).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 鼠标移动
    def mouseOffset(self, x: int, y: int):
        ActionChains(self.driver).move_by_offset(x, y).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, x, y)
        self._trackingOut(st)
        return self

    # 鼠标移动到某个元素
    def mouseToElement(self):
        ActionChains(self.driver).move_to_element(self.element()).perform()
        return self

    # 拖拽元素在到其它元素
    def mouseDrag_And_Drop(self, target:WebElement):
        s=self.driver.find_element(By.ID,"drag1")
        print(s.rect)
        e=self.driver.find_element(By.ID,"div2")
        print(e.size)
        pyautogui.moveTo(s.rect["x"],s.rect["y"])
        print(pyautogui.position())
        pyautogui.click()
        # self.element()
        # ActionChains(self.driver).drag_and_drop(s, e).perform()
        # st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        # self._trackingOut(st)
        return self

    # 将鼠标移动到距某个元素多少距离的位置
    def mouseMove_To_Element_With_Offset(self, x: int, y: int):
        ActionChains(self.driver).move_to_element_with_offset(self.element(), x, y).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, x, y)
        self._trackingOut(st)
        return self

    # 拖拽到某个坐标然后松开
    def mouseDrag_And_By_Offset(self, x: int, y: int):
        ActionChains(self.driver).drag_and_drop_by_offset(self.element(), x, y).perform()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, x, y)
        self._trackingOut(st)
        return self

    # ------------鼠标操作End--------------

    # ------------滚动条操作-----------
    # 滚动条
    def scroll(self, value: int = 0):
        scroll_js = "document.documentElement.scrollTop={}".format(value)
        self.exec_script(scroll_js)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return self

    # 滚动条到底端
    def scrollBottom(self):
        self.scroll(10000)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 滚动条到顶端
    def scrollTop(self):
        self.scroll(0)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 滚动条向左移动
    def scrollLeftValue(self, value: int):
        js = "window.scrollTo(0,{})".format(value)
        self.exec_script(js)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return self

    # 滚动条向右移动
    def scrollRightValue(self, value: int):
        js = "window.scrollTo({},0)".format(value)
        self.exec_script(js)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return self

    # 滚动条向左移动
    def scrollLeft(self):
        self.scrollLeftValue(10000)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 滚动条向右移动
    def scrollRight(self):
        self.scrollRightValue(10000)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # -------------------滚动条操作End----------

    # 关闭浏览器
    def quit(self):
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        self.driver.quit()

    # 设置语言
    def setLanguage(self, language: str = "Chinese"):
        self.__steps.setLanguage(language)

    # 返回所有get访问过到url  Returns all gets visited to the URL
    def allUrl(self) -> list:
        '''
        返回所有get访问过到url
        :return: list
        Returns all gets visited to the URL
        '''
        return self.__his_url

    # 元素长度
    @property
    def len(self) -> int:
        '''
        元素长度
        :return: int
        len
        '''
        if isinstance(self.element(), WebDriverWait):
            return 1
        if isinstance(self.elements(), list):
            return len(self.elements())

    # ----------------select菜单------------------
    # 通过下标 匹配select菜单
    def selectIndex(self, index: int = 0):
        Select(self.element()).select_by_index(index)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, index)
        self._trackingOut(st)
        return self

    # 通过文本 匹配select菜单
    def selectVisText(self, text: str):
        Select(self.element()).select_by_visible_text(text)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, text)
        self._trackingOut(st)
        return self

    # 通过select菜单里面的value匹配
    def selectValue(self, value):
        Select(self.element()).select_by_value(value)
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime, value)
        self._trackingOut(st)
        return self

    # --------------------select菜单End--------

    # 处理checkbox 全选
    def checkboxAll(self):
        '''
        select all checkbox
        :return:
        '''
        for e in self.elements():
            e = e  # type:ChromeSelenium
            e.click()
        st = self._getLan(getCurrentFuncName()).format(self.getBrowserName(),self.currentTime)
        self._trackingOut(st)
        return self

    # 输出步骤 output step
    def pintStep(self) -> None:
        '''
        output step
        :return: None
        '''
        if self.__isLog():
            self.__steps.pintStep(io="file",
                                  path_file=self.getLogFilePath())
        else:
            self.__steps.pintStep()

    # 模拟下标
    def __getitem__(self, item):
        return self.elements()[item]

    def __len__(self):
        if isinstance(self.element(), WebDriverWait):
            return 1
        if isinstance(self.element(), list):
            return len(self.elements())

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= self.len:
            raise StopIteration()  # 触发异常,停止迭代
        else:
            return self.elements()[self.__index]


# 多浏览器执行方法,目前不完善,测试中
# Multi - browser execution method, currently not perfect, testing
class CSeleniumThread(ChromeSelenium):
    '''
        一种写法对映多个浏览器执行
        为了保证这个类正常运行,请将 浏览器驱动 放在与Python解释器同级目录下
        One script executes against multiple browsers
        To keep this class running, place the browser driver in the same directory as the Python interpreter
    '''
    def __init__(self, browser_names: list=["chrome"],driver_path:dict=None,*args,**kwargs):
        '''

        :param browser_names: 浏览器驱动列表(不能传递相同的浏览器名称)
        :param driver_path: 浏览器驱动路径字典
        :param args:
        :param kwargs:
        '''
        # 给父类驱动传-1,阻止打开浏览器
        super(CSeleniumThread, self).__init__(driver=-1,*args,**kwargs)
        # 浏览器列表
        self.__browsers = []
        # 浏览器驱动字典
        self.__browser_drivers = dict()
        # 浏览器驱动路径
        self.__browser_driver_path = {"chrome":"chromedriver",
                                      "firefox":"geckodriver",
                                      "edge":None,
                                      "ie":None,
                                      "safari":None,
                                      "opera":None}
        # 浏览器驱动路径
        if browser_names:
            self.appendBrowser(browser_names)
        # 函数列表
        # 线程列表
        self.__threads = dict()
        # 执行函数列表
        self.__exec_func = []
        self.lock = threading.RLock()

    # 添加浏览器
    def appendBrowser(self,browser_names:[str,list]):
        if isinstance(browser_names,str):
            self.__createBrowser(browser_names)
            self.__browsers.append(browser_names)
        elif isinstance(browser_names,list):
            for _dri in browser_names:
                try:
                    self.__createBrowser(_dri)
                    self.__browsers.append(_dri)
                except Exception:
                    raise TypeError("[{}] Driver error".format(_dri))
        else:
            raise TypeError("The argument must be a string or a list of strings")

    # 设计驱动字典
    def setBrowserDriverPath(self,driver_path_dict:dict):
        for browser_name,driver_path in driver_path_dict.items():
            try:
                self.__browser_driver_path[browser_name]=driver_path
            except Exception:
                raise DriverError("The driver name or path is incorrect.\
                                  Name of chrome, firefox, edge, Internet explorer, safari, opera")

    def _getDriver(self,driver):
        _driver = driver.lower()

        # 获取浏览器驱动,Get the browser driver
        if _driver == "chrome":
            return webdriver.Chrome
        if _driver == "firefox":
            # executable_path="/Users/lx/Downloads/geckodriver"
            return webdriver.Firefox
        if _driver == "edge":
            return webdriver.Edge
        if _driver == "ie":
            return webdriver.Ie
        if _driver == "safari":
            return webdriver.Safari
        if _driver == "opera":
            return webdriver.Opera

    @staticmethod
    def __isFunc(f:types.FunctionType):
        '''
            判断参数是否为函数
        :param f: 函数
        :return:
        '''
        if type(f) == types.FunctionType:
            return True
        return False

    def __createBrowser(self,driver:str):
        '''
            创建驱动
        :return:
        '''
        _driver = driver.lower()

        if _driver not in self.__browser_drivers:
            self.__browser_drivers[_driver] = []
        # 添加浏览器驱动
        self.__browser_drivers[_driver].append(self._getDriver(_driver))

    # 多进程运行
    def runFork(self):
        '''
            这个方法必须放在与该类相关的所有代码之后.
            注意:改方法必须在linux/Unix系统下运行
            This method must come after all code associated with the class.
            Note: The change method must run on Linux /Unix
        :return:
        '''
        # 等待执行的语句
        '''
        waiting_statement 字典结构
        {
            "浏览器名称":[浏览器驱动,(函数名称,参数)]
        }
        '''
        waiting_statement = dict()
        for _b in self.__browsers:
            _driver = None
            browser_name = _b.lower()
            # 获取驱动
            _driver = self._getDriver(_b)

            if _b not in waiting_statement:
                waiting_statement[_b] = []

            # 添加驱动
            if _driver:
                waiting_statement[_b].append(_driver)

            # 添加操作
            for _f in self.__exec_func:
                fun_name = _f[0]
                fun_parameter = _f[1:][0]
                try:
                    if fun_parameter:
                        # 添加操作
                        waiting_statement[_b].append((fun_name,fun_parameter))
                    else:
                        # 添加操作
                        waiting_statement[_b].append((fun_name, tuple()))
                except Exception:
                    print(fun_name,fun_parameter)
                    print(sys.exc_info())

        # ---多进程
        def _execFunc(self, exec_func, browser_name):
            '''

            :param self: 自身对象
            :param exec_func: 执行函数
            :param browser_name: 浏览器名称
            :return:
            '''
            # 设置驱动
            _driver_ = exec_func[0]
            self.setDriver(_driver_(executable_path=self.__browser_driver_path.get(browser_name)))

            # 逐个执行函数
            for _e in exec_func[1:]:
                f_name = _e[0]
                f_argc = _e[1]
                if f_argc:
                    f_name(*f_argc)
                else:
                    f_name()
            print("\n\n-------------------")

        for browser_name,exec_func in waiting_statement.items():
            try:
                pid = os.fork()
                if pid == 0:  # 子进程
                    # print("C pid={} ppid={} p={}".format(os.getpid(), os.getppid(), pid))
                    _execFunc(self, exec_func,browser_name)
                    exit(0) # 退出
                # else:
                    # print("P pid={} ppid={} p={}".format(os.getpid(),os.getppid(),pid))
            except OSError as e:
                print(e)
        os.wait()

    # 正常
    def run(self):
        '''
            这个方法必须放在与该类相关的所有代码之后
        :return:
        '''
        # 等待执行对语句
        '''
        waiting_statement 结构
        {
            "浏览器名称":[浏览器驱动,(函数名称,参数)]
        }
        '''
        for _b in self.__browsers:
            browser_name = _b.lower()
            # 获取驱动,设置驱动
            _driver = self._getDriver(browser_name)(executable_path=self.__browser_driver_path.get(browser_name))
            self.setDriver(_driver)
            # 添加操作
            for _f in self.__exec_func:
                fun_name = _f[0]
                fun_parameter = _f[1:][0]
                try:
                    if fun_parameter:
                        # 执行
                        fun_name(*fun_parameter)
                    else:
                        fun_name()
                except Exception:
                    print(fun_name,fun_parameter)
                    print(sys.exc_info())

    def get(self, url: str = "", wait_time: float = 1.0):
        self.__exec_func.append([super().get,tuple([url,wait_time])])
        return self

    def send_keys(self, *value):
        self.__exec_func.append([super().send_keys, tuple(value)])
        return self

    def click(self):
        self.__exec_func.append([super().click, tuple()])
        return self

    def wait(self, wait_time: float = 0.0):
        self.__exec_func.append([super().wait, tuple([wait_time])])
        return self

    def id(self, value, text: str = None, wait_time: int = 0, is_press=False):
        self.__exec_func.append([super().id, tuple([value, text, wait_time, is_press])])
        return self

    def xpath(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().xpath, tuple([value, text, wait_time, is_press])])
        return self

    def className(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().className, tuple([value, text, wait_time, is_press])])
        return self

    def css(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().css, tuple([value, text, wait_time, is_press])])
        return self

    def linkText(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().linkText, tuple([value, text, wait_time, is_press])])
        return self

    def tagName(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().tagName, tuple([value, text, wait_time, is_press])])
        return self

    def name(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().name, tuple([value, text, wait_time, is_press])])
        return self

    def maxWin(self):
        self.__exec_func.append([super().maxWin,tuple()])
        return self

    def minWin(self):
        self.__exec_func.append([super().minWin,tuple()])
        return self

    def resizeWin(self, w: int, h: int):
        self.__exec_func.append([super().resizeWin,tuple([w,h])])
        return self

    def frame(self):
        self.__exec_func.append([super().frame,tuple()])
        return self

    def parentFrame(self):
        self.__exec_func.append([super().parentFrame,tuple()])
        return self

    def defaultContent(self):
        self.__exec_func.append([super().defaultContent, tuple()])
        return self

    def submit(self):
        self.__exec_func.append([super().submit, tuple()])
        return self

    def alert(self):
        self.__exec_func.append([super().alert, tuple()])
        return self

    def alertOK(self):
        self.__exec_func.append([super().alertOK, tuple()])
        return self

    def alertNO(self):
        self.__exec_func.append([super().alertNO, tuple()])
        return self

    def save_screenshot(self, image_name: str = None, path: str = None, suffix: str = "png"):
        self.__exec_func.append([super().save_screenshot,tuple([image_name,path,suffix])])
        return self

    def moreWin(self, i: int):
        self.__exec_func.append([super().moreWin,tuple([i])])
        return self

    def implicitly_wait(self, wait_time: float = 7.0):
        self.__exec_func.append([super().implicitly_wait,tuple([wait_time])])
        return self

    def nextWin(self):
        self.__exec_func.append([super().nextWin,tuple()])
        return self

    def onWin(self):
        self.__exec_func.append([super().onWin,tuple()])
        return self

    def partialLineText(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        self.__exec_func.append([super().partialLineText, tuple([value, text, wait_time, is_press])])
        return self

    def xpaths(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().xpaths,tuple([value, wait_time])])
        return self

    def csss(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().csss,tuple([value,wait_time])])
        return self

    def classNames(self, value, wait_time: float):
        self.__exec_func.append([super().classNames,tuple([value,wait_time])])
        return self

    def tagNames(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().tagNames,tuple([value,wait_time])])
        return self

    def linkTexts(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().linkTexts,tuple([value,wait_time])])
        return self

    def names(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().names,tuple([value,wait_time])])
        return self

    def partialLineTexts(self, value, wait_time: float = 0.0):
        self.__exec_func.append([super().partialLineTexts,tuple([value,wait_time])])
        return self

    def exec_script(self, js: str, *args):
        self.__exec_func.append([super().exec_script,tuple([js,*args])])
        return self

    def exec_async_script(self, js, *args):
        self.__exec_func.append([super().exec_async_script, tuple([js, *args])])
        return self

    def back(self):
        self.__exec_func.append([super().back,tuple()])
        return self

    def forward(self):
        self.__exec_func.append([super().forward, tuple()])
        return self

    def refresh(self):
        self.__exec_func.append([super().refresh, tuple()])
        return self

    def mouseClick_and_hold(self):
        self.__exec_func.append([super().mouseClick_and_hold,tuple()])
        return self

    def mouseRelease(self):
        self.__exec_func.append([super().mouseRelease, tuple()])
        return self

    def mouseDoubleClick(self):
        self.__exec_func.append([super().mouseDoubleClick, tuple()])
        return self

    def mouseRightClick(self):
        self.__exec_func.append([super().mouseRightClick, tuple()])
        return self

    def mouseOffset(self, x: int, y: int):
        self.__exec_func.append([super().mouseOffset, tuple([x,y])])
        return self

    def mouseToElement(self):
        self.__exec_func.append([super().mouseToElement,tuple()])
        return self

    def mouseDrag_And_Drop(self, target: WebElement):
        self.__exec_func.append([super().mouseDrag_And_Drop, tuple([target])])
        return self

    def mouseMove_To_Element_With_Offset(self, x: int, y: int):
        self.__exec_func.append([super().mouseMove_To_Element_With_Offset,tuple([x,y])])
        return self

    def mouseDrag_And_By_Offset(self, x: int, y: int):
        self.__exec_func.append([super().mouseDrag_And_By_Offset,tuple([x,y])])
        return self

    def scroll(self, value: int = 0):
        self.__exec_func.append([super().scroll,tuple([value])])
        return self

    def scrollBottom(self):
        self.__exec_func.append([super().scrollBottom, tuple()])
        return self

    def scrollTop(self):
        self.__exec_func.append([super().scrollTop, tuple()])
        return self

    def scrollLeftValue(self, value: int):
        self.__exec_func.append([super().scrollLeftValue, tuple([value])])
        return self

    def scrollRightValue(self, value: int):
        self.__exec_func.append([super().scrollRightValue, tuple([value])])
        return self

    def scrollLeft(self):
        self.__exec_func.append([super().scrollLeft, tuple()])
        return self

    def scrollRight(self):
        self.__exec_func.append([super().scrollRight, tuple()])
        return self

    def selectIndex(self, index: int = 0):
        self.__exec_func.append([super().selectIndex,tuple([index])])
        return self

    def selectVisText(self, text: str):
        self.__exec_func.append([super().selectVisText, tuple([text])])
        return self

    def selectValue(self, value):
        self.__exec_func.append([super().selectValue, tuple([value])])
        return self

    def checkboxAll(self):
        self.__exec_func.append([super().checkboxAll,tuple()])
        return self

    def clear(self):
        self.__exec_func.append([super().clear, tuple()])
        return self

    def quit(self):
        self.__exec_func.append([super().quit, tuple()])



# d = webdriver.Chrome()
# d.get("https://www.runoob.com/html/html5-draganddrop.html")
# s = d.find_element(By.ID, "drag1")
# e = d.find_element(By.ID, "div2")
# Action = ActionChains(d)
# '''将【拖拽我吧！】元素拖拽到第一个对话框'''
# Action.drag_and_drop(s,e).perform()   #将【拖拽我吧！】拖到第一个对话框
# time.sleep(3)
# d.quit()
