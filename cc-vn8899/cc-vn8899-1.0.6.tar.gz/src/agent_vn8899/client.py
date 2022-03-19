import string
import time
from functools import cached_property

from api_helper import BaseClient, login_required
from bs4 import BeautifulSoup

from . import settings, exceptions


class Vn8899Client(BaseClient):
    @property
    def default_domain(self):
        return settings.VN8899_AGENT_DOMAIN

    @property
    def root(self):
        return self.profile[0]

    @property
    def date_time_pattern(self):
        return '%Y-%m-%d'

    @property
    def login_url(self):
        return self._url('login.action')

    @property
    def captcha_url(self):
        return self._url('backstage/rand.action')

    @property
    def captcha(self):
        tried = 0
        while tried < settings.MAX_CAPTCHA_TRY:
            tried += 1

            r = self.get(self.captcha_url, params={'d': int(time.time())})
            captcha = self.captcha_solver(r.content, whitelist=string.ascii_lowercase)

            if len(captcha) == 4:
                return captcha

        raise Exception('Reach maximum captcha try')

    @property
    def login_data(self):
        return {
            'acctId': self.username.upper(),
            'password': self.password,
            'lang': 'en',
            'validateCode': self.captcha,
            'doLogin': 'Login'
        }

    @staticmethod
    def login_error_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        dom = soup.find('font', attrs={'color': 'red'})
        return dom.get_text()

    @staticmethod
    def login_response_hook(r, **kwargs):
        if '<font color="red">' in r.text:
            error = Vn8899Client.login_error_parser(r.text)
            if 'Invalid Code' in error:
                raise exceptions.CaptchaError(error)

            raise exceptions.AuthenticationError(error)

    def login(self):
        self.get(self.login_url)
        try_count = 0
        while try_count < settings.MAX_LOGIN_TRY:
            try_count += 1
            try:
                self.post(self.login_url, data=self.login_data, hooks={
                    'response': self.login_response_hook
                }, headers={
                    'Referer': self.login_url
                })

                self.is_authenticated = True
                return
            except exceptions.CaptchaError:
                pass

        raise Exception('Reach maximum login try')

    @property
    def welcome_url(self):
        return self._url('welcome.action')

    @staticmethod
    def profile_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        try:
            row = table.find('tr')
            cols = row.find_all('td')
            return cols[1].get_text().strip('\n\t ').lower(), cols[3].get_text().strip('\n\t ')
        except IndexError:
            row = table.find_all('tr')[1]
            cols = row.find_all('td')
            username = cols[1].get_text().strip('\n\t ').lower()
            username = username.split('_')[0]
            return username, cols[3].get_text().strip('\n\t ')

    @cached_property
    @login_required
    def profile(self):
        r = self.get(self.welcome_url)
        return self.profile_parser(r.text)

    @property
    def win_lose_url(self):
        return self._url('report/rptPL.action')

    @staticmethod
    def report_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', attrs={'id': 'plTable'})
        for row in table.find_all('tr')[1:-1]:
            cols = row.find_all('td')
            username = cols[1].get_text().strip('\n').lower()
            yield {
                'username': username,
                'turnover': Vn8899Client.format_float(cols[5].get_text()),
                'commission': Vn8899Client.format_float(cols[6].get_text()),
                'win_lose': Vn8899Client.format_float(cols[7].get_text()),
            }

    @login_required
    def win_lose(self, from_date, to_date, **kwargs):
        data = {
            'finished': 'true',
            'pltype': 'A',
            'startDate': self.format_date(from_date),
            'endDate': self.format_date(to_date),
            'drawTemplate': '1,2,3,4',
            'acctId': None,
            'roleId': None
        }

        r = self.get(self.win_lose_url, params=data)
        yield from self.report_parser(r.text)
