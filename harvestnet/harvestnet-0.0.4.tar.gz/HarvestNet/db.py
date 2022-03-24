import pymysql
host = "39.98.144.212"
port = 3306
user = "root"
passwd = "admin123"
db = "login_test"
conn = None
cur = None

# 执行数据库操作之前判断数据库连接是否OK，如果异常则创建一次连接
def db_opt(func):
    def db_ping():
        global conn, cur
        try:
            cur.execute("select 1")
            cur.fetchone()
        except:
            conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset="utf8")
            cur = conn.cursor()
            print("build a new connection")

    def wrapper(*args, **kwargs):
        global conn, cur

        try:
            db_ping()
            res =  func(*args, **kwargs)
            print("db_opt", func, args, res)
            return res
        except:
            # traceback.print_exc('wrapper ')
            return {'status':False, 'data':'db operation maybe have some errors.'}
    return wrapper

class DbUser:
    @staticmethod
    @db_opt
    def get_id(id):
        sql = 'select ID from Login where ID = "%s"' % id
        cur.execute(sql)
        res = cur.fetchall()
        if len(res) == 0:
            print("error")
            return '0'
        else:
            id = res[0]
            id = str(id[0])
            user_id ={}
            user_id['id'] = id
            print(user_id['id'])
            return user_id['id']


if __name__ == '__main__':
    print("id",DbUser.get_id("096992"))