# -*- coding: utf-8 -*-

from pip_services3_commons.refer import Descriptor
from pip_services3_components.build import Factory

from service_firemap_python.logic import FireMapController
from service_firemap_python.persistence import (
    FireMapMemoryPersistence, FireMapFilePersistence, FireMapMongoDbPersistence
)
from service_firemap_python.services.version1 import FireMapsCommandableHttpServiceV1


class FireMapServiceFactory(Factory):
    __MemoryPersistenceDescriptor = Descriptor(
        'eic-stopfires-services-firemap', 'persistence', 'memory', '*', '1.0')

    __FilePersistenceDescriptor = Descriptor(
        'eic-stopfires-services-firemap', 'persistence', 'file', '*', '1.0')

    __MongoDbPersistenceDescriptor = Descriptor(
        'eic-stopfires-services-firemap', 'persistence', 'mongodb', '*', '1.0')

    __ControllerDescriptor = Descriptor(
        'eic-stopfires-services-firemap', 'controller', 'default', '*', '1.0')

    __CommandableHttpServiceV1Descriptor = Descriptor(
        'eic-stopfires-services-firemap',
        'service',
        'commandable-http',
        '*',
        '1.0')

    def __init__(self):
        super().__init__()

        self.register_as_type(self.__MemoryPersistenceDescriptor, FireMapMemoryPersistence)
        self.register_as_type(self.__FilePersistenceDescriptor, FireMapFilePersistence)
        self.register_as_type(self.__MongoDbPersistenceDescriptor, FireMapMongoDbPersistence)
        self.register_as_type(self.__ControllerDescriptor, FireMapController)
        self.register_as_type(self.__CommandableHttpServiceV1Descriptor, FireMapsCommandableHttpServiceV1)
