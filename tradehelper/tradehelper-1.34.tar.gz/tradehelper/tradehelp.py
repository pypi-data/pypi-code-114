import requests
import datetime
import pandas as pd


import requests
import datetime
import numpy as np


class utilities:

    def __init__(self):
        self.base_url = "https://api.greentecq.com/v2/paper/"
        self.headers = {"Content-type": "application/x-www-form-urlencoded",
                        "Accept": "text/plain"}
        self.type = 2

    def get_expiry_kite(self):
        try:
            df_inst = pd.read_csv("https://api.kite.trade/instruments")
            df = df_inst[df_inst['segment'] == "NFO-OPT"]
            df = df[df['tradingsymbol'].str.startswith(
                "{}".format("BANKNIFTY"))]
            df['expiry'] = pd.to_datetime(df['expiry'])

            expirylist = list(set(df[['tradingsymbol', 'expiry']].sort_values(
                by=['expiry'])['expiry'].values))
            expirylist = np.array([np.datetime64(x, 'D') for x in expirylist])
            expirylist = np.sort(expirylist)
            today = np.datetime64('today', 'D') + np.timedelta64(0, 'D')
            expirylist = expirylist[expirylist >= today]
            expiry_index = 0
            next_expiry = expirylist[expiry_index]
            next_expiry = pd.to_datetime(str(next_expiry))

            return datetime.date(next_expiry.year, next_expiry.month, next_expiry.day)
        except Exception as e:
            print(e)
            return None

    def myround(self, x, base):
        return base * round(x/base)

    def roundtick(self, x):
        ticksize = 0.05
        return round(x/ticksize)*ticksize

    def get_url(self, url):
        response = requests.get(url)
        # print(response.text)
        content = response.content.decode("utf8")
        return content

    def send_telegram_message(self, token, receipt_id, message):
        try:
            URL = "https://api.telegram.org/bot{}/".format(token)
            url = URL + \
                "sendMessage?text={}&chat_id={}".format(message, receipt_id)
            return self.get_url(url)
        except:
            print("Error occured in sending telegram notification")

    def check_limit_long_count(self, orderBook, option_type=None):

        if option_type is not None:
            checkOrderBook = orderBook.loc[(orderBook['OT'] == option_type) & (orderBook['signal'] == "Long")
                                           & (orderBook['status'] == "open") & (orderBook['exit_time'].isnull())]
        else:
            checkOrderBook = orderBook.loc[(orderBook['signal'] == "Long") & (orderBook['exit_time'].isnull())
                                           & (orderBook['status'] == "open")]
        if len(checkOrderBook) > 0:
            return len(checkOrderBook)
        return 0

    def check_pending_long_count(self, orderBook, option_type=None):

        if option_type is not None:
            checkOrderBook = orderBook.loc[(orderBook['OT'] == option_type) & (orderBook['signal'] == "Long")
                                           & (orderBook['status'] == "pending") & (orderBook['exit_time'].isnull())]
        else:
            checkOrderBook = orderBook.loc[(orderBook['signal'] == "Long") & (orderBook['exit_time'].isnull())
                                           & (orderBook['status'] == "pending")]
        if len(checkOrderBook) > 0:
            return len(checkOrderBook)
        return 0

    def check_open_long_count(self, orderBook, option_type=None):

        # print(orderBook)
        if option_type is not None:
            checkOrderBook = orderBook.loc[(orderBook['OT'] == option_type) & (orderBook['signal'] == "Long")
                                           & (orderBook['status'] == "TRAD") & (orderBook['exit_time'].isnull())]
        else:
            checkOrderBook = orderBook.loc[(orderBook['signal'] == "Long") & (orderBook['exit_time'].isnull())
                                           & (orderBook['status'] == "TRAD")]
        # print(checkOrderBook)
        if len(checkOrderBook) > 0:
            return len(checkOrderBook)
        return 0

    def check_limit_short_count(self, orderBook, option_type=None):

        if option_type is not None:
            checkOrderBook = orderBook.loc[(orderBook['OT'] == option_type) & (orderBook['signal'] == "Short")
                                           & (orderBook['status'] == "open") & (orderBook['exit_time'].isnull())]
        else:
            checkOrderBook = orderBook.loc[(orderBook['signal'] == "Short") & (orderBook['exit_time'].isnull())
                                           & (orderBook['status'] == "open")]
        if len(checkOrderBook) > 0:
            return len(checkOrderBook)
        return 0

    def check_open_short_count(self, orderBook, option_type=None):
        if option_type is not None:
            checkOrderBook = orderBook.loc[(orderBook['OT'] == option_type) & (orderBook['signal'] == "Short")
                                           & (orderBook['status'] == "TRAD") & (orderBook['exit_time'].isnull())]
        else:
            checkOrderBook = orderBook.loc[(orderBook['signal'] == "Short") & (orderBook['exit_time'].isnull())
                                           & (orderBook['status'] == "TRAD")]

        if len(checkOrderBook) > 0:
            return len(checkOrderBook)
        return 0

    def print_live(self, text):
        print(text, end='\r', flush=True)

    def entry(self, args, instrument, entry_time, order_id, ltp, signal, status):
        try:
            if 'strategy_name' in args:
                if 'daily_execution_id' in args:
                    data = {
                        'strategy_name': args["strategy_name"],
                        'symbol': instrument.symbol,
                        'entry_date': entry_time,
                        'order_id': order_id,
                        'qty': args["quantity"] * 25,
                        'option_type': instrument.option_type,
                        'entry_price': ltp,
                        'signal': signal,
                        'status': status,
                        'daily_execution_id': args["daily_execution_id"],
                    }
                else:
                    data = {
                        'strategy_name': args["strategy_name"],
                        'symbol': instrument.symbol,
                        'entry_date': entry_time,
                        'order_id': order_id,
                        'qty': args["quantity"] * 25,
                        'option_type': instrument.option_type,
                        'entry_price': ltp,
                        'signal': signal,
                        'status': status,
                    }
                response = requests.post(
                    self.base_url+"entry", headers=self.headers, data=data)
                response_json = (response.json())
                return int(response_json['execution_id'])
        except Exception as e:
            print(e)

    def exit(self, args, execution_id, exit_time, order_id, ltp, remarks, profit, loss, mtm, mtm_high, mtm_low):
        try:
            data = {
                'execution_id':  execution_id,
                'exit_date': exit_time,
                'exit_order_id': order_id,
                'exit_qty': args["quantity"] * 25,
                'exit_price': ltp,
                'exit_status': 'complete',
                'remarks': remarks,
                'profit': profit,
                'loss': loss,
                'mtm': mtm,
                'mtm_high':  mtm_high,
                'mtm_low':  mtm_low,

            }
            response = requests.post(
                self.base_url+"exit", headers=self.headers, data=data)
            response_json = (response.json())

        except Exception as e:
            print(e)

    def log(self, args):
        # try:
        if self.type is None:
            execution_type = 2
        else:
            execution_type = self.type 

        if 'strategy_name' in args:
            if 'api_key' in args:
                data = {
                    'strategy_name': args["strategy_name"],
                    'type': execution_type,
                    'api_key': args["api_key"]
                }
            else:
                data = {
                    'strategy_name': args["strategy_name"],
                        'type': execution_type,
                }
            print(data)
            response = requests.post(
                self.base_url+"execution", headers=self.headers, data=data)
            response_json = (response.json())
            print(response_json)
            return int(response_json['daily_execution_id'])
        # except Exception as e:
        #     print(e)

    def log_update(self, args, mtm, high, low):
        try:
            if 'daily_execution_id' in args:
                data = {
                    'daily_execution_id': args["daily_execution_id"],
                    'mtm': mtm,
                    'high': high,
                    'low': low,
                }

                response = requests.post(
                    self.base_url+"update", headers=self.headers, data=data)
                response_json = (response.json())
        except Exception as e:
            print(e)
