NAME = "name"
TABLES = "tables"
COLUMNS = "columns"


class SchemaWrapper(object):
    schema = {}

    def __init__(self, schema):
        self.schema = schema

    def tables(self) -> list:
        return self.schema[TABLES]

    def table(self, table_name):
        tables = self.tables()
        for table in tables:
            if table_name == table[NAME]:
                return table

        return tables[0]

    def columns(self, table_name) -> list:
        return self.table(table_name)[COLUMNS]

    def column(self, table_name, column_name) -> list:
        columns = self.columns(table_name)
        for column in columns:
            if column_name == column[NAME]:
                return column

        return columns[0]
