# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert
import pandas as pd
import pymysql
import sqlalchemy
import sys
import time
import traceback
import warnings
warnings.filterwarnings('ignore', category=pymysql.Warning)


class FEDB:
    def __init__(self):
        self.fedb_engine = None
        self.fedb_connection = None
        self.create_connection()

    def create_connection(self):
        vaild = False
        while not vaild:
            try:
                self.fedb_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
                                                 'admin', 'mysql', '192.168.223.152', '3306', 'fe_temp_data'),
                                   connect_args={'charset': 'utf8'}, pool_recycle=360,
                                   pool_size=2, max_overflow=10, pool_timeout=360)
                self.fedb_connection = self.fedb_engine.connect()
                vaild = True
            except Exception as e:
                self.close_connection()
                print('[FEDB] mysql connect error')
                time.sleep(5)
        return

    def close_connection(self):
        # 1) close connection
        try:
            if self.fedb_connection is not None:
                self.fedb_connection.close()
        except Exception as e:
            print('[FEDB] close connect error')
        # 2) dispose engine
        try:
            if self.fedb_engine is not None:
                self.fedb_engine.dispose()
        except Exception as e:
            print('[FEDB] dispose engine error')
        return

    def get_df(self, sql):
        valid = False
        df = None
        while not valid:
            try:
                df = pd.read_sql_query(sql, self.fedb_engine)
                self.close_connection()
                valid = True
            except Exception as e:
                self.close_connection()
                self.create_connection()
                print('[FEDB] sql error:{0}'.format(sql))
                time.sleep(5)
        return df

    def create_metadata(self, metadata):
        valid = False
        while not valid:
            try:
                metadata.create_all(self.fedb_engine)
                valid = True
            except Exception as e:
                self.close_connection()
                self.create_connection()
                exc_type, exc_value, exc_trackback = sys.exc_info()
                print(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
                print('[FEDB] create metadata error')
            return metadata

    def insert_data(self, table, params):
        try:
            self.fedb_connection.execute(table.insert(), params)
        except Exception as e:
            conn = self.fedb_engine.connect()
            conn.execute(table.insert(), params)
            self.fedb_connection = conn
            exc_type, exc_value, exc_trackback = sys.exc_info()
            print(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
            print('[FEDB] insert data error')
        return

    def replace_data(self, table, params):
        # @compiles(Insert)
        def replace_string(insert, compiler, **kw):
            s = compiler.visit_insert(insert, **kw)
            s = s.replace("INSERT INTO", "REPLACE INTO")
            return s

        valid = False
        times = 0
        while not valid and times < 5:
            try:
                times += 1
                self.fedb_connection.execute(table.insert(replace_string=""), params)
                valid = True
            except Exception as e:
                self.close_connection()
                self.create_connection()
                time.sleep(2)
                exc_type, exc_value, exc_trackback = sys.exc_info()
                print(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
                print('[FEDB] replace data error')
            return

    def update_data(self, table, params):
        # @compiles(Insert)
        def append_string(insert, compiler, **kw):
            s = compiler.visit_insert(insert, **kw)
            if insert.kwards.get('on_duplicates_key_update'):
                fields = s[s.find("(") + 1:s.find(")")].replace(" ", "").split(",")
                generated_directive = ["{0}=VALUES({0})".format(field) for field in fields]
                return s + " ON DUPLICATES KEY UPDATE " + ",".join(generated_directive)
            return s

        valid = False
        times = 0
        while not valid and times < 5:
            try:
                times += 1
                self.fedb_connection.execute(table.insert(on_duplicates_key_update=True), params)
                valid = True
            except Exception as e:
                self.close_connection()
                self.create_connection()
                time.sleep(2)
                exc_type, exc_value, exc_trackback = sys.exc_info()
                print(repr(traceback.format_exception(exc_type, exc_value, exc_trackback)))
                print('[FEDB] update data error')
            return

    def insert_df(self, factor_df):
        table_name = 'mutual_fund_holding_label'
        metadata = sqlalchemy.MetaData()
        table = sqlalchemy.Table(
            table_name, metadata,
            sqlalchemy.Column('REPORT_DATE'),
            sqlalchemy.Column('REPORT_HISTORY_DATE'),
            sqlalchemy.Column('FUND_UNIVERSE'),
            sqlalchemy.Column('IS_ZC'),
            sqlalchemy.Column('LABEL_TYPE'),
            sqlalchemy.Column('LABEL_NAME'),
            sqlalchemy.Column('LABEL_VALUE'),
            sqlalchemy.Column('LABEL_VALUE_STRING')
        )
        metadata = self.create_metadata(metadata)
        params = []
        for idx in range(len(factor_df)):
            rows = factor_df.iloc[idx]
            param = dict()
            param['REPORT_DATE'] = rows['REPORT_DATE']
            param['REPORT_HISTORY_DATE'] = rows['REPORT_HISTORY_DATE']
            param['FUND_UNIVERSE'] = rows['FUND_UNIVERSE']
            param['IS_ZC'] = rows['IS_ZC']
            param['LABEL_TYPE'] = rows['LABEL_TYPE']
            param['LABEL_NAME'] = rows['LABEL_NAME']
            param['LABEL_VALUE'] = rows['LABEL_VALUE']
            param['LABEL_VALUE_STRING'] = rows['LABEL_VALUE_STRING']
            params.append(param)
            if len(params) > 1000:
                self.update_data(table, params)
                del params
                params = []
        if len(params) > 0:
            self.update_data(table, params)
        self.close_connection()
        return

    def read_data(self, date, label_type):
        sql = "SELECT REPORT_DATE, REPORT_HISTORY_DATE, FUND_UNIVERSE, IS_ZC, LABEL_TYPE, LABEL_NAME, LABEL_VALUE, LABEL_VALUE_STRING FROM fe_temp_data.mutual_fund_holding_label where REPORT_DATE='{0}' AND LABEL_TYPE='{1}' AND FUND_UNIVERSE='FOCUS_MUTUAL_FUND_UNIVERSE' AND IS_ZC=1".format(date, label_type)
        df = self.get_df(sql)
        df['REPORT_DATE'] = df['REPORT_DATE'].astype(str)
        df['REPORT_HISTORY_DATE'] = df['REPORT_HISTORY_DATE'].astype(str)
        df['IS_ZC'] = df['IS_ZC'].astype(int)
        return df