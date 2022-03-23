#!/usr/bin/env python
# pylint: disable=no-value-for-parameter
import os
import sys

import click
import requests
from wechatpy import WeChatClient

from wxcloud.apis import CollectionAdd, CollectionQuery, Query

from .officialaccount import OfficialAccount
from .tools import filter_existed_data, read_from_file


@click.group()
def cli():
    """This is the root command"""

@cli.command()
@click.option('--data', default='data/20200823-special.json', show_default=True, help='specify a scraped-json data file')
@click.option('--env', default=lambda: os.environ.get('WX_ENV', 'dev-f7e8f5'), show_default='Environment variable: WX_ENV', help='WeChat Mini Program env variable')
@click.option('--appid', default=lambda: os.environ.get('WX_APPID', None), show_default='Environment variable: WX_APPID', required=True, help='WeChat Mini Program app id')
@click.option('--secret', default=lambda: os.environ.get('WX_SECRET', None), show_default='Environment variable: WX_SECRET', required=True, help='WeChat Mini Program app secret')
@click.option('--after', default='2020/05/01', show_default=True, help='Any latest data before this date can be included')
@click.option('--tag', default='VOA Special English', show_default=True, help='Manually maintain the data tags')
def miniprogram(data, env, appid, secret, after, tag):
    """[WeChat Mini Program] Operator"""
    c = CollectionQuery('posts', 'digest')
    read_from_file(c, data, after, tag)

    q = Query(env, c)
    text = q.decode()

    r = requests.get(f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}')
    ak = r.json()['access_token']

    r = requests.post(f'https://api.weixin.qq.com/tcb/databasequery?access_token={ak}', data=text)
    results = r.json()['data']
    excludes = filter_existed_data(results, c.data)

    c = CollectionAdd('posts')
    c.data = excludes
    q = Query(env, c)
    text = q.decode()

    r = requests.post(f'https://api.weixin.qq.com/tcb/databaseadd?access_token={ak}', data=text)
    print(r.json())
    
@cli.command()
@click.option('--data', default='data/20200823-special.json', show_default=True, help='specify a scraped-json data file')
@click.option('--appid', default=lambda: os.environ.get('WX_APPID', None), show_default='Environment variable: WX_APPID', required=True, help='WeChat Mini Program app id')
@click.option('--secret', default=lambda: os.environ.get('WX_SECRET', None), show_default='Environment variable: WX_SECRET', required=True, help='WeChat Mini Program app secret')
def officialaccount(data,appid,secret):
    """[WeChat Official Account] Operator"""
    client = WeChatClient(appid, secret)
    oa = OfficialAccount(client)
    oa.articleUpload(data)

@cli.command()
@click.option('--appid', default=lambda: os.environ.get('WX_APPID', None), show_default='Environment variable: WX_APPID', required=True, help='WeChat Mini Program app id')
@click.option('--secret', default=lambda: os.environ.get('WX_SECRET', None), show_default='Environment variable: WX_SECRET', required=True, help='WeChat Mini Program app secret')
def alphabet(appid,secret):
    """[WeChat Official Account] Print the available alphabet"""
    client = WeChatClient(appid, secret)
    oa = OfficialAccount(client)
    alphabet = oa.getAlphabet()
    print(alphabet)

if __name__ == '__main__':
    sys.exit(cli())

