import json
import requests
from .base import ATF_LOGGER, ApcKind, AuthError, NullAuth

class Cs141(ApcKind):
    def fetch(self, user: str, password: str):
        base_url = F'http://{self._host}/api'
        upsst = None

        with requests.Session() as s:
            s.auth = NullAuth()
            headers = {
                'content-type': 'application/json',
            }
            lgdat = {
                'userName': user,
                'password': password,
                'anonymous': '',
                'newPassword': '',
            }
            r = self.urlway(0, base_url + '/login', s.post, headers = headers, data = json.dumps(lgdat))
            rj = r.json()
            if 'message' in rj:
                raise AuthError(rj['message'])
            ATF_LOGGER.debug(F'{self._host}: [cookies] {repr(s.cookies.get_dict())}')

            try:
                r = self.urlway(1, base_url + '/devices/ups/report', s.get)
            finally:
                self.urlway(2, base_url + '/logout', s.post, headers = headers, data = json.dumps({ 'userName': user }))

            rj = r.json()
            if ('message' in rj) and (rj['message'] == 'Unauthorized'):
                raise AuthError(rj['message'])
            upsst = rj['ups']['valtable']

        ATF_LOGGER.debug(F'{self._host}: [result] {repr(upsst)}')
        return upsst

    @staticmethod
    def extract(upsst) -> str: return upsst['TEMPDEG']
