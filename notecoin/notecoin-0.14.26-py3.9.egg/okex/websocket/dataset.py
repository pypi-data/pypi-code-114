from notecoin.database.base import Base
from sqlalchemy import BIGINT, Column, Float, String


class BaseTable(object):
    def json(self):
        res = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return res


class OkexSocketPublicTickers(Base, BaseTable):
    __tablename__ = 'okex_socket_public_tickets'
    instType = Column(String(120), comment='产品类型', primary_key=True)
    instId = Column(String(120), comment='产品ID', primary_key=True)

    last = Column(Float(), comment='最新成交价')
    lastSz = Column(Float(), comment='最新成交的数量')

    askPx = Column(Float(), comment='卖一价')
    askSz = Column(Float(), comment='卖一价对应的量')
    bidPx = Column(Float(), comment='买一价')
    bidSz = Column(Float(), comment='买一价对应的量')

    open24h = Column(Float(), comment='24小时开盘价')
    high24h = Column(Float(), comment='24小时最高价')
    low24h = Column(Float(), comment='24小时最低价')
    volCcy24h = Column(Float(), comment='24小时成交量，以计价货币为单位')
    vol24h = Column(Float(), comment='24小时成交量，以交易货币为单位')

    sodUtc0 = Column(Float(), comment='UTC 0时开盘价')
    sodUtc8 = Column(Float(), comment='UTC+8时开盘价')

    ts = Column(BIGINT(), comment='数据产生时间，Unix时间戳的毫秒数格式')

    def __init__(self, *args, **kwargs):
        self.instType = kwargs.get("instType", "SPOT")
        self.instId = kwargs.get("instId", "")
        self.last = kwargs.get("last", 0)
        self.lastSz = kwargs.get("lastSz", 0)
        self.askPx = kwargs.get("askPx", 0)
        self.askSz = kwargs.get("askSz", 0)
        self.bidPx = kwargs.get("bidPx", 0)

        self.bidSz = kwargs.get("bidSz", 0)
        self.open24h = kwargs.get("open24h", 0)
        self.high24h = kwargs.get("high24h", 0)
        self.low24h = kwargs.get("low24h", 0)
        self.volCcy24h = kwargs.get("volCcy24h", 0)

        self.vol24h = kwargs.get("vol24h", 0)
        self.sodUtc0 = kwargs.get("sodUtc0", 0)
        self.sodUtc8 = kwargs.get("sodUtc8", 0)
        self.ts = kwargs.get("ts", 0)

    def __repr__(self):
        return f"instType{self.instType},instId:{self.instId}"
