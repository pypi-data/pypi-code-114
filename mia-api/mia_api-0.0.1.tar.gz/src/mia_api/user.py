import requests
import json
from mia_api.config_file import APIPATH
from mia_api.utils import response_return

def access_token(username: str, password: str):
  tokenpath = APIPATH + '/token'
  headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
  data = {
    'grant_type': '',
    'username': username,
    'password': password,
    'scope': '',
    'client_id': '',
    'client_secret': ''
    }
  response = requests.request("POST", tokenpath, headers=headers, data=data)
  response_return(response)
  return response.json()["access_token"]

def current_user(token: str):
  currentuserpath = APIPATH + '/users/me'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", currentuserpath, headers=headers)
  response_return(response)
  return response.json()
