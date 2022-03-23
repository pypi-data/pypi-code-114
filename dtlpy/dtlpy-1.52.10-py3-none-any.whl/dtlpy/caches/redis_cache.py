import redis
import json
import datetime
from .base_cache import BaseCache


class RedisCache(BaseCache):
    def __init__(self, options=None, ttl=1000):
        if options is None:
            options = {}
        self.cache = redis.Redis(
            host=options.get('host', '127.0.0.1'),
            port=options.get('port', 6379),
            socket_keepalive=options.get('keepalive', True)
        )
        self.ttl = datetime.timedelta(seconds=ttl)

    def set(self, key, value):
        """
        set or add a key and value to the cache
        :param key: str or int type of key
        :param value: pickled value
        :return:
        """
        if not isinstance(key, str):
            raise ValueError("key must be string")
        self.cache.set(name=key, value=value)

    def list(self, pattern):
        """
        get the value of the key from the cache
        :param pattern: str or int type of key
        :return: the value of the key
        """
        # TODO make it genrator
        if '\\' in pattern:
            pattern = pattern.replace('\\', '\\\\')
        keys_list = self.cache.keys(pattern=r'{}'.format(pattern))
        return [json.loads(self.cache.get(k).decode("UTF-8")) for k in keys_list]

    def get(self, key):
        """
        get the value of the key from the cache
        :param key: str or int type of key
        :return: the value of the key
        """
        res = self.cache.get(r'{}'.format(key))
        if res is not None:
            return json.loads(res.decode("UTF-8"))

    def delete(self, key):
        """
        delete the element from the cache
        :param key: str or int type of key
        :return:
        """
        if '\\' in key:
            key = key.replace('\\', '\\\\')
        keys_list = self.cache.keys(pattern=key)
        for k in keys_list:
            self.cache.delete(k)

    def keys(self):
        """
        return all the cache keys
        :return: list of the keys
        """
        for output in list(self.cache.keys()):
            if output is not None:
                yield output.decode('utf-8')

    def clear(self):
        """
        return all the cache keys
        :return: list of the keys
        """
        all_keys = self.cache.keys('*')
        for k in all_keys:
            self.cache.delete(k)
