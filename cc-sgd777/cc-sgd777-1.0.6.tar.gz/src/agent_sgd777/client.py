import logging
from collections import defaultdict
from datetime import timedelta
from functools import cached_property

from api_helper import BaseClient, login_required
from bs4 import BeautifulSoup

from . import settings, exceptions


class Sgd777Client(BaseClient):
    is_authenticated = False

    @property
    def default_domain(self):
        return settings.SGD777_AGENT_DOMAIN

    @property
    def login_url(self):
        return self._url('Login.aspx')

    @property
    def captcha_url(self):
        return self._url('VerifyCode.aspx')

    @property
    def profile_url(self):
        return self._url('header.aspx')

    @property
    def win_lose_url(self):
        return self._url('Reports/WinLose.aspx')

    @property
    def captcha(self):
        while True:
            r = self.get(self.captcha_url)
            captcha = self.captcha_solver(r.content, filters='clean_noise', whitelist='0123456789')

            if len(captcha) == 4:
                return captcha
            else:
                logging.error('Wrong captcha {}'.format(captcha))

    @staticmethod
    def get_login_error(html):
        soup = BeautifulSoup(html, 'html.parser')
        error = soup.find(attrs={'id': 'wErrMsg'})
        if error:
            return error.text

    def login_error_hook(self, r, **kwargs):
        if r.status_code != 200:
            return

        error = self.get_login_error(r.text)

        if error:
            if 'Verification Code error' in error:
                raise exceptions.CaptchaError(error)

            raise exceptions.AuthenticationError(error)

    MAX_LOGIN_TRY = 10

    def login(self):
        tried = 0
        while tried < self.MAX_LOGIN_TRY:
            tried += 1
            try:
                r = self.get(self.login_url)
                _, form_data = self.get_form(r.text, id='form1')

                form_data.update({
                    'wUserId': self.username,
                    'wPassword': self.password,
                    'txtVerCode': self.captcha,
                    # 'txtVerCode': '7155',
                    'wLang': 2,
                    'submitButton.x': 173,
                    'submitButton.y': 25
                })

                self.post(self.login_url, data=form_data, hooks={'response': self.login_error_hook})
                self.is_authenticated = True
                return
            except exceptions.CaptchaError:
                pass

    _profile = None

    @staticmethod
    def get_name(html):
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find(id='lblConCreteID')

        if info:
            return info.text

    @cached_property
    @login_required
    def profile(self):
        r = self.get(self.profile_url)
        return self.get_name(r.text), ''

    @property
    def root(self):
        return self.profile[0]

    @staticmethod
    def format_date(date_time):
        return date_time.strftime('%Y-%m-%d')

    def parse_row(self, row):
        cols = row.find_all('td')
        return {
            'username': cols[1].text.lower(),
            'turnover': self.format_float(cols[3].text),
            'net_turnover': self.format_float(cols[5].text),
            'win_lose': self.format_float(cols[4].text),
            'commission': self.format_float(cols[8].text),
        }

    def parse_report(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find(id='detailsGrid')
        if table:
            rows = table.find_all('tr')[1:-1]
            return list(map(self.parse_row, rows))

        return []

    @login_required
    def win_lose(self, from_date, to_date):
        _start = self.str2time(from_date)
        _end = self.str2time(to_date) + timedelta(days=1)

        r = self.get(self.win_lose_url)
        _, form_data = self.get_form(r.text, id='form1')

        data = form_data.copy()
        data.update({
            'wFromDate': self.format_date(_start),
            'wToDate': self.format_date(_end),
            'wTable': 999,
            'btnQuery': 'Query',
            # '__EVENTTARGET': 'AcctLinks1$LNK%s' % root,
            # '__EVENTARGUMENT': ''
        })

        r = self.post(self.win_lose_url, data=data)

        _, form_data2 = self.get_form(r.text, id='form1')

        form_data2.update({
            'wFromDate': self.format_date(_start),
            'wToDate': self.format_date(_end),
            'wTable': 999,
            'btnQuery': 'Query',
            '__EVENTTARGET': 'AcctLinks1$LNK%s' % self.root,
            '__EVENTARGUMENT': ''
        })

        form_data2.pop('btnQuery', None)

        r = self.post(self.win_lose_url, data=form_data2)

        reports = self.parse_report(r.text)

        root_report = defaultdict(int)

        for report in reports:
            yield report
            for k, v in report.items():
                if isinstance(v, (float, int)):
                    root_report[k] += v

        if len(root_report.keys()) > 0:
            yield dict(root_report, username=self.root.lower())
