'''
This module contains functions to handle database interactions.
Document stores like mongodb will be preferred choice for DB.
'''
# Import Libraries
from os import environ
from pymongo import MongoClient
from pandas import read_csv
class db_handler():
    connected_db = None
    def __init__(self,db_details) -> None:
        self.mongo_host = db_details['MONGO_HOST']
        self.mongo_port = db_details['MONGO_PORT']
        self.mongo_db_name = db_details['MONGO_DB_NAME']
        self.mongo_user = db_details['MONGO_USER']
        try:
            self.mongo_db_table_name = db_details['MONGO_DB_I18N_TABLE']
        except:
            pass
        self.mongo_password = db_details['MONGO_PASSWORD']
        if db_details['MONGO_HOST'] != "localhost":
            self.mongo_client = MongoClient(f'mongodb://{self.mongo_user}:{self.mongo_password}@{self.mongo_host}:{self.mongo_port}/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
        else:
            self.mongo_client = MongoClient(self.mongo_host, int(self.mongo_port))
        self.connected_db = self.mongo_client[self.mongo_db_name]
    def csv_to_db(self,table_name,file_path):
        df = read_csv(file_path)
        data = df.to_dict(orient="records")
        col = self.connected_db[table_name]
        col.insert_many(data)
        print("Completed the csv to db task")
    def get_document_for_key(self,table_name,key ,search_value):
        print(f"Finding document {search_value} in {table_name} mongodb collection in {self.mongo_db_name} database.")
        col = self.connected_db[table_name]
        result_value = col.find_one({
            key : search_value
            })
        return result_value
    def set_document_for_key(self, table_name,key,search_value,replace_key,replace_value):
        print(f"updating {replace_key} to {replace_value} in {table_name} mongodb collection in {self.mongo_db_name} database.")
        col = self.connected_db[table_name]
        query = {key : search_value}
        update_data = {'$set':
            {replace_key : replace_value}
        }
        col.update_one( query, update_data)
        print("Completed set_document_for_key task")
    def get_translated_text_for_lang(self, text, lang_code):
        table_name = self.mongo_db_table_name
        col = self.connected_db[table_name]
        search_query = {'$and':[{'texts': {"$eq":text.strip()}},{'lang_code':{"$eq":lang_code}}]}
        result = col.find_one(search_query)
        if result is not None:
            return result['lang_text']
        return result
    def reverse_translate(self, text):
        table_name = self.mongo_db_table_name
        result = self.get_document_for_key(table_name=table_name, key='lang_text', search_value=text.strip())
        if result is not None:
            return result['texts']
        return text
    def insert_data(self,table_name, entry):
        mycol = self.connected_db[table_name]
        mycol.insert_one(entry)
        return