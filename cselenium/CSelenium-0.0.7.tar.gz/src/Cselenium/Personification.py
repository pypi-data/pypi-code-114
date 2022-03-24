'''

    自动化操作 拟人化
'''
import random
from src.Cselenium.RandomData import RandomData
from Cselenium.CSelenium import ChromeSelenium
import pyautogui
from selenium.webdriver.remote.webdriver import WebDriver


# 拟人自动化操作类
class PersonificationAuto(ChromeSelenium):
    def __init__(self, url: str = None, is_interface: bool = True, executable_path="chromedriver",
                 info_tracking: bool = False, log: [str, bool] = "", ignore_err: bool = True, wait_time: float = 1.0,
                 driver: WebDriver = None):
        super().__init__(url, is_interface, executable_path, info_tracking, log, ignore_err, wait_time, driver)

        self.__random_obj = RandomData()

    def __randomMove(self) -> None:
        # 在随机时间内移动到当前元素位置
        pos=self.elementPos()
        x, y = pos["x"],pos["y"]
        pyautogui.moveTo(x, y, self.__random_obj.randomTimeInt())

    def id(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        super().id(value, text, wait_time, is_press)
        self.implicitly_wait()
        self.__randomMove()
        return self

    def xpath(self, value, text: str = None, wait_time: float = 0.0, is_press=False):
        super().xpath(value, text, wait_time, is_press)
        self.__randomMove()
        return self

    def click(self):
        pyautogui.click(button='left')
        self.wait(self.__random_obj.randomTimeInt())
        return self

    def send_keys(self, *value):
        pyautogui.typewrite(*value,interval=self.__random_obj.randomTimeFloat())
        self.wait(self.__random_obj.randomTimeInt(1,2))
        return self

    # 键盘上键
    def keyUp(self):
        pyautogui.keyDown("up")
        return self

    # 键盘下键
    def keyDown(self):
        pyautogui.keyDown("down")
        return self

    # 进行n次随机上下键操作
    def randomUpDown(self,number:int=4):
        up_down = [self.keyUp, self.keyDown]
        for i in range(number):
            e_f = random.choice(up_down)
            self.wait(self.__random_obj.randomTimeFloat())
            e_f()
        return self
