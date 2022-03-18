         
import io
import os
import re
import attr
import urllib
import logging
import json
import requests
from requests.adapters import HTTPAdapter
try:
    import ujson as json
except:
    import json

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)

class BaseAPI(object):
    DEFAULT_URL = 'https://cryptounifier.io/api/v1/'

    def __init__(self, suffix, headers, timeout=None, connection_timeout=None, max_retries=None, 
                     proxies=None, verify=False, **kwargs): 
        self.suffix = suffix
        self._headers = headers or {} 
        
        self._url = self.setApiUrl(self.DEFAULT_URL)   
             

    def setApiUrl(self, defaultUrl):    
        if defaultUrl[-1] != '/':
            defaultUrl += '/'
        return urllib.parse.urljoin(defaultUrl, self.suffix)

    def create_session(self):
        session = requests.Session()
        session.headers.update(self._headers)
        return session

    @property
    def http(self):
        return self.create_session()

    @staticmethod
    def _prepare_kwargs(method, args, kwargs): 
        if method == 'POST':
            kwargs['json'] = args[1]
        else:
            kwargs['params'] = json.dumps(args[1]) if len(args) > 1 else {}         
        kwargs['timeout'] = None           
        kwargs['verify'] = False

    def executeRequest(self, method, *args, **kwargs):                    
        url = self._url + '/' + args[0]   
        headers = dict(self.http.headers)
        response = None             
        try:
            self._prepare_kwargs(method, args, kwargs)                        
            response = self.http.request(method, url=url, **kwargs)  
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            logger.debug('Error getting response from ' + url, exc_info=True)
            status_code = response.status_code if response is not None else 0
            error_msg = response.content.decode('utf-8') if response is not None else str(e)
            return ApiResult(url, {}, {'error': error_msg}, headers, 'error', status_code=status_code)
        status_code = response.status_code
        try:                      
            return response.json()
        except ValueError as e:
            logger.debug('Error parsing JSON response from '+url+'. Response: ' + str(response.content), exc_info=True)
            return ApiResult(
                url, {}, {'error': str(e), 'response': response.content.decode('utf-8')}, headers, 'error',
                status_code=status_code
            )        


@attr.s
class ApiResult(object):
    """
    Response returned form ML API
    """
    url = attr.ib(default='')
    request = attr.ib(default='')
    response = attr.ib(default=attr.Factory(dict))
    headers = attr.ib(default=attr.Factory(dict))
    type = attr.ib(default='ok')
    status_code = attr.ib(default=200)

    @property
    def is_error(self):        
        return self.status_code != 200

    @property
    def error_message(self):
        return self.response.get('error')