#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 20:13
# @Author : 心蓝
import time
import threading
import pymysql
from multiprocessing.pool import ThreadPool


class DB:
    def __init__(self, pool_size=5, max_size=32, **kwargs):
        if pool_size > max_size:
            pool_size = max_size
        self.pool_size = pool_size
        self.max_size = max_size
        self.db_config = kwargs
        self.db_config['autocommit'] = True
        self.pool = []
        self.running_conn_num = 0
        # self.conn = pymysql.connect(**kwargs)
        self.cursor_args = kwargs.pop('cursor_args', {})
        self.lock = threading.Lock()

        if not self.cursor_args:
            self.cursor_args = {}

    def __get_conn(self):
        if self.pool:
            return self.pool.pop()
        else:
            self.lock.acquire()
            if self.running_conn_num < self.pool_size:
                try:
                    conn = pymysql.connect(**self.db_config, connect_timeout=3)
                    self.running_conn_num += 1
                except Exception as e:
                    raise e
                else:
                    return conn
                finally:
                    self.lock.release()

            else:
                self.lock.release()
                time.sleep(0.1)
                return self.__get_conn()

    def __execute(self, action, sql, **kwargs):
        conn = self.__get_conn()
        with conn.cursor(**self.cursor_args) as cursor:
            count = cursor.execute(sql)

            if action == 'exist':
                if cursor.fetchone():
                    res = True
                else:
                    res = False
            elif action == 'get_one':
                res = cursor.fetchone()
            elif action == 'get_one_value':
                res = cursor.fetchone()
                if isinstance(res, tuple):
                    res = res[0]
                elif isinstance(res, dict):
                    for value in res.values():
                        res = value
            elif action == 'get_many':
                res = cursor.fetchmany(**kwargs)
            elif action == 'get_all':
                res = cursor.fetchall()
            elif action == 'count':
                res = count
        self.pool.append(conn)
        return res

    def exist(self, sql):
        """
        查询是否存在数据
        :param sql: 需要执行的sql
        :return:
        """
        return self.__execute(action='exist', sql=sql)

    def get_one(self, sql):
        """
        获取一条查询结果
        :param sql:
        :return:
        """
        return self.__execute(action='get_one', sql=sql)

    def get_one_value(self, sql):
        """
        获取一个值
        :param sql:
        :return:
        """
        return self.__execute(action='get_one_value', sql=sql)

    def get_many(self, sql, size):
        """
        获取指定条数的查询结果
        :param sql:
        :param size: 指定条数 整数
        :return:
        """
        return self.__execute(action='get_many', sql=sql, size=size)

    def get_all(self, sql):
        """
        获取所有的查询结果
        :param sql:
        :return:
        """
        return self.__execute(action='get_all', sql=sql)

    def get_value(self, sql):
        res = self.__execute(action='get_all', sql=sql)
        res = [item[0] for item in res]
        if len(res) == 0:
            return res
        elif len(res) == 1:
            return res[0]
        else:
            return res

    def __del__(self):
        for conn in self.pool:
            conn.close()
# db = DB(**settings.DATABASE_CONFIG)

if __name__ == '__main__':
    db = DB(
    pool_size= 32,
    host='api.lemonban.com',
    user='future',
    password='123456',
    db='futureloan',
    charset='utf8',
    )
    pool = ThreadPool(2)
    sql = 'select * from member order by id desc limit 1'
    res = []

    for i in range(10):
        res.append(pool.apply_async(db.exist, args=(sql, )))
    pool.close()
    pool.join()

    print(db.running_conn_num, 'a')
    print([x.get() for x in res])


    # with db.conn.cursor() as cursor:
    #     cursor.close()
    #     cursor.execute(sql)
    # print(db.exist(sql))

    # print(db.get_one(sql))
    # cursor = db.conn.cursor()
    # try:
    #     cursor.execute(sql)
    # except:
    #     cursor.close()
    # print(cursor.fetchmany(2))
    # cursor.close()
    # print(db.exist(sql))
    # print(db.get_one(sql))
    # print(db.get_one_value(sql))
    # print(db.get_many(sql, 2))
    # print(db.get_all(sql))
    # res = db.exist("select id from member where mobile_phone='157'")
    # print(res)





