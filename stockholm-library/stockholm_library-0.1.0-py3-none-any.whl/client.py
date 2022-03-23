from typing import List, Union

import requests

from models import Loan
from parsers import LoanParser


class Client:

    BASE_URL = "https://biblioteket.stockholm.se"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"

    def __init__(self):
        self.is_logged_in = False
        self.session = requests.session()

    def login(self, user: str, pin: str) -> bool:
        url = f"{Client.BASE_URL}/user"
        headers = {"User-Agent": Client.USER_AGENT}
        data = {"name": user, "pass": pin, "form_id": "user_login"}
        res: requests.Response = self.session.post(url=url, data=data, headers=headers)
        if "Felaktigt kortnummer eller pinkod." in res.text:
            self.is_logged_in = False
            return False
        else:
            self.is_logged_in = True
            return True

    def logout(self):
        url = f"{Client.BASE_URL}/logout"
        headers = {"User-Agent": Client.USER_AGENT}
        _res: requests.Response = self.session.get(url=url, headers=headers)
        self.is_logged_in = False

    def get_loans(self) -> List[Loan]:
        assert self.is_logged_in, "Must be logged in before doing server requests"
        url = f"{Client.BASE_URL}/lan"
        headers = {"User-Agent": Client.USER_AGENT}
        res: requests.Response = self.session.get(url=url, headers=headers)
        if not res.ok:
            raise Exception("Not allowed")

        return LoanParser.parse_loans(res.content.decode("utf-8"))

    def get_reservations(self) -> List:
        raise NotImplementedError

    def re_borrow(self, loans: Union[int, Loan, List[Union[int, Loan]]]):
        raise NotImplementedError
