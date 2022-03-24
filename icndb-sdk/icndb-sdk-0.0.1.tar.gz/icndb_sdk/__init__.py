"""Just messing around"""
import requests


class API:
    """Simple class for ICNDB"""

    def __init__(self, base_url="https://api.icndb.com", **kwargs):
        """Init"""
        self.base_url = base_url
        self.kwargs = kwargs

    def get_jokes_all(self, params: dict = ""):
        """
        Function summary
        Args:
            params (dict): Used to pass in any call params
        Returns:
            dict: Returns all jokes in database
        Examples:
        >>> api = API()
        >>> jokes = api.get_jokes_all()
        >>> print(jokes)
        {
            'type': 'success',
            'value': [
                {
                    'id': 1,
                    'joke': 'Faster than a speeding bullet... More powerful than a locomotive...
                    Ableto leap tall buildings in a single bound... These are some of Chuck Norris's
                    warm-up exercises.',
                    'categories': ['explicit']
                }
                ...
            ]
        }
        """

        try:
            res = requests.get(self.base_url + "/jokes", params=params)
        except Exception as get_exception:
            print("Exception while sending GetRequest", get_exception)
        return res.json()

    def get_jokes_random(self, params: dict = "", amount: int = 1):
        """
        Function summary
        Args:
            params (dict): Used to pass in any call params
            amount (int): Used to select amount of jokes to return
        Returns:
            dict: Returns random joke or specific amount of random jokes
        Examples:
        >>> api = API()
        >>> jokes = api.get_jokes_random()
        >>> print(jokes)
        {
            'type': 'success',
            'value': {
                'id': 354,
                'joke': 'For undercover police work, Chuck Norris pins his badge underneath his
        shirt, directly into his chest.',
                'categories': []
            }
        }
        """
        try:
            if amount >= 1:
                res = requests.get(
                    self.base_url + f"/jokes/random/{amount}", params=params)
            else:
                res = requests.get(
                    self.base_url + "/jokes/random", params=params)
        except Exception as get_exception:
            print("Exception while sending GetRequest", get_exception)
        return res.json()

    def get_jokes_specific(self, params: dict = "", id_number: int = 354):
        """
        Function summary
        Args:
            params (dict): Used to pass in any call params
            id (int): Used to select specific joke by ID number
        Returns:
            dict: Returns joke by ID
        Examples:
        >>> api = API()
        >>> jokes = api.get_jokes_specific(id_number=20)
        >>> print(jokes)
        {
            'type': 'success',
            'value': {
                'id': 20,
                'joke': 'The Chuck Norris military unit was not used in the game Civilization
        4, because a single Chuck Norris could defeat the entire combined nations of the world
        in one turn.',
                'categories': ['nerdy']
            }
        }
        """
        try:
            res = requests.get(
                self.base_url + f"/jokes/{id_number}", params=params)
        except Exception as get_exception:
            print("Exception while sending GetRequest", get_exception)
        return res.json()

    def get_jokes_amount(self):
        """
        Function summary
        Args: N/A
        Returns:
            dict: Returns amount of jokes in database
        Examples:
        >>> api = API()
        >>> jokes = .get_jokes_amount()
        >>> print(jokes)
        {'type': 'success', 'value': 574}
        """
        try:
            res = requests.get(
                self.base_url + "/jokes/count")
        except Exception as get_exception:
            print("Exception while sending GetRequest", get_exception)
        return res.json()

    def get_jokes_category(self):
        """
        Function summary
        Args:
        Returns:
            dict: Returns available categories in database
        Examples:
        >>> api = API()
        >>> jokes = api.get_jokes_category()
        >>> print(jokes)
        {'type': 'success', 'value': ['explicit', 'nerdy']}
        """
        try:
            res = requests.get(
                self.base_url + "/categories")
        except Exception as get_exception:
            print("Exception while sending GetRequest", get_exception)
        return res.json()
