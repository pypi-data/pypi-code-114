"""
mongodb数据文件操作
"""
from similib.cmd import exe_command
import pymongo


class Mongo(object):
    def __init__(self, ip, port, user, passwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.passwd = passwd
        self.conn = pymongo.MongoClient(host=ip, port=port, username=user, password=passwd)

    def import_json(self, db, col, file_path):
        cmd = "mongoimport -h {} --port {} -u {} -p {} --authenticationDatabase admin --db {} --collection {} --file {}".format(
            self.ip, self.port, self.user, self.passwd, db, col, file_path)
        exe_command(cmd)

    def export_json(self, db, col, file_path):
        cmd = "mongoexport -h {} --port {} -u {} -p {} --authenticationDatabase admin -d {} -c {} -o {}".format(
            self.ip, self.port, self.user, self.passwd, db, col, file_path)
        exe_command(cmd)

    def import_csv(self, db, col, file_path):
        cmd = "mongoimport -h {} --port {} -u {} -p {} --authenticationDatabase admin --db {} --collection {} --type csv --headerline --ignoreBlanks --file {}".format(
            self.ip, self.port, self.user, self.passwd, db, col, file_path)
        exe_command(cmd)

    def export_csv(self, db, col, file_path):
        cmd = "mongoexport -h {} --port {} -u {} -p {} --authenticationDatabase admin -d {} -c {} --type csv -fields --out {} --limit 50".format(
            self.ip, self.port, self.user, self.passwd, db, col, file_path)
        exe_command(cmd)

    def create_index(self, db, col, fields: list, direct=pymongo.ASCENDING, raw=None, unique=True):
        raw = raw if raw else []
        for f in fields:
            raw.append((f, direct))
        self.conn[db][col].create_index(raw, unique=unique)


if __name__ == '__main__':
    pass
