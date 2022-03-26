
import os, sys, getopt

import re
import json
import requests
import random
import hashlib

from unittest import result
from collections import namedtuple
from termcolor import cprint
from urllib.parse import quote

appid = '20220325001140552'
secretKey = 'LiIWn_rNJrbLErVu6sGT'

def get_myurl(word,fromLang='auto',toLang = 'zh'):   
        salt = random.randint(32768, 65536)
        sign = appid + word + str(salt) + secretKey
        myMd5 = hashlib.md5()
        myMd5.update(sign.encode("utf-8"))
        sign = myMd5.hexdigest()
        yield '/api/trans/vip/translate'+'?appid='+appid+'&q='+quote(word)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

def get_translate_word(url):
    try:
        response = requests.get('http://api.fanyi.baidu.com' + url)
        return response.json()
    except Exception as e:
        pass


def get_response(word):
    for u in get_myurl(word):
        get_translate_word(u)

#显示函数
def show(response):
    for item in response['trans_result']:
        cprint (item['dst'], 'green')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], ["help"])
        #获取命令行输入
    except getopt.GetoptError :
        pass

    match = re.findall(r'[\w.]+', " ".join(args).lower())
    word = " ".join(match)
    response = get_response(word)
    if not response:
        return
    show(response)


if __name__ == '__main__':
    main()
