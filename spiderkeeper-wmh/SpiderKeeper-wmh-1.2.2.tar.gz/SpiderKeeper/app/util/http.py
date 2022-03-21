import logging

import requests
from requests.auth import HTTPBasicAuth


def request_get(url, retry_times=5):
    '''
    :param url:
    :param retry_times:
    :return: response obj
    '''
    from SpiderKeeper.app import app
    username = app.config.get("SCRAPYD_BASIC_AUTH_USERNAME")
    password = app.config.get("SCRAPYD_BASIC_AUTH_PASSWORD")

    for i in range(retry_times):
        try:
            res = requests.get(url, auth=HTTPBasicAuth(username, password))
        except Exception as e:
            logging.warning('request error retry %s' % url)
            continue
        return res


def request_post(url, data, retry_times=5):
    '''
    :param url:
    :param retry_times:
    :return: response obj
    '''
    from SpiderKeeper.app import app
    username = app.config.get("SCRAPYD_BASIC_AUTH_USERNAME")
    password = app.config.get("SCRAPYD_BASIC_AUTH_PASSWORD")

    for i in range(retry_times):
        try:
            res = requests.post(url, data, auth=HTTPBasicAuth(username, password))
        except Exception as e:
            logging.warning('request error retry %s' % url)
            continue
        return res


def request(request_type, url, data=None, retry_times=5, return_type="text"):
    '''

    :param request_type: get/post
    :param url:
    :param data:
    :param retry_times:
    :param return_type: text/json
    :return:
    '''
    if request_type == 'get':
        res = request_get(url, retry_times)
    if request_type == 'post':
        res = request_post(url, data, retry_times)
    if not res: return res
    if return_type == 'text': return res.text
    if return_type == 'json':
        try:
            res = res.json()
            return res
        except Exception as e:
            logging.warning('parse json error %s' % str(e))
            return None
