
import requests


class TokenAuth(object):
    
    def __init__(self, CLIENT_ID, CLIENT_SECRET, TENANT_ID):
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.TENANT_ID = TENANT_ID

        self.TOKEN_ENDPOINT = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"

        self.fetch_token()

    def fetch_token(self):
        urlheaders = {"Content-Type": "application/x-www-form-urlencoded"}
        urldata = {
            "grant_type": "client_credentials",
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "resource": "https://purview.azure.net"
        }
        request = requests.post(self.TOKEN_ENDPOINT, headers=urlheaders, data=urldata, allow_redirects=True)
        
        if request.status_code == 200:
            self.TOKEN = request.json()["access_token"]
        else:
            raise Exception(request.status_code, request.text)
    
    def return_token(self):
        return self.TOKEN

    def refresh_token(self):
        # TODO
        pass

