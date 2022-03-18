# -*- coding: utf-8 -*-
import collections

import pandas as pd
from sqlalchemy import MetaData, Table, inspect
from sqlalchemy.sql import text

from dblinea.db_postgresql import DBPostgresql


class DBBase:

    _database = None
    _engine = None

    # TODO: OS dados de coneção com o banco devem vir de outro lugar!
    _available_databases = dict(
        {
            "gavo": {
                "ENGINE": "postgresql_psycopg2",
                "HOST": "desdb4.linea.gov.br",
                "PORT": "5432",
                "USER": "untrustedprod",
                "PASSWORD": "untrusted",
                "DATABASE": "prod_gavo",
            }
        }
    )

    def __init__(
        self,
        database="gavo",
        dbhost=None,
        dbname=None,
        dbuser=None,
        dbpass=None,
        dbport=None,
        dbengine="postgresql_psycopg2",
    ):
        # Se todas as variaveis de configuração forem None
        # Vai criar a conexão usando um dos _available_databases.
        # Default "gavo" ou o valor informado pelo usuario em database
        if all(x is None for x in [dbhost, dbname, dbuser, dbpass, dbport]):
            self.__set_database(database)
        else:
            # Se ao menos umas dessas variaveis
            # [dbhost, dbname, dbuser, dbpass, dbport]
            # For diferente de None, vai tentar criar uma conexão
            # usando os dados que o usuario passou.
            # Util para:
            # - Acessar outros bancos de dados que o usuario tenha acesso
            # - Conectar ao banco usando suas credenciais
            # - Para executar os Unit tests fora do ambiente.
            db_settings = {
                "ENGINE": dbengine,
                "HOST": dbhost,
                "PORT": "5432",
                "USER": dbuser,
                "PASSWORD": dbpass,
                "DATABASE": dbname,
            }

            self._database = DBPostgresql(db_settings)

    def __set_database(self, database):
        """Instancia a classe de Banco de dados.

        Este Metodo é utilizado quando é passado o
        parametro database na instancia da Classe.
        verifica se o database está na lista _available_databases

        Args:
            database (str): Nome do database como está no
            atributo _available_databases.

        Raises:
            ValueError: Database not available.
        """

        if database not in self._available_databases:
            raise ValueError("Database not available.")

        db_settings = self._available_databases[database]

        if db_settings["ENGINE"] == "postgresql_psycopg2":
            self._database = DBPostgresql(db_settings)

        # if db["ENGINE"] == "sqlite3":
        #     return DBSqlite(db)

        # if db_settings["ENGINE"] == "oracle":
        #     return DBOracle(db_settings)

    def available_databases(self):
        """Lista os bancos de dados disponiveis

        Returns:
            Lista de databases pre configurados na bibloteca.
            cada elemento da lista representa um db.

            exemplo:
            [{'config_name': 'gavo', 'dbname': '<database_name>',
            'host': '<database_host.linea.gov.br>', 'engine': 'postgresql_psycopg2'}]
        """

        dbs = list()
        for config_name in self._available_databases:
            dbs.append(
                dict(
                    {
                        "config_name": config_name,
                        "dbname": self._available_databases[config_name]["DATABASE"],
                        "host": self._available_databases[config_name]["HOST"],
                        "engine": self._available_databases[config_name]["ENGINE"],
                    }
                )
            )

        return dbs

    def get_engine(self):
        """Retorna uma sqlalchemy.Engine

        Cria ou retorna uma engine para o database solicitado na Instancia da DBBase.
        Mais informações sobre Engine em
        https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine

        Returns:
            sqlalchemy.engine.Engine:
        """

        if self._engine is None:

            self._engine = self._database.get_engine()

        return self._engine

    def get_table(self, tablename, schema=None):
        """Retona uma instancia de sqlalchemy.schema.Table que representa uma tabela no database.
        https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Table

        Args:
            tablename (str): Nome da tabela sem o schema.
            schema (str, optional): Schema onde a tabela se encontra. Defaults to None.

        Returns:
            sqlalchemy.schema.Table: instancia de Table representando a tabela solicitada.
        """
        engine = self.get_engine()
        tbl = Table(tablename, MetaData(engine), autoload=True, schema=schema)
        return tbl

    def execute(self, stm):
        """Executa a query usando con.execute,
        recomendada para query de Delete, Update ou outras
        querys que não precisem de iteração com o resultado.

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            CursorResult: [description]
        """
        with self.get_engine().connect() as con:
            return con.execute(stm)

    def fetchall(self, stm):
        """Executa a query e retorna todos os resultados em uma lista.

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            list: Lista com os resultado no formato original do SqlAlchemy LegacyRow.
        """
        # Convert Raw sql to Sql Alchemy TextClause
        stm = self.raw_sql_to_stm(stm)

        with self.get_engine().connect() as con:
            queryset = con.execute(stm).fetchall()
            return queryset

    def fetchall_dict(self, stm):
        """Executa a query e retorna todos os resultados em uma lista de Dicts.
            exemplo:[{'col': 'value', ..., 'colN':'valueN'}]

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            list: Resultado da query em uma lista de dicionários.
        """
        # Convert Raw sql to Sql Alchemy TextClause
        stm = self.raw_sql_to_stm(stm)

        with self.get_engine().connect() as con:
            queryset = con.execute(stm)

            rows = list()
            for row in queryset:
                rows.append(self.to_dict(row))

            return rows

    def fetchall_df(self, stm):
        """Executa a query usando Pandas e retorna um Dataframe com o resultado.

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            Pandas.Dataframe: Dataframe com o resultado da query.
        """
        df = pd.read_sql(stm, con=self.get_engine())

        return df

    def fetchone(self, stm):
        """Executa a query retorna a primeira linha do resultado

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            sqlalchemy.engine.row.LegacyRow: Primeira linha do resultado da query.
        """

        # Convert Raw sql to Sql Alchemy TextClause
        stm = self.raw_sql_to_stm(stm)

        with self.get_engine().connect() as con:
            queryset = con.execute(stm).fetchone()
            return queryset

    def fetchone_dict(self, stm):
        """Executa a query retorna a primeira linha do resultado convertida em Dict

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            dict: Primeira linha do resultado da query.
        """
        # Convert Raw sql to Sql Alchemy TextClause
        stm = self.raw_sql_to_stm(stm)

        with self.get_engine().connect() as con:
            queryset = con.execute(stm).fetchone()

            if queryset is not None:
                return self.to_dict(queryset)
            else:
                return None

    def fetch_scalar(self, stm):
        """Retorna o valor da primeira coluna na primeira linha do resultado da query
        util para querys de count por exemplo, ou quando se quer apenas um unico valor.

        Args:
            stm (statement): Query a ser executada, pode ser escrita em SqlAlchemy
            ou string no caso de string ela sera convertida para TextClause.

        Returns:
            any: Valor da primeira coluna na primeira linha.
        """
        # Convert Raw sql to Sql Alchemy TextClause
        stm = self.raw_sql_to_stm(stm)

        with self.get_engine().connect() as con:
            return con.execute(stm).scalar()

    def to_dict(self, row):
        """Converte uma linha de resultado do SQLAlchemy queryset para Dict

        Args:
            row (sqlalchemy.engine.row.LegacyRow): Row retornada pelo execute.

        Returns:
            dict : Row convertida para Dict {colname: value, colname2: value2 ...}
        """
        return dict(collections.OrderedDict(row))

    def raw_sql_to_stm(self, stm):
        """Converte uma string raw sql para SqlAlchemy TextClause

        Args:
            stm (str): Query SQL em string. ex: Select * from tablename...

        Returns:
            TextClause: TextClause representando uma string SQL.
        """
        if isinstance(stm, str):
            return text(stm)
        return stm

    def get_table_columns(self, tablename, schema=None):
        """Retorna os nomes das colunas de uma tabela.

        Args:
            tablename (string): Nome da tabela sem schema.
            schema (string): Nome do schema ou None quando nao houver.

        Returns:
            columns (list): Colunas disponiveis na tabela
        """
        insp = inspect(self.get_engine())
        return [value["name"] for value in insp.get_columns(tablename, schema)]

    def describe_table(self, tablename, schema=None):
        """Retorna uma lista de dicionarios com nome e
        tipo das colunas de uma tabela.
        exemplo: [{"name": "", "type": ""}]

        Args:
            tablename (str): Nome da tabela sem schema.
            schema (str, optional): Nome do schema. Defaults to None.

        Returns:
            list: Lista de colunas com seu tipo
        """

        cols = list()

        insp = inspect(self.get_engine())
        for c in insp.get_columns(tablename, schema):
            cols.append(dict({"name": c["name"], "type": c["type"]}))

        return cols
