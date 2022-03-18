from sqlalchemy import create_engine

class dbintf:
    """dbintf setup database connection info and establish an DB engine
    """
    def __init__(self, db_name:str, user:str='postgres', password:str='password', host:str='localhost', port:str='5432', vendor:str='postgresql'):
        """Setup database connection and establish an DB engine

        :param db_name: database name
        :param user: authorized user name, defaults to 'postgres'
        :param password: authorized user password, defaults to 'password'
        :param host: host url of database connection, defaults to 'localhost'
        :param port: port of database connection, defaults to '5432'
        :param vendor: vendor of database, defaults to 'postgresql'
        """
        self.db_name = db_name
        self.user, self.password = user, password
        self.host, self.port, self.vendor = host, port, vendor
        self.sqlalchemy_url = f"{self.vendor}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        self.engine = create_engine(self.sqlalchemy_url)
