import prometeo

class SandboxClient(prometeo.banking.BankingAPIClient):
    ENVIRONMENTS = {
        'sandbox': 'https://banking.sandbox.prometeoapi.com'
    }

class ClientWrapper(prometeo.Client):

    def __init__(self, api_key, environment='sandbox'):
        super().__init__(api_key, environment)
        self._api_key = api_key
        self._environment = environment


    @property
    def banking(self):
        self._banking = SandboxClient(self._api_key, self._environment)
        return self._banking


class PrometeoClient(prometeo.Client):

    def __init__(self, api_key):
        self._api_key = api_key
        self._client = ClientWrapper(api_key)
        self._session = None

    def login(self, provider, username, password, **kwargs):
        self._session = self._client.banking.login(provider, username, password, **kwargs)
        return self._session.get_session_key()

    def get_session(self):
        return self._session


