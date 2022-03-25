from urllib.parse import ParseResult
import requests
from django.urls.base import reverse
from api.views.sync import VIEWSETS
from typing import List
from django.conf import settings


class ViewsetSyncer:
    """
    This has two different modes:
    Single -> Updates the object directly
    All -> Syncs all qs objects when attributes changed
    """

    def __init__(self, shop, viewset):
        self.viewset = viewset()
        self.serializer = self.viewset.serializer_class
        self.model = self.viewset.model
        self.shop = shop
        self.hash_url = self.get_url(reverse(self.viewset.hash_url))
        self.list_url = self.get_url(reverse(self.viewset.list_url))
        self.delete_objects = self.viewset.force_delete or shop.sync_delete

    @property
    def headers(self):
        return {'Authorization':self.shop.key.key}

    def get_url(self, path:str) -> ParseResult:
        url_kwargs={
            'scheme': self.shop.schema,
            'netloc': self.shop.domain,
            'path': path,
            'query': 'limit=1000000&format=json',
            'params': '',
            'fragment': '',
        }
        return ParseResult(**url_kwargs).geturl()

    def get_detail_url(self, sync_id):
        detail_urlname = 'sync-api:' + self.viewset.get_detail_urlname()
        path = reverse(detail_urlname, kwargs={'sync_id': sync_id})
        return self.get_url(path)

    def sync(self, qs=None):
        qs = qs or self.get_queryset()
        new_data = self.serializer(
            qs, many=True, context={'request': None}, hash_only=True).data
        print(f'{"GET:":8}' + self.hash_url, end='', flush=True)
        response = requests.get(self.hash_url, headers=self.headers)
        self.raise_for_status(response)
        existing_data = response.json()['results']
        create, update, delete = self.classify(existing_data, new_data)
        qs_dict = {}
        for obj in qs:
            key = getattr(obj, 'sync_id', False)
            if not key:
                key = self.hash_instance(obj)
                obj.sync_id = str(key)
            qs_dict[str(key)] = obj

        if self.delete_objects:
            for element in delete:
                self.delete(element['sync_id'])
        for element in update:
            self.update(qs_dict[element['sync_id']])
        for element in create:
            self.create(qs_dict[element['sync_id']])

    def create(self, instance):
        data = self.serialize(instance)
        url = self.list_url
        print(f'{"POST:":8}{url} {instance.sync_id}', end='', flush=True)
        response = requests.post(url, json=data, headers=self.headers)
        self.raise_for_status(response)

    def update(self, instance):
        data = self.serialize(instance)
        url = self.get_url(data['sync_url'])
        print(f'{"PATCH:":8}' + url, end='', flush=True)
        response = requests.patch(url, json=data, headers=self.headers)
        self.raise_for_status(response)

    def delete(self, sync_id):
        path = reverse(self.viewset.detail_url, kwargs={'sync_id': sync_id})
        url = self.get_url(path)
        print(f'{"DELETE:":8}' + url, end='', flush=True)
        response = requests.delete(url, headers=self.headers)
        self.raise_for_status(response)

    def serialize(self, instance):
        return self.serializer(instance, context={'request': None}).data

    def classify(self, existing:List, new:List):
        existing = {x['sync_id']: x for x in existing}
        new = {x['sync_id']: x for x in new}

        create = [v for k, v in new.items() if k not in existing]
        update = [v for k, v in new.items() if v not in create
                  and v['hash'] != existing[k]['hash']]
        delete = [v for k, v in existing.items() if k not in new]
        return create, update, delete

    def get_queryset(self, instance=None):
        qs = self.model.objects.all()
        return qs.filter(pk=instance.pk) if instance else qs

    def hash_instance(self, instance):
        return self.serializer(
            instance, context={'request': None}, hash_only=True)['hash'].value

    def raise_for_status(self, response):
        if settings.DEBUG:
            print(f' > {response.status_code} ({response.reason})')
        if response.status_code >= 300 and settings.DEBUG:
            print(f'\n{response.text}'[:100])
        response.raise_for_status()


class Syncer(ViewsetSyncer):
    """ Factory for ViewsetSyncer 
    Converts the viewset name to a api viewset object
    """
    VIEWSETS = {viewset().name: viewset for viewset in VIEWSETS}

    def __init__(self, shop, viewset_name):
        super().__init__(shop, self.VIEWSETS[viewset_name])
