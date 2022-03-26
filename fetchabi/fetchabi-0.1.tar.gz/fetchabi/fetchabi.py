#!/usr/bin/python
import requests
import json

# Exports contract ABI in JSON

ABI_ENDPOINT = 'https://api.etherscan.io/api?module=contract&action=getabi&address='

def fetch_abi(contract_address):
    response = requests.get('%s%s'%(ABI_ENDPOINT, contract_address))
    response_json = response.json()
    abi_json = json.loads(response_json['result'])
    result = json.dumps({"abi":abi_json}, indent=4, sort_keys=True)

    return result

if __name__ == '__main__':
    abi = fetch_abi("0xe11c90922BB5d6fe661B44039DA64c04b5B153E9")
    print(abi)