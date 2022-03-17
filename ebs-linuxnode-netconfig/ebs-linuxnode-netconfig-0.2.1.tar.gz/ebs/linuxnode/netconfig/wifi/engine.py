

import logging
from typing import Optional

from typing import List
from fastapi import Body
from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter

from ebs.linuxnode.netconfig.core import app
from ebs.linuxnode.netconfig.core import ActionResultModel
from ebs.linuxnode.netconfig.core import auth_token
from ebs.linuxnode.netconfig import config

from .models import WiFiManagerProxy
from .models import WifiNetworkModel

logger = logging.getLogger(__name__)

_manager_proxy: Optional[WiFiManagerProxy] = None


wifi_router = APIRouter(prefix='/wifi',
                        dependencies=[Depends(auth_token)])


@app.on_event('startup')
async def init():
    global _manager_proxy
    if config.wifi_manager == 'wpa_supplicant':
        from .supplicant import WPASupplicantProxy
        _manager_proxy = WPASupplicantProxy(cpath=config.wpa_supplicant_path)
    elif config.wifi_manager == 'netplan':
        from .netplan import NetplanWifiProxy
        _manager_proxy = NetplanWifiProxy(cpath=config.netplan_path,
                                          device=config.wifi_device)


@wifi_router.get("/networks/show", response_model=List[WifiNetworkModel], status_code=200)
async def show_configured_wifi_networks():
    networks = _manager_proxy.show_networks()
    logger.info("Currently configured networks :\n{}".format(
        "\n".join(["{:20} {}".format(x.ssid, x.psk)
                   for x in networks])))
    return networks


@wifi_router.post("/networks/add", response_model=ActionResultModel, status_code=201)
async def add_wifi_network(network: WifiNetworkModel):
    if _manager_proxy.has_network(network.ssid):
        raise HTTPException(
            status_code=409,
            detail="SSID '{}' already exists. Modify the existing network or remove it and try again."
                   "".format(network.ssid)
        )
    _manager_proxy.add_network(ssid=network.ssid, psk=network.psk)
    return {"result": True}


@wifi_router.post("/networks/remove", response_model=ActionResultModel, status_code=200)
async def remove_wifi_network(ssid: str = Body(...)):
    if not _manager_proxy.has_network(ssid):
        raise HTTPException(
            status_code=416,
            detail="SSID '{}' not recognized. Cannot remove.".format(ssid)
        )
    _manager_proxy.remove_network(ssid=ssid)
    return {"result": True}


@wifi_router.get("/status")
async def wifi_network_status():
    return {"message": "WNS"}


@wifi_router.get("/scan")
async def scan_wifi_networks():
    return {"message": "SN"}


@wifi_router.get("/note")
async def note():
    return _manager_proxy.manager_note
