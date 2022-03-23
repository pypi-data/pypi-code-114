import configparser
import requests
import json
import uuid
import hashlib

class binubuo:
    def __init__(self, apikey=None):
        self.rapidapi_key = None
        self.binubuo_key = None
        self.error_string = None
        self.unique_url_path = None
        if(apikey is None):
            print("No API key specified. Please set api key before making calls to binubuo.")
        else:
            self.key(apikey)
        self.readconfig()

    def set_unique_url(self):
        self.setheaders()
        self.resp = requests.request("GET", self.baseurl + '/binubuo-actions/get-unique-url-path', headers=self.headers)
        if self.resp.ok:
            self.response_json = json.loads(self.resp.text)
            for key, value in self.response_json.items():
                if key == 'unique_url':
                    self.unique_url_path = value
        else:
            if self.resp.status_code == 404:
                print("Unique url endpoint not found: " + self.baseurl + "/binubuo-actions/get-unique-url-path")
            else:
                print("Communication failure")

    def set_temp_key(self):
        # Asking to set a temporary key outside of regular user scope.
        fp_val1 = str(uuid.getnode())
        fp_val2 = hashlib.md5(fp_val1.encode())
        fp_s = fp_val2.hexdigest()
        # We need to change the host, since we have to go direct to binubuo.
        self.binubuo_host = "binubuo.com"
        self.baseurl = "https://" + self.binubuo_host + '/api'
        # Set headers
        self.binubuo_key = fp_s
        self.setheaders()
        # Send key request
        self.resp = requests.request("POST", self.baseurl + '/binubuo-actions/get-temp-key', headers=self.headers)
        # instead of printing key, send request to get back actual temp key using fp_s
        if self.resp.ok:
            self.response_json = json.loads(self.resp.text)
            for key, value in self.response_json.items():
                # Getting the temporary key back we set it
                if key == "temp_key":
                    self.binubuo_key = value
                if key == 'unique_url':
                    self.unique_url_path = value
        else:
            if self.resp.status_code == 404:
                print("Temp key creation endpoint not found: " + self.baseurl + "/binubuo-actions/get-temp-key")
            else:
                print("Communication failure")

    def create_account(self, account_name, account_email, user_name=None):
        # Creating account directly from python client is only supported against binubuo.com directly.
        fp_val1 = str(uuid.getnode())
        fp_val2 = hashlib.md5(fp_val1.encode())
        fp_s = fp_val2.hexdigest()
        self.binubuo_host = "binubuo.com"
        self.baseurl = "https://" + self.binubuo_host + '/api'
        query_string = {"account_name": account_name}
        query_string["account_email"] = account_email
        if (user_name is not None):
            query_string["user_name"] = user_name
        headers = {}
        headers["x-binubuo-key"] = fp_s
        self.resp = requests.request("POST", self.baseurl + '/binubuo-actions/create-account', headers=headers, params=query_string)
        if self.resp.ok:
            self.response_json = json.loads(self.resp.text)
            self.challenge_hash = self.response_json["challenge_id"]
            print("Please got to this url in your browser: " + self.response_json["challenge_url"])
            challenge_response = input("Please input the code displayed in the above URL: ")
            query_string = {"challenge": self.challenge_hash}
            query_string["response"] = challenge_response
            self.resp = requests.request("POST", self.baseurl + '/binubuo-actions/verify-account', headers=headers, params=query_string)
            if self.resp.ok:
                # We now have the actual key 
                self.response_json = json.loads(self.resp.text)
                self.key(self.response_json["binubuo_key"])
                print("Your API key for Binubuo is (please save it.): " + self.binubuo_key)
            else:
                if self.resp.status_code == 401:
                    print("Verify account called wronng. Unauthorized")
                else:
                    print("Communication failure in verify-account")
        else:
            if self.resp.status_code == 401:
                print("Create account called wronng. Unauthorized")
            else:
                print("Communication failure in create-account")

    def key(self, key=None):
        if len(key.split('-')) > 1:
            # We know that we have a temporary key.
            self.binubuo_key = key
            self.binubuo_host = "binubuo.com"
            self.baseurl = "https://" + self.rapidapi_host + '/api'
            self.set_unique_url()
        elif(key is not None):
            rapid = 0
            for c in key:
                if c.islower():
                    rapid = 1
            if rapid == 1:
                self.rapidapi_key = key
                self.rapidapi_host = "binubuo.p.rapidapi.com"
                self.baseurl = "https://" + self.rapidapi_host
            else:
                self.binubuo_key = key
                self.binubuo_host = "binubuo.com"
                self.baseurl = "https://" + self.binubuo_host + '/api'
            self.set_unique_url()
        else:
            print("Key unset. Please set key before making calls to binubuo.")

    def readconfig(self):
        if(self.rapidapi_key is not None):
            self.rapidapi_host = "binubuo.p.rapidapi.com"
            self.baseurl = "https://" + self.rapidapi_host
        elif(self.binubuo_key is not None):
            self.binubuo_host = "binubuo.com"
            self.baseurl = "https://" + self.binubuo_host + '/api'
        else:
            # No key set. Base direct settings.
            self.binubuo_host = "binubuo.com"
            self.baseurl = "https://" + self.binubuo_host + '/api'
        self.default_generator_rows = 1
        self.default_dataset_rows = 10
        self.locale_set = None
        self.tag_set = None
        self.tz_set = None
        self.csv_set = None
        self.load_as = "json"
        self.generator_dict_cache = 0
        self.dataset_dict_cache = 0
        self.dict_cache = {}
        self.qf = 0

    def setheaders(self):
        self.headers = {}
        if(self.rapidapi_key is not None):
            self.headers["x-rapidapi-host"] = self.rapidapi_host
            self.headers["x-rapidapi-key"] = self.rapidapi_key
        elif(self.binubuo_key is not None):
            self.headers["x-binubuo-key"] = self.binubuo_key

    def __check_key_status_before_run(self):
        if self.binubuo_key is None and self.rapidapi_key is None:
            # Seems we are beeing called and no key is set.
            # Generate a temp key and alert user.
            self.set_temp_key()
            print("WARNING: Calling without a fixed key set. Will run on temporary key. Please remember to set key")
            print("If you do not have a key, you can always create one with the create_account method.")
            print("See details here: https://binubuo.com/ords/r/binubuo_ui/binubuo/python-client")


    def call_binubuo(self, rest_path, query_string):
        self.__check_key_status_before_run()
        self.setheaders()
        if(self.locale_set is not None):
            query_string["locale"] = self.locale_set
        if(self.tag_set is not None):
            query_string["tag"] = self.tag_set
        if(self.tz_set is not None):
            query_string["tz"] = self.tz_set
        if(self.category is None) and (self.csv_set is not None):
            query_string["csv"] = 1
        if(self.category is not None):
            self.resp = requests.request("GET", self.baseurl + self.category.lower() + rest_path.lower(), headers=self.headers, params=query_string)
        else:
            self.resp = requests.request("GET", self.baseurl + self.dataset_type.lower() + rest_path.lower(), headers=self.headers, params=query_string)
        if self.resp.ok:
            if self.load_as == "json":
                self.response_json = json.loads(self.resp.text)
            elif(self.category is None) and (self.csv_set is not None):
                self.response_csv = self.resp.text
            else:
                # Default to loads json
                self.response_json = json.loads(self.resp.text)
        else:
            if self.resp.status_code == 403:
                try:
                    error_json = json.loads(self.resp.text)
                    self.error_string = error_json["string_out"]
                    print(self.error_string)
                except:
                    print("Invalid API key specified.")
                    self.error_string = "Invalid API key specified."
            elif self.resp.status_code == 401:
                try:
                    error_json = json.loads(self.resp.text)
                    self.error_string = error_json["string_out"]
                    print(self.error_string)
                except:
                    print("Authorization failure")
                    self.error_string = "Authorization failure"
            elif self.resp.status_code == 404:
                print("Generator/Dataset path not found: " + rest_path)
                self.error_string = "Generator/Dataset path not found: " + rest_path
            else:
                print("Communication failure")
                self.error_string = "Communication failure"

    def call_binubuo_to_file(self, rest_path, query_string):
        self.__check_key_status_before_run()
        self.setheaders()
        if(self.locale_set is not None):
            query_string["locale"] = self.locale_set
        if(self.tag_set is not None):
            query_string["tag"] = self.tag_set
        if(self.tz_set is not None):
            query_string["tz"] = self.tz_set
        if(self.category is None) and (self.csv_set is not None):
            query_string["csv"] = 1
        if(self.category is not None):
            url_call = self.baseurl + self.category + rest_path
            #self.resp = requests.request("GET", self.baseurl + self.category + rest_path, headers=self.headers, params=query_string)
        else:
            url_call = self.baseurl + self.dataset_type + rest_path
            #self.resp = requests.request("GET", self.baseurl + self.dataset_type + rest_path, headers=self.headers, params=query_string)
        with requests.get(url_call, stream=True, headers=self.headers, params=query_string) as br:
            br.raise_for_status()
            with open(self.file_name, 'wb') as bf:
                for chunk in br.iter_content(chunk_size=8192):
                    bf.write(chunk)

    def tz(self, tz=None):
        self.tz_set = tz

    def locale(self, locale=None):
        self.locale_set = locale

    def tag(self, tag=None):
        self.tag_set = tag

    def csv(self, csv=None):
        self.csv_set = csv

    def grows(self, rows=1):
        self.default_generator_rows = rows

    def drows(self, rows=10):
        self.default_dataset_rows = rows

    def get_generator_response_value(self):
        if self.default_generator_rows == 1:
            # Request a single value directly.
            self.generator_response_value = list(list(self.response_json.values())[0][0].values())[0]
        else:
            # Request for more values. Make response into a list and return
            self.generator_response_value = []
            for prime_key in self.response_json:
                for idx, val in enumerate(self.response_json[prime_key]):
                    for key, value in val.items():
                        self.generator_response_value.append(value)

    def get_dataset_response_value(self, response_type="list"):
        if (self.dataset_type.find("data/standard") >= 0 or self.qf == 1) and (self.csv_set is None):
            # Purify result
            for standard_key in self.response_json:
                self.response_clean = self.response_json[standard_key]
        elif(self.csv_set is not None):
            self.response_clean = self.response_csv
        else:
            self.response_clean = self.response_json
        if response_type == "list":
            self.dataset_response_value = []
            if (self.csv_set is None):
                for rows in self.response_clean:
                    self.dataset_response_value.append(list(rows.values()))
            else:
                for line in self.response_clean.splitlines():
                    self.dataset_response_value.append(line.rstrip().split(','))
        elif response_type == "tuple":
            self.dataset_response_value = ()
            if (self.csv_set is None):
                for rows in self.response_clean:
                    self.dataset_response_value = self.dataset_response_value + tuple(list(rows.values()))
            else:
                for line in self.response_clean.splitlines():
                    self.dataset_response_value = self.dataset_response_value + tuple(line.rstrip().split(','))

    def print_dir_list(self, type_in="generators", only_cache=0):
        # Purify result only if we are getting from outside cache
        if (type_in == "generators" and self.generator_dict_cache == 0) or (type_in == "datasets" and self.dataset_dict_cache == 0):
            for standard_key in self.response_json:
                self.response_clean = self.response_json[standard_key]
                self.dict_cache[type_in] = self.response_clean
        else:
            # Dealing with an already cached request. Just load from cache
            self.response_clean = self.dict_cache[type_in]
        if type_in == "generators":
            if only_cache == 0:
                print("{:<20} {:<30}".format('Category:', 'Function:'))
                print("{:<20} {:<30}".format('===================', '============================='))
            for idx, val in enumerate(self.response_clean):
                for key, value in val.items():
                    if key == "GENERATOR_CATEGORY_NAME":
                        ws_cat = value
                    if key == "GENERATOR_WEBSERVICE_NAME":
                        ws_func = value
                if only_cache == 1:
                    self.generator_dict_cache = 1
                else:
                    print("{:<20} {:<30}".format(ws_cat, ws_func))
        elif type_in == "datasets":
            if only_cache == 0:
                print("{:<10} {:<20} {:<30}".format('Type:', 'Category:', 'Dataset:'))
                print("{:<10} {:<20} {:<30}".format('=========', '===================', '============================='))
            for idx, val in enumerate(self.response_clean):
                for key, value in val.items():
                    if key == "DATASET_TYPE_NAME":
                        ws_type = value.split(' ')[0]
                    if key == "DATASET_CATEGORY_NAME":
                        if value == "Custom":
                            ws_cat = ""
                        else:
                            ws_cat = value
                    if key == "DATASET_WEBSERVICE_NAME":
                        ws_func = value
                if only_cache == 1:
                    self.dataset_dict_cache = 1
                else:
                    print("{:<10} {:<20} {:<30}".format(ws_type, ws_cat, ws_func))


    def list_generators(self, only_cache=0):
        self.category = None
        self.dataset_type = "/"
        rest_path = "generator/"
        query_string = {}
        if self.generator_dict_cache == 0:
            # Only call if we have not cached already
            self.call_binubuo(rest_path, query_string)
            if self.resp.ok:
                pass
            else:
                print(self.error_string)
        self.print_dir_list("generators", only_cache)

    def list_datasets(self, only_cache=0):
        self.category = None
        self.dataset_type = "/"
        rest_path = "data/"
        query_string = {}
        if self.dataset_dict_cache == 0:
            # Only call if we have not cached already
            self.call_binubuo(rest_path, query_string)
            if self.resp.ok:
                pass
            else:
                print(self.error_string)
        self.print_dir_list("datasets", only_cache)

    def generate(self, category, function):
        # Incase called directly
        self.category = "/generator/" + category
        rest_path = "/" + function
        query_string = {"rows": self.default_generator_rows}
        self.call_binubuo(rest_path, query_string)
        if self.resp.ok:
            self.get_generator_response_value()
            return self.generator_response_value
        else:
            return self.error_string

    def dataset(self, dataset_name, dataset_type="custom", dataset_category=None):
        self.category = None
        if dataset_type.lower() == "custom":
            self.dataset_type = "/data/custom/" + self.unique_url_path
        elif dataset_type.lower() == "standard":
            self.dataset_type = "/data/standard/" + dataset_category
        rest_path = "/" + dataset_name
        query_string = {"rows": self.default_dataset_rows}
        self.call_binubuo(rest_path, query_string)
        if self.resp.ok:
            self.get_dataset_response_value()
            return self.dataset_response_value
        else:
            return self.error_string

    def dataset_to_file(self, dataset_name, file_name="same", dataset_type="custom", dataset_category=None):
        self.category = None
        if file_name == "same":
            if(self.csv_set is None):
                self.file_name = dataset_name + ".json"
            else:
                self.file_name = dataset_name + ".csv"
        else:
            self.file_name = file_name
        if dataset_type == "custom":
            self.dataset_type = "/data/custom/" + self.unique_url_path
        elif dataset_type == "standard":
            self.dataset_type = "/data/standard/" + dataset_category
        rest_path = "/" + dataset_name
        query_string = {"rows": self.default_dataset_rows}
        self.call_binubuo_to_file(rest_path, query_string)

    def quick_fetch(self, columns="first_name,last_name,address,city"):
        self.category = None
        self.dataset_type = "/data/custom"
        rest_path = "/quick_fetch"
        query_string = {"rows": self.default_dataset_rows}
        query_string["cols"] = columns
        self.call_binubuo(rest_path, query_string)
        if self.resp.ok:
            self.qf = 1
            self.get_dataset_response_value()
            self.qf = 0
            return self.dataset_response_value
        else:
            return self.error_string

    def quick_fetch_to_file(self, columns="first_name,last_name,address,city", file_name="same"):
        self.category = None
        if file_name == "same":
            if(self.csv_set is None):
                self.file_name = "quick_fetch-" + columns.replace(',', '-') + ".json"
            else:
                self.file_name = "quick_fetch-" + columns.replace(',', '-') + ".csv"
        else:
            self.file_name = file_name
        self.dataset_type = "/data/custom"
        rest_path = "/quick_fetch"
        query_string = {"rows": self.default_dataset_rows}
        query_string["cols"] = columns
        self.call_binubuo_to_file(rest_path, query_string)