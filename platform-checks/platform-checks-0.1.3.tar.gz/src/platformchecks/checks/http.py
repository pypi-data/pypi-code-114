#   -------------------------------------------------------------
#   Platform checks
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Check if a HTTP resource is alive
#                   and return expected HTTP status code.
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


import requests
from requests.exceptions import ConnectionError


class HttpCheck:
    def __init__(self, service, check_type, url, expected_status_code=200):
        self.service = service
        self.check_type = check_type
        self.url = url

        self.can_connect = False
        self.connection_error = ""

        self.expected_status_code = expected_status_code

        self.status_code = None
        self.success = None

    def is_alive_check(self):
        return "_alive" in self.check_type

    def is_proxy_check(self):
        return self.check_type[-6:] == "_proxy"

    def perform(self):
        try:
            r = requests.head(self.url)
        except ConnectionError as e:
            self.success = False
            self.connection_error = str(e)
            return

        self.can_connect = True
        self.status_code = r.status_code
        self.success = r.status_code == self.expected_status_code

        if self.success and self.is_alive_check():
            r = requests.get(self.url)
            self.success = r.text.strip() == "ALIVE"

    def build_message(self):
        if self.success:
            message = [f"Service {self.service} healthy"]
        else:
            message = [f"Service {self.service} NOT healthy"]

            if not self.can_connect:
                message.append(self.connection_error)
            elif self.status_code != self.expected_status_code:
                message.append(f"HTTP {self.status_code}")
            else:
                message.append(f"Unexpected body content")

        if self.is_proxy_check():
            message.append("Checked at PROXY level")

        return " - ".join(message)
