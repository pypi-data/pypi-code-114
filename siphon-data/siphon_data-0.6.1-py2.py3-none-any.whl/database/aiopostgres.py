from typing import AsyncGenerator, List, Tuple, Type

from asyncpg import Record, create_pool
from pydantic import BaseModel

from siphon.database.config import PostgresConfig


class AioPostgres:
    def __init__(
        self, config: PostgresConfig, timeout: int = None, min_size: int = 1, max_size: int = 10
    ):
        """
        AioPostgres is an async postgres client that allows you to setup a connection pool for
        Postgres and read and write data asynchronously. Contains an async context manager for easy
        setup and closing of the connections that you open.
        Args:
            config: a DatabaseConfig object that contains all the connection details for postgres
            timeout: max time before a query is cancelled
            min_size: The minimum # of connections that will be reserved for this client
            max_size: The maximum # of connections that will be reserved for this client
        """
        self.pool = None
        self.config = config
        self.timeout = timeout
        self.min_size = min_size
        self.max_size = max_size

    @property
    def closed(self) -> bool:
        return self.pool._closed  # type: ignore

    async def setup_pool(self) -> None:
        self.pool = await create_pool(
            host=self.config.host.get_secret_value(),
            port=self.config.port,
            user=self.config.user.get_secret_value(),
            password=self.config.password.get_secret_value(),
            database=self.config.database,
            command_timeout=self.timeout,
            min_size=self.min_size,
            max_size=self.max_size,
        )

    async def __aenter__(self):
        await self.setup_pool()
        return self

    async def read(
        self, query: str, params: Tuple = None, model: Type[BaseModel] = None
    ) -> AsyncGenerator:
        """
        Read results from postgres and return an AsyncGenerator. This allows you to read large
        amounts of data without having to store them in memory.
        Examples:
            pg = Postgres()
            async for row in pg.read("SELECT * FROM bigtable"):
                process(row)
        Args:
            query: The query you want to return data for
            params: Any params you need to pass to the query
            model: An optional pydantic.BaseModel that will be run over the row to parse to
            a standard format

        Returns: An AsyncGenerator

        """
        async with self.pool.acquire() as conn:  # type: ignore
            async with conn.transaction():
                if params:
                    cur = conn.cursor(query, *params)
                else:
                    cur = conn.cursor(query)
                async for row in cur:
                    if model:
                        yield model(**row)
                    else:
                        yield row

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_pool()

    async def read_all(
        self, query: str, params: Tuple = None, model: Type[BaseModel] = None
    ) -> List[Record]:
        """
        In some cases you might want to just return the data without dealing with iteration you can
        use this. We'll return all the records in a list. Be careful using this for large datasets
        as it will try and load everything in memory.
        Args:
            query: The query you want to return data for
            params: Any params you need to pass to the query
            model:

        Returns: A List of Records that can be accessed as you would a Tuple (E.g record[0] or
        a Dict (E.g record["column"])

        """
        rows = []
        async for row in self.read(query=query, params=params, model=model):
            rows.append(row)
        return rows

    async def write(self, stmt: str, params: Tuple) -> None:
        """
        Write data to a table with the given statement and data
        Args:
            stmt: The Insert statement you want to run
            params: The data to pass as params

        Returns: None

        """
        async with self.pool.acquire() as conn:  # type: ignore
            async with conn.transaction():
                await conn.executemany(stmt, params)

    async def commit(self, stmt: str) -> None:
        """
        Run a command against the database. This is useful for statements where you need to change
        the database in some way E.g ALTER, CREATE, DROP statements etc
        Args:
            stmt: The statement to run

        Returns: None

        """
        async with self.pool.acquire() as conn:  # type: ignore
            await conn.execute(stmt)

    async def close_pool(self) -> None:
        await self.pool.close()  # type: ignore

    def writer(self, stmt: str):
        """return a writer for the given statment.

        Basically just currys the write method into a coroutine that accepts a batch of parameters
        and writes using the given statement. Obviously this is useful if you are batching inserts.

        Args:
            stmt: The Insert statement you want to run
        """

        async def writer(batch):
            await self.write(stmt, batch)

        return writer
