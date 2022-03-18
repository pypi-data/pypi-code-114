import requests
import logging
import json

from pemudapersis_bot.src.configs.environment import EnvConfig


class APIHandler:
    def __init__(self):
        self.config = EnvConfig()
        self.request_headers = {
            "Authorization": f"Basic {self.config.OAUTH_CREDS}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.access_token = None

    def check_npa(self, npa: str) -> str:
        api_url = f"{self.config.API_ENDPOINT}/v1/api/anggota/check"
        if not self.access_token:
            self.access_token = self.__get_access_token()
        self.request_headers = {
            "Authorization": f'bearer {self.access_token.get("access_token")}',
            "Content-Type": "application/json",
        }
        request_body = json.dumps({"npa": npa})
        try:
            response = requests.post(
                api_url, headers=self.request_headers, data=request_body
            )
            npa_data = response.json()
            logging.debug(npa_data)
            if npa_data.get("data"):
                return "Valid"
        except requests.RequestException as exp:
            logging.error(f"Failed to verify NPA : {exp}")
            return "Error"
        return "Invalid"

    def __get_access_token(self):
        logging.debug("Getting access token from Pemuda API..")
        response = {}
        request_body = {
            "username": self.config.OAUTH_USERNAME,
            "password": self.config.OAUTH_PASSWORD,
            "grant_type": self.config.OAUTH_GRANT_TYPE,
        }

        login_url = self.config.OAUTH_URL
        try:
            response = requests.post(
                login_url, data=request_body, headers=self.request_headers
            )
        except requests.RequestException as exp:
            logging.error(f"Failed to get access token : {exp}")
        return response.json()
