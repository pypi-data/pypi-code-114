# -*- coding: utf-8 -*-
import json
import requests

class Endereco:
    def __init__(self,descricao):
        self.descricao = descricao

    def __call__(self):
        url = "https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php"
        payload = {'endereco': self.descricao,'tipoCEP': 'ALL'}
        response = requests.request("POST", url, headers={}, data=payload)
        return response.text
    
    def __convert__(self):
        return json.loads(self.__call__())

    def mensagem(self):
        return self.__convert__()["mensagem"]
    
    def total(self):
        return self.__convert__()["total"]
    
    def resultados(self):
        return self.__convert__()["dados"]