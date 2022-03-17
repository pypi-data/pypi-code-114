import requests
import json
from mia_api.config_file import APIPATH
from mia_api.utils import response_return

def new(token: str, user_id: int, name: str):
  newbarpath = APIPATH + '/users/' + str(user_id) + '/bars'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
    }
  data = {
    'name': name
    }
  response = requests.request("POST", newbarpath, headers=headers, json=data)
  response_return(response)
  return response.json()

def list(token: str, user_id: int):
  listbarpath = APIPATH + '/users/' + str(user_id) + '/bars'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", listbarpath, headers=headers)
  response_return(response)
  return response.json()

def menu(token: str, user_id: int, bar_id: int):
  menubarpath = APIPATH + '/users/' + str(user_id) + '/bars/' + str(bar_id) + '/menu?html=false'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token,
    }
  response = requests.request("GET", menubarpath, headers=headers)
  response_return(response)
  return response.json()
