

from wpasupplicantconf import WpaSupplicantConf
from .models import WiFiManagerProxy
from .models import WifiNetworkModel


class WPASupplicantProxy(WiFiManagerProxy):
    def __init__(self, cpath='/etc/wpa_supplicant/wpa_supplicant.conf'):
        self._cpath = cpath
        self._config = None
        super(WPASupplicantProxy, self).__init__()

    def _read_config(self):
        self._logger.info("Reading WPA supplicant configuration from {}".format(self._cpath))
        with open(self._cpath, 'r') as f:
            lines = f.readlines()
            self._config = WpaSupplicantConf(lines)

    def _get_configured_networks(self):
        networks = self._config.networks()
        return [WifiNetworkModel(ssid=k, psk=v['psk'])
                for k, v in networks.items()]

    def _write_config(self):
        self._logger.info("Writing WPA supplicant configuration to {}".format(self._cpath))
        with open(self._cpath, 'w') as f:
            self._config.write(f)

    def add_network(self, ssid, psk, **kwargs):
        super(WPASupplicantProxy, self).add_network(ssid, psk, **kwargs)
        psk = '"{}"'.format(psk)
        self._config.add_network(ssid, psk=psk, key_mgmt="WPA-PSK", **kwargs)
        self._write_config()

    def remove_network(self, ssid):
        super(WPASupplicantProxy, self).remove_network(ssid)
        self._config.remove_network(ssid)
        self._write_config()
