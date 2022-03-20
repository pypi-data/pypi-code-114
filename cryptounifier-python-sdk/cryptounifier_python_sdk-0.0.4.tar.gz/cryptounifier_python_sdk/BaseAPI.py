         
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
        self._prepare_kwargs(method, args, kwargs) 
                     
        response = self.http.request(method, url=url, **kwargs)  
        return response.json()


       