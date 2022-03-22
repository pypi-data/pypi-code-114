# -*- coding: utf-8 -*-

from pip_services3_container import ProcessContainer
from pip_services3_rpc.build import DefaultRpcFactory
from pip_services3_swagger.build import DefaultSwaggerFactory

from service_firemap_python.build import FireMapServiceFactory


class FireMapProcess(ProcessContainer):

    def __init__(self):
        super(FireMapProcess, self).__init__('firemap', 'FireMap microservice')
        self._factories.add(FireMapServiceFactory())
        self._factories.add(DefaultRpcFactory())
        self._factories.add(DefaultSwaggerFactory())
