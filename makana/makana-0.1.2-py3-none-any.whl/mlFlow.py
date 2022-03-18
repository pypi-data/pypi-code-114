import enum
import json
import uuid
import requests
from makana.authService import Authentication

class ContainerRunMode(enum.Enum):
    Continuous = 0
    OnDemand = 1

class IdleTimeUnit(enum.Enum):
    Minute = 0
    Hour = 1
    Day = 2

class MLModel():
  
    def getModelFramworks(baseUrl: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url =  baseUrl + "api/makana/modelframeworks"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())

    def getMakanaModels(baseUrl: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/models"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def getMakanaModel(baseUrl: str, id: uuid):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/model/" + id
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def registerModel(baseUrl: str, modeName: str, description: str, modelFrameworkId: int, frameworkName: str, frameworkVersion:float,
                    modelFileName: str, modelFileDirectory: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/models"
        headers = {
            'Authorization': access_token_header
        }
        payload = {
            'id': '',
            'name': modeName,
            'description': description,
            'modelFrameworkId': str(modelFrameworkId),
            'frameworkName': frameworkName,
            'frameworkVersion': str(frameworkVersion),
            'modelFileName': modelFileName,
            'modelFileUri': ''
        }
        files = [
            ('modelFile',(modelFileName,open(modelFileDirectory,'rb'),'application/octet-stream'))
        ]
        
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())


class MLService():

    def getMakanaServices(baseUrl: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/modelservices"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def getMakanaService(baseUrl: str, id: uuid):
        
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/modelservice/" + id
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def registerModelService(baseUrl: str, serviceName: str, description: str, modelDefinitionId: uuid, scriptFileName:str, dependenciesFileName: str,
                             scriptFileDirectory: str, dependenciesFileDirectory: str,containerRunMode: ContainerRunMode, idleTimeUnit: IdleTimeUnit=None, idleTimeDuration: int=None):
        
        if containerRunMode.value == 1 and idleTimeDuration == None and idleTimeUnit == None:
            return print("IdleTimeDuration And IdleTimeUnit Require..")
            
        authentication = Authentication
        access_token_header = authentication.getToken(baseUrl)
        url = baseUrl + "api/makana/modelservices"
        headers = {
            'Authorization': access_token_header
        }
        dependenciesFileDirectory = dependenciesFileDirectory.replace("\r","\\r")
        payload = {
            'id': '',
            'name': serviceName,
            'description': description,
            'modelDefinitionId': modelDefinitionId,
            'containerRunMode': str(containerRunMode.value),
            'idleTimeUnit': str(idleTimeUnit.value) if containerRunMode.value == 1 else '',
            'idleTimeDuration': idleTimeDuration if containerRunMode.value == 1 else '',
            'scriptFileName': scriptFileName,
            'scriptFileUri': '',
            'dependenciesFileName': dependenciesFileName,
            'dependenciesFileUri': ''
        }
        files=[
            ('scriptFile',(scriptFileName,open(scriptFileDirectory,'rb'),'application/octet-stream')),
            ('dependenciesFile',(dependenciesFileName,open(dependenciesFileDirectory,'rb'),'text/plain'))
        ]
        
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())

