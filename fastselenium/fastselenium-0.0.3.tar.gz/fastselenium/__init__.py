#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pyperclip
import platform
import showlog
import time
import json
try_times_default = 100  # 默认重试次数


def save_cookie(
        driver,
        file_name: str = 'cookies.txt'
):
    """
    暂存cookie到本地
    """
    cookies = driver.get_cookies()
    with open(file_name, "w") as fp:
        json.dump(cookies, fp)


def read_cookie(
        driver,
        url,
        pop_list: list = None,
        file_name: str = 'cookies.txt'
):
    """
    从本地文件读取cookie并加载到指定页面
    """
    driver.get(url)
    driver.delete_all_cookies()
    with open(file_name, "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            print(cookie)
            if pop_list is not None:
                for each in pop_list:
                    cookie.pop(each)  # 如果报domain无效的错误
            if cookie.get("expiry") is not None:
                del cookie['expiry']
            driver.add_cookie(cookie)
    driver.get(url)


def click(
        driver,
        css_selector: str = None,  # 第1优先
        xpath: str = None,  # 第2优先
        try_times: int = try_times_default
):
    local_try_times = 0
    while local_try_times < try_times:
        try:
            if css_selector is not None:
                driver.find_element_by_css_selector(css_selector).click()
                return driver
            elif xpath is not None:
                driver.find_element_by_xpath(xpath).click()
                return driver
            else:
                return
        except:
            local_try_times += 1
            showlog.error('%s/%s retry in 1s ...' % (local_try_times, try_times))
            time.sleep(1)
    return


def send_keys(
        driver,
        keys: str = '',
        css_selector: str = None,  # 第1优先
        xpath: str = None,  # 第2优先
        try_times: int = try_times_default
):
    local_try_times = 0
    while local_try_times < try_times:
        try:
            if css_selector is not None:
                driver.find_element_by_css_selector(css_selector).send_keys(keys)
                return driver
            elif xpath is not None:
                driver.find_element_by_xpath(xpath).send_keys(keys)
                return driver
            else:
                return
        except:
            local_try_times += 1
            showlog.error('%s/%s retry in 1s ...' % (local_try_times, try_times))
            time.sleep(1)
    return


def paste_by_xpath(
        driver,
        xpath: str = '',
        keys: str = ''
):
    # 尝试清除内容后粘贴，不适用于linux
    import pyautogui  # 在无GUI界面的Linux系统中会出现KeyError: 'DISPLAY'的问题，未解决
    while True:
        try:
            driver.find_element_by_xpath(xpath).click()
            if platform.system() == 'Darwin':
                pyautogui.hotkey('command', 'a')
                pyautogui.press('delete')
                pyperclip.copy(keys)
                pyautogui.hotkey('command', 'v')
            elif platform.system() == 'Windows':
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('delete')
                pyperclip.copy(keys)
                pyautogui.hotkey('ctrl', 'v')
            else:
                print('未知平台！')
            break
        except:
            time.sleep(1)


def wait_for_xpath(
        driver,
        xpath: str = '',
        wait_sec: int = 60
):
    try:
        WebDriverWait(driver, wait_sec).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except:
        print('元素加载失败')
        return False


def wait_for_url(
        driver,
        url: str = '',
        wait_sec: int = 60
):
    try:
        WebDriverWait(driver, wait_sec).until(
            expected_conditions.url_to_be(url)
        )
        return True
    except:
        print('未匹配到正确的url')
        return False


def do_slide(
        driver,
        track: list,  # 滑动轨迹
        class_name: str = None,
        id_str: str = None,
        find_by: str = None,
        find_value: str = None
):
    """
    按照提供的track滑动
    """
    if class_name is not None:
        slider = driver.find_element_by_class_name(class_name)
    elif id_str is not None:
        slider = driver.find_element_by_id(class_name)
    elif find_by is not None and find_value is not None:
        slider = driver.find_element(by=find_by, value=find_value)
    else:
        return False
    action = ActionChains(driver)
    action.click_and_hold(slider).perform()
    for x in track:
        action.move_by_offset(xoffset=x, yoffset=0).perform()
        action = ActionChains(driver)  # 新建ActionChains对象防止累加位移
    time.sleep(0.5)
    ActionChains(driver).release().perform()
    return driver
