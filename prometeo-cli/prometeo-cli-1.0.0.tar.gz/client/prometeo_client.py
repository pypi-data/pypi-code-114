import prometeo

TESTING_URL = 'https://test.prometeo.qualia.uy'
PRODUCTION_URL = 'https://prometeo.qualia.uy'
SANDBOX_URL = 'https://banking.sandbox.prometeoapi.com'

class SandboxClient(prometeo.banking.BankingAPIClient):

    ENVIRONMENTS = {
        'testing': TESTING_URL,
        'production': PRODUCTION_URL,
        'sandbox': SANDBOX_URL
    }



class ClientWrapper(prometeo.Client):

    def __init__(self, api_key, environment):
        super().__init__(api_key, environment)
        self._api_key = api_key
        self._environment = environment


    @property
    def banking(self):
        self._banking = SandboxClient(self._api_key, self._environment)
        return self._banking


class PrometeoClient(ClientWrapper):

    def __init__(self, api_key, environment):
        super().__init__(api_key, environment)
        self._client = ClientWrapper(api_key, environment=environment)

    def login(self, provider, username, password, **kwargs):
        session = self._client.banking.login(provider, username, password, **kwargs)
        return session.get_session_key()

    def logout(self):
        self._client.banking.logout()





