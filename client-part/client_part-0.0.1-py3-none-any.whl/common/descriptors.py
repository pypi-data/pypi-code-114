import sys
from ipaddress import ip_address
from logging import getLogger
from common.variables import DEF_PORT, DEF_IP_ADDRESS
from log import config_server_log

logger = getLogger('server')


class Port:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value=DEF_PORT):

        if not 1023 < value < 65536:
            logger.critical(
                f'exit(1). Номер порта - число от 1024 до 65535. Передано: {value}')
            sys.exit(1)
        # Если порт верифицирован, добавляет в список атрибутов экземпляра
        instance.__dict__[self.name] = value


class Host:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value=DEF_IP_ADDRESS):
        if not value == '':
            try:
                address = ip_address(value)
            except ValueError:
                logger.critical(
                    f'exit(1). Неверный IP-адрес. Передано: {value}')
                sys.exit(1)
        # Если ip-адрес верифицирован, добавляет в список атрибутов экземпляра
        instance.__dict__[self.name] = value


if __name__ == '__main__':
    class MyTest:
        port = Port()
        #ip = Host()

    test = MyTest()
    test.port = 50000
    test.ip = '8.8.8.u'
    print(test.port, test.ip)
