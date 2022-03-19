import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from torch.utils.data import (
    DataLoader, 
    Dataset
    )


def create_rolling_ts(
    input_data, 
    lookback=5, 
    return_target=True,
    ):
    """
    Make flat data by using pd.concat instead, pd.concat([df1, df2]).
    Slow function.
    Save data as preprocessed?
    """
    x = []
    y = []
    rows = len(input_data)
    features = input_data.copy()
    target = input_data.copy()
    for i in range(rows - lookback):
        rolling_features = features.iloc[i: i + lookback]
        rolling_target = target.iloc[i + lookback: i + lookback + 1]
        x.append(rolling_features)
        y.append(rolling_target)
    if return_target:
        return x, y
    return x


def date_features(df):
    # Check if index is datetime.
    if isinstance(df, pd.core.series.Series):
        df = pd.DataFrame(df, index=df.index)

    df.loc[:, 'day_of_year'] = df.index.dayofyear
    df.loc[:, 'month'] = df.index.month
    df.loc[:, 'day_of_week'] = df.index.day
    df.loc[:, 'hour'] = df.index.hour
    return df
    

def ts_split(data, train_size, valid_size):
    """
    Implement data based splitting. 
    Do normalization.
    
    """
    train_size = int(len(data) * train_size)
    valid_size = int(train_size + len(data) * valid_size)
    try:
        train_set = data.iloc[: train_size]
        valid_set = data.iloc[train_size: valid_size]
        test_set = data.iloc[valid_size: ]
        return train_set, valid_set, test_set
    except Exception as e:
        print(f'Exception from _ts_split: {e}')


def is_pandas(data):
    return isinstance(
        data, 
        (pd.core.frame.DataFrame, pd.core.series.Series)
        )


class ContCatSplit:
    def __init__(
        self, 
        data, 
        add_date=False,
        cat_types=None
        ):

        self.data = data.copy()
        self.add_date = add_date
        self.cat_types = cat_types

    def  add_datepart(self, data):
        if self.add_date:
            data = date_features(data)
            return data

    def cont_cat_split(self):
        try:
            if is_pandas(self.data):
                if self.add_date:
                    self.data = self.add_datepart(self.data)
                self.cat = self.data.select_dtypes(include=self.cat_types)
                cat_cols = self.cat.columns
                self.cont = self.data.drop(cat_cols, axis=1)
                return self.cont, self.cat
        except Exception as e:
            print(f'from cont_cat_split: {e}')


class ToTorch(Dataset):

    def __init__(
            self,
            features,
            target
            ):
        
        self.features = features
        self.target = target

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        features = self.features[idx]
        target = self.target[idx]

        """Return dict of dicts"""
        return {
            'features': torch.from_numpy(np.array(features)).float(), 
            'target': torch.from_numpy(np.array(target)).float()
            }


class Normalize:
    def __init__(self, trans_name='standard'):
        if trans_name == 'standard':
            self.transform = StandardScaler()
        elif trans_name == 'minmax':
            self.transform = MinMaxScaler()
        else:
            pass

    def train_transform(self, xtrain):
        return self.transform.fit_transform(xtrain)

    def test_transform(self, xtest):
        return self.transform.transform(xtest)

    def inverse(self, x):
        return self.transform.inverse_transform(x)
        

def ts_split(data, train_size, valid_size):
    """
    Implement data based splitting. 
    Do normalization.
    
    """
    train_size = int(len(data) * train_size)
    valid_size = int(train_size + len(data) * valid_size)
    try:
        train_set = data.iloc[: train_size]
        valid_set = data.iloc[train_size: valid_size]
        test_set = data.iloc[valid_size: ]
        return train_set, valid_set, test_set
    except Exception as e:
        print(f'Exception from _ts_split: {e}')