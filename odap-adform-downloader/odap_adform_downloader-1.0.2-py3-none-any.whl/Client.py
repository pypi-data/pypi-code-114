import sys
import traceback
from collections import Counter
from math import isclose
from pathlib import Path
from typing import List

import requests
import logging
from datetime import datetime, timedelta
from adform.Credentials import Credentials
import os
import json

logging = logging.getLogger("adform.Client")


class FilePersistingHandler:
    def __init__(self, location: str):
        self.location = location

    @property
    def state(self) -> dict:
        """
        Returns dict representation of state file or empty dict if not present
        Returns:
            dict:
        """
        logging.info("Loading state file..")
        state_file_path = os.path.join(self.location, "state.json")
        if not os.path.isfile(state_file_path):
            logging.info("State file not found. First run?")
            return {}
        try:
            with open(state_file_path, "r") as state_file:
                return json.load(state_file)
        except (OSError, IOError):
            raise ValueError("State file state.json unable to read ")

    @state.setter
    def state(self, state_dict: dict):
        """
        Stores [state file]
        Args:
            state_dict (dict):
        """
        if not isinstance(state_dict, dict):
            raise TypeError("Dictionary expected as a state file datatype!")

        with open(os.path.join(self.location, "state.json"), "w+") as state_file:
            json.dump(state_dict, state_file)


class Client:
    """
    AdForm client
    """

    ADFORM_URL = "https://api.adform.com"
    API_VERSION = "v1"

    AUTH_URL = "https://id.adform.com/sts/connect/token"
    ENLIST_FILES_ON_SERVER_API_ADDRESS = ADFORM_URL + "/" + API_VERSION + "/buyer/masterdata/files"
    DOWNLOAD_MASTERDATA_API_ADDRESS = ADFORM_URL + "/" + API_VERSION + "/buyer/masterdata/download"

    DEFAULT_DOWNLOAD_CHUNK_SIZE = 8 * 1024 * 1024

    END_DAY = datetime.now()
    START_DAY = END_DAY - timedelta(days=30)

    auth_headers = {"Content-Type": "x-www-form-urlencoded"}
    grant_type = "client_credentials"

    # download_timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    def __init__(self, credentials: Credentials, persisting_handler: FilePersistingHandler, chunk_size=None):

        self.api_url = "{}/{}".format(self.ENLIST_FILES_ON_SERVER_API_ADDRESS, credentials.setup_id)
        self.api_file_url = "{}/{}".format(self.DOWNLOAD_MASTERDATA_API_ADDRESS, credentials.setup_id)
        self.chunk_size = chunk_size if chunk_size is not None else self.DEFAULT_DOWNLOAD_CHUNK_SIZE

        self.auth = self._auth(credentials)

        self.app_headers = {"Authorization": self.auth, "Accept": "application/json"}
        self.credentials = credentials
        self.persisting_handler = persisting_handler
        self.state = self.persisting_handler.state

    def _auth(self, credentials: Credentials):
        """
        Obtain Bearer Tokens.
        This can end up with several errors due to authorization issue or network issue,
        better to keep it in mind and place few try catch blocks
        :param credentials:
        :return:
        """
        scope = " ".join(credentials.scopes)
        auth_payload = {
            "scope": scope,
            "grant_type": self.grant_type,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
        }

        # self.api_files_download_url = '{}/{}'.format(self.download_url, credentials.setup_id)

        try:
            response = requests.post(url=self.AUTH_URL, headers=self.auth_headers, data=auth_payload)
            logging.info(response)
            logging.debug(response.json())

            if response.ok:
                return "Bearer {}".format(response.json()["access_token"])

            elif response.status_code >= 400 and response.status_code < 500:
                logging.warning("Authorization to Adform failed.")
                sys.exit(1)
            else:
                logging.warning("Sorry, problem on adform api side, try again later.")
                sys.exit(2)

            # return "Bearer {}".format(response.json()['access_token'])
        except Exception as e:
            logging.warning("Login was not successful.")
            traceback.print_exc()
            # posunu tim raise o uroven vys
            raise e

    def get_master_data_file_list(self):
        """
        Enlist files, which waiting for processing on the AdForm server
        :return:
        """
        response = requests.get(url=self.api_url, headers=self.app_headers)
        # print(type(response.json()))
        # print(response.json())
        if type(response.json()) == list:
            return response.json()
        else:
            logging.info(response.json()["Message"])
            sys.exit(3)

    def filter_files_based_on_name(self, s):
        return s["name"].replace(".", "_").split("_")[0] in self.credentials.tables

    @staticmethod
    def isoformat_to_date(date_time):
        return datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%SZ")

    def get_start_day(self, table_name):
        """
        Explore state file for latest processing date for given dataset
        :return:
        """
        if self.credentials.start_day:
            return datetime.strptime(self.credentials.start_day, "%d-%m-%Y")
        elif self.state.get(table_name):
            return self.isoformat_to_date(self.state.get(table_name)["date"])
        else:
            return self.START_DAY

    def get_end_day(self):
        if self.credentials.end_day:
            return datetime.strptime(self.credentials.end_day, "%d-%m-%Y")
        else:
            return self.END_DAY

    def filter_files_based_on_date(self, x):
        return self.get_start_day((x["name"]).split("_")[0]) <= self.isoformat_to_date((x["createdAt"])) <= self.get_end_day()

    # def get_files_id_list(self):
    #     filtered_by_name = filter(self.filter_files_based_on_name, self.get_master_data_file_list())
    #     filtered_by_date = filter(self.filter_files_based_on_date, list(filtered_by_name))
    #     files_ids = [(item["name"], item["id"]) for item in list(filtered_by_date)]
    #     return files_ids

    def get_filtered_files_for_download(self):
        filtered_by_name = filter(self.filter_files_based_on_name, self.get_master_data_file_list())
        filtered_by_date = filter(self.filter_files_based_on_date, list(filtered_by_name))
        return list(filtered_by_date)

    # def get_files_id_list(self):
    #     files_ids = [(item["name"], item["id"]) for item in self.get_filtered_files_for_download()]
    #     return files_ids

    def get_file_report(self, file, report_options: List[str] = None):

        _TABLE_NAME = file["name"].split("_")[0]
        _FILE_NUMBER = file["id"].split("_")[1]
        _NAME = file["name"]
        _TIMESTAMP = file["createdAt"]
        _ID = file["id"]
        _SETUP = file["setup"]
        _SIZE = file["size"]
        _CHECKSUMMD5 = file["checksumMD5"]

        report = {
            "tablename": _TABLE_NAME,
            "filenumber": _FILE_NUMBER,
            "name": _NAME,
            "timestamp": _TIMESTAMP,
            "id": _ID,
            "setup": _SETUP,
            "size": _SIZE,
            "checksumMD5": _CHECKSUMMD5,
        }

        if report_options:
            report = {key: report[key] for key in report_options}
        return report

    def get_file_path_to_download(self, file_id):
        path = "{}/{}".format(self.api_file_url, file_id)
        response = requests.get(url=path, headers=self.app_headers)
        return response

    def download_masterdata_file(self, name, file_id, destination_file):

        path = f"{self.credentials.landing_file}/{destination_file}"
        file_name = f"{self.credentials.landing_file}/{destination_file}/{name}"
        if not os.path.exists(path):
            os.makedirs(path)

        # try:
        with open(file_name, "wb") as f:
            for chunk in self.get_file_path_to_download(file_id).iter_content(chunk_size=self.chunk_size):
                if chunk:
                    f.write(chunk)
                    f.flush()

            os.fsync(f.fileno())
            f.close()
        # except OSError:
        #     logging.warning("Could not download" + file_name)

    def check_downloaded_file_size(self, downloaded_file, filename):
        """
        If size of downloaded file is different from proclaimed size, it return filename on list to download it again
        :param filename: path to file
        :param downloaded_file:
        :return:
        """
        if not isclose(Path(filename).stat().st_size, downloaded_file["size"], abs_tol=50):
            logging.warning(f"Size of {filename} is not correct!")
            return True

    def download_masterdata_files_by_id(self):
        list_of_files_to_download = self.get_filtered_files_for_download()
        counter_of_tries = Counter()

        while list_of_files_to_download:
            file = list_of_files_to_download.pop()
            report = self.get_file_report(file, report_options=["name", "id", "timestamp", "size", "tablename"])
            file_id = report["id"]
            counter_of_tries[file_id] += 1
            if counter_of_tries[file_id] > 5:
                with open(self.credentials.landing_file + "/unsuccesfully_downloaded.json", "w") as f:
                    json.dump(list_of_files_to_download, f)
                break

            self.download_masterdata_file(report["name"], file_id, report["tablename"])

            file_name = f"{self.credentials.landing_file}/{report['tablename']}/{report['name']}"
            if not isclose(Path(file_name).stat().st_size, report["size"], abs_tol=50):
                logging.warning(f"Size of {file_name} is not correct!")
                list_of_files_to_download.insert(0, file)

            dataset = report["tablename"]
            if self.state.get(dataset):
                if self.isoformat_to_date(self.state.get(dataset)["date"]) < (self.isoformat_to_date(report["timestamp"])):
                    self.state.update({dataset: {"date": report["timestamp"]}})
            else:
                self.state.update({dataset: {"date": report["timestamp"]}})
        self.persisting_handler.state = self.state
