import logging

from fastapi import APIRouter
from notebuild.tool.fastapi import add_api_routes, api_route
from notecoin.database.base import create_all, session
from notecoin.database.connect.base import BaseConnect
from notecoin.okex.database.client import OkexClientAccountBalance
from notecoin.okex.database.websocket import OkexWebsocketChannels
from notecoin.okex.websocket.channel import PublicChannel
from notecoin.okex.websocket.connect import PublicConnect


class WebsocketService(APIRouter):
    def __init__(self, connect: BaseConnect = None, prefix='/websocket', *args, **kwargs):
        self.connect = connect or PublicConnect(channels=[PublicChannel.public_tickers().to_json()])
        super(WebsocketService, self).__init__(prefix=prefix, *args, **kwargs)
        add_api_routes(self)
        self.connect.run()

    def update_channels_db(self):
        details = session.query(OkexClientAccountBalance).filter(OkexClientAccountBalance.eqUsd > 10).all()

        for _detail in details:
            detail = _detail.json()
            if detail['ccy'] == 'USDT':
                continue
            instId = f"{detail['ccy']}-USDT"
            param = {
                "channel_json": str(PublicChannel.public_tickers(instId).to_json()),
                "channel": "tickers",
                "instId": instId
            }
            session.merge(OkexWebsocketChannels(**param))
        create_all()
        session.commit()
        return {"success": len(details)}

    @api_route('/update/channel', description="get value")
    def update_channels(self):
        try:
            self.update_channels_db()

            new_channels = session.query(OkexWebsocketChannels).all()
            new_channels = [eval(channel.channel_json) for channel in new_channels]

            old_channels_str = [str(channel) for channel in self.connect.channels]
            new_channels_str = [str(channel) for channel in new_channels]
            if new_channels_str is not None and len(new_channels_str) > 0:
                if len(list(set(old_channels_str) - set(new_channels_str))) == len(
                        list(set(new_channels_str) - set(old_channels_str))) == 0:
                    logging.info(f"old:{old_channels_str},new:{new_channels_str}")
                    self.connect.channels = new_channels
                    self.connect.subscribe_restart()
            return {"update": "success"}
        except Exception as e:
            return {"update": "fails", "error": str(e)}
