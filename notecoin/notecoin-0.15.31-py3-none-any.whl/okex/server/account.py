import pandas as pd
from notebuild.tool.fastapi import add_api_routes, api_route
from notecoin.database.base import create_all, session,crea
from notecoin.database.connect import RedisConnect
from notecoin.okex.client.const import account_api
from notecoin.okex.database.client import OkexClientAccountBalance


class AccountAccount(RedisConnect):
    def __init__(self, prefix="/account", cache_prefix='okex_account_balance', *args, **kwargs):
        super(AccountAccount, self).__init__(prefix=prefix, cache_prefix=cache_prefix, *args, **kwargs)
        add_api_routes(self)
        create_all()

    @api_route('/update', description="update market tickers")
    def update_value(self, suffix=""):
        data = account_api.get_account().data[0]['details']
        self.put_value(self.get_key(suffix=suffix), data)
        for detail in data:
            print(detail)
            create_all()
            session.merge(OkexClientAccountBalance(**detail))
        session.commit()
        create_all()
        return {"success": len(data)}

    def get_value(self, suffix=""):
        return super(AccountAccount, self).get_value(suffix=suffix)
