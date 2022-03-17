"""
    Fatture in Cloud API v2 - API Reference

    Connect your software with Fatture in Cloud, the invoicing platform chosen by more than 400.000 businesses in Italy.   The Fatture in Cloud API is based on REST, and makes possible to interact with the user related data prior authorization via OAuth2 protocol.  # noqa: E501

    The version of the OpenAPI document: 2.0.14
    Contact: info@fattureincloud.it
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from fattureincloud_python_sdk.api_client import ApiClient, Endpoint as _Endpoint
from fattureincloud_python_sdk.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fattureincloud_python_sdk.model.create_supplier_request import CreateSupplierRequest
from fattureincloud_python_sdk.model.create_supplier_response import CreateSupplierResponse
from fattureincloud_python_sdk.model.get_supplier_response import GetSupplierResponse
from fattureincloud_python_sdk.model.list_suppliers_response import ListSuppliersResponse
from fattureincloud_python_sdk.model.modify_supplier_request import ModifySupplierRequest
from fattureincloud_python_sdk.model.modify_supplier_response import ModifySupplierResponse


class SuppliersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_supplier_endpoint = _Endpoint(
            settings={
                'response_type': (CreateSupplierResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/entities/suppliers',
                'operation_id': 'create_supplier',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'create_supplier_request',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'create_supplier_request':
                        (CreateSupplierRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'create_supplier_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_supplier_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/entities/suppliers/{supplier_id}',
                'operation_id': 'delete_supplier',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'supplier_id',
                ],
                'required': [
                    'company_id',
                    'supplier_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'supplier_id':
                        (int,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'supplier_id': 'supplier_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'supplier_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_supplier_endpoint = _Endpoint(
            settings={
                'response_type': (GetSupplierResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/entities/suppliers/{supplier_id}',
                'operation_id': 'get_supplier',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'supplier_id',
                    'fields',
                    'fieldset',
                ],
                'required': [
                    'company_id',
                    'supplier_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fieldset',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fieldset',): {

                        "BASIC": "basic",
                        "DETAILED": "detailed"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'supplier_id':
                        (int,),
                    'fields':
                        (str,),
                    'fieldset':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'supplier_id': 'supplier_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                },
                'location_map': {
                    'company_id': 'path',
                    'supplier_id': 'path',
                    'fields': 'query',
                    'fieldset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_suppliers_endpoint = _Endpoint(
            settings={
                'response_type': (ListSuppliersResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/entities/suppliers',
                'operation_id': 'list_suppliers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'fields',
                    'fieldset',
                    'sort',
                    'page',
                    'per_page',
                    'q',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fieldset',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fieldset',): {

                        "BASIC": "basic",
                        "DETAILED": "detailed"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'fields':
                        (str,),
                    'fieldset':
                        (str,),
                    'sort':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'q':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'fields': 'fields',
                    'fieldset': 'fieldset',
                    'sort': 'sort',
                    'page': 'page',
                    'per_page': 'per_page',
                    'q': 'q',
                },
                'location_map': {
                    'company_id': 'path',
                    'fields': 'query',
                    'fieldset': 'query',
                    'sort': 'query',
                    'page': 'query',
                    'per_page': 'query',
                    'q': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.modify_supplier_endpoint = _Endpoint(
            settings={
                'response_type': (ModifySupplierResponse,),
                'auth': [
                    'OAuth2AuthenticationCodeFlow'
                ],
                'endpoint_path': '/c/{company_id}/entities/suppliers/{supplier_id}',
                'operation_id': 'modify_supplier',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'supplier_id',
                    'modify_supplier_request',
                ],
                'required': [
                    'company_id',
                    'supplier_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (int,),
                    'supplier_id':
                        (int,),
                    'modify_supplier_request':
                        (ModifySupplierRequest,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'supplier_id': 'supplier_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'supplier_id': 'path',
                    'modify_supplier_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_supplier(
        self,
        company_id,
        **kwargs
    ):
        """Create Supplier  # noqa: E501

        Creates a new supplier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_supplier(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            create_supplier_request (CreateSupplierRequest): The supplier to create. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreateSupplierResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        return self.create_supplier_endpoint.call_with_http_info(**kwargs)

    def delete_supplier(
        self,
        company_id,
        supplier_id,
        **kwargs
    ):
        """Delete Supplier  # noqa: E501

        Deletes the specified supplier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_supplier(company_id, supplier_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            supplier_id (int): The ID of the supplier.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['supplier_id'] = \
            supplier_id
        return self.delete_supplier_endpoint.call_with_http_info(**kwargs)

    def get_supplier(
        self,
        company_id,
        supplier_id,
        **kwargs
    ):
        """Get Supplier  # noqa: E501

        Gets the specified supplier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_supplier(company_id, supplier_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            supplier_id (int): The ID of the supplier.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GetSupplierResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['supplier_id'] = \
            supplier_id
        return self.get_supplier_endpoint.call_with_http_info(**kwargs)

    def list_suppliers(
        self,
        company_id,
        **kwargs
    ):
        """List Suppliers  # noqa: E501

        Lists the suppliers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_suppliers(company_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.

        Keyword Args:
            fields (str): List of comma-separated fields.. [optional]
            fieldset (str): Name of the fieldset.. [optional]
            sort (str): List of comma-separated fields for result sorting (minus for desc sorting).. [optional]
            page (int): The page to retrieve.. [optional] if omitted the server will use the default value of 1
            per_page (int): The size of the page.. [optional] if omitted the server will use the default value of 5
            q (str): Query for filtering the results.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListSuppliersResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        return self.list_suppliers_endpoint.call_with_http_info(**kwargs)

    def modify_supplier(
        self,
        company_id,
        supplier_id,
        **kwargs
    ):
        """Modify Supplier  # noqa: E501

        Modifies the specified supplier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_supplier(company_id, supplier_id, async_req=True)
        >>> result = thread.get()

        Args:
            company_id (int): The ID of the company.
            supplier_id (int): The ID of the supplier.

        Keyword Args:
            modify_supplier_request (ModifySupplierRequest): The modified Supplier. First level parameters are managed in delta mode.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ModifySupplierResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['company_id'] = \
            company_id
        kwargs['supplier_id'] = \
            supplier_id
        return self.modify_supplier_endpoint.call_with_http_info(**kwargs)

