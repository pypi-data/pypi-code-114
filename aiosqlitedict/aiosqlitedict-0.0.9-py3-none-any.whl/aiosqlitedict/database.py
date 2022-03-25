import aiosqlite


class connect:

    """
    Instantiate a conversion to and from sqlite3 database and python dictionary.
    """
    
    def __init__(self, database_name: str, id_column: str):
        self.database_name = database_name
        self.id_column = id_column

    async def to_dict(self, table_name, id_column, *column_names: str):
        """
        Convert a sqlite3 table into a python dictionary.
        :param table_name: The name of the database table.
        :type table_name: str

        :param id_column: The id of the row.
        :type id_column: int

        :param column_names: The column name.
        :type column_names: str

        :return: The dictionary.
        :rtype: dict
        """
        async with aiosqlite.connect(self.database_name) as db:
            async with db.cursor() as cursor:

                table_name = table_name.replace("'", "").replace('"', "")
                data = {}
                columns = str(column_names).replace("(", "").replace(")", "").replace('"', "").replace("'", "")
                columns = columns.replace(columns[-1], "") if columns.endswith(",") else columns
                getID = await cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {self.id_column} = ?", (id_column,))
                values = await getID.fetchone()
                values = list(values)
                for v in range(len(values)):
                    if str(values[v]).startswith("["):
                        values[v] = values[v].replace("[", "").replace(']', "").replace(" ' ", "").replace(' " ', "").replace(" '", "").replace(' "', "").replace("' ", "").replace('" ', "").replace("'", "").replace('"', "").replace(",", "|")
                        values[v] = values[v].split("|")
                    else:
                        continue
                for i in range(len(column_names)):
                    data[column_names[i]] = values[i]
                return data

    #  To push data to db

    async def to_sql(self, table_name, my_id, dictionary: dict):
        """
        Convert a python dictionary into a sqlite3 table.
        :param table_name: The name of the database table.
        :type table_name: str

        :param my_id: The id of the row.
        :type my_id: int

        :param dictionary: The dictionary object.
        :type dictionary: dict

        :return: The SQLite3 Table.
        :rtype: sqlite
        """
        async with aiosqlite.connect("main.db") as db:
            async with db.cursor() as cursor:
                table_name = table_name.replace("'", "").replace('"', "")
                getUser = await cursor.execute(f"SELECT {self.id_column} FROM {table_name} WHERE {self.id_column} = ?", (my_id,))
                isUserExists = await getUser.fetchone()
                if isUserExists:
                    for key, val in dictionary.items():
                        key = key.replace("'", "").replace('"', "")
                        val = str(val) if str(val).startswith("[") else val
                        await cursor.execute(f"UPDATE {table_name} SET {key} = ? WHERE {self.id_column} = ?", (val, my_id,))
                else:
                    await cursor.execute(f"INSERT INTO {table_name} ({self.id_column}) VALUES ( ? )", (my_id,))
                    for key, val in dictionary.items():
                        key = key.replace("'", "").replace('"', "")
                        val = str(val) if str(val).startswith("[") else val
                        await cursor.execute(f"UPDATE {table_name} SET {key} = ? WHERE {self.id_column} = ?", (val, my_id,))

            await db.commit()
