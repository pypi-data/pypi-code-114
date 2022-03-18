import requests

class Authentication():
    
    def getToken(baseUrl: str):
        url = baseUrl + "connect/token"
        payload='client_id=makana_api&grant_type=client_credentials&scope=makanaapp_api&client_secret=TAxhx%409tH(l%5EMgQ9FWE8%7DT%40NWUT9U)'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response =  requests.post(url, headers=headers, data=payload, verify=False)
        auth_response_json = response.json()
        auth_token = auth_response_json["access_token"]
        auth_token_header_value = "Bearer %s" % auth_token
        return auth_token_header_value