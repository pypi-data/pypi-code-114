import requests
import json
import re
import os
from typing import Optional
from urllib.parse import unquote
from mia_api.config_file import APIPATH
from mia_api.utils import response_return
from fastapi import UploadFile

def new(token: str, user_id: int, bar_id: int, name: str):
  newjuicepath = APIPATH + '/users/' + str(user_id) + '/bars/' + str(bar_id)
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
    }
  data = {
    'name': name
    }
  response = requests.request("POST", newjuicepath, headers=headers, json=data)
  response_return(response)
  return response.json()

def make(token: str, pythonfile, jsonfile):
  makejuicepath = APIPATH + '/juices/'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  files = [
    ('subs', (os.path.basename(pythonfile.name), open(pythonfile.name, "rb"), 'text/x-python')),
    ('subs', (os.path.basename(jsonfile.name), open(jsonfile.name, "rb"), 'application/json'))
    ]
  response = requests.post(makejuicepath, headers=headers, files=files)
  response_return(response)
  return response.json()

def available_list(token: str):
  alistjuicepath = APIPATH + '/juices'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", alistjuicepath, headers=headers)
  response_return(response)
  return response.json()

def list(token: str, user_id: int, bar_id: int):
  listjuicepath = APIPATH + '/users/' + str(user_id) + '/bars/' + str(bar_id) + '/juices'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", listjuicepath, headers=headers)
  response_return(response)
  return response.json()

def get(token: str, user_id: int, bar_id: int, juice_id: int, rundate: Optional[int] = None, operational: bool = True):
  getjuicepath = APIPATH + '/users/' + str(user_id) + '/bars/' + str(bar_id) + '/juices/' + str(juice_id) + '/?operational=' + str(operational)
  if rundate: getjuicepath += '&rundate=' + str(rundate)
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", getjuicepath, headers=headers)
  response_return(response)
  filename = re.findall(r'"([^"]*)"', str(unquote(response.headers["content-disposition"])))[0]
  with open(filename, 'wb') as f:
    f.write(response.content)
  return filename + " has been created"

def remove(token: str, user_id: int, bar_id: int, juice_id: int):
  removejuicepath = APIPATH + '/users/' + str(user_id) + '/bars/' + str(bar_id) + '/juices/' + str(juice_id) + '/delete'
  headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + token
    }
  response = requests.request("GET", removejuicepath, headers=headers)
  response_return(response)
  return response.json()
