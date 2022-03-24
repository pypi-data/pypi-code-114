# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from urllib.parse import quote_plus as url_quote
import yaml
from src.DataExtractionPackage.controller.GenericController import GenericController
from src.DataExtractionPackage.controller.Access_Token import AccessToken
from sqlalchemy import create_engine
import sqlalchemy
from datetime import datetime
import os


class MainClass:
    # The child directory class is needed to determine where the class is being called from.
    def __init__(self, config_file):
        with open(config_file, "r") as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        try:
            self.token_auth = config["AUTH"]["token_auth_header"]
            self.database_name = str(config["MYSQL_CONNECTION_DETAILS"]["DATABASE_NAME"])
            self.server_name = config["MYSQL_CONNECTION_DETAILS"]["SERVER_NAME"]
            self.sql_user = config["MYSQL_CONNECTION_DETAILS"]["LOGIN"]
            self.sql_password = config["MYSQL_CONNECTION_DETAILS"]["PASSWORD"]
            self.cookie = config["AUTH"]["cookie"]

            self.schema = "extract"
            #self.user = config["AUTH"]["username"]
            #self.password = config["AUTH"]["password"]
            self.environment = config["ENVIRONMENT"]["gore"]
            self.auth = config["AUTH"]["auth-header"]
            self.api_limit = config["API_CONFIG"]["limit"]
            self.connection_string = 'mssql+pyodbc://' + self.sql_user + ':' + url_quote(
                self.sql_password) + '@' + self.server_name + '/' + self.database_name + '?driver=SQL+Server+Native+Client+11.0'
            self.varchar_length = config["MYSQL_CONNECTION_DETAILS"]["VARCHAR_LENGTH"]
        except KeyError:
            print("The config file is incorrectly setup")
            os._exit(1)

        self.setup_database()
        # datetime object containing current date and time
        now = datetime.now()
        self.extraction_time = now.strftime("%d-%m-%Y %H:%M:%S")

        self.access_token = self.get_access_token()
        self.auth = "Bearer " + self.get_access_token()

        self.users_controller = self.setup_users_controller()
        self.asset_controller = self.setup_asset_controller()
        self.attribute_controller = self.setup_attribute_controller()
        self.attribute_type_controller = self.setup_attribute_type_controller()
        self.domain_controller = self.setup_domain_controller()
        self.community_controller = self.setup_communitiy_controller()
        self.relation_controller = self.setup_relation_controller()
        self.relation_type_controller = self.setup_relation_types_controller()
        self.responsibilities_controller = self.setup_responsibilities_controller()


        self.controller_list = [
            self.users_controller,
            self.asset_controller,
            self.domain_controller,
            self.community_controller,
            self.relation_controller,
            self.relation_type_controller,
            self.responsibilities_controller,
            self.attribute_type_controller,
            self.attribute_controller,
        ]

    def run(self):

        self.start_time = time.perf_counter()
        for controller in self.controller_list:
            temp_start_time = time.perf_counter()
            dataframe = controller.get_pandas_db()
            # dataframe.to_sql(
            # "collibra_" + controller.name + "_raw",
            # schema="extract",
            # con=self.engine,
            # chunksize=100,
            # method="multi",
            # index=False,
            # if_exists="replace",
            # )
            controller.write_to_sql()
            temp_end_time = time.perf_counter()
            temp_total_time = temp_end_time - temp_start_time
            print(
                str(controller.name) + " Dataframe:\nLoaded in " + str(temp_total_time)
            )

        end_time = time.perf_counter()
        print("Total Runtime: " + str(end_time - self.start_time))

    def get_access_token(self):
        access_token_class = AccessToken(self.token_auth)
        return access_token_class.get_bearer_token()

    def setup_database(self):
        # self.quoted = urllib.parse.quote(
        #     "driver={SQL Server};"
        #     "server=anvrdmexldv03;"
        #     "database=EXL_MDSDev;"
        #     "Trusted_Connection=yes;"
        # )
        # self.engine = create_engine(
        #     "mssql+pyodbc:///?odbc_connect={}".format(self.quoted)
        # )
        print("Using connection string: " + self.connection_string)
        self.engine = create_engine(self.connection_string)
        # self.engine=create_engine(driver='ODBC Driver 17 for SQL Server',
        #                                server=self.server_name,
        #                                database=self.database_name,
        #                                uid=self.sql_user,
        #                                pwd=quote(self.password),
        #                                trusted_connection="no"
        #                                )

        # engine = create_engine(
        #     'mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')

    def setup_responsibilities_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/responsibilities"
                                                "?limit=" + str(self.api_limit)
        )
        attribute_list = [
            "id",
            "resourceType",
            ["role", "id"],
            ["role", "name"],
            ["baseResource", "id"],
            ["baseResource", "resourceType"],
            ["owner", "id"],
            ["owner", "resourceType"],
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]

        column_names = {
            "Responsibility_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Role_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Role_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Base_Resource_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Base_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Owner_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Owner_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        responsibility_controller = GenericController(
            "responsibilities",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return responsibility_controller

    def setup_relation_controller(self):
        url = "https://" + self.environment + "/rest/2.0/relations" "?limit=" + str(
            self.api_limit
        )

        attribute_list = [
            "id",
            ["source", "id"],
            ["source", "name"],
            ["source", "resourceType"],
            ["target", "id"],
            ["target", "name"],
            ["target", "resourceType"],
            ["type", "id"],
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]

        column_names = {
            "Relation_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        relation_controller = GenericController(
            "relations",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return relation_controller

    def setup_relation_types_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/relationTypes?offset=0"
                                                "&limit=" + str(self.api_limit)
        )
        attribute_list = [
            "id",
            ["sourceType", "id"],
            ["sourceType", "name"],
            ["sourceType", "resourceType"],
            ["targetType", "id"],
            ["targetType", "name"],
            ["targetType", "resourceType"],
            "role",
            "coRole",
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        column_names = {
            "Relation_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Source_Type_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Target_Type_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Role": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Co_Role": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        relation_type_controller = GenericController(
            "relation_types",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return relation_type_controller

    def setup_domain_controller(self):
        url = (
                "https://"
                + self.environment
                + "/rest/2.0/domains"
                + "?offset=0"
                + "&limit=0&nameMatchMode=ANYWHERE"
        )
        domain_attribute_list = [
            "id",
            ["type", "id"],
            ["type", "resourceType"],
            ["type", "name"],
            ["community", "id"],
            ["community", "resourceType"],
            ["community", "name"],
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        domain_column_names = {
            "Domain_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Domain_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Domain_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Domain_ResourceType_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Community_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Community_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Community_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        domain_controller = GenericController(
            "domains",
            url,
            self.auth,
            self.cookie,
            domain_attribute_list,
            domain_column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return domain_controller

    def setup_communitiy_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/communities?offset=0"
                                                "&limit=" + str(self.api_limit)
        )

        attribute_list = [
            "id",
            "name",
            "resourceType",
            ["parent", "id"],
            ["parent", "resourceType"],
            ["parent", "name"],
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        community_column_names = {
            "Community_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Parent_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Parent_Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Parent_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        communityController = GenericController(
            "communities",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            community_column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return communityController

    def setup_asset_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/assets?offset=0"
                                                "&nameMatchMode=ANYWHERE&typeInheritance=true"
                                                "&excludeMeta=true&sortField=NAME"
                                                "&sortOrder=ASC"
                                                "&limit=" + str(self.api_limit)
        )

        attribute_list = [
            "id",
            "name",
            "displayName",
            ["status", "name"],
            ["type", "name"],
            ["domain", "name"],
            ["domain", "id"],
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        asset_column_names = {
            "Asset_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Display_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Status": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Asset_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Domain_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Domain_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        assetController = GenericController(
            "assets",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            asset_column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )

        return assetController

    def setup_attribute_controller(self):
        url = "https://" + self.environment + "/rest/2.0/attributes?" "limit=" + str(
            self.api_limit
        )

        attribute_list = [
            "id",
            "resourceType",
            ["type", "id"],
            ["type", "name"],
            ["asset", "id"],
            "value",
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        column_names = {
            "Attribute_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Attribute_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Attribute_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Parent_Asset_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Attribute_Value": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        attribute_controller = GenericController(
            "attributes",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return attribute_controller

    def setup_attribute_type_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/attributeTypes"
                                                "?limit=" + str(self.api_limit)
        )

        attribute_list = [
            "id",
            "name",
            "resourceType",
            "description",
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]
        column_names = {
            "Attribute_Type_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Attribute_Type_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Resource_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Attribute_Type_Description": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        attribute_type_controller = GenericController(
            "attribute_types",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name
        )
        return attribute_type_controller

    def setup_users_controller(self):
        url = (
                "https://" + self.environment + "/rest/2.0/users"
                                                "?limit=" + str(self.api_limit)
        )

        attribute_list = [
            "id",
            "userName",
            "firstName",
            "lastName",
            "emailAddress",
            "licenseType",
            "activated",
            "enabled",
            "createdOn",
            "lastModifiedOn",
            "createdBy",
            "lastModifiedBy"
        ]

        column_names = {
            "User_ID": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Username": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "First_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Name": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Email_Address": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "License_Type": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Activated": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Enabled": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Created_Date": sqlalchemy.types.DateTime(),
            "Last_Modified_Date": sqlalchemy.types.DateTime(),
            "Created_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Last_Modified_By": sqlalchemy.types.VARCHAR(length=self.varchar_length),
            "Extraction_Date": sqlalchemy.types.DateTime(),
        }
        users_controller = GenericController(
            "users",
            url,
            self.auth,
            self.cookie,
            attribute_list,
            column_names,
            self.extraction_time,
            self.engine,
            self.database_name

        )
        return users_controller


if __name__ == "__main__":
    # Run main class

    main = MainClass("../../prod_config.yml")
    main.run()
    # mainClass = MainClass("")
