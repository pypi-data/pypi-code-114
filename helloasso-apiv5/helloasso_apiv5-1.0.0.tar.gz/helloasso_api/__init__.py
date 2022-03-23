from helloasso_api.apiv5client import ApiV5Client
from helloasso_api.client.authorization import AuthorizationApi

"""
Manage all calls to Helloasso api (including authentication calls).
Api endpoints are ordered by domain.

-- Setter and Getter for access/refresh tokens
Refresh and access tokens are stored in apiv5 instance. If you have multiples instances running 
and want to share tokens across instances you can use custom set/get methods.
If you do so you will have to handle storage logic on your side. 
Authentication logic will still be handle by ApiV5Client. 

Example:

def getter(token_key: str) -> str:
    redis.hget("token", token_key)
    
def setter(token_key: str, token: str) -> None:
    redis.hset("token", token_key, token)
    
api = ApiV5(
        client_id="XXXX",
        client_secret="XXXX",
        api_base="XXXX",
        oauth2_token_getter=getter
        oauth2_token_setter=setter
    )
"""


class HaApiV5(ApiV5Client):
    def __init__(self, *args, **kwargs):
        super(HaApiV5, self).__init__(*args, **kwargs)
        self.authorization = AuthorizationApi(self)
