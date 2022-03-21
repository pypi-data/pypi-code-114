from psycopg2.errors import DuplicateDatabase, InvalidCatalogName

from .psyco import quoted_identifier as qi


class DatabaseCreateDrop:
    def check_connection(self):
        return self.q("select 1")

    def create_db(
        self, name, *, fail_if_exists=True, drop_and_recreate_if_exists=False
    ):
        _name = qi(name)

        recreate = False

        try:
            self.autocommit(f"create database {_name};")

        except DuplicateDatabase:
            if fail_if_exists:
                raise

            elif drop_and_recreate_if_exists:
                self.drop(name)
                recreate = True

        if recreate:
            self.autocommit(f"create database {_name};")

    def drop_db(self, name, *, fail_if_not_exists=True):
        _name = qi(name)

        try:
            self.autocommit(f"drop database {_name};")
        except InvalidCatalogName:
            if fail_if_not_exists:
                raise
