

class PurviewConnection(object):
    
    def __init__(self, resource, auth):
        self.purviewEndpoint = f"https://{resource}.purview.azure.com"
        self.auth = auth
        self.headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.auth.return_token()}"}

