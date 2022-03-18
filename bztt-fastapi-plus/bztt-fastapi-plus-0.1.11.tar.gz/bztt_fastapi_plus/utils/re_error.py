#####
# 处理错误
#####

# 数据库错误
class DbError():
    def __init__(self, name: str):
        self.name = name

    def noFind(self, name: str):
        self.name = name


#  JWT错误
class JWTError(Exception):
    def __init__(self, name: str):
        self.name = name
    pass