from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def wait_ele(driver, xpath, ts=10):
    try:
        WebDriverWait(driver, ts).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except Exception:
        pass


def my_wait(driver, xpath, ts=10):
    for i in range(ts):
        try:
            driver.find_element_by_xpath(xpath)
        except Exception:
            time.sleep(1)
        else:
            return True
    return False


def driver_safe_find_element_by_xpath(driver, ele_xpath):
    try:
        return driver.find_element_by_xpath(ele_xpath)
    except NoSuchElementException:
        return None


def driver_safe_find_elements_by_xpath(driver, ele_xpath):
    try:
        return driver.find_elements_by_xpath(ele_xpath)
    except NoSuchElementException:
        return None


def drive_wait_element_by_xpath(driver, ele_xpath, ts=10):
    my_wait(driver, ele_xpath, ts)
    return driver_safe_find_element_by_xpath(driver, ele_xpath)


def ele_safe_find_element_by_xpath(ele, ele_xpath):
    try:
        return ele.find_element_by_xpath(ele_xpath)
    except NoSuchElementException:
        return


def isclickable(driver,xpath):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        return True
    except :
        return False


if __name__ == '__main__':
   pass
