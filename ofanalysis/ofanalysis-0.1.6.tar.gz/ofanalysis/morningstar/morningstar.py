import datetime

import const
import utility as ut

import pandas as pd

morningstar_df = pd.read_csv('./fund_morning_star_0306.csv')

morningstar_df['代码'] = morningstar_df['代码'].str.strip(' ')
morningstar_df['晨星专属号'] = morningstar_df['代码'].str.strip(' ')
morningstar_df['名称'] = morningstar_df['名称'].str.strip(' ')
morningstar_df['类型'] = morningstar_df['类型'].str.strip(' ')
morningstar_df['今年回报率'] = morningstar_df['今年回报率'].str.strip(' ')

morningstar_df['update_date'] = datetime.date.today().strftime('%Y%m%d')
morningstar_df.reset_index(drop=True, inplace=True)

ut.db_del_dict_from_mongodb(
    mongo_db_name=const.MONGODB_DB_MORNINGSTAR,
    col_name=const.MONGODB_COL_MORNINGSTAR_RATING,
    query_dict={}
)

ut.db_save_dict_to_mongodb(
    mongo_db_name=const.MONGODB_DB_MORNINGSTAR,
    col_name=const.MONGODB_COL_MORNINGSTAR_RATING,
    target_dict=morningstar_df.to_dict(orient='records')
)
