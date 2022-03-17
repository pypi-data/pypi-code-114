"""
    Karrio API

     ## API Reference  Karrio is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Karrio API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Karrio API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released. The current version is `2022.4`.  Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade.   ## Pagination  All top-level API resources have support for bulk fetches via \"list\" API methods. For instance, you can list addresses, list shipments, and list trackers. These list API methods share a common structure, taking at least these two parameters: limit, and offset.  Karrio utilizes offset-based pagination via the offset and limit parameters. Both parameters take a number as value (see below) and return objects in reverse chronological order. The offset parameter returns objects listed after an index. The limit parameter take a limit on the number of objects to be returned from 1 to 100.   ```json {     \"next\": \"/v1/shipments?limit=25&offset=25\",     \"previous\": \"/v1/shipments?limit=25&offset=25\",     \"results\": [     ] } ```  ## Environments  The Karrio API offer the possibility to create and retrieve certain objects in `test_mode`. In development, it is therefore possible to add carrier connections, get live rates, buy labels, create trackers and schedule pickups in `test_mode`.    # noqa: E501

    The version of the OpenAPI document: 2022.4
    Contact: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from karrio.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from karrio.exceptions import ApiAttributeError


def lazy_import():
    from karrio.model.message import Message
    from karrio.model.tracking_event import TrackingEvent
    globals()['Message'] = Message
    globals()['TrackingEvent'] = TrackingEvent


class TrackingStatus(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'PENDING': "pending",
            'IN_TRANSIT': "in_transit",
            'INCIDENT': "incident",
            'DELIVERED': "delivered",
        },
    }

    validations = {
        ('carrier_name',): {
            'min_length': 1,
        },
        ('carrier_id',): {
            'min_length': 1,
        },
        ('tracking_number',): {
            'min_length': 1,
        },
        ('id',): {
            'min_length': 1,
        },
        ('estimated_delivery',): {
            'min_length': 1,
        },
        ('object_type',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'carrier_name': (str,),  # noqa: E501
            'carrier_id': (str,),  # noqa: E501
            'tracking_number': (str,),  # noqa: E501
            'test_mode': (bool,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'events': ([TrackingEvent], none_type,),  # noqa: E501
            'delivered': (bool,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'estimated_delivery': (str,),  # noqa: E501
            'object_type': (str,),  # noqa: E501
            'metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'messages': ([Message],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'carrier_name': 'carrier_name',  # noqa: E501
        'carrier_id': 'carrier_id',  # noqa: E501
        'tracking_number': 'tracking_number',  # noqa: E501
        'test_mode': 'test_mode',  # noqa: E501
        'id': 'id',  # noqa: E501
        'events': 'events',  # noqa: E501
        'delivered': 'delivered',  # noqa: E501
        'status': 'status',  # noqa: E501
        'estimated_delivery': 'estimated_delivery',  # noqa: E501
        'object_type': 'object_type',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'messages': 'messages',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, carrier_name, carrier_id, tracking_number, test_mode, *args, **kwargs):  # noqa: E501
        """TrackingStatus - a model defined in OpenAPI

        Args:
            carrier_name (str): The tracking carrier
            carrier_id (str): The tracking carrier configured identifier
            tracking_number (str): The shipment tracking number
            test_mode (bool): Specified whether the object was created with a carrier in test mode

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): A unique identifier. [optional]  # noqa: E501
            events ([TrackingEvent], none_type): The tracking details events. [optional]  # noqa: E501
            delivered (bool): Specified whether the related shipment was delivered. [optional]  # noqa: E501
            status (str): The current tracking status. [optional] if omitted the server will use the default value of "pending"  # noqa: E501
            estimated_delivery (str): The delivery estimated date. [optional]  # noqa: E501
            object_type (str): Specifies the object type. [optional] if omitted the server will use the default value of "tracker"  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): User metadata for the tracker. [optional]  # noqa: E501
            messages ([Message]): The list of note or warning messages. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.carrier_name = carrier_name
        self.carrier_id = carrier_id
        self.tracking_number = tracking_number
        self.test_mode = test_mode
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, carrier_name, carrier_id, tracking_number, test_mode, *args, **kwargs):  # noqa: E501
        """TrackingStatus - a model defined in OpenAPI

        Args:
            carrier_name (str): The tracking carrier
            carrier_id (str): The tracking carrier configured identifier
            tracking_number (str): The shipment tracking number
            test_mode (bool): Specified whether the object was created with a carrier in test mode

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): A unique identifier. [optional]  # noqa: E501
            events ([TrackingEvent], none_type): The tracking details events. [optional]  # noqa: E501
            delivered (bool): Specified whether the related shipment was delivered. [optional]  # noqa: E501
            status (str): The current tracking status. [optional] if omitted the server will use the default value of "pending"  # noqa: E501
            estimated_delivery (str): The delivery estimated date. [optional]  # noqa: E501
            object_type (str): Specifies the object type. [optional] if omitted the server will use the default value of "tracker"  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): User metadata for the tracker. [optional]  # noqa: E501
            messages ([Message]): The list of note or warning messages. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.carrier_name = carrier_name
        self.carrier_id = carrier_id
        self.tracking_number = tracking_number
        self.test_mode = test_mode
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
