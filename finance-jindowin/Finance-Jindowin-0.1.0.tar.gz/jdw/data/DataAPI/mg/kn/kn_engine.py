from jdw.kdutils.singleton import Singleton
from .. fetch_engine import FetchEngine
import pandas as pd
import six,os,pdb
os.environ
@six.add_metaclass(Singleton)
class FetchKNEngine(FetchEngine):
    def __init__(self, name=None, uri=None):
        if uri is None and name is None:
            super(FetchKNEngine, self).__init__('KN',os.environ['KN_MG'])
        else:
            super(FetchKNEngine, self).__init__(name, uri)
    
    def _general_query(self, **kwargs):
        query = {}
        if 'begin_date' in kwargs and 'end_date' in kwargs:
            query['trade_date'] = {"$gte": kwargs['begin_date'],
                                   "$lte": kwargs['end_date']
            }
        if 'codes' in kwargs:
            query['code'] = {'$in':kwargs['codes']}
        return query

    def _filter_columns(self, result):
        if not result.empty:
            result =  result.drop(['_id'],axis=1) if '_id' in result.columns else result
            result =  result.drop(['flag'],axis=1) if 'flag' in result.columns else result
            result =  result.drop(['timestamp'],axis=1) if 'timestamp' in result.columns else result
        return result

    def _base_dabase(self, **kwargs):
        query = self._general_query(**kwargs)
        columns = kwargs['columns'] if 'columns' in kwargs else None
        result = self.base(table_name=kwargs['table_name'],query=query,columns=columns)
        result = pd.DataFrame(result)
        return self._filter_columns(result)
        
    def market_pre_fut(self, **kwargs):
        return self._base_dabase(**kwargs)
    
    def fut_fundamenal(self, **kwargs):
        return self._base_dabase(**kwargs)
    
    def research(self, **kwargs):
        return self._base_dabase(**kwargs)



        