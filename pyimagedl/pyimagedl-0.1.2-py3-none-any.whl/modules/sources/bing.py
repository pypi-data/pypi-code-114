'''
Function:
    必应图片搜索和下载类
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import re
import math
import threading
from lxml import etree
from urllib.parse import quote
from alive_progress import alive_bar
from .base import BaseImageDownloader


'''必应图片搜索和下载类'''
class BingImageDownloader(BaseImageDownloader):
    def __init__(self, auto_set_proxies=True, auto_set_headers=True, **kwargs):
        super(BingImageDownloader, self).__init__(auto_set_proxies=auto_set_proxies, auto_set_headers=auto_set_headers, **kwargs)
        self.source_name = 'bing'
    '''搜索'''
    def search(self, keyword, search_limits=1000, num_threadings=5):
        # 构建所有urls
        base_url = 'https://cn.bing.com/images/async?q={}&first={}&count={}&cw=1536&ch=240&relp={}&tsc=ImageBasicHover&datsrc=I&layout=RowBased&mmasync=1&dgState=x*1063_y*768_h*186_c*5_i*71_r*10&IG=D6A4AD486F3A49F1BE164BC50750D641&SFX=3&iid=images.5555'
        search_urls, pagesize = [], 35
        for pn in range(math.ceil(search_limits * 1.2 / pagesize)):
            search_url = base_url.format(quote(keyword), pn * pagesize, pagesize, pagesize)
            search_urls.append(search_url)
        # 多线程请求获取所有图片链接
        def searchapi(self, search_urls, image_urls, bar):
            while len(search_urls) > 0:
                search_url = search_urls.pop(0)
                response = self.get(search_url)
                if response is None: 
                    bar()
                    continue
                html = etree.HTML(response.text)
                for link in html.xpath('//a[@class="iusc"]/@m'):
                    image_urls.add(re.search('"murl":"(.*?)"', link).group(1))
                bar()
        task_pool, image_urls = [], set()
        with alive_bar(min(len(search_urls), search_limits)) as bar:
            for idx in range(num_threadings):
                task = threading.Thread(
                    target=searchapi,
                    args=(self, search_urls, image_urls, bar)
                )
                task_pool.append(task)
                task.start()
            for task in task_pool: task.join()
        # 返回结果
        return list(image_urls)[:search_limits]