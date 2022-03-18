from functools import cached_property

from api_helper import BaseClient, auth_check
from bs4 import BeautifulSoup

from . import settings, exceptions


class HkClient(BaseClient):
    @property
    def default_domain(self):
        return settings.HK_AGENT_DOMAIN

    @property
    def date_time_pattern(self):
        return '%d-%m-%Y'

    @property
    def captcha_url_seed(self):
        return self._url('auth/captcha/')

    @property
    def captcha_url(self):
        return self._url(self.get(self.captcha_url_seed, params={'reload': 'true'}).text)

    @property
    def login_url(self):
        return self._url('auth/login')

    @property
    def profile_url(self):
        return self._url()

    @property
    def win_lose_url(self):
        return self._url('invoices/agent')

    @property
    def captcha(self):
        r = self.get(self.captcha_url)
        return self.captcha_solver(r.content)

    @property
    def login_data(self):
        if 'sub' in self.username:
            return {
                'username': self.username,
                'password': self.password,
                'validation': self.captcha,
                'is_viewer': 1
            }

        return {
            'username': self.username,
            'password': self.password,
            'validation': self.captcha
        }

    @staticmethod
    def get_login_error(html):
        soup = BeautifulSoup(html, 'html.parser')
        error = soup.find(attrs={'id': 'flashMessage'})
        if error:
            return error.text

    @staticmethod
    def login_error_hook(r, *args, **kwargs):
        if r.status_code != 200:
            return

        error = HkClient.get_login_error(r.text)
        if error:
            if 'Mã CODE sai' in error:
                raise exceptions.CaptchaError

            raise exceptions.AuthenticationError(error)

    LOGIN_MAX_TRY = 10

    def login(self):
        tried = 0
        while tried < self.LOGIN_MAX_TRY:
            tried += 1
            try:
                self.post(self.login_url, data=self.login_data, hooks={'response': self.login_error_hook})
                self.is_authenticated = True
                return
            except exceptions.CaptchaError:
                continue

    @staticmethod
    def get_name_rank(html):
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find(attrs={'class': 'navbar-brand'}).find('b')
        rank, name = info.text.split(':')
        return name.lower().split('-')[0].split('sub')[0].strip(), rank.replace('panel', '').strip()

    @cached_property
    @auth_check
    def profile(self):
        r = self.get(self._url(''))
        return self.get_name_rank(r.text)

    @property
    def root(self):
        return self.profile[0]

    @staticmethod
    def parse_reports(html):
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('tbody').find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            username = cols[1].find('a').text.lower()

            yield {
                'username': username,
                'order_count': BaseClient.format_float(cols[2].text),
                'origin_2d': BaseClient.format_float(cols[3].text),
                'origin_3_4d': BaseClient.format_float(cols[4].text),
                '2d': BaseClient.format_float(cols[5].text),
                '3_4d': BaseClient.format_float(cols[6].text),
                'win': BaseClient.format_float(cols[7].text),
                'win_lose': BaseClient.format_float(cols[8].text),
                'win_lose_percentage': BaseClient.format_float(cols[9].find('div').text),
                'parent_2d': BaseClient.format_float(cols[10].text),
                'parent_3_4d': BaseClient.format_float(cols[11].text),
                'parent_win': BaseClient.format_float(cols[12].text),
                'parent_win_lose': BaseClient.format_float(cols[13].text),
                'parent:win_lose_percentage': BaseClient.format_float(cols[14].find('div').text),
                'commission': BaseClient.format_float(cols[13].text) - BaseClient.format_float(cols[8].text)
            }

    @auth_check
    def win_lose(self, from_date, to_date):
        r = self.get(self.win_lose_url, params={
            'start': self.format_date(from_date),
            'end': self.format_date(to_date)
        })

        yield from self.parse_reports(r.text)
