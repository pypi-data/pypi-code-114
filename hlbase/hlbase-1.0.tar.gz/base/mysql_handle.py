# -*- coding: utf-8 -*-
# python 3.x
# author：huangxiaoyan
# data:"2021/7/20 10:47"

import pymysql.cursors
from dbutils.pooled_db import PooledDB
from base.config_util import ConfigUtil


class MysqlHandle:
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = MysqlUtil.get_conn()
    释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    env = {'b2h': None, 'h2b2': None, 'h2b3': None, 'h2b4': None, 'h2b5': None, 'sync': None, 'pro': None}

    @classmethod
    def db(cls, dbName='health_management', db='db'):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        cls.conn = MysqlHandle.get_conn(dbName, db)
        cls.cursor = cls.conn.cursor()
        return cls

    @classmethod
    def get_conn(cls, dbName, db):
        """
        @summary: 从连接池中取出连接
        @return pymysql.connection
        """
        if db:
            db_config = ConfigUtil.getDb(db)
        else:
            db_config = ConfigUtil.getDb()
        if db_config is None:
            exit('数据库配置不存在')
        curEnv = ConfigUtil().getGlobalsProjectEnv().lower()
        connargs = {"host": db_config['host'], "user": db_config['user'], "passwd": db_config['password'],
                    "db": '{}{}'.format(curEnv + '_' if curEnv != 'pro' else '', dbName), "charset": 'utf8mb4',
                    "port": db_config['port']}
        if MysqlHandle.env[curEnv] is None:
            MysqlHandle.env[curEnv] = PooledDB(creator=pymysql, mincached=5, **connargs)
        return MysqlHandle.env[curEnv].connection()

    @classmethod
    def get_all(cls, sql, param=None):
        """
        @summary: 执行查询，并取出所有结果集
        @param sql:查询sql，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list(字典对象)/boolean 查询到的结果集
        """
        if param is None:
            count = cls.cursor.execute(sql)
        else:
            count = cls.cursor.execute(sql, param)
        if count > 0:
            result = cls.cursor.fetchall()
        else:
            result = False
        return result

    @classmethod
    def get_one(cls, sql, param=None):
        """
        @summary: 执行查询，并取出第一条
        @param sql:查询sql，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = cls.cursor.execute(sql)
        else:
            count = cls.cursor.execute(sql, param)
        if count > 0:
            result = cls.cursor.fetchone()
        else:
            result = False
        return result

    @classmethod
    def get_many(cls, sql, num, param=None):
        """
        @summary: 执行查询，并取出num条结果
        @param sql:查询sql，如果有查询条件，请只指定条件列表，并将条件值使用参数[param]传递进来
        @param num:取得的结果条数
        @param param: 可选参数，条件列表值（元组/列表）
        @return: result list/boolean 查询到的结果集
        """
        if param is None:
            count = cls.cursor.execute(sql)
        else:
            count = cls.cursor.execute(sql, param)
        if count > 0:
            result = cls.cursor.fetchmany(num)
        else:
            result = False
        return result

    @classmethod
    def insert_one(cls, sql, fields):
        """
        @summary: 向数据表插入一条记录
        @param sql:要插入的sql格式
        @param fields:要插入的记录数据键值对tuple/list
        @return: insert_id 受影响的行数
        """
        try:
            data = []
            for value in fields.values():
                # logging.info(value)
                # logging.info('------------------')
                data.append(value)
            cls.cursor.execute(sql, data)
            cls.conn.commit()
            return cls.get_insert_id()
        except Exception as e:
            cls.conn.rollback()
            return e

    @classmethod
    def insert_many(cls, sql, values):
        """
        @summary: 向数据表插入多条记录
        @param sql:要插入的sql格式
        @param values:要插入的记录数据tuple(tuple)/list[list]
        @return: count 受影响的行数
        """
        try:
            count = cls.cursor.executemany(sql, values)
            cls.conn.commit()
            return count
        except:
            cls.conn.rollback()
            return 0

    @classmethod
    def get_insert_id(cls):
        """
        获取当前连接最后一次插入操作生成的id,如果没有则为0
        """
        cls.cursor.execute("SELECT @@IDENTITY AS id")
        result = cls.cursor.fetchall()
        return result[0][0]

    @classmethod
    def query(cls, sql, param=None):
        try:
            if param is None:
                count = cls.cursor.execute(sql)
                cls.conn.commit()
            else:
                count = cls.cursor.execute(sql, param)
                cls.conn.commit()
            return count
        except:
            cls.conn.rollback()
            return 0

    @classmethod
    def update(cls, sql, param=None):
        """
        @summary: 更新数据表记录
        @param sql: sql格式及条件，使用(%s,%s)
        @param param: 要更新的  值 tuple/list
        @return: count 受影响的行数
        """
        return cls.query(sql, param)

    @classmethod
    def delete(cls, sql, param=None):
        """
        @summary: 删除数据表记录
        @param sql: sql格式及条件，使用(%s,%s)
        @param param: 要删除的条件 值 tuple/list
        @return: count 受影响的行数
        """
        return cls.query(sql, param)

    @classmethod
    def begin(cls):
        """
        @summary: 开启事务
        """
        cls.conn.autocommit(0)

    @classmethod
    def end(cls, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            cls.conn.commit()
        else:
            cls.conn.rollback()

    @classmethod
    def dispose(cls, is_end=1):
        """
        @summary: 释放连接池资源
        """
        if is_end == 1:
            cls.end('commit')
        else:
            cls.end('rollback')
        cls.cursor.close()
        cls.conn.close()

    @classmethod
    def execute_sql(cls, sql):
        """
        @summary:执行原生SQL，主要是插入、更新、删除
        :param sql: 要执行的SQL语句
        :return: 1代表成功 0代表失败
        """
        try:
            cls.cursor.execute(sql)
            cls.conn.commit()
            return 1
        except:
            cls.conn.rollback()
            return 0
