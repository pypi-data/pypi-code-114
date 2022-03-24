# Author: Salyl Bhagwat, Gammath Works
# Copyright (c) 2021-2022, Salyl Bhagwat, Gammath Works
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = 'Salyl Bhagwat'
__copyright__ = 'Copyright (c) 2021-2022, Salyl Bhagwat, Gammath Works'

import pandas as pd
from backtesting import Backtest, Strategy

#def getgScores(tsymbol):
#    print('Get gScores')

class gScoreAction(Strategy):
    a = None
    def init(self):
        a = None
#        print('gScoreAction init')
#        self.I(getgScores, 'GOOGL')

    def next(self):
        a = None
#        print('Next')

df = pd.read_csv('GOOGL_history.csv', index_col='Date', parse_dates=True)

backtest = Backtest(df, gScoreAction, cash=5000)
bt_stats = backtest.run()

