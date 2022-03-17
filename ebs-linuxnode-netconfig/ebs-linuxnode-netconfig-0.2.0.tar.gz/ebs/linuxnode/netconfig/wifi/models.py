

from pydantic import Field
from pydantic import BaseModel

import logging


class WifiNetworkModel(BaseModel):
    ssid: str = Field(None, title="Wifi SSID")
    psk: str = Field(None, title="Wifi PSK (WPA2)")


class WiFiScanProxy(object):
    pass


class WiFiManagerProxy(object):
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._configured_networks = []
        self._read_config()

    def _read_config(self):
        raise NotImplementedError

    def _get_configured_networks(self):
        raise NotImplementedError

    @property
    def configured_networks(self):
        if not self._configured_networks:
            self._configured_networks = self._get_configured_networks()
        return self._configured_networks

    @property
    def configured_ssids(self):
        return [x.ssid for x in self.configured_networks]

    def show_networks(self):
        return self.configured_networks

    def has_network(self, ssid):
        return ssid in self.configured_ssids

    def add_network(self, ssid, psk, **kwargs):
        self._logger.info("Adding WiFi network '{}' with psk '{}'".format(ssid, psk))
        self._configured_networks.append(WifiNetworkModel(ssid=ssid, psk=psk))

    def remove_network(self, ssid):
        self._logger.info("Removing WiFi network '{}'".format(ssid))
        for network in self._configured_networks:
            if network.ssid == ssid:
                self._configured_networks.remove(network)
