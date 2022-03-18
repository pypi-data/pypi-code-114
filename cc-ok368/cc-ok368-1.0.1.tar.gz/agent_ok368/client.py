import random
import re
import string
from functools import cached_property

from api_helper import BaseClient, auth_check
from bs4 import BeautifulSoup

from . import settings, exceptions


class Ok368Client(BaseClient):

    @property
    def default_domain(self):
        return settings.OK368_AGENT_DOMAIN

    @property
    def root(self):
        return self.profile[0]

    @property
    def date_time_pattern(self):
        return '%Y-%m-%d'

    @property
    def index_url(self):
        return self._url('index.do')

    @property
    def login_standard_url(self):
        return self._url('agent_login_standard.jsp')

    @staticmethod
    def get_session_id(html):
        return re.findall(r'jsessionid=([a-zA-Z0-9\-\_]*)', html)[0]

    @cached_property
    def session_id(self):
        r = self.get(self.index_url)
        return self.get_session_id(r.text)

    @staticmethod
    def get_rsa_public_key(html):
        rsa_public_key_string = re.findall(r"var publicKey = new RSAKeyPair\('(.*?)'\);", html)[0]
        rsa_public_key_arr = rsa_public_key_string.split("', '', '")
        encryption_exponent = rsa_public_key_arr[0]
        encryption_modulus = rsa_public_key_arr[1]
        return encryption_exponent, encryption_modulus

    def encrypt_string(self, encryption_exponent, encryption_modulus, string_to_encrypt):
        return self.get('https://ok368.lehongnam.com',
                        params=dict(
                            expo=encryption_exponent,
                            modulus=encryption_modulus,
                            str=string_to_encrypt
                        )).text

    @staticmethod
    def random_word(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    def session_url(self, path=''):
        return self._url(path) + ';jsessionid=' + self.session_id

    @property
    def captcha_url(self):
        return self.session_url('validationCode/{}/'.format(self.random_word(8)))

    @property
    def login_url(self):
        return self.session_url('agent/stdLogin.action')

    @property
    def captcha(self):
        while True:
            r = self.get(self.captcha_url)
            captcha = self.captcha_solver(r.content, mode='ok368')

            if len(captcha) == 4:
                return captcha

    @property
    def enc_password(self):
        r = self.get(self.login_standard_url)
        encryption_exponent, encryption_modulus = self.get_rsa_public_key(r.text)
        return self.encrypt_string(encryption_exponent, encryption_modulus, self.password)

    @property
    def login_data(self):
        return {
            'loginName': self.username,
            'password': self.enc_password,
            'mode': 'S',
            'randomCode': self.captcha
        }

    @staticmethod
    def get_error_msg(html):
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find(attrs={'id': 'errMsg'})
        return info.text.strip() if info else None

    LOGIN_MAX_TRY = 10

    def login(self):
        try_count = 0
        while try_count < self.LOGIN_MAX_TRY:
            try_count += 0
            try:
                r = self.post(self.login_url, data=self.login_data)

                if 'agent/main' not in r.url:
                    error_message = self.get_error_msg(r.text)

                    if 'Validate code error' in error_message:
                        raise exceptions.CaptchaError

                    raise exceptions.AuthenticationError(error_message)

                self.is_authenticated = True
                return
            except exceptions.CaptchaError:
                pass

        raise Exception('Max login try')

    RANK_STR = {
        5: 'Super',
        6: 'Master',
        7: 'Agent'
    }

    @property
    def profile_url(self):
        return self.session_url('agent/acct/list.action')

    @cached_property
    @auth_check
    def profile(self):
        r = self.get(self.profile_url)
        real_name = re.findall(r'var acctId = (.+);', r.text)[0].strip('\'"')
        rank = int(re.findall(r'var roleId = (.+);', r.text)[0].strip('\'"'))
        rank_str = self.RANK_STR.get(rank)

        return real_name.lower(), rank_str

    @property
    def win_lose_url(self):
        return self.session_url('report/winLossDetail.action')

    @auth_check
    def win_lose(self, from_date, to_date):
        data = {
            'acctId': self.root.upper(),
            'beginDate': self.format_date(from_date),
            'endDate': self.format_date(to_date),
            'finished': 'true',
        }

        r = self.post(self.win_lose_url, data=data)

        for item in r.json().get('list'):
            item.update({
                'turnover': item.get('share8'),
                'win_lose': item.get('wl8'),
                'username': item.get('acctId').lower()
            })
            yield item
