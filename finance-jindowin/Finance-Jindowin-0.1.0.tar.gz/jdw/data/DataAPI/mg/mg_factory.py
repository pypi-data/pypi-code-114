# -*- coding: utf-8 -*-
import pdb
class EngineFactory():
    def create_engine(self, engine_class):
        return engine_class()
    
    def __init__(self, engine_class=None):
        self._fetch_engine = self.create_engine(engine_class) \
            if engine_class is not None else None


class MarketPreFut(EngineFactory):
    def result(self, **kwargs):
        return self._fetch_engine.market_pre_fut(table_name='market_pre_fut',**kwargs)

class FutFundamenal(EngineFactory):
    def result(self, **kwargs):
        return self._fetch_engine.fut_fundamenal(table_name='fut_fundamenal',**kwargs)

class Research(EngineFactory):
    def result(self, **kwargs):
        return self._fetch_engine.research(table_name='research', **kwargs)
