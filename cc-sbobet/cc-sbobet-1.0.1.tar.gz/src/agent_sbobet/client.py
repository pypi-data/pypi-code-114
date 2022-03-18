import datetime
import itertools
import logging
import re
from urllib.parse import urlparse

import jwt
from bs4 import BeautifulSoup

from api_helper import BaseClient, auth_check

from agent_sbobet import settings
from agent_sbobet.exceptions import FrequentlyRequestException, AuthenticationError

LOG = logging.getLogger(__name__)


class SbobetApi(BaseClient):

    @property
    def default_domain(self):
        return settings.SBOBET_DOMAIN

    @property
    def date_time_pattern(self):
        return '%Y-%m-%d'

    _token = None
    _session_domain = None
    refresh_token = None

    def __init__(self, *args, **kwargs):
        super(SbobetApi, self).__init__(*args, **kwargs)

        # global hooks
        self.hooks['response'].append(self.generic_error_hook)
        self.hooks['response'].append(self.under_maintenance_hook)
        self.hooks['response'].append(self.rate_limit_hook)
        self.hooks['response'].append(self.user_code_challenge_hook)
        self.hooks['response'].append(self.guest_code_challenge_hook)
        self.hooks['response'].append(self.login_redirect_hook)
        self.hooks['response'].append(self.user_term_challenge_hook)

        # setup default headers
        self.headers.update(settings.DEFAULT_HEADERS)

        self.random_ip('103.149.172.{}')

    @property
    def token_info(self):
        if not self.token:
            self.refresh()

        return jwt.decode(self.token, options={'verify_signature': False})

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        self.headers.update({
            'Authorization': 'Bearer {}'.format(self.token)
        })

    @property
    def settings(self):
        return {
            'authority': 'Fr',
            'client_id': "libra-agent-site",
            'response_type': "code",
            'scope': "openid agent.id api offline_access"
        }

    @property
    def customer_id(self):
        return self.token_info.get('aid')

    @property
    def root(self):
        return self.token_info.get('agt')

    @property
    def expire_time(self):
        return self.token_info.get('exp')

    def is_expire(self):
        return datetime.datetime.now().timestamp() >= self.expire_time

    def get_sub_domain(self, sub):
        def f(path=''):
            return '{origin.scheme}://{sub}.{origin.netloc}/{path}'.format(
                sub=sub,
                path=path.lstrip('/'),
                origin=self.base_uri
            )

        return f

    @property
    def agent_auth_url(self):
        return self.get_sub_domain('agent-auth')

    @property
    def refresh_url(self):
        return self.agent_auth_url('connect/token')

    @property
    def agent_api_url(self):
        return self.get_sub_domain('agent-api')

    @property
    def report_win_loss_url(self):
        return self.agent_api_url('report/winloss')

    @property
    def agent_url(self):
        return self.get_sub_domain('agent')

    def refresh(self):
        if self.refresh_token:
            self.post(self.refresh_url, {
                'client_id': self.settings.get('client_id'),
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token
            }, hooks={
                'response': self.refresh_hook
            })
        else:
            self.login()
            self.api_login()

    # noinspection PyUnusedLocal
    def refresh_hook(self, r, **kwargs):
        json_response = r.json()
        self.token = json_response.get('access_token')

    def request(self, method, url, **kwargs):
        if self.agent_api_url() in url:
            if self.is_expire():
                self.refresh()

        return super().request(method, url, **kwargs)

    @staticmethod
    def get_timestamp(_date):
        if isinstance(_date, str):
            _date = datetime.datetime.fromisoformat('{}T11:00:00'.format(_date))
        return int(_date.timestamp() * 1000)

    # legacy methods

    URI_AUTH = 'Captcha'
    URI_AUTH_VALIDATE = '/Captcha/Validate'
    URI_TERM_AGREEMENT = 'webroot/restricted/tc/termsconditions.aspx'
    URI_PASSWORD_FRAME = 'WebRoot/Restricted/Security/passwordframe.aspx'
    URI_CODE_PROMPT = 'webroot/restricted/security/security-code-prompt.aspx'
    URI_PROFILE_RANK = 'webroot/restricted/HomeTop.aspx'
    URI_INIT_REPORT = 'webroot/restricted/report2/winlost.aspx?P=WL'
    URI_INIT_SIMPLE_REPORT = 'webroot/restricted/report2/winlost.aspx'

    @property
    def agent_login_url(self):
        return self.agent_url(self.URI_AUTH)

    def session_url(self, path):
        return '{origin.scheme}://{origin.netloc}/{path}'.format(
            path=path.lstrip('/'),
            origin=urlparse(self._session_domain)
        )

    # noinspection PyUnusedLocal
    @staticmethod
    def generic_error_hook(r, **kwargs):
        if 'Error.htm' in r.url:
            raise Exception('Generic Error {}'.format(r.url))

    # noinspection PyUnusedLocal
    @staticmethod
    def under_maintenance_hook(r, **kwargs):
        if "window.top.location.href = '/um.aspx'" in r.text:
            raise Exception('Under Maintenance')

    @staticmethod
    def get_user_code_position(html):
        TEXT_TO_INT = {
            'first': 0,
            'second': 1,
            'third': 2,
            'fourth': 3,
            'fifth': 4,
            'sixth': 5,
            'seventh': 6,
            'eighth': 7
        }

        soup = BeautifulSoup(html, 'html.parser')
        hidck = soup.select('#HidCK')[0].val()
        pos1, pos2 = [TEXT_TO_INT.get(i.get_text()) for i in soup.select('form strong')]

        data = {
            'HidCK': hidck,
            'cmd': 'securityCode',
            'digit1': '',
            'digit2': ''
        }

        return pos1, pos2, data

    # noinspection PyUnusedLocal
    def user_code_challenge_hook(self, r, **kwargs):
        if r.status_code != 200:
            return

        if self.URI_CODE_PROMPT not in r.url:
            return

        pos1, pos2, data = self.get_user_code_position(r.text)

        data.update({
            'digit1': self.security_code[pos1],
            'digit2': self.security_code[pos2]
        })

        return self.post(r.url, data)

    @staticmethod
    def get_code_position(html):
        soup = BeautifulSoup(html, 'html.parser')
        form = soup.find('form', attrs={'name': 'securityCodeForm'})
        target_url = form.get('action')
        form_data = dict(map(lambda n: (n.get('name'), n.get('value')), form.find_all('input')))
        first_pos = int(soup.select('#firstposition')[0].get_text().strip()[0]) - 1
        second_pos = int(soup.select('#secondposition')[0].get_text().strip()[0]) - 1

        return first_pos, second_pos, target_url, form_data

    # noinspection PyUnusedLocal
    def guest_code_challenge_hook(self, r, **kwargs):
        if r.status_code != 200:
            return

        if 'Security/SecurityCode' not in r.url:
            return

        LOG.info('trigger guest_code_challenge')

        pos1, pos2, action, form_data = self.get_code_position(r.text)

        form_data.update({
            'FirstChar': self.security_code[pos1],
            'SecondChar': self.security_code[pos2],
        })

        return self.post(self.agent_url(action), form_data)

    @property
    def username(self):
        return self.credentials.get('username')

    @property
    def password(self):
        return self.credentials.get('password')

    @property
    def security_code(self):
        return self.credentials.get('code')

    @staticmethod
    def init_token_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find(attrs={'name': '__RequestVerificationToken'}).get('value')

    @property
    def login_init_token(self):
        r = self.get(self.agent_url())
        return self.init_token_parser(r.text)

    # noinspection PyUnusedLocal
    @staticmethod
    def rate_limit_hook(r, *args, **kwargs):
        if "You Are Requesting Too Frequently, Please Try Again Later" in r.text:
            raise FrequentlyRequestException

    @staticmethod
    def login_redirect_form_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        form = soup.find('form', attrs={'name': 'f'})
        target_url = form.get('action')
        form_data = dict(map(lambda n: (n.get('name'), n.get('value')), form.find_all('input')))
        return target_url, form_data

    # noinspection PyUnusedLocal
    def login_redirect_hook(self, r, **kwargs):
        if '/Login/ProcessSecurityResult' in r.url and r.status_code == 200:
            target_url, redirect_data = self.login_redirect_form_parser(r.text)
            self._session_domain = target_url

            return self.post(target_url, redirect_data)

    # noinspection PyUnusedLocal
    def user_term_challenge_hook(self, r, **kwargs):
        if self.URI_TERM_AGREEMENT in r.url and r.status_code != 302:
            LOG.info('trigger user_term_challenge')
            return self.post(r.url, {'agree': '1'})

    # noinspection PyUnusedLocal
    @staticmethod
    def change_password_request(r, **kwargs):
        if 'WebRoot/Restricted/Security/Password.aspx?f=1' in r.url:

            LOG.info('trigger user_password_challenge')

            if 'Please note that your login name cannot be changed after it has been created.' in r.text:
                raise AuthenticationError('Please choose login name.')

            raise AuthenticationError('Password expired.')

            # hidck = parsers.get_hidck(r.text)
            # domain = get_base_url(r.url)
            #
            # LOG.info("%s %s" % (hidck, domain))
            #
            # r2 = force_change_password(session, domain, hidck, password, password + '.', code)
            #
            # if "You have successfully saved your changes." in r2.text:
            #     change_password(session, domain, password + '.', password, code)

    def _login_error(self, r, **kwargs):
        uri = urlparse(r.url)
        if self.agent_url() in r.url and uri.path == '/':
            print('_login_error {}'.format(r.url))
            print(urlparse(r.url))
            alert = re.findall('alert\("(.*)"\)', r.text)
            if len(alert) > 3:
                raise AuthenticationError(alert[0])

    @property
    def login_data(self):
        return {
            'lang': 'en',
            'password': self.password,
            'username': self.username,
            'btnSubmit': 'Sign In',
            '__RequestVerificationToken': self.login_init_token,
        }

    def login(self):
        self.post(self.agent_login_url, self.login_data, hooks={
            'response': self.hooks['response'] + [self._login_error]
        })

    # noinspection PyUnusedLocal
    def parse_auth_access_token_hooks(self, r, **kwargs):
        try:
            self.token = re.findall("auth_access_token', '(.*)'", r.text)[0]
            self.refresh_token = re.findall("auth_refresh_token', '(.*)'", r.text)[0]
        except IndexError:
            raise Exception('Api Login Error!')

    def api_login(self):
        self.get(self.session_url('p/reports/winloss'), hooks={'response': self.parse_auth_access_token_hooks})

    def profile(self):
        return self.root, self.agent_tier

    def win_lose(self, from_date, to_date, deep=False):
        """
        get win lose just from 1st level
        """
        pool = iter([(self.customer_id, self.agent_tier), ])
        while next_data := next(pool, None):
            customer_id, agent_tier = next_data

            params = {
                'CustomerId': customer_id,
                'Filters': [1, 2, 3, 4],
                'FromDate': self.get_timestamp(from_date),
                'ToDate': self.get_timestamp(to_date)
            }

            r = self.get(self.report_win_loss_url, params=params)
            data: list[dict] = r.json().get('data')

            # next pool holder to maintenance order
            next_pool = []

            for row in data:
                category = row.pop('displayName')

                for field in ['filter']:
                    row.pop(field)

                row.update({
                    'category': category,
                    'username': row.get('accountId'),
                    'commission': row.get('grossCommission'),
                    'win_lose': row.get('playerWinloss'),
                    'tier': agent_tier - 1
                })

                yield row

                # add item to next pool
                if deep and agent_tier > 2:
                    next_pool.append((row.get('customerId'), agent_tier - 1))

            # merge next pool to pool
            if len(next_pool) > 0:
                pool = itertools.chain(next_pool, pool)

    @property
    def agent_tier(self):
        return self.token_info.get('at')

    @staticmethod
    def member_sport_only(x):
        return x.get('category') == 'SportsBook' and x.get('tier') == 1

    @property
    def bet_list_url(self):
        return self.agent_api_url('betlist/settled/new')

    def tickets(self, from_date, to_date):
        for member in filter(self.member_sport_only, self.win_lose(from_date, to_date, True)):
            params = {
                'CustomerId': member.get('customerId'),
                'Filters': [1, 2, 3, 4],
                'FromDate': self.get_timestamp(from_date),
                'ToDate': self.get_timestamp(to_date)
            }

            r = self.get(self.bet_list_url, params=params)

            for i in r.json().get('sports'):
                yield i.get('bet')

    @property
    def outstanding_url(self):
        return self.agent_api_url('wallet/outstanding')

    def outstanding(self, deep=False):
        pool = iter([(self.customer_id, self.agent_tier), ])
        while next_data := next(pool, None):
            customer_id, agent_tier = next_data

            params = {
                'CustomerId': customer_id,
                'ProductFilter': 1,
            }

            r = self.get(self.outstanding_url, params=params)

            # next pool holder to maintenance order
            next_pool = []

            for i in r.json():
                i.update({
                    'username': i.get('accountId'),
                    'category': 'SportsBook',
                    'outstanding': i.get('memberTotal')
                })
                yield i

                if deep and agent_tier > 2:
                    next_pool.append((i.get('customerId'), agent_tier - 1))

            # merge next pool to pool
            if len(next_pool) > 0:
                pool = itertools.chain(next_pool, pool)
