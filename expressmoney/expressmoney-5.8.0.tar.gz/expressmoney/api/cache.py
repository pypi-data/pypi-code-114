__all__ = ('CacheMixin', 'CacheObjectMixin', 'FlushCache')

import os
from typing import Union

from django.contrib.auth import get_user_model
from django.core.cache import cache

from expressmoney.api.utils import log

User = get_user_model()


class BaseCacheMixin:
    _cache_period: int = None

    @property
    def _cache_key(self):
        return getattr(self._user, 'id')

    @property
    def _data_key(self):
        return self._point_id.id

    @property
    def _cache(self):
        if self._memory_cache is None:
            all_cache_data = cache.get(self._cache_key)
            self._memory_cache = all_cache_data.get(self._data_key) if all_cache_data else None
            if os.getenv('IS_ENABLE_API_LOG') and self._memory_cache is not None:
                print(f'GET REDIS {self}')
        return self._memory_cache

    @_cache.setter
    def _cache(self, value: any):
        if value is not None:
            data = cache.get(self._cache_key)
            ext_data = {f'{self._data_key}': value}
            data = dict(**data, **ext_data) if data else ext_data
            cache.set(self._cache_key, data, self._cache_period)
            self._memory_cache = value

    @log
    def flush_cache(self):
        """Delete Redis cache for current endpoint"""
        data = cache.get(self._cache_key)
        if data:
            data.pop(self._data_key, False)
            cache.set(self._cache_key, data, self._cache_period)

    def _get_related_points(self) -> list:
        """Set related points here"""
        return list()

    def _flush_cache_related_points(self):
        related_points = self._get_related_points()
        for point in related_points:
            point.flush_cache()


class CacheMixin(BaseCacheMixin):

    def __init__(self, user: User, is_async: bool = False):
        super().__init__(user, is_async)
        self._memory_cache = None
        self._payload = None

    def _get(self) -> dict:
        if self._cache is not None:
            return self._cache
        return super()._get()

    def _post(self, payload: dict):
        self._payload = payload
        super()._post(payload)
        self._memory_cache = None
        self._flush_cache_related_points()

    def _post_file(self, file, file_name, type_):
        super()._post_file(file, file_name, type_)
        self._memory_cache = None
        self._flush_cache_related_points()


class CacheObjectMixin(BaseCacheMixin):

    def __init__(self, user: User, lookup_field_value: Union[None, str, int] = None, is_async: bool = False):
        super().__init__(user, lookup_field_value, is_async)
        self._memory_cache = None
        self._payload = None

    def _get(self) -> dict:
        if self._cache is not None:
            return self._cache
        return super()._get()

    def _put(self, payload: dict):
        self._payload = payload
        super()._put(payload)
        self._memory_cache = None
        self._flush_cache_related_points()

    @property
    def _data_key(self):
        return f'{super()._data_key}_{self._lookup_field_value}'


class FlushCache:
    """"Delete cache for all API points"""

    def __init__(self, user: User):
        self._user = user

    @log
    def flush_cache(self):
        cache.delete(self._cache_key)

    @property
    def _cache_key(self):
        return getattr(self._user, 'id')
