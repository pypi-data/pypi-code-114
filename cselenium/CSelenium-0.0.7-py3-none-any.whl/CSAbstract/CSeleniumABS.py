'''

    CSelenium抽象类文件
    适用 selenium 3.xx的版本

'''
from abc import ABCMeta
from abc import abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver,WebElement


class CSeleniumABS(metaclass=ABCMeta):
    '''
        自动化框架的抽象类,所有子类必须实现一下方法
    '''
    # @abstractmethod
    # def __init__(self,*args,**kwargs):
    #     pass

    # @abstractmethod
    # def _trackingOut(self,st) -> None:
    #     '''
    #         内部调用方法
    #         是否追踪输出
    #         :param st:
    #         :return: None
    #     '''
    #     pass

    @abstractmethod
    def setDriver(self, driver: WebDriver):
        '''
            设置驱动
            :param driver: 支持将原生selenium驱动对象转换成ChromeSelenium对象
            :return: self
            Set the drive
            Support for converting native Selenium driver objects into ChromeSelenium objects
        '''
        pass

    @abstractmethod
    def setElement(self, ele: [WebElement,list]):
        '''
            设置文档元素
            :param ele: 支持将原生selenium文档对象转换成ChromeSelenium文档对象
            :return: self
            Setting document Elements
            Support for converting native Selenium driver objects into ChromeSelenium objects
        '''
        pass

    @abstractmethod
    def newElement(self,by,value) -> WebElement:
        '''
            创建一个新的元素对象
        :return: WebElement
        '''
        pass

    # ----------窗口操作-----------
    @abstractmethod
    def minWin(self):
        '''
        最小化窗口
        :return:
        '''
        pass

    @abstractmethod
    def maxWin(self):
        '''
        最大化窗口
        :return:
        '''
        pass

    @abstractmethod
    def resizeWin(self, w: int, h: int):
        '''
            自定义窗口大小
        :param w: 窗口宽度
        :param h: 窗口高度
        :return: self
        '''
        pass

    @abstractmethod
    def moreWin(self, index: int):
        '''
        多窗口切换
        :param index: 窗口下标
        :return: self
        '''
        pass

    @abstractmethod
    def nextWin(self):
        '''
        切换到下一个窗口
        :return: self
        '''
        return

    @abstractmethod
    def onWin(self):
        '''
        切换到上一个窗口
        :return: self
        '''
    # -----------------------------

    @abstractmethod
    def get(self, url: str, wait_time:float):
        '''
            输入网URL
            :param url: url
            :param wait_time: 等待时间
            :return: self
            url
            wait time
        '''
        pass

    @abstractmethod
    def send_keys(self, *value):
        '''

            :param *value: 文本或者图片路径
            :return: self
            text
        '''
        pass

    @abstractmethod
    def click(self):
        '''
            点击
            :return: self
        '''
        pass

    @abstractmethod
    def wait(self, wait_time:float):
        '''
            强制等待
            :param wait_time: 时间
            :return:
            Mandatory waiting
        '''
        pass

    @abstractmethod
    def implicitly_wait(self, wait_time:float):
        '''
            隐试等待
            :param wait_time: 时间
            :return: self
        '''
        pass

    # @abstractmethod
    # def pintStep(self) -> None:
    #     '''
    #         输出操作步骤
    #     :return: None
    #     '''

    @abstractmethod
    def clear(self):
        '''
            清除
        :return: self
        '''

    @abstractmethod
    def submit(self):
        '''
            提交
        :return: self
        '''
        pass

    # -----------属性方法---------
    @abstractmethod
    def driver(self) -> WebDriver:
        '''
            返回当前selenium驱动
            Returns the original driver object
        :return: selenium
        '''
        pass

    @abstractmethod
    def element(self) -> WebElement:
        '''
        返回通过方法定位后的对象
        :return: WebElement
        '''
        pass

    @abstractmethod
    def location(self) -> dict:
        pass

    @abstractmethod
    def elements(self) -> list:
        pass

    @abstractmethod
    def currentUrl(self) -> str:
        '''
            当前操作的url
            :return: str
            Url of the current operation
        '''
        pass

    @abstractmethod
    def currentTime(self, connector:str) -> str:
        '''
            返回当前时间
            Return current time
            :connector: 连接符
            :return: str
        '''
        pass

    @abstractmethod
    def text(self) -> str:
        '''
            获取元素文本
            :return: self
            Get element text
        '''
        pass

    @abstractmethod
    def value(self) -> str:
        '''
            获取属性中的value
        :return: self
        '''
        pass

    @abstractmethod
    def class_(self) -> str:
        '''
            获取属性中的class属性
        :return: self
        '''

    @abstractmethod
    def name_(self) -> str:
        '''
            获取属性中的name
        :return:
        '''

    @abstractmethod
    def title(self) -> str:
        '''
           网页标题
           :return: str
            page title
        '''
        pass
    # -------------------------

    # ------------处理内嵌框架-----
    @abstractmethod
    def frame(self):
        '''
        处理内嵌框架
        :return: self
        Processing framework
        '''

    @abstractmethod
    def defaultContent(self):
        '''
            切换默认文档
        :return: self
        Switching between default documents
        '''
        pass

    @abstractmethod
    def parentFrame(self):
        '''
            切换到父框架(上一层)
        :return: self
        Switch to parent frame (previous layer)
        '''
        pass
    # ------------------------

    # -----------处理弹窗---------
    @abstractmethod
    def alert(self):
        '''
        处理弹窗
        :return: self
        Handle the pop-up
        '''
        pass

    @abstractmethod
    def alertOK(self):
        '''
        接收弹窗
        :return: self
        Receive the pop-up
        '''
        pass

    @abstractmethod
    def alertNO(self):
        '''
        取消弹窗
        :return: self
        Cancel the popup window
        '''
        pass

    @abstractmethod
    def alertText(self) -> str:
        '''
        获取弹窗文本
        :return: str
        Gets popover text
        '''
        pass
    # -----------------------------

    @abstractmethod
    def save_screenshot(self, image_name: str, path: str, suffix: str):
        '''
        快照
        :param image_name:图片名称
        :param path:路径
        :param suffix:后缀
        :return:
        snapshot
        '''
        pass

    @abstractmethod
    def _posTemplate(self, by, value, text: str, wait_time:float, is_press:bool):
        '''

        :param by: 匹配方式
        :param value:值
        :param text: 输入文本
        :param wait_time: 等待时间
        :param is_press: 是否按下
        :return:
        '''
        pass

    @abstractmethod
    def _posTemplates(self,by,value,wait_time:float):
        pass

    # ----------------元素信息--------
    @abstractmethod
    def elementSize(self) -> dict:
        '''
        元素大小
        :return: dict
        '''
        pass

    @abstractmethod
    def elementWidth(self) -> int:
        '''
        元素宽度
        :return: int
        '''
        pass

    @abstractmethod
    def elementHeight(self) -> int:
        '''
        元素高度
        :return: int
        '''
        pass

    @abstractmethod
    def elementPos(self) -> dict:
        '''
        元素绝对位置
        :return: dict
        '''
        pass

    @abstractmethod
    def elementX(self) -> int:
        '''
        元素位置-X
        :return:
        '''
        pass

    # 元素当绝对位置y
    def elementY(self) -> int:
        '''
        元素位置-Y
        :return: int
        '''
        pass
    # --------------------------------

    @abstractmethod
    def getElementAttr(self, attribute, index: int) -> str:
        '''
        返回元素的属性
        :param attribute: 属性名称
        :param index: 元素下标
        :return: str
        '''
        pass

    @abstractmethod
    def isElementDisplayed(self) -> bool:
        '''
        判断元素是否可见
        :return: bool
        '''
        pass

    # -----------元素定位方式
    @abstractmethod
    def id(self,value,text:str,wait_time:float,is_press:bool):
        '''
        id查找
        :return: self
        '''
        pass

    @abstractmethod
    def xpath(self,value,text:str,wait_time:float,is_press:bool):
        '''
        XPATH查找
        :return: self
        '''
        pass

    @abstractmethod
    def className(self,value,text:str,wait_time:float,is_press:bool):
        '''
        className查找
        :return: self
        '''
        pass

    @abstractmethod
    def css(self,value,text:str,wait_time:float,is_press:bool):
        '''
        css查找
        :return: self
        '''
        pass

    @abstractmethod
    def tagName(self,value,text:str,wait_time:float,is_press:bool):
        '''
        TAG_NAME查找
        :return: self
        '''
        pass

    @abstractmethod
    def linkText(self,value,text:str,wait_time:float,is_press:bool):
        '''
        LINK_TEXT查找
        :return: self
        '''
        pass

    @abstractmethod
    def name(self,value,text:str,wait_time:float,is_press:bool):
        '''
        NAME查找
        :return:self
        '''
        pass

    @abstractmethod
    def partialLineText(self,value,text:str,wait_time:float,is_press:bool):
        '''

        PARTIAL_LINK_TEXT查找
        :return:self
        '''

    @abstractmethod
    def xpaths(self,value,wait_time:float):
        '''
            XPATH查找 多匹配
        :return: self
        '''

    @abstractmethod
    def csss(self,value,wait_time:float):
        '''
        css查找 多匹配
        :return: self
        '''

    @abstractmethod
    def classNames(self,value,wait_time:float):
        '''
        classNames多匹配
        :return: self
        '''

    @abstractmethod
    def tagNames(self,value,wait_time:float):
        '''
        TAG_NAME查找 多匹配
        :return: self
        '''
        pass

    @abstractmethod
    def linkTexts(self,value,wait_time:float):
       '''
       LINK_TEXT查找 多匹配
       :return: self
       '''
       pass

    @abstractmethod
    def names(self,value,wait_time:float):
        '''
        NAME查找 多匹配
        :return: self
        '''

    @abstractmethod
    def partialLineTexts(self,value,wait_time:float):
        '''
        PARTIAL_LINK_TEXT查找 多匹配
        :return: self
        '''
    # ----------------------------------------------

    @abstractmethod
    def exec_script(self, js: str, *args):
        '''
        执行脚本
        :param js: js代码
        :param args:
        :return: self
        '''
        pass

    @abstractmethod
    def exec_async_script(self, js, *args):
        '''
        执行异步脚本
        :param js: js代码
        :param args:
        :return: self
        '''
        pass

    @abstractmethod
    def source(self, encoding=None) -> str:
        '''
        网页源码
        :param encoding: 编码
        :return: str
        '''
        pass

    @abstractmethod
    def back(self):
        '''
        浏览器后退
        :return: self
        '''

    @abstractmethod
    def forward(self):
        '''
        浏览器前进
        :return: self
        '''

    @abstractmethod
    def refresh(self):
        '''
        刷新
        :return: self
        '''

    @abstractmethod
    def mouseClick_and_hold(self):
        '''
        按住左键不放
        :return: self
        '''

    @abstractmethod
    def mouseRelease(self):
        '''
        在某个元素位置松开左键
        :return: self
        '''

    @abstractmethod
    def mouseDoubleClick(self):
        '''
        双击鼠标左键
        :return: self
        '''

    @abstractmethod
    def mouseRightClick(self):
        '''
        鼠标右键按下
        :return: self
        '''

    @abstractmethod
    def mouseOffset(self,x:int,y:int):
        '''
        鼠标移动
        :param x: x
        :param y: y
        :return: self
        '''

    @abstractmethod
    def mouseToElement(self):
        '''
        鼠标移动到某个元素
        :return: self
        '''

    @abstractmethod
    def mouseDrag_And_Drop(self,target_element:WebElement):
        '''
        拖拽元素在到其它元素
        :param target_element: 目标元素
        :return: self
        '''
        pass

    @abstractmethod
    def mouseMove_To_Element_With_Offset(self,x:int,y:int):
        '''
        将鼠标移动到距某个元素多少距离的位置
        :param x: x
        :param y: y
        :return: self
        '''
        pass

    @abstractmethod
    def mouseDrag_And_By_Offset(self,x:int,y:int):
        '''
        拖拽到某个坐标然后松开
        :param x: x
        :param y: y
        :return: self
        '''

    # ------------多选框---------
    # @abstractmethod
    # def selectIndex(self,index:int):
    #     '''
    #     通过下标 匹配select菜单
    #     :param index: 下标
    #     :return: self
    #     '''
    #
    # @abstractmethod
    # def selectVisText(self, text: str):
    #     '''
    #     通过文本 匹配select菜单
    #     :param text: 文本
    #     :return: self
    #     '''
    #     pass
    #
    # @abstractmethod
    # def selectValue(self,value):
    #     '''
    #     通过select菜单里面的value匹配
    #     :param value: value属性值
    #     :return: self
    #     '''
    # ------------------------

    @abstractmethod
    def scroll(self,value:int=0):
        '''

        :param value: 滚动的数值
        :return:
        '''

    @abstractmethod
    def scrollBottom(self):
        '''
        滚动条到底端
        :return: self
        '''

    @abstractmethod
    def scrollTop(self):
        '''
        滚动条到顶端
        :return: self
        '''

    @abstractmethod
    def scrollLeftValue(self, value: int):
        '''
        滚动条向左移动
        :param value: 数值
        :return: self
        '''

    @abstractmethod
    def scrollRightValue(self, value: int):
        '''
        滚动条向右移动
        :param value: 数值
        :return: self
        '''

    @abstractmethod
    def scrollLeft(self):
        '''
        滚动条向左移动
        :return: self
        '''

    @abstractmethod
    def scrollRight(self):
        '''
        滚动条向右移动
        :return: self
        '''

    # @abstractmethod
    # def checkboxAll(self):
    #     '''
    #     处理checkbox 全选
    #     :return: self
    #     '''

    @abstractmethod
    def quit(self) -> None:
        '''
        关闭浏览器
        :return:
        '''
