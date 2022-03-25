import requests
from urllib.parse import urljoin
from .base import ATF_LOGGER, ApcKind, AuthError, NullAuth

class UpsParserStateMachine:
    def __init__(self) -> None:
        self.upsst = {}
        self.state = self.wait_for_upss
        self.key = ''

    def wait_for_upss(self, line: str) -> None:
        if "UPS Status" in line:
            self.state = self.handle_kov_start

    def handle_kov_start(self, line: str) -> None:
        if line == '<div class="dataName">':
            self.key = ''
            self.state = self.handle_key
        elif self.key and line == '<div class="dataValue">':
            self.state = self.handle_value

    def handle_key(self, line: str) -> None:
        if "</span>" in line:
            self.key = line.split('<', 2)[0]
        elif line == '</div>':
            self.key = ''
        else:
            return
        self.state = self.handle_kov_start

    def handle_value(self, line: str) -> None:
        if line == '</div>':
            self.key = ''
            self.state = self.handle_kov_start
        elif '<span ' not in line:
            tmp = line.split('<', 2)[0].replace('&nbsp;', '').lstrip()
            if self.key not in self.upsst:
                self.upsst[self.key] = tmp
            else:
                self.upsst[self.key] += ' ' + tmp

class Frmnc(ApcKind):
    def fetch(self, user: str, password: str):
        base_url = "http://" + self._host
        s = requests.Session()
        s.auth = NullAuth()
        r = self.urlway(0, base_url, s.get, stream=True)
        forml = next(filter(lambda value: "name=\"frmLogin\"" in value, r.iter_lines(decode_unicode=True)))
        forml = next(filter(lambda value: "action=" in value, forml.split())).split('=', 2)[1].split('"', 3)[1]

        r = self.urlway(1, urljoin(base_url, forml), s.post, stream=True, data = {
            'login_username': user,
            'login_password': password,
        })
        if (r.status_code == 403) or (r.url == urljoin(base_url, forml)):
            del r, s
            raise AuthError()
        del forml

        try:
            statemach = UpsParserStateMachine()
            for line in r.iter_lines(decode_unicode=True):
                (statemach.state)(line)
            upsst = statemach.upsst
            del statemach
            ATF_LOGGER.debug(F'{self._host}: [result] {repr(upsst)}')
        finally:
            self.urlway(2, urljoin(r.url, "logout.htm"), s.get)
            del r, s

        return upsst

    @staticmethod
    def extract(upsst) -> str: return upsst['Internal Temperature'].replace('&deg;C', '')
