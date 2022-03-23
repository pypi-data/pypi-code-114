from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
class WOE(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__() 
        self.WOE_ = {}

    def fit(self, X, colname, targetname):
        woe_df = X.groupby(colname, as_index=False).agg({targetname: ['sum', 'count']})
        woe_df.columns = [colname, 'one', 'total']
        woe_df['zero'] = woe_df.total - woe_df.one
        woe_df['ratio_one'] = woe_df.one / woe_df.one.sum()
        woe_df['ratio_zero'] = woe_df.zero/ woe_df.zero.sum()
        woe_df['defined_woe'] = (woe_df.ratio_zero> 0) & (woe_df.ratio_one > 0)
        woe_df['woe'] = 0
        woe_df.loc[woe_df.defined_woe, 'woe'] = woe_df.loc[woe_df.defined_woe, 'woe'] = np.log(woe_df.loc[woe_df.defined_woe, 'ratio_one'] / woe_df.loc[woe_df.defined_woe, 'ratio_zero'] )
        self.WOE_[colname]  = woe_df
        return self
        

    def transform(self, X, colname, targetname):
        X.loc[:,colname] = pd.merge(X[colname], self.WOE_[colname][[colname, 'woe']], how='left')['woe'].values
        return X

    def get_WOE_dict(self):
        return self.WOE_