import json
import io
import os
from enum import Enum

from drb_impl_odata.cache import timed_lru_cache
from requests.auth import AuthBase
from typing import List
from defusedxml import ElementTree
from defusedxml.ElementTree import ParseError
from drb.predicat import Predicate
from drb.exceptions import DrbException
from drb_impl_http import DrbHttpNode

from .odata_node import OdataNode
from .exceptions import OdataRequestException

USER_CACHE_EXPIRE_SEC = \
    os.environ.get('DRB_ODATA_NODE_REQUEST_CACHE_EXPIRE_TIME_SEC')

USER_CACHE_MAX_ELEMENTS = \
    os.environ.get('DRB_ODATA_NODE_REQUEST_CACHE_MAX_ELEMENTS')

DEFAULT_REQUEST_CACHE_EXPIRE_TIME_SEC = int(USER_CACHE_EXPIRE_SEC) \
    if USER_CACHE_EXPIRE_SEC is not None else 120

DEFAULT_USER_CACHE_MAX_ELEMENTS = int(USER_CACHE_MAX_ELEMENTS) \
    if USER_CACHE_MAX_ELEMENTS is not None else 32


class OdataServiceType(Enum):
    UNKNOWN = 0
    CSC = 1
    DHUS = 2
    ONDA_DIAS = 3


def get_url_uuid_product(odata: OdataNode, prd_uuid: str):
    if odata.type_service == OdataServiceType.DHUS:
        return f'{odata.get_service_url()}/Products(\'{prd_uuid}\')'
    # elif odata.type_service() in [OdataServiceType.CSC,
    # OdataServiceType.UNKNOWN]:

    return f'{odata.get_service_url()}/Products({prd_uuid})'


def get_url_attributes(odata: OdataNode, prd_uuid: str):
    if odata.type_service == OdataServiceType.ONDA_DIAS:
        return get_url_uuid_product(odata, prd_uuid) + '/Metadata'
    else:
        return get_url_uuid_product(odata, prd_uuid) + '/Attributes'


def http_node_to_json(node: DrbHttpNode) -> dict:
    try:
        with node.get_impl(io.BytesIO) as stream:
            data = json.load(stream)
            if 'error' in data.keys():
                raise OdataRequestException(str(data['error']))
            return data
    except json.JSONDecodeError:
        raise OdataRequestException(f'Invalid json from {node.path.name}')
    except DrbException:
        raise OdataRequestException(f'Invalid node: {type(node)}')


def get_type_odata_svc(service_url: str, auth: AuthBase = None) \
        -> OdataServiceType:
    """
    Retrieve with the given URL the OData service type (CSC or DHuS).
    :param service_url: service URL
    :type service_url: str
    :param auth: (optional) authentication mechanism required by the service
    :param auth: AuthBase
    :returns: OdataServiceType value corresponding to service.
    :rtype: OdataServiceType
    """
    try:
        url = f'{service_url}/$metadata'
        node = DrbHttpNode(url, auth=auth)
        tree = ElementTree.parse(node.get_impl(io.BytesIO))
        ns = tree.getroot()[0][0].get('Namespace', None)
        if 'OData.CSC'.lower() == ns.lower():
            return OdataServiceType.CSC
        elif 'OData.DHuS'.lower() == ns.lower():
            return OdataServiceType.DHUS
        elif 'Ens'.lower() == ns.lower():
            return OdataServiceType.ONDA_DIAS
        return OdataServiceType.UNKNOWN
    except (DrbException, ParseError):
        return OdataServiceType.UNKNOWN


@timed_lru_cache(
    seconds=DEFAULT_REQUEST_CACHE_EXPIRE_TIME_SEC,
    maxsize=DEFAULT_USER_CACHE_MAX_ELEMENTS)
def req_svc(odata: OdataNode) -> dict:
    node = DrbHttpNode(odata.get_service_url(), auth=odata.get_auth(),
                       params={'$format': 'json'})
    data = http_node_to_json(node)
    return data


def req_svc_count(odata: OdataNode) -> int:
    url = f'{odata.get_service_url()}/Products/$count'
    node = DrbHttpNode(url, auth=odata.get_auth())
    stream = node.get_impl(io.BytesIO)
    value = stream.read().decode()
    stream.close()
    return int(value)


@timed_lru_cache(
    seconds=DEFAULT_REQUEST_CACHE_EXPIRE_TIME_SEC,
    maxsize=DEFAULT_USER_CACHE_MAX_ELEMENTS)
def req_svc_products(odata: OdataNode, **kwargs) -> list:
    params = {'$format': 'json'}
    if 'filter' in kwargs.keys() and kwargs['filter'] is not None:
        params['$filter'] = kwargs['filter'].replace('\'', '%27')
    if 'search' in kwargs.keys() and kwargs['search'] is not None:
        params['$search'] = kwargs['search']
    if 'order' in kwargs.keys() and kwargs['order'] is not None:
        params['$orderby'] = kwargs['order']
    if 'skip' in kwargs.keys() and kwargs['skip'] is not None:
        params['$skip'] = kwargs['skip']
    if 'top' in kwargs.keys() and kwargs['top'] is not None:
        params['$top'] = kwargs['top']

    query = '&'.join(map(lambda k: f'{k[0]}={k[1]}', params.items()))
    url = f'{odata.get_service_url()}/Products?{query}'
    node = DrbHttpNode(url, auth=odata.get_auth())
    data = http_node_to_json(node)
    return data['value']


@timed_lru_cache(
    seconds=DEFAULT_REQUEST_CACHE_EXPIRE_TIME_SEC,
    maxsize=DEFAULT_USER_CACHE_MAX_ELEMENTS)
def req_product_by_uuid(odata: OdataNode, prd_uuid: str) -> dict:
    url = get_url_uuid_product(odata, prd_uuid)
    params = {'$format': 'json'}
    node = DrbHttpNode(url, auth=odata.get_auth(), params=params)
    return {
        k: v for k, v in http_node_to_json(node).items()
        if not k.startswith('@odata.')
    }


@timed_lru_cache(
    seconds=DEFAULT_REQUEST_CACHE_EXPIRE_TIME_SEC,
    maxsize=DEFAULT_USER_CACHE_MAX_ELEMENTS)
def req_product_attributes(odata: OdataNode, prd_uuid: str) -> List[dict]:
    url = get_url_attributes(odata, prd_uuid)
    params = {'$format': 'json'}
    node = DrbHttpNode(url, auth=odata.get_auth(), params=params)
    data = http_node_to_json(node)
    return data['value']


def req_product_download(
        odata: OdataNode,
        prd_uuid: str,
        start=None,
        end=None
) -> io.BytesIO:
    url = get_url_uuid_product(odata, prd_uuid) + '/$value'
    node = DrbHttpNode(url, auth=odata.get_auth())
    if start is None or end is None:
        return node.get_impl(io.BytesIO)
    return node.get_impl(io.BytesIO, start=start, end=end)


class ODataQueryPredicate(Predicate):
    """
    This Predicate allows to customize the OData query request.

    ODataCustomQuery constructor

        :key filter: OData query filter
        :key search: OData query search
        :key order: OData query orderby
        :key skip: OData query skip
        :key top: ODate query top
    """

    def __init__(self, **kwargs):
        """

        """
        self.__filter = kwargs['filter'] if 'filter' in kwargs.keys() else None
        self.__search = kwargs['search'] if 'search' in kwargs.keys() else None
        self.__order = kwargs['order'] if 'order' in kwargs.keys() else None
        self.__skip = kwargs['skip'] if 'skip' in kwargs.keys() else None
        self.__top = kwargs['top'] if 'top' in kwargs.keys() else None

    def matches(self, key) -> bool:
        return False

    def apply_query(self, node: OdataNode) -> List[dict]:
        """
        Performs the request with specific given query parameters.

        :param node: OData service on which perform the request.
        :type node: OdataNode
        :returns: list of dictionary (JSON OData response)
        :rtype: list
        """
        return req_svc_products(node, filter=self.__filter, order=self.__order,
                                skip=self.__skip, top=self.__top,
                                search=self.__search)
