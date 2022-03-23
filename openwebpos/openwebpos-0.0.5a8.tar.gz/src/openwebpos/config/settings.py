import os
from openwebpos.utils import gen_urlsafe_token

SECRET_KEY = gen_urlsafe_token(16)

# database
DB_DIALECT = 'sqlite'
DB_DRIVER = 'mysqldb'
DB_USER = 'mysql_user'
DB_PASS = 'mysql_password'
DB_HOST = '172.16.0.64'
DB_PORT = '3306'
DB_NAME = 'openwebpos_db'

if DB_DIALECT == 'sqlite':
    db_uri = 'sqlite:///' + os.path.join(os.getcwd(), 'openwebpos.db')
else:
    db_uri = f'{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
