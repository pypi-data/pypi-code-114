from georacle.endpoints.endpoint import Endpoint


class Info(Endpoint):
    def __init__(self, headers: str):
        """
        Construct a new :code:`Info` endpoint

        :param dict[str, str] headers: Custom request headers
        """

        self.base_url = "https://api.georacle.io/info/{id}"
        super().__init__(headers)

    def query(self, id: str, keys: list[str], decode: bool = False) -> dict[str, str]:
        """
        Filter the attributes of a location

        :param str id: A location ID
        :param list[str] keys: A list of attribute keys to filer
        :param bool decode: Decode ABI-packed payload if true (optional)
        :return: A map of resulting key-value pairs
        :rtype: dict[str, str]
        """

        params = {"keys": keys}
        url = self.base_url.format(id=id)
        resp = self._raw_query(url, params)
        if decode:
            vals = self._decode_location(resp)
            return dict(zip(keys, vals))
        return resp
