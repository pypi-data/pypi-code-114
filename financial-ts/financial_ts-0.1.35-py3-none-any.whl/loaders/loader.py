import pandas as pd
import warnings
import requests 
import getpass
import csv


def from_list_df(price_list):
    """
    Create dataframe from list from 
    data_alpha_vantage.
    """
    time_col = [col[0] for col in price_list[1:]]
    open_col = [col[1] for col in price_list[1:]]
    high_col = [col[2] for col in price_list[1:]]
    low_col = [col[3] for col in price_list[1:]]
    close_col = [col[4] for col in price_list[1:]]
    vol_col = [col[5] for col in price_list[1:]]

    df = pd.DataFrame(
        {
        'open': open_col, 
        'high': high_col,
        'low': low_col,
        'close': close_col,
        'volume': vol_col
        }, index=time_col
        )
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df = df.astype(float)
    return df


def data_alpha_vantage(
    key=None, 
    ticket='IBM', 
    interval_minutes='15min&slice=year1month12'
    ):
    """Get data from alpha vantage. Return list with
    time, open, high, low, close, volume."""
    try:
        function='TIME_SERIES_INTRADAY_EXTENDED'
        ROOT_URL = 'https://www.alphavantage.co/query?'
        url = f'{ROOT_URL}function={function}&symbol={ticket}&interval_minutes={interval_minutes}&apikey={key}'
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            price_list = list(cr)
        return price_list

    except ConnectionError:
        raise ConnectionError("Connection error, you need to pass key.")


def dataframe_from_list(price_list):
    """Convert price series from 
    list to dataframe. Input comes 
    from data_alpha_vantage."""
    return from_list_df(price_list)


class IntradayExtended:
    def __init__(
        self, 
        key, 
        ticket='AAPL', 
        interval_minutes='15min&slice=year1month12'
        ):

        self.key = key
        self.ticket = ticket
        self.interval_minutes = interval_minutes

    def get_intraday_extended(self):
        df = data_alpha_vantage(self.key, self.ticket, self.interval_minutes)
        df = from_list_df(df)
        return df


class Loader:
    """Create Loader for historic data"""
    def __init__(self):
        pass
    
    def get_csv(self):
        """Can use minio"""

    def get_pickle(self):
        """Can use minio""" 


class LoaderAlphaV:
    """
    Data loader of time series. Based on the 
    Alpha Vantage API. This class mostly transform data 
    to pandas dataframes.

    Supported values for interval_minutes:
    * 1min, 5min, 15min, 30min, 60min
    """
    def __init__(
        self, 
        symbol, 
        function='TIME_SERIES_INTRADAY', 
        interval_minutes=5, 
        adjusted=True,
        outputsize='full'
        ):

        self.symbol = symbol
        self.source = "https://www.alphavantage.co/query?"
        self.function = function
        self.interval_minutes = interval_minutes
        self.apikey = self.set_apikey()
        self.adjusted = str(adjusted).lower()
        self.outputsize = outputsize


    def set_apikey(self):
        try:
            apikey = getpass.getpass(prompt="Enter your apikey: ")
            return apikey
        except getpass.GetPassWarning:
            raise ValueError("You have to enter an apikey.")

    def get_json(self, url):
        """Pass the relevant url"""
        json_data = requests.get(url)
        data = json_data.json()
        return data
        
    def ts_intraday(self):
        url = f'{self.source}function={self.function}&symbol={self.symbol}&interval={self.interval_minutes}min&apikey={self.apikey}&adjusted={self.adjusted}&outputsize={self.outputsize}'
        data = self.get_json(url)
        df = pd.DataFrame.from_dict(data[f'Time Series ({self.interval_minutes}min)']).T
        return df

    def ts_day_adjusted(self):
        try:
            func = 'TIME_SERIES_DAILY_ADJUSTED'
            url = f'{self.source}function={func}&symbol={self.symbol}&apikey={self.apikey}'
            data = self.get_json(url)
            df = pd.DataFrame.from_dict(data['Time Series (Daily)']).T
            return df
        except:
            raise ConnectionError("time series adjusted is a paid service.")

    def ts_intraday_extended(self, interval_minutes):
        df = IntradayExtended(
            self.apikey, 
            self.symbol, 
            interval_minutes
            ).get_intraday_extended()
        return df


