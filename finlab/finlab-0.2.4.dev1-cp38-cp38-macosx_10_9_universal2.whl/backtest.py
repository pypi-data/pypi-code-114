import re
import datetime
import threading
import numpy as np
import pandas as pd
from typing import Union
from pandas.tseries.offsets import DateOffset

import finlab
from finlab import report
from finlab import data
from finlab import mae_mfe
from finlab.utils import check_version, requests, set_global
from finlab.backtest_core import backtest_, get_trade_stocks, get_stock_operations

def futureDateFactory():
  """  get future date factory

  Returns
      function of get_future_date

  """
  latest = None
  date = None

  def ret(d):

    nonlocal latest
    nonlocal date

    if latest == d:
      return date

    latest = d
    adj_close = data.get('etl:adj_close')

    t = pd.to_datetime(d).to_pydatetime(adj_close.index.tzinfo)

    if t >= adj_close.index[-1]:

      url = "https://asia-east1-fdata-299302.cloudfunctions.net/future_date"
      res = requests.get(url, {'datestr': str(pd.to_datetime(d).to_pydatetime().date())})
      date = res.text

      return date

    if t < adj_close.index[-1]:
      if d in adj_close.index:
        date = str(adj_close.loc[d:].index[1].date())
      else:
        date = str(adj_close.loc[d:].index[0].date())

    return date
  return ret

get_future_date = futureDateFactory()

def download_backtest_encryption_function_builder():

    encryption_time = datetime.datetime.now()
    encryption = ''

    def ret():

        nonlocal encryption_time
        nonlocal encryption

        if datetime.datetime.now() < encryption_time + datetime.timedelta(days=1) and encryption:
            return encryption

        res = requests.get('https://asia-east2-fdata-299302.cloudfunctions.net/auth_backtest',
                {'api_token': finlab.get_token(), 'time': str(datetime.datetime.now())})

        if not res.ok:
            return ''

        d = res.json()

        if 'v' in d and 'v_msg' in d and finlab.__version__ < d['v']:
            print(d['v_msg'])

        if 'msg' in d:
            print(d['msg'])

        encryption_time = datetime.datetime.now()
        encryption = d['encryption']

        return encryption
    return ret

download_backtest_encryption = download_backtest_encryption_function_builder()

def arguments(price, position, resample_dates=None):
    resample_dates = price.index if resample_dates is None else resample_dates
    resample_dates = pd.Series(resample_dates).view(np.int64).values

    position = position.astype(float).fillna(0)
    price = price.astype(float)

    return [price.values,
            price.index.view(np.int64),
            price.columns.astype(str).values,
            position.values,
            position.index.view(np.int64),
            position.columns.astype(str).values,
            resample_dates
            ]

def sim(position: Union[pd.DataFrame, pd.Series], resample=None, trade_at_price='close',
        position_limit=1, fee_ratio=1.425/1000,
        tax_ratio=3/1000, name=None, stop_loss=None,
        take_profit=None, touched_exit=False,
        mae_mfe_window=0, mae_mfe_window_step=1, upload=True):

    # check version
    check_version()

    # check name is valid
    if name:
        head_is_eng = len(re.findall(
            r'[\u0041-\u005a|\u0061-\u007a]', name[0])) > 0
        has_cn = len(re.findall('[\u4e00-\u9fa5]', name[1:])) > 0
        if head_is_eng and has_cn:
            raise Exception('Strategy Name Error: 名稱如包含中文，需以中文當開頭。')

    # check position is valid
    if position.sum().sum() == 0 or len(position.index) == 0:
        raise Exception('Position is empty and zero stock is selected.')

    # format position index
    if isinstance(position.index[0], str):
        position = position.index_str_to_date()

    # asset type
    asset_type = 'tw_stock'
    if isinstance(position, pd.DataFrame) and (position.columns.str.find('USDT') != -1).any():
        asset_type = 'crypto'
    if isinstance(position, pd.Series) and 'USDT' in position.name:
        asset_type = 'crypto'

    # determine trading price
    table_name = 'etl:adj_' if asset_type == 'tw_stock' else 'crypto:'
    if isinstance(trade_at_price, str):
        price = data.get(f'{table_name}{trade_at_price}')
    elif isinstance(trade_at_price, pd.Series):
        trade_at_price.name = position.name
        price = trade_at_price.to_frame()
    elif isinstance(trade_at_price, pd.DataFrame):
        price = trade_at_price
    else:
        raise Exception(f'**ERROR: trade_at_price is not allowed (accepted types: pd.DataFrame, pd.Series, str).')

    # check position types
    if isinstance(position, pd.Series):
        if position.name in price.columns:
            position = position.to_frame()
        else:
            raise Exception('Asset name not found. Please asign asset name by "position.name = \'2330\'".')

    # if position date is very close to price end date, run all backtesting dates
    assert len(position.shape) >= 2
    delta_time_rebalance = position.index[-1] - position.index[-3]
    backtest_to_end = position.index[-1] + \
        delta_time_rebalance > price.index[-1]

    position = position[position.index <= price.index[-1]]
    backtest_end_date = price.index[-1] if backtest_to_end else position.index[-1]

    # resample dates
    future_bdate = None
    if asset_type == 'tw_stock':
        future_bdate = pd.to_datetime(get_future_date(position.index[-1]))\
                .to_pydatetime(position.index.tzinfo)

    if isinstance(resample, str):

        offset_days = 0
        if '+' in resample:
            offset_days = int(resample.split('+')[-1])
            resample = resample.split('+')[0]
        if '-' in resample and resample.split('-')[-1].isdigit():
            offset_days = -int(resample.split('-')[-1])
            resample = resample.split('-')[0]

        dates = pd.date_range(
            position.index[0], position.index[-1]+ datetime.timedelta(days=720), freq=resample, tz=position.index.tzinfo)
        dates += DateOffset(days=offset_days)
        dates = [d for d in dates if position.index[0]
                 <= d and d <= position.index[-1]]

        next_trading_date = min(
                set(pd.date_range(position.index[0],
                    datetime.datetime.now(position.index.tzinfo)
                    + datetime.timedelta(days=720),
                    freq=resample)) - set(dates))

        if future_bdate is not None and future_bdate > next_trading_date:
            dates += [next_trading_date]

    elif resample is None:
        dates = None
        next_trading_date = position.index[-1] + datetime.timedelta(days=1)

    if stop_loss is None or stop_loss == 0:
        stop_loss = -np.inf

    if take_profit is None or take_profit == 0:
        take_profit = np.inf

    if dates is not None:
        position = position.reindex(dates, method='ffill')


    encryption = download_backtest_encryption()

    creturn_value = backtest_(*arguments(price, position, dates),
                              encryption=encryption,
                              fee_ratio=fee_ratio, tax_ratio=tax_ratio,
                              stop_loss=stop_loss, take_profit=take_profit,
                              touched_exit=touched_exit, position_limit=position_limit,
                              mae_mfe_window=mae_mfe_window, mae_mfe_window_step=mae_mfe_window_step)

    position = position.div(position.sum(axis=1)+0.0001, axis=0)
    position = position.clip(-abs(position_limit), abs(position_limit))

    creturn = pd.Series(creturn_value, price.index)
    creturn = creturn[(creturn != 1).cumsum().shift(-1, fill_value=1) != 0]
    creturn = creturn.loc[:backtest_end_date]
    if len(creturn) == 0:
        creturn = pd.Series(1, position.index)

    trades = pd.DataFrame(
        get_trade_stocks(position.columns.astype(str).values, price.index.view(np.int64)))

    if len(trades) != 0:

        trades.columns = ['stock_id', 'entry_date', 'exit_date',
                     'entry_sig_date', 'exit_sig_date',
                     'position', 'period', 'entry_index', 'exit_index']

        trades.index.name = 'trade_index'

        for col in ['entry_date', 'exit_date', 'entry_sig_date', 'exit_sig_date']:
            trades[col] = pd.to_datetime(trades[col])

        trades.loc[trades.exit_index == -1, ['exit_date', 'exit_sig_date']] = np.nan

        m = pd.DataFrame(mae_mfe.mae_mfe)
        nsets = int((m.shape[1]-1) / 6)

        metrics = ['mae', 'gmfe', 'bmfe', 'mdd', 'pdays', 'return']

        tuples = sum([[(n, metric) if n == 'exit' else (n * mae_mfe_window_step, metric)
                       for metric in metrics] for n in list(range(nsets)) + ['exit']], [])

        m.columns = pd.MultiIndex.from_tuples(
            tuples, names=["window", "metric"])
        m.index.name = 'trade_index'
        m[m == -1] = np.nan

        trades['return'] = m.iloc[:, -1]

    r = report.Report(
        creturn, position, fee_ratio, tax_ratio, trade_at_price, next_trading_date)

    if len(trades) != 0:
        r.trades = trades

    if len(m) != 0:
        r.mae_mfe = m

    operation_and_weight = get_stock_operations()

    if len(operation_and_weight['actions']) != 0:

        # find selling and buying stocks
        actions = pd.Series(operation_and_weight['actions'])
        actions.index = r.position.columns[actions.index]

        sell_sids = actions[actions == 'exit'].index
        buy_sids = actions[actions == 'enter'].index
        r_position = set(trades.stock_id[trades.exit_sig_date.isna()])

        # check if the sell stocks are in the current position
        assert len(set(sell_sids) - r_position) == 0

        # fill exit_sig_date and exit_date
        trades.loc[trades.stock_id.isin(sell_sids), 'exit_sig_date'] = \
            trades.loc[trades.stock_id.isin(sell_sids), 'exit_sig_date'].fillna(price.index[-1])
        trades.loc[trades.stock_id.isin(sell_sids), 'exit_date'] = \
            trades.loc[trades.stock_id.isin(sell_sids), 'exit_date'].fillna(get_future_date(price.index[-1]))

        final_trades = pd.concat([trades, pd.DataFrame({
          'stock_id': buy_sids,
          'entry_date': pd.to_datetime(get_future_date(price.index[-1])),
          'entry_sig_date': price.index[-1],
        })], ignore_index=True)

        r.trades = final_trades

    # calculate r.current_trades
    # find trade without end or end today
    r.current_trades = r.trades[
            r.trades.exit_sig_date.isna()
            | (r.trades.exit_sig_date == price.index[-1]).fillna(False)].set_index('stock_id')


    if len(operation_and_weight['weights']) != 0:
        r.weight = pd.Series(operation_and_weight['weights'])
        r.weight.index = r.position.columns[r.weight.index]

        r.current_trades['weight'] = r.weight / r.weight.sum()
        r.current_trades['weight'].fillna(0, inplace=True)
    else:
        r.current_trades['weight'] = 0


    set_global('backtest_report', r)

    if not upload:
        return r

    r.upload(name)
    return r
