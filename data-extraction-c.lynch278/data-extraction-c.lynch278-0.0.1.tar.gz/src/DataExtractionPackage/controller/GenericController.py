import requests
import pandas as pd
import datetime

import sqlalchemy.types


class GenericController:
    def __init__(self, name, url, auth, cookie, attribute_list, column_names, start_time, engine, database_name):
        self.name = name
        self.start_time = start_time
        self.column_names = column_names
        self.auth = auth
        self.attribute_list = attribute_list
        self.url = url
        self.cookie = cookie
        self.engine = engine
        self.connection = self.engine.connect()
        self.database_name = database_name

    def get_objects(self):

        payload = {}
        headers = {
            'Authorization': self.auth,
            'Cookie': self.cookie
        }

        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response

    def extract_objects(self, http_result):
        object_list = []
        for asset in http_result.json()['results']:
            result_list = []
            for attribute in self.attribute_list:
                if isinstance(attribute, list):
                    if str(attribute[0]) in asset:
                        result_list.append(str(asset[str(attribute[0])][str(attribute[1])]))
                    else:
                        result_list.append(None)
                else:
                    if str(attribute) in asset:
                        result_list.append(str(asset[str(attribute)]))
                    else:
                        result_list.append(None)

            # For the extraction date
            result_list.append(self.start_time)
            object_list.append(result_list)

        return object_list

    def add_to_pandas(self, object_list):

        df = pd.DataFrame(object_list,
                          columns=self.column_names.keys())

        # Add logic to change column data type
        if 'Created_Date' in df:
            df['Created_Date'] = \
                df['Created_Date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1e3))
        if 'Last_Modified_Date' in df:
            df['Last_Modified_Date'] = \
                df['Last_Modified_Date'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1e3))
        if 'Extraction_Date' in df:
            df['Extraction_Date'] = pd.to_datetime(df['Extraction_Date'])

        return df

    def get_pandas_db(self):
        response = self.get_objects()
        asset_list = self.extract_objects(response)
        dataframe = self.add_to_pandas(asset_list)
        return dataframe

    def delete_existing_data(self):
        table_name = "[" + self.database_name + "].[Extract].[collibra_" + self.name + "_raw]"
        self.connection.execute('DELETE FROM' + table_name+' ;' )

    def write_to_sql(self):
        self.delete_existing_data()
        dataframe = self.get_pandas_db()
        dataframe.to_sql(
            "collibra_" + self.name + "_raw",
            schema="extract",
            con=self.engine,
            chunksize=100,
            method="multi",
            index=False,
            if_exists="append",
            dtype= self.column_names
        )