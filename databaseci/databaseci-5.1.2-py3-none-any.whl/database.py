import getpass
from contextlib import contextmanager
from inspect import currentframe
from threading import get_ident

from psycopg2 import connect as pgconnect
from psycopg2.extras import NamedTupleCursor, RealDictCursor, execute_batch
from psycopg2.pool import ThreadedConnectionPool

from .createdrop import DatabaseCreateDrop
from .notify import ListenNotify
from .paging import Paging
from .psyco import reformat_bind_params
from .schemas import Schemas

conns = {}


def get_conn(db_url):
    tid = get_ident()

    if db_url not in conns:
        conns[db_url] = ThreadedConnectionPool(1, 1024, db_url)

    pool = conns[db_url]

    conn = pool.getconn(tid)

    return conn


def put_conn(conn, db_url):
    tid = get_ident()

    pool = conns[db_url]
    pool.putconn(conn, tid)


class Rows(list):
    pass


class Transaction(Paging):
    def __init__(self):
        self._back = 0

    def ex(self, *args, **kwargs):
        self.c.execute(*args, **kwargs)

    def execute(self, *args, **kwargs) -> Rows:
        self.c.execute(*args, **kwargs)

        if self.c.description is None:
            return None

        fetched = self.c.fetchall()
        descr = list(self.c.description)

        rows = Rows(fetched)
        rows.desc = descr

        return rows

    def q(self, query):
        query = reformat_bind_params(query)

        frame = currentframe()

        try:
            if self._back:
                fback = frame.f_back.f_back
            else:
                fback = frame.f_back

            caller_locals = fback.f_locals

            return self.execute(query, caller_locals)
        finally:
            del frame

    def insert(self, t, rows):
        batch_size = len(rows)
        width = len(rows[0])

        params = ", ".join(["%s"] * width)

        sql = f"insert into {t} values ({params})"
        execute_batch(self.c, sql, rows, page_size=batch_size)


@contextmanager
def autocommit_transaction(db_url):
    conn = pgconnect(db_url)

    conn.autocommit = True

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as curs:
            t = Transaction()
            t.c = curs
            yield t
    finally:
        conn.close()


@contextmanager
def autocommit_connection(db_url):
    conn = pgconnect(db_url)

    conn.autocommit = True

    try:
        yield conn
    finally:
        conn.close()


@contextmanager
def transaction(db_url, cursor_factory=RealDictCursor):
    conn = get_conn(db_url)

    try:
        with conn:
            with conn.cursor(cursor_factory=cursor_factory) as curs:
                t = Transaction()
                t.c = curs
                yield t
    finally:
        put_conn(conn, db_url)


def db(url):
    return Database(url)


class Database(DatabaseCreateDrop, Schemas, ListenNotify):
    def __init__(self, url):
        if ":" not in url and "/" not in url:
            url = f"postgresql:///{url}"

        self.url = url

    @contextmanager
    def t(self):
        with transaction(self.url) as t:
            yield t

    @contextmanager
    def t_autocommit(self):
        with autocommit_transaction(self.url) as t:
            yield t

    @contextmanager
    def c_autocommit(self):
        with autocommit_connection(self.url) as t:
            yield t

    @contextmanager
    def _t_namedtuple(self):
        with transaction(self.url, cursor_factory=NamedTupleCursor) as t:
            yield t

    def autocommit(self, *args, **kwargs):
        with self.t_autocommit() as t:
            t.q(*args, **kwargs)

    def __getattr__(self, name):
        def method(*args, **kwargs):
            with self.t() as t:
                t._back = 1
                m = getattr(t, name)
                return m(*args, **kwargs)

        return method

    def __repr__(self):
        return f"db(url={self.url})"
