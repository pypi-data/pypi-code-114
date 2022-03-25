from requests import Request, Session
import datetime
import time
import hmac, hashlib
import logging
import json
from .constant import API_TYPE
from .utils import Utils

class Order(object):
    # BASE_URL = 'http://sandbox.lan:9000/'

    def __init__(self, base_url, apiType=API_TYPE.REDIRECT ,token=None, provider='Ksher', mid=None, timeout=10, verify=True):
        self.token = token
        self.provider = provider
        self.mid = mid
        self.base_url = base_url
        self.orderApi = '/api/v1' + apiType + '/orders'
        self.timeout = timeout
        self.verify = verify
        self.utils = Utils()

    def create(self, data):
        endpoint = self.orderApi
        if self.mid:
            data['mid'] = self.mid
        return self.utils._request(method='POST', base_url=self.base_url, endpoint=endpoint, data=data, token=self.token, timeout=self.timeout, verify=self.verify)

    def query(self, order_id, params={}):
        endpoint = self.orderApi + '/{}'.format(order_id)
        if self.mid:
            params['mid'] = self.mid
        return self.utils._request(method='GET', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)

    def refund(self, order_id, params={}):
        endpoint = self.orderApi + '/{}'.format(order_id)
        if self.mid:
            params['mid'] = self.mid
        return self.utils._request(method='PUT', base_url=self.base_url, endpoint=endpoint, data=params, token=self.token, timeout=self.timeout, verify=self.verify)

    def cancel(self, order_id):
        endpoint = self.orderApi + '/{}'.format(order_id)
        return self.utils._request(method='DELETE', base_url=self.base_url, endpoint=endpoint, data={}, token=self.token, timeout=self.timeout, verify=self.verify)

    def _request(self, method, endpoint, data = {}):
        method = method.upper()
        if self.mid:
            data['mid'] = self.mid
        data['timestamp'] = str(self._make_timestamp())
        # data['provider'] = self.provider
        data['signature'] = self._make_sign(endpoint,data)
        url = self.base_url + endpoint
        if method == "GET":
            headers =  {"Accept": "application/json" }
            req = Request(method, url, headers=headers, params=data)
        else:
            headers =  {"Content-Type": "application/json",}
            req = Request(method, url, headers=headers, json=data)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped, timeout=self.timeout)
        s.close()

        if (resp.status_code == 200) and self.verify:
            data = resp.json()
            isValid = self.checkSignature(endpoint, data)
            if not isValid:
                resp_data = {
                    'force_clear': False, 
                    'cleared': False, 
                    'error_code': '"VERIFY_KSHER_SIGN_FAIL', 
                    'error_message': 'verify signature failed',
                    'locked': False
                }
                resp._content =  json.dumps(resp_data).encode('utf-8')

        return resp

    def generate_order_id(self, orderName='OrderAt'):
        curTime = datetime.datetime.now()
        timeStr = curTime.strftime('%Y%m%dT%H%M%S')
        orderName ='{}{}'.format(orderName, timeStr)
        return orderName

    def _make_timestamp(self):
        return int(time.time())

    # def _check_sign(self, sign):
        
    def _make_sign(self, url, data):
        # make sure it's is not include a signature value
        data.pop('signature', None)
        # data.pop('channel_list', None)
        sort_list = sorted(data)
        dataStr = url + ''.join(f"{key}{data[key]}" for key in sort_list)
        # print("data for making signanuture:{}".format(dataStr))
        dig = hmac.new(self.token.encode(), msg=dataStr.encode(), digestmod=hashlib.sha256).hexdigest()
        return dig.upper()

    def checkSignature(self, url, data):
        """
        input: data(dict)
        output return true when the signature is valid
        """
        signature = data.pop('signature',None)

        # log_entry_url is not include in make_signature process
        data.pop('log_entry_url',None)
        
        if not signature:
            return False
        dig = self._make_sign(url, data)
        return signature == dig
