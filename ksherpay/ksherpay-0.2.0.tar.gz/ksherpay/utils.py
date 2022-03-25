from requests import Request, Session
import datetime
import time
import hmac
import hashlib
import logging
import json


class Utils(object):

    def _request(self, method, base_url, endpoint, data={}, token="", timeout=10, verify=True):
        method = method.upper()
        data['timestamp'] = str(self._make_timestamp())
        # data['provider'] = self.provider
        data['signature'] = self._make_sign(endpoint, data, token=token)
        url = base_url + endpoint
        if method == "GET":
            headers = {"Accept": "application/json"}
            req = Request(method, url, headers=headers, params=data)
        else:
            headers = {"Content-Type": "application/json", }
            req = Request(method, url, headers=headers, json=data)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped, timeout=timeout)
        s.close()

        if (resp.status_code == 200) and verify:
            data = resp.json()
            isValid = self.checkSignature(endpoint, data, token=token)
            if not isValid:
                resp_data = {
                    'force_clear': False,
                    'cleared': False,
                    'error_code': '"VERIFY_KSHER_SIGN_FAIL',
                    'error_message': 'verify signature failed',
                    'locked': False
                }
                resp._content = json.dumps(resp_data).encode('utf-8')

        return resp

    def generate_order_id(self, orderName='OrderAt'):
        curTime = datetime.datetime.now()
        timeStr = curTime.strftime('%Y%m%dT%H%M%S')
        orderName = '{}{}'.format(orderName, timeStr)
        return orderName

    def _make_timestamp(self):
        return int(time.time())

    def _make_sign(self, url, data, token):
        # make sure it's is not include a signature value
        data.pop('signature', None)
        # data.pop('channel_list', None)
        sort_list = sorted(data)
        dataStr = url + ''.join(f"{key}{data[key]}" for key in sort_list)
        # print("data for making signanuture:{}".format(dataStr))
        dig = hmac.new(token.encode(), msg=dataStr.encode(),
                       digestmod=hashlib.sha256).hexdigest()
        return dig.upper()

    def checkSignature(self, url, data, token):
        """
        input: data(dict)
        output return true when the signature is valid
        """
        signature = data.pop('signature', None)

        # log_entry_url is not include in make_signature process
        data.pop('log_entry_url', None)

        if not signature:
            return False
        dig = self._make_sign(url=url, data=data, token=token)
        return signature == dig
