import json
import chardet
from bs4 import BeautifulSoup
from scan.common import logger


class Response:
    def __init__(self, req_resp):
        self.req_resp = req_resp
        self.status_code = req_resp.status_code
        # self.content = req_resp.content

    def json(self):
        try:
            return json.loads(self.req_resp.content)
        except Exception as e:
            logger.error(f'格式化json异常:{e}, 数据:{self.req_resp.content}')

    def soup(self):
        try:
            soup = BeautifulSoup(self.req_resp.content, 'lxml')
            return soup
        except Exception as e:
            logger.error(f'格式化soup异常:{e}, 数据:{self.req_resp.content}')

    def text(self):
        try:
            return self.req_resp.content.decode()
        except UnicodeDecodeError:
            try:
                encoding = chardet.detect(self.req_resp.content).get('encoding')
                return self.req_resp.content.decode(encoding)
            except Exception as e:
                logger.error(f'格式化text异常:{e}, 数据:{self.req_resp.content}')
        except Exception as e:
            logger.error(f'格式化text异常:{e}, 链接:{self.req_resp.url}')

    def content(self):
        try:
            content = self.req_resp.content
            return content
        except Exception as e:
            logger.error(f'获取content异常:{e}')



