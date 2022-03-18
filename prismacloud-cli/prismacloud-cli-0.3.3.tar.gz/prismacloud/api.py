import logging
import coloredlogs
import os
import json
import click
import prismacloud.version
from apiclient import *
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

global token

class PrismaCloudClient(APIClient):
    def request(self, method, params=None, type='cwpp'):
        logging.debug(self)
        if type=='cspm': 
            url = "https://{}/{}".format(API_ENDPOINT, method)
        else:
            url = "https://{}/api/v1/{}".format(PCC_API_ENDPOINT, method)

        logging.debug("Executing {} request [data:{}]".format(url, params))

        try:
            if params:
                response = self.get(url, params)
            else:
                response = self.get(url)
            
            # Response.content can but might not be json
            try:
                result = json.loads(response.content)
            except:
                result = response

            logging.debug(result)
            return result
        except Exception as e:
            logging.error(e)
            logging.error("Try to disable any SSL interception / VPN connections.")
            exit(1)


def get(method, params='', type='cwpp'):
    global token 

    click.get_current_context()

    # Before sending out the request, we are going to retrieve the configuration
    getConfig()

    logging.debug("Calling api method: /{}".format(method))
    logging.debug("Username: {}".format(ACCESS_KEY_ID))

    if type=='cspm':
        
        if 'token' in globals() and len(token) > 10:
            logging.debug("Token available")
        else:
            logging.debug("Creating a connection to cspm; login to fetch token.")
            token = loginCSPM(API_ENDPOINT, ACCESS_KEY_ID, SECRET_KEY)

        client = PrismaCloudClient(
            authentication_method=HeaderAuthentication(token=token),
        )
    if type=='cwpp':
        client = PrismaCloudClient(
            authentication_method=BasicAuthentication(username=ACCESS_KEY_ID, password=SECRET_KEY),
            response_handler=JsonResponseHandler
        )
        
    result = client.request(method, params, type)
    return result

def loginCSPM(base_url, access_key, secret_key):
    url = "https://%s/login" % (base_url)

    payload = json.dumps({
        "username": access_key,
        "password": secret_key
    })
    headers = {"content-type": "application/json; charset=UTF-8"}
    response = requests.post(url, headers=headers, data=payload)

    logging.debug("Logging into CSPM with username: {}".format(access_key))

    if response.status_code == 401:
        logging.error("Authentication error, check your configuration file.")
        exit(1)

    return response.json()["token"]

def getParamFromJson(config_file):
    logging.debug('Retrieving configuration')
    f = open(config_file,)
    params = json.load(f)
    try:
        api_endpoint = params["api_endpoint"]
        pcc_api_endpoint = params["pcc_api_endpoint"]
        access_key_id = params["access_key_id"]
        secret_key = params["secret_key"]
        # Closing file
        f.close()
        return api_endpoint, pcc_api_endpoint, access_key_id, secret_key
    except:
        api_endpoint = False
        pcc_api_endpoint = params["pcc_api_endpoint"]
        access_key_id = params["access_key_id"]
        secret_key = params["secret_key"]
        # Closing file
        f.close()
        return api_endpoint, pcc_api_endpoint, access_key_id, secret_key


def getConfig():
    global params
    params = click.get_current_context().find_root().params

    global API_ENDPOINT, PCC_API_ENDPOINT, ACCESS_KEY_ID, SECRET_KEY, token, version
    version = prismacloud.version.version

    logging.info('Running prismacloud-cli version {}'.format(version))
    PRISMA_CLOUD_DIRECTORY = os.environ['HOME'] + "/.prismacloud/"

    if os.path.exists(PRISMA_CLOUD_DIRECTORY):
        if os.path.exists(os.environ['HOME'] + "/.prismacloud/{}.json".format(params['configuration'])):
            try:
                CONFIG_FILE = PRISMA_CLOUD_DIRECTORY + \
                    "{}.json".format(params['configuration'])
                API_ENDPOINT, PCC_API_ENDPOINT, ACCESS_KEY_ID, SECRET_KEY = getParamFromJson(
                    CONFIG_FILE)
            except Exception as e:
                logging.info(e)
        else:
            CONFIG_FILE = os.environ['HOME'] + "/.prismacloud/credentials.json"
            API_ENDPOINT, PCC_API_ENDPOINT, ACCESS_KEY_ID, SECRET_KEY = getParamFromJson(
                CONFIG_FILE)

        logging.debug("Config loaded: {}".format(params['configuration']))

    else:
        logging.info(
            'Prisma cloud directory does not exists, let\'s create one in your $HOME/.prismacloud')
        os.makedirs(PRISMA_CLOUD_DIRECTORY)
        CONFIG_FILE = PRISMA_CLOUD_DIRECTORY + "credentials.json"
        API_ENDPOINT = input(
            "Enter CSPM API Endpoint (OPTIONAL if PCCE), eg: api.prismacloud.io: ")
        PCC_API_ENDPOINT = input(
            "Enter CWPP API Endpoint, eg: us-east1.cloud.twistlock.com/<tenant-id>: ")
        ACCESS_KEY_ID = input("Enter the access key ID: ")
        SECRET_KEY = input("Enter the secret key: ")
        API_FILE = {
            "api_endpoint": API_ENDPOINT,
            "pcc_api_endpoint": PCC_API_ENDPOINT,
            "access_key_id": ACCESS_KEY_ID,
            "secret_key": SECRET_KEY
        }

        json_string = json.dumps(API_FILE, sort_keys=True, indent=4)

        with open(CONFIG_FILE, 'w') as outfile:
            outfile.write(json_string)

    return
