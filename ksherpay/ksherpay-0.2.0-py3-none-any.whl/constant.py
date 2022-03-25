from collections import namedtuple

_apiType = namedtuple('API_TYPE', 'REDIRECT CSCANB BSCANC MINIAPP APP FINANCE')
API_TYPE = _apiType('/redirect','/cscanb','/bscanc','/miniapp','/app','/finance')