from html.parser import HTMLParser
import requests
from urllib.parse import urljoin
from .base import ATF_LOGGER, ApcKind, AuthError, NullAuth

class UpsStatEntity:
    def __init__(self) -> None:
        self.description = ''
        self.value = ''
        self.units = ''

class UpsParserStateMachine(HTMLParser):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.stats = dict()
        self.__sel = None

    def handle_starttag(self, tag: str, attrs) -> None:
        namattrs = [i[1] for i in attrs if i[0] == 'name']
        if (tag != 'span') or (len(namattrs) != 1):
            return
        parts = namattrs[0].split('?')
        if len(parts) != 2:
            return
        ty, eid = parts
        if eid not in self.stats:
            self.stats[eid] = UpsStatEntity()
        self.__sel = self.stats[eid]
        self.__selty = ty

    def handle_endtag(self, tag: str) -> None:
        self.__sel = None
        self.__selty = ''

    def handle_data(self, data: str) -> None:
        if not self.__sel:
            return
        ty = self.__selty
        if ty == 'description':
            self.__sel.description += data.replace(':', '')
        elif ty == 'value':
            self.__sel.value += data.strip()
        elif ty == 'units':
            self.__sel.units += data

class GdenNt07(ApcKind):
    def fetch(self, user: str, password: str):
        base_url = F'http://{self._host}'
        upsst = None

        with requests.Session() as s:
            s.auth = NullAuth()
            r = self.urlway(0, base_url, s.get, stream=True)
            forml = next(filter(lambda value: "name=\"HashForm1\"" in value, r.iter_lines(decode_unicode=True)))
            forml = next(filter(lambda value: "action=" in value, forml.split())).split('=', 2)[1].split('"', 3)[1]

            r = self.urlway(1, urljoin(base_url, forml), s.post, data = {
                'login_username': user,
                'login_password': password,
                'prefLanguage': '00000000',
                'submit': 'Log+On',
            })
            if (r.status_code == 403) or (r.url == urljoin(base_url, forml)):
                del r, s
                raise AuthError()
            del forml

            try:
                r = self.urlway(2, urljoin(r.url, 'batts.htm'), s.get, stream=True)
                statemach = UpsParserStateMachine()
                for chunk in r.iter_lines(decode_unicode=True):
                    statemach.feed(chunk)
                statemach.close()
                upsst = statemach.stats
            finally:
                self.urlway(3, urljoin(r.url, 'logout.htm'), s.get)

        upsst2 = {}
        for i in upsst.values():
            upsst2[i.description] = (i.value, i.units)
        upsst = upsst2

        ATF_LOGGER.debug(F'{self._host}: [result] {repr(upsst)}')
        return upsst

    @staticmethod
    def extract(upsst) -> str:
        value, units = upsst['Battery Temperature']
        return value
