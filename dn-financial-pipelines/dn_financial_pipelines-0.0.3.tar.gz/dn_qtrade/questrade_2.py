import qtrade
import pathlib
from datetime import datetime, timedelta
from dn_date_util.utility import DATE_FORMAT, process_window, get_date_res, populate_dates, parse_prefix
# internal
from sql_queries import Query
# TODO return share count as dictionary time series symbol as key, count as value


class QTAccount:

    def __init__(self, filepath=pathlib.Path(__file__).absolute().parent):
        self.qt_fp = filepath
        self.yaml_path = self.qt_fp.joinpath('access_token.yml')

        self.conn = self.qtrade_connect()

        self.accounts = self.conn.get_account_id()

        # self.txns = list()
        self.positions = list()

        for account in self.accounts:
            self.positions.append(self.conn.get_account_positions(account_id=int(account)))

    def qtrade_connect(self,):
        try:
            conn = qtrade.Questrade(token_yaml=self.yaml_path)
            conn.refresh_access_token(from_yaml=True)
        except:
            access_code = input("please input Questrade API Access token ")
            conn = qtrade.Questrade(access_code=access_code)

        return conn

    def get_txns(self, dates):
        """ dates can have max resolution of monthly dates - API will fail if larger request is made
        args:
            dates           list of tuples of string or datetime dates as format %Y-%m-%d denoting desired window

        returns:
            all account transactions linked to connection token
        """
        all_txns = list()
        for account in self.accounts:
            for date in dates:
                # TODO add loading bar
                # QT Api will fail if future dates are requested
                if date <= datetime.now():
                    date = date.__str__().split()
                    date = date[0]
                    txns = self.conn.get_account_activities(account_id=int(account),
                                                            start_date='2020-11-13',
                                                            end_date=date)
                else:
                    txns = list()

                for txn in txns:
                    all_txns.append(txn)

        return all_txns

    def get_share_balance(self, dates):
        """
        dates can be one tuple or many for single points in time or timeseries of points in time

        takes in str dates as list of tuples indicating a window
        and returns share balances for each holding at the date specified

        returns balances at end date of each period of date tuples
        """

        txns = self.get_txns(dates)
        balances = list()

        # get amount of each share at the first date, initial amounts
        for date in dates:
            period_balances = dict()
            sample_date = date

            for txn in txns:
                # parse questrade date into date format being used
                txn_date = parse_prefix(txn['settlementDate'], DATE_FORMAT)
                if txn_date <= sample_date:
                    if txn['action'].lower() == 'BUY'.lower() or txn['action'].lower() == 'SELL'.lower():
                        if not txn['symbol'] in period_balances:
                            period_balances[txn['symbol']] = txn['quantity']
                        else:
                            period_balances[txn['symbol']] += txn['quantity']

            # only append keys with non-zero entries
            balances.append({x: y for x, y in period_balances.items() if y != 0})

        return balances


def __main__():
    tfsa = QTAccount()

    sample_date = datetime.strptime('2020-12-14', DATE_FORMAT)
    # sample_date = datetime.now()
    balances = tfsa.get_share_balance([sample_date])


if __name__ == '__main__':
    __main__()
