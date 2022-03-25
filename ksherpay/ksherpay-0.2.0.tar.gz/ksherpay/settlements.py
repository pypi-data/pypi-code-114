from .constant import API_TYPE
from .utils import Utils


class Settlements(object):
    # BASE_URL = 'http://sandbox.lan:9000/'

    def __init__(self, base_url, apiType=API_TYPE.FINANCE, token=None, provider='Ksher', mid=None, timeout=10, verify=True):
        self.token = token
        self.provider = provider
        self.mid = mid
        self.base_url = base_url
        self.settlementsApi = '/api/v1' + apiType + '/settlements'
        self.timeout = timeout
        self.verify = verify
        self.utils = Utils()

    def channels(self, params={}):
        endpoint = self.settlementsApi + '/channels'
        return self.utils._request(method='GET', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)

    def order(self, yyyymmdd, params={}):
        endpoint = self.settlementsApi + '/order' + '/{}'.format(yyyymmdd)
        return self.utils._request(method='GET', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)

    def settlements(self, yyyymmdd, params={}):
        endpoint = self.settlementsApi + '/{}'.format(yyyymmdd)
        return self.utils._request(method='GET', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)

    def settlement_order(self, params={}):
        endpoint = self.settlementsApi + '/settlement_order'
        return self.utils._request(method='GET', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)
