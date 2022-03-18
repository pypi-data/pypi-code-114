from functools import cached_property
from urllib.parse import urlparse

from api_helper import BaseClient, auth_check

from . import settings, exceptions


class Ld789Client(BaseClient):

    @property
    def default_domain(self):
        return settings.LD789_AGENT_DOMAIN

    @property
    def be_uri(self):
        return urlparse(self.base_domain.replace('ag.', 'be.'))

    def be_url(self, path):
        return self._url(path, self.be_uri)

    @property
    def root(self):
        return self.profile[0]

    @property
    def date_time_pattern(self):
        return '%Y-%m-%d'

    @property
    def login_url(self):
        return self.be_url('auth/sign-in')

    @property
    def login_data(self):
        return {
            # 'grant_type': 'password',
            'Scope': 'backend',
            'Username': self.username,
            'Password': self.password,
            # 'otp': ''
        }

    @staticmethod
    def auth_check2(r, **kwargs):
        if r.status_code != 200:
            return

        json = r.json()
        if json is dict and json.get('message') == 'Unauthorized':
            print(r.request.headers)
            raise exceptions.AuthenticationError('Unauthorized')

    def login(self):
        r = self.post(self.login_url, json=self.login_data)

        error = r.json().get('message')

        if error:
            raise exceptions.AuthenticationError(error)

        self.headers.update({
            'authorization': 'Bearer %s' % r.json().get('IdToken'),
            'referer': 'https://ag.one789.net/'
        })

        self.hooks['response'] = [self.auth_check2]

    @property
    def profile_url(self):
        return self.be_url('users/profile')

    @cached_property
    @auth_check
    def profile(self):
        r = self.get(self.profile_url).json()
        return r.get('Username').lower().split('sub')[0], ''

    @property
    def win_lose_url(self):
        return 'https://report.lotusapi.com/' + 'statements/agent/statements/children-user'

    @staticmethod
    def parse_report(i):
        yield dict(i,
                   username=i.get('Username').lower(),
                   turnover=i.get('Player').get('NetAmount') / 1000,
                   win_lose=i.get('Player').get('WinLose') / 1000
                   )

    IGNORE_FIELDS = ['Level']

    @auth_check
    def win_lose(self, from_date, to_date, root=None):
        uri = self.win_lose_url
        r = self.get(uri, params={
            'from': self.format_date(from_date),
            'to': self.format_date(to_date),
            'productTypes': [0, 1, 2, 100],
            'size': 100,
            'page': 1
        })

        for i in r.json():
            ancestor = i.pop('Ancestor')

            if ancestor:
                for k, v in ancestor.items():
                    i['ancestor_{}'.format(k)] = v

            player = i.pop('Player')

            for k, v in player.items():
                i['player_{}'.format(k)] = v

            i.update(
                turnover=i.get('player_NetAmount') / 1000,
                win_lose=i.get('player_WinLose') / 1000,
                username=i.get('Username').lower(),
            )

            yield i
