import re
import math
from time import sleep, time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from lib.mysnowflake import IdWorker
from selenium import webdriver
from urllib import parse
import os

cookie_str = 'MS_LocalEmailAddr=laye0619@gmail.com=; ASP.NET_SessionId=0cix2b55qpodn555d0e0hq55; Hm_lvt_eca85e284f8b74d1200a42c9faa85464=1646530878,1647832258; MSCC=tiB/Pjhr3HE=; user=username=laye0619@gmail.com&nickname=laye0619&status=Free&memberId=458975&password=trWMrjKv97VkUvhSrVRdJw==; authWeb=3533FB8C0EF9D7DCD862EE04EC4AF013368C41532E616383894981585ADE15DC6BC9BB8190FE512E9DA7864993BB39F6F89B8D55FB22A5F942CCC30D310BC69F25AB4104F6A09B1C4B018F18E9EC8490155508C82DBD82A0105B61E19A7436FF474FE027398D675501161DFAB58EDAD80A6D3432; Hm_lpvt_eca85e284f8b74d1200a42c9faa85464=1647832296; AWSALB=UWQEIjEPcklG8mlC17YkKFwkTQq9dLZJbTprG2ThJru6WsIpSJQvK0YPhzoXSGw57CP3eb+AKDSaK/Z4jMOxKx4e0E1Z9fNe9uQkC3zFpzTinaMn70XCLIYHU2vg; AWSALBCORS=UWQEIjEPcklG8mlC17YkKFwkTQq9dLZJbTprG2ThJru6WsIpSJQvK0YPhzoXSGw57CP3eb+AKDSaK/Z4jMOxKx4e0E1Z9fNe9uQkC3zFpzTinaMn70XCLIYHU2vg'


def text_to_be_present_in_element(locator, text, next_page_locator):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """

    def _predicate(driver):
        try:
            element_text = driver.find_element_by_xpath(locator).text
            # 比给定的页码小的话，触发下一页
            if int(element_text) < int(text):
                print(element_text, text)
                next_page = driver.find_element_by_xpath(
                    next_page_locator)
                # driver.refresh()
                next_page.click()
                sleep(5)
                # 比给定的页码大的话，触发上一页
            elif int(element_text) > int(text):
                print(element_text, text)
                prev_page = driver.find_element_by_xpath(
                    '/html/body/form/div[8]/div/div[4]/div[3]/div[3]/div[1]/a[2]')
                # driver.refresh()
                prev_page.click()
                sleep(5)
            return text == element_text
        except:
            return False

    return _predicate


def get_fund_list():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('headless')
    chrome_driver = webdriver.Chrome(executable_path="./drivers/chromedriver", options=chrome_options)
    chrome_driver.set_page_load_timeout(12000)  # 防止页面加载个没完

    morning_fund_selector_url = "https://www.morningstar.cn/fundselect/default.aspx"
    set_cookies(chrome_driver, morning_fund_selector_url, cookie_str)

    existed_df = pd.read_csv('./output/fund_morning_star.csv', dtype={'代码': str})
    if existed_df.empty:
        page_num = 1
    else:
        page_num = existed_df.iloc[-1]['页码'] + 1
    page_count = 25
    page_num_total = math.ceil(
        int(chrome_driver.find_element(
            by=By.XPATH,
            value='/html/body/form/div[8]/div/div[4]/div[3]/div[2]/span'
        ).text) / page_count
    )

    output_head = '代码' + ',' + '晨星专属号' + ',' + '名称' + ',' + \
                  '类型' + ',' + '三年评级' + ',' + '五年评级' + ',' + '今年回报率' + ',' + '页码' + '\n'
    # 设置表头
    if page_num == 1:
        with open('./output/fund_morning_star.csv', 'w+') as csv_file:
            csv_file.write(output_head)
    while page_num <= page_num_total:
        # 求余
        remainder = page_num_total % 10
        # 判断是否最后一页
        num = (remainder +
               2) if page_num > (page_num_total - remainder) else 12
        xpath_str = '/html/body/form/div[8]/div/div[4]/div[3]/div[3]/div[1]/a[%s]' % (
            num)
        print('page_num', page_num)
        # 等待，直到当前页（样式判断）等于page_num
        WebDriverWait(chrome_driver, timeout=600).until(text_to_be_present_in_element(
            "/html/body/form/div[8]/div/div[4]/div[3]/div[3]/div[1]/span[@style='margin-right:5px;font-weight:Bold;color:red;']",
            str(page_num), xpath_str))
        sleep(1)
        # 列表用于存放爬取的数据
        id_list = []  # 雪花id
        code_list = []  # 基金代码
        morning_star_code_list = []  # 晨星专属代码
        name_list = []  # 基金名称
        fund_cat = []  # 基金分类
        fund_rating_3 = []  # 晨星评级（三年）
        fund_rating_5 = []  # 晨星评级（五年）
        rate_of_return = []  # 今年以来汇报（%）

        # 获取每页的源代码
        data = chrome_driver.page_source
        # 利用BeautifulSoup解析网页源代码
        bs = BeautifulSoup(data, 'lxml')
        class_list = ['gridItem', 'gridAlternateItem']  # 数据在这两个类下面

        # 取出所有类的信息，并保存到对应的列表里
        for i in range(len(class_list)):
            for tr in bs.find_all('tr', {'class': class_list[i]}):
                # 雪花id
                worker = IdWorker()
                id_list.append(worker.get_id())
                tds_text = tr.find_all('td', {'class': "msDataText"})
                tds_nume = tr.find_all('td', {'class': "msDataNumeric"})
                # 基金代码
                code_a_element = tds_text[0].find_all('a')[0]
                code_list.append(code_a_element.string)
                # 从href中匹配出晨星专属代码
                current_morning_code = re.findall(
                    r'(?<=/quicktake/)(\w+)$', code_a_element.get('href')).pop(0)
                # 晨星基金专属晨星码
                morning_star_code_list.append(current_morning_code)
                name_list.append(tds_text[1].find_all('a')[0].string)
                # 基金分类
                fund_cat.append(tds_text[2].string)
                # 三年评级
                rating = get_star_count(tds_text[3].find_all('img')[0]['src'])
                fund_rating_3.append(rating)
                # 5年评级
                rating = get_star_count(tds_text[4].find_all('img')[0]['src'])
                fund_rating_5.append(rating)
                # 今年以来回报(%)
                return_value = tds_nume[3].string if tds_nume[3].string != '-' else None
                rate_of_return.append(return_value)

        print('数据准备完毕')
        fund_df = pd.DataFrame(
            {
                'id': id_list,
                'fund_code': code_list,
                'morning_star_code': morning_star_code_list,
                'fund_name': name_list,
                'fund_cat': fund_cat,
                'fund_rating_3': fund_rating_3,
                'fund_rating_5': fund_rating_5,
                'rate_of_return': rate_of_return,
                'page_number': page_num
            })
        fund_list = fund_df.values.tolist()
        print('fund_list', fund_list)
        with open('./output/fund_morning_star.csv', 'a') as csv_file:
            for fund_item in fund_list:
                output_line = ','.join(str(x) for x in fund_item) + '\n'
                csv_file.write(output_line)

        # 获取下一页元素
        next_page = chrome_driver.find_element_by_xpath(
            xpath_str)
        # 点击下一页
        next_page.click()
        page_num += 1
    chrome_driver.close()
    print('end')


def parse_cookiestr(cookie_str, split_str="; "):
    cookielist = []
    for item in cookie_str.split(split_str):
        cookie = {}
        itemname = item.split('=')[0]
        iremvalue = item.split('=')[1]
        cookie['name'] = itemname
        cookie['value'] = parse.unquote(iremvalue)
        cookielist.append(cookie)
    return cookielist


def set_cookies(chrome_driver, url, cookie_str):
    chrome_driver.get(url)
    # 2.需要先获取一下url，不然使用add_cookie会报错，这里有点奇怪
    cookie_list = parse_cookiestr(cookie_str)
    chrome_driver.delete_all_cookies()
    for i in cookie_list:
        cookie = {}
        # 3.对于使用add_cookie来说，参考其函数源码注释，需要有name,value字段来表示一条cookie，有点生硬
        cookie['name'] = i['name']
        cookie['value'] = i['value']
        # 4.这里需要先删掉之前那次访问时的同名cookie，不然自己设置的cookie会失效
        # chrome_driver.delete_cookie(i['name'])
        # 添加自己的cookie
        # print('cookie', cookie)
        chrome_driver.add_cookie(cookie)
    chrome_driver.refresh()


def get_star_count(morning_star_url):
    import numpy as np
    import requests
    from PIL import Image
    module_path = os.path.dirname(__file__)
    temp_star_url = module_path + '/assets/star/tmp.gif'
    r = requests.get(morning_star_url)
    with open(temp_star_url, "wb") as f:
        f.write(r.content)
    f.close()
    path = module_path + '/assets/star/star'

    # path = './assets/star/star'
    for i in range(6):
        p1 = np.array(Image.open(path + str(i) + '.gif'))
        p2 = np.array(Image.open(temp_star_url))
        if (p1 == p2).all():
            return i


def login_site(chrome_driver, site_url, redirect_url=None):
    site_url = site_url if redirect_url == None else site_url + '?ReturnUrl=' + redirect_url
    chrome_driver.get(site_url)
    sleep(2)
    from selenium.webdriver.support import expected_conditions as EC
    username = chrome_driver.find_element_by_id('emailTxt')
    password = chrome_driver.find_element_by_id('pwdValue')
    check_code = chrome_driver.find_element_by_id('txtCheckCode')
    username.send_keys('18219112108@163.com')
    password.send_keys('w780880')
    count = 1
    flag = True
    while count < 10 and flag:
        code = identify_verification_code(chrome_driver)
        check_code.clear()
        time.sleep(1)
        check_code.send_keys(code)
        time.sleep(3)
        submit = chrome_driver.find_element_by_id('loginGo')
        submit.click()
        # 通过弹窗判断验证码是否正确
        time.sleep(3)
        from selenium.webdriver.common.by import By
        # message_container = chrome_driver.find_element_by_id('message-container')
        try:
            message_box = chrome_driver.find_element_by_id(
                'message-container')
            flag = message_box.is_displayed()
            if flag:
                close_btn = message_box.find_element(
                    By.CLASS_NAME, "modal-close")
                close_btn.click()
                time.sleep(1)
            print('flag', flag)

        except:
            return True

    if count > 10:
        return False
    return True


if __name__ == "__main__":
    fund_list = get_fund_list()
