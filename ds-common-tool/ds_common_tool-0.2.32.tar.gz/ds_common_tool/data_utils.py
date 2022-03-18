# some data processing function #

import pandas as pd
from datetime import datetime

def create_date_df(startDate = '20200101', endDate = '20210101'):
  date_list = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start = startDate, end= endDate))]
  date_pd = pd.DataFrame(date_list)
  date_pd.rename(columns={0:'DATE'}, inplace= True)
  return date_pd