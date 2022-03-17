

import os
import yaml
from .models import WiFiManagerProxy
from .models import WifiNetworkModel


class NetplanWifiProxy(WiFiManagerProxy):
    def __init__(self, cpath='/etc/netplan/01-ebs-netconfig-wifi.conf', device='wlan0'):
        self._cpath = cpath
        self._device = device
        self._config = None
        super(NetplanWifiProxy, self).__init__()

    @property
    def _stub(self):
        return {
            'network': {
                'version': 2,
                'wifis': {
                    self._device: {
                        'access-points': {},
                        'dhcp4': True,
                        'optional': True,
                    }
                }
            }
        }

    def _read_config(self):
        self._logger.info("Reading netplan WiFi configuration from {}".format(self._cpath))
        if not os.path.exists(self._cpath):
            self._logger.info("Writing netplan WiFi configuration stub to {}".format(self._cpath))
            with open(self._cpath, 'w') as f:
                yaml.safe_dump(self._stub, f)
        with open(self._cpath, 'r') as f:
            self._config = yaml.safe_load(f)

    def _get_configured_networks(self):
        return [WifiNetworkModel(ssid=k, psk=v['password'])
                for k, v in self._network_list.items()]

    def _write_config(self):
        self._logger.info("Writing netplan wifi configuration to {}".format(self._cpath))
        with open(self._cpath, 'w') as f:
            yaml.safe_dump(self._config, f)

    @property
    def _network_list(self):
        return self._config['network']['wifis'][self._device]['access-points']

    def add_network(self, ssid, psk, **kwargs):
        super(NetplanWifiProxy, self).add_network(ssid, psk, **kwargs)
        self._network_list[ssid] = {'password': psk}
        self._write_config()

    def remove_network(self, ssid):
        super(NetplanWifiProxy, self).remove_network(ssid)
        self._network_list.pop(ssid)
        self._write_config()
