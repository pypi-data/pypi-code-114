from uuid import RESERVED_FUTURE
import pymysql
import html


class MySQLClient:
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306) -> None:
        '''
        初始化数据库连接
        :param host 主机地址
        :param user 用户名
        :param password 密码
        :param database 数据库
        :param port 端口，默认3306
        return {bool} True/False
        '''
        # 打开数据库连接
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def insert(self, table: str, data: dict):
        '''
        插入数据
        :param table 表名
        :param data 需要插入的数据
        return {bool} True/False
        '''
        result = False
        # 列
        col = []
        # 行
        row = []
        for d in data.keys():
            col.append(d)
            row.append('"'+html.escape(data[d])+'"')
        sql = 'INSERT INTO %s (%s) VALUES (%s)' % (
            table,
            ','.join(col),
            ','.join(row)
        )
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            result = True
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            result = False
        self.db.close()
        return result

    def fetch(self, fields: list, table: str, query: str):
        '''
        查询数据
        :param fields 要查询的字段名
        :param table 表名
        :param query 查询条件
        :return {tuple}
        '''
        sql = 'SELECT %s FROM %s WHERE %s' % (
            ','.join(fields),
            table,
            query
        )
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
        except:
            print("Error: unable to fetch data")
        # 关闭数据库连接
        self.db.close()
        return results

    def update(self, table: str, set: str, query: str):
        '''
        更新数据
        :param table 表名
        :param set 修改内容
        :param query 查询条件
        return {bool} True/False
        '''
        result = False
        sql = 'UPDATE %s SET %s WHERE %s' % (
            table,
            set,
            query
        )
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            result = True
        except:
            # 发生错误时回滚
            self.db.rollback()
            result = False
        # 关闭数据库连接
        self.db.close()
        return result

    def delete(self, table: str, query: str):
        '''
        删除数据
        :param table 表名
        :param query 查询条件
        return {bool} True/False
        '''
        result = False
        sql = 'DELETE FROM %s WHERE %s' % (
            table,
            query
        )
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
            result = True
        except:
            # 发生错误时回滚
            self.db.rollback()
            result = False
        # 关闭数据库连接
        self.db.close()
        return result


if __name__ == '__main__':
    pass
