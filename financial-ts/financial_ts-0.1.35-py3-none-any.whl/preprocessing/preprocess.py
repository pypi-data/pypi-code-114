import pandas as pd
import numpy as np
import torch
from torch.utils.data import (
    DataLoader, 
    Dataset
    )


def create_rolling_ts(
    input_data, 
    lookback=5, 
    return_target=True,
    apply_datefeatures=True,
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
        """Create embeddings for the date-features"""
        if apply_datefeatures:
            rolling_features = date_features(features.iloc[i: i + lookback])
        else:
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
    

def split_data(data, train_size, valid_size):
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
        print(f'Exception from _split_data: {e}')


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


class SplitCatNum:
    def __init__(
        self, 
        num_data, 
        cat_data=None, 
        how='inner',
        train_size=0.7,
        valid_size=0.125,
        lookback=30,
        num_col='close'
        ):
        """
        This class merges and splits numerical and categorical data.
        This way we get the same time stamps. 
        #TODO:
        #  1. check the time units!!! 2022-02-04.
        #  2. normalize data
        For rolling window return only target for time series.

        """
        self.num_data = num_data
        self.cat_data = cat_data
        self.how = how
        self.train_size = train_size
        self.valid_size = valid_size
        self.lookback = lookback
        self.num_col = num_col

    def merge_split(self):
        """Merge then split to get same index."""
        if isinstance(self.num_data, pd.core.frame.DataFrame):
            tot_data = self.num_data.merge(
                self.cat_data, 
                left_index=True, 
                right_index=True, 
                how=self.how
                )
        return tot_data[self.num_col], tot_data.drop(self.num_col, axis=1)

    def set_train_val_test(self):
        if self.cat_data is not None:
            numerical, categorical = self.merge_split()

        self.num_train, self.num_valid, self.num_test = split_data(
            numerical, 
            self.train_size, 
            self.valid_size
            )

        self.cat_train, self.cat_valid, self.cat_test = split_data(
            categorical, 
            self.train_size, 
            self.valid_size
            )

    def get_rolling_data(self):
        self.set_train_val_test()
        num_roll = {}
        num_data = [self.num_train, self.num_valid, self.num_test]
        keys = ['train', 'valid', 'test']

        for data, key in zip(num_data, keys):
            x, y = create_rolling_ts(
                input_data=data, 
                lookback=self.lookback, 
                return_target=True
                )
            num_roll[key] = {f'x_num_{key}': x, f'y_num_{key}': y}

        cat_roll = {}
        cat_data = [self.cat_train, self.cat_valid, self.cat_test]

        for data, key in zip(cat_data, keys):
            x = create_rolling_ts(
                input_data=data, 
                lookback=self.lookback, 
                return_target=False
                )
            cat_roll[key] = {f'x_cat_{key}'}
        return num_roll, cat_roll


class TimeSeriesDataset(Dataset):

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

        