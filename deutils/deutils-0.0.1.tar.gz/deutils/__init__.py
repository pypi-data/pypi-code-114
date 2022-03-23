import os
import json
from types import FunctionType
import boto3
import datetime
import shutil
from pyparsing import col
import snowflake.connector # pip install "snowflake-connector-python[pandas]"
import pandas as pd
import botocore
from io import BytesIO, StringIO, TextIOWrapper
import gzip
from botocore.client import Config
from sys import prefix
from google.cloud import storage # pip install google-api-python-client # pip install --upgrade google-cloud-storage
from google.oauth2 import service_account
from snowflake.connector.pandas_tools import write_pandas 
from sqlalchemy import create_engine # snowflake-sqlalchemy
from snowflake.sqlalchemy import URL 
import numpy as np
from multiprocessing.dummy import Pool
from messytables import CSVTableSet, type_guess, types_processor, headers_guess, headers_processor, offset_processor, any_tableset
import pandavro as pdx
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from pyspark import SQLContext
from pyspark.sql.functions import lit
import pyspark
import threading

def run_funct_multiprocess(funct,args:list(tuple()),args_count:int):
    """
    example:
    t1 = ['fdsfds','fsdfs']
    t2 = ['fdsfd','dfsdiofdsajfoisdf']
    run_funct_parallelly(funct=do_more_thing,args=[(t1,t2),(t2,t1)],args_count=2)
    run_funct_parallelly(funct=do_more_thing,args=[(t1),(t2)],args_count=1)
    https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments

    """
    with Pool() as pool:
        if args_count >= 2:
            pool.starmap(funct,args)
        else:
            pool.map(funct, args)
        pool.close()
        pool.join()

def run_funct_multithread(funct_list,arg_list):
    """
    example:
    t1 = ['fdsfds','fsdfs']
    t2 = {'fsdf':'fhyyjdsf','fdsf':'fdsfdsfsdfdsffsdfds'}
    run_funct_multithread(funct_list=[do_something_else,do_more_thing,do_something],arg_list=[[],[t1,t2],[5]])
    """
    for i in range(len(funct_list)):
        t = threading.Thread(target=funct_list[i],args=arg_list[i])
        t.start()
    t.join()

def convert_string_to_data_type_dict(dtype_string) -> dict:
    """
    example:
    dtype_string = ""SESSIONSTARTDATETIMEUTC	string SESSIONENDDATETIMEUTC	string SESSIONSTARTDATETIMESLT	string""
    print(convert_string_to_data_type_dict(dtype_string=dtype_string))
    output: {'SESSIONSTARTDATETIMEUTC': 'string', 'SESSIONENDDATETIMEUTC': 'string','SESSIONSTARTDATETIMESLT': 'string'}
    """
    string_list = dtype_string.split()
    
    data_type_dict = {}
    
    for index, dtype_string in enumerate(string_list):
        if index % 2 == 0:
            print(dtype_string)
            next_string = string_list[index+1]
            data_type_dict.update({dtype_string:next_string})

    return data_type_dict

def convert_data_type_dict_to_string(dtype_dict) -> str:
    """
    example:
    dtype_dict = {'SESSIONSTARTDATETIMEUTC': 'string', 'SESSIONENDDATETIMEUTC': 'string', 'SESSIONSTARTDATETIMESLT': 'string'}
    print(convert_data_type_dict_to_string(dtype_dict=dtype_dict))
    output: SESSIONSTARTDATETIMEUTC string ,SESSIONENDDATETIMEUTC string ,SESSIONSTARTDATETIMESLT string ,SESSIONENDDATETIMESLT string
    """
    dtype_str = ''
    for data, type in dtype_dict.items():
        dtype_str += f'{data} {type} ,'

    dtype_str = dtype_str.rstrip(',')

    return dtype_str

def data_type_mapper(dtype_dict: dict,map_to = 'snowflake' or 'pandas' or 'spark'):
    """
    example:
    dtype_dict = {'brand':'string','stationid':'int'}
    print(data_type_mapper(dtype_dict=dtype_dict,convert_to='spark'))
    output: {'brand': 'StringType()', 'stationid': 'IntegerType()'}
    """
    pandas    = {"string":"string", "int":"int64", "float":"float64", "bool":"bool", "JSON":"string","url":"string","date":"datetime64", "time":"datetime64[ns]","epoch":"int64"}
    spark     = {"string":"StringType()", "int":"IntegerType()", "float":"FloatType()", "bool":"BooleanType()", "JSON":"StringType()","url":"StringType()","date":"DateType()", "time":"TimestampType()","epoch":"LongType()"}
    snowflake = {"string":"VARCHAR", "int":"INTEGER", "float":"FLOAT", "bool":"BOOLEAN", "JSON":"VARCHAR","url":"VARCHAR","date":"DATE", "time":"TIMESTAMP","epoch":"INTEGER","timestamp":"timestamp"}

    if map_to == 'snowflake':
        map_to_dict = snowflake
    elif map_to == 'pandas':
        map_to_dict = pandas
    elif map_to == 'spark':
        map_to_dict = spark

    for data, type in dtype_dict.items():
        # if data type in specified dictionary then map, else use string
        if type in map_to_dict.keys():
            dtype_dict[data] = map_to_dict[type]
        else:
            dtype_dict[data] = map_to_dict['string']
    
    return dtype_dict

def pandas_data_type_recognition(df:pd.DataFrame):
    """
    example:
    schema_sf_lst = pandas_data_type_recognition(dataframe=df)
    df = fix_df(df)
    """

    # # get df data types # #
    # dataframe = pd.read_csv(file,nrows=nrows)
    df_dtype_dict = {}
    for col, data_type in df.dtypes.items():

        if len(df[col].value_counts()) == 0:
            print(col,'is empty')
            df_dtype_dict[col] = 'varchar(1)'
            continue

        if data_type == 'object':
            try:
                df[col] = pd.to_datetime(df[col])
                df_dtype_dict[col] = 'DATETIME'
                #print(f'successfully converted {col} to DATETIME')
                continue
            except:
                #print(f'failed converting {col} to DATETIME')
                pass
            try:
                df[col] = pd.to_numeric(df[col])
                df_dtype_dict[col] = 'INT'
                #print(f'successfully converted {col} to INT')
                continue
            except:
                #print(f'failed converting {col} to INT')
                pass
            try:
                col_max_len = int(df[col].str.len().max())
                df_dtype_dict[col] = f'varchar({col_max_len})'
            except:
                df_dtype_dict[col] = f'varchar(50)'
        else:
            df_dtype_dict[col] = data_type

    print('datafram_dtypes: ',df_dtype_dict,'\n')

    # # output data types string # #
    dtype_string = ''
    for col, data_type in df_dtype_dict.items():   
        dtype_string += str(col) + ' ' + str(data_type) + ','

    # match snowflake support data types
    dtype_string = dtype_string.upper().replace("BOOL",'BOOLEAN').replace('INT64','INT').replace('FLOAT64','FLOAT').replace('DATETIME64[NS]','DATETIME').rstrip(',')
    
    return dtype_string, df_dtype_dict

def pandas_default_data_type(df: pd.DataFrame, guess_data_type: bool =False, sample_size: str ='max') -> str:
    df = df.rename(str.upper, axis="columns")
    df.columns = df.columns.str.replace(" ", "_").str.replace('[^a-zA-z0-9_]', '', regex=True)
    
    if sample_size != 'max':
        df = df.sample(n=int(sample_size))

    # using dataframe default data types
    if guess_data_type:
        columns_string = ''
        for key, value in df.dtypes.items():
            columns_string += str(key) + ' ' + str(value) + ','
        columns_string = columns_string.replace('object', 'string').replace('bool','boolean').rstrip(',')  # replace object with string, and remove the last comma
        return columns_string
    else:
        # default use varchar for all columns
        df = df.astype(str)
        dataframe_cols = df.columns

        columns_string = ''

        for col in dataframe_cols:
            col_max_len = df[col].str.len().max()
            columns_string += col + f' varchar({col_max_len}),'
        
        columns_string = columns_string.rstrip(',')

        return columns_string

def fix_df(df: pd.DataFrame, fix_dates_col=True) -> pd.DataFrame:
    df = df.rename(str.upper, axis="columns")
    df.columns = df.columns.str.replace(" ", "_").str.replace('[^a-zA-z0-9_]', '',regex=True)
    if fix_dates_col:
        cols = df.select_dtypes(include=['datetime64[ns]','datetime']).columns
        for col in cols:
            df[col] = df[col].dt.tz_localize('UTC')

    return df

def convert_local_to_airflow_code(aws_secret_name, run_from_folder):
    # current_folder = str(os.path.dirname(os.path.abspath(__file__))).replace('\\','/')
    current_folder = str(run_from_folder).replace('\\','/')
    print('current_folder: ',current_folder)

    file_name = [i for i in os.listdir(current_folder) if 'local_dev.py' in i][0]
    print('file_name: ',file_name)

    local_dev_file = current_folder + '/' + file_name
    print('local_dev_file: ',local_dev_file)

    local_dev_copy_file = local_dev_file.replace('local_dev','local_dev_copy')
    print('local_dev_copy: ',local_dev_copy_file)

    shutil.copy(local_dev_file,local_dev_copy_file)

    airflow_etl_file_path = local_dev_copy_file.replace('local_dev_copy','airflow_etl')
    print('airflow_etl_file_path: ',airflow_etl_file_path)

    airflow_etl_file_name = airflow_etl_file_path.split('/')[-1].strip()
    print('airflow_etl_file_name: ',airflow_etl_file_name)

    try:
        open(airflow_etl_file_path,'x')
        print('airflow_etl_file_path created')
    except:
        print('airflow_etl_file_path already exists')
        pass

    variables = {}
    dag = ["""with DAG(dag_id=os.path.basename(__file__).replace(".py", ""), start_date=days_ago(1),schedule_interval="0 08 * * *") as dag:\n"""]
    pipelines = []

    airflow_packages = """from airflow import DAG
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import slack
import json
import os
"""

    alert_string = """
def on_failure_callback(context):
    channel_name = '#etl-status-slack-notification'
    ti = context['task_instance']
    status_message = f"task: {ti.task_id } failed in dag: { ti.dag_id } "
    print(status_message)
    client = slack.WebClient(token=slack_token)
    client.chat_postMessage(channel=channel_name,text=status_message)
"""

    secret_manager_string = """
def read_from_aws_sm_fn(sm_secretId_name):
    # get Secrets Manager credentials
    hook = AwsBaseHook(client_type='secretsmanager')
    client = hook.get_client_type('secretsmanager')
    response = client.get_secret_value(SecretId=sm_secretId_name)
    myConnSecretString = response["SecretString"]
    ConnSecretString = json.loads(myConnSecretString)
    return ConnSecretString
"""

    file  = open(local_dev_copy_file,'r').read()
    if 'read_from_aws_sm_fn' in file:
        secret_manager = True
    else:
        secret_manager = False

    if 'on_failure_callback' in file:
        alert = True
    else:
        alert = False

    with open(local_dev_copy_file,'r') as local,open(airflow_etl_file_path,'r+') as airflow:
        local.seek(0)
        airflow.seek(0)
        airflow.truncate()
        airflow.write(airflow_packages)
        lines = local.readlines()
        for line in lines: 
            # # write secret manager to airflow file
            if len(line) < 2 and secret_manager == False:
                airflow.write(secret_manager_string)
                airflow.write(f"\ncredentials = read_from_aws_sm_fn(sm_secretId_name='{aws_secret_name}')\n")
                secret_manager = True
            
            # # write slack alert to airflow file
            if len(line) <2 and alert == False:
                airflow.write(alert_string)
                alert = True

            # # write variables to file, and store variables in dict for aws secret manager terraform file
            # if not line.startswith(' ') and '=' in line and 'def' not in line and '[' not in line and '{' not in line and (("'" in line) or ('"' in line)):
            # if not line.startswith(' ') and '=' in line and (("'" in line) or ('"' in line)) and any(value not in line for value in ['def', '[', '{']) :
            if 'airflow_variable' in line:
                line = line.split('#')[0]
                variable = line.split('=')[0].rstrip()
                value = line.split('=')[1].strip()
                variables.update({variable:value})
                secret_manager_variable = f"credentials['{variable}']"
                line = f'{variable}={secret_manager_variable}\n'

            # # get airflow functions
            # if not line.startswith((' ','def')) and '(' in line: 
            if 'airflow_function' in line:
                print('running functions: ', line)

                # # get running function name
                function = line.split('(')[0].strip()

                # # insert to pipelines : function >> function >> function
                pipelines.append(function)

                # # if dag has arguments, then dags op_kwargs={'name':'good'},
                args = line[line.find("(")+1:line.rfind(")")] # get text between first open bracket and last clos bracket
                if args:
                    args_list = args.split(',')
                    # op_kwargs = {}
                    for arg in args_list:
                        arg = arg.split('=')
                        print('arg: ',arg)
                        param = arg[0]
                        input = arg[1]
                        # op_kwargs.update({param:input})
                    task = f"""\t{function} = PythonOperator(task_id="{function}",python_callable={function},op_kwargs={{'{param}':{input}}},provide_context=True,on_failure_callback = on_failure_callback)\n"""
                else:
                    task = f"""\t{function} = PythonOperator(task_id="{function}",python_callable={function},provide_context=True,on_failure_callback = on_failure_callback)\n"""
                dag.append(task)
                line = ''
            airflow.write(line)

        # # write tasks to airflow file:  task1 = PythonOperator(task_id=function) ...
        for task in dag:
            if dag.index(task) == len(dag)-1:
                task = str(task).rstrip().rstrip(',') + '\n'
            airflow.write(task)

        # write pipelines to airflow: function >> function >> function
        pipelines_flow = '\t' + ' >> '.join(pipelines)
        airflow.write(pipelines_flow)

    print('variables: ',variables)
    print('dag: ',dag)
    print('piplines (also functions): ',pipelines)
    print('\nwrote to airflow_etl_file_path')

    # # upload to s3
    to_s3_cmd = f"aws s3 cp {airflow_etl_file_path} s3://audacy-airflow-dev/dags/{airflow_etl_file_name}"
    os.system(to_s3_cmd)
    print('loaded to s3')

    # # create secret manager secrets if not exists
    aws_copy_tf = r"C:\Users\ALi\Desktop\code\main_etl\terraform\aws_copy.tf"
    check_aws_secret_name_exists = open(aws_copy_tf,'r').read()
    if aws_secret_name in check_aws_secret_name_exists:
        print(f'aws_secret_name: {aws_secret_name} found in docker-compose_copy.yml')
    else:
        print(f'aws_secret_name: {aws_secret_name} not found in docker-compose_copy.yml -> updating aws_copy.tf')
        with open(aws_copy_tf,'a') as file:

            # start creating aws secret manager string and write to terraform aws_copy.tf
            tf_secret_name = aws_secret_name.split('/')[-1]
            secret_manager_variables = ''

            for variable, value in variables.items():
                variable = f'"{variable}"'
                value = value.replace("'",'')
                value = f'"{value}"'
                secret_manager_variables += variable + ':' + value + ',\n'

            secret_manager_variables = secret_manager_variables.strip().rstrip(',')

            secret_manager_string = f"""
resource "aws_secretsmanager_secret" "aws_secretsmanager_secret_{tf_secret_name}" {{ 
name = "{aws_secret_name}"
}}
\n
resource "aws_secretsmanager_secret_version" "aws_secretsmanager_secret_version_{tf_secret_name}" {{
secret_id     = aws_secretsmanager_secret.aws_secretsmanager_secret_{tf_secret_name}.id
secret_string = <<-EOF
{{
{secret_manager_variables}
}}
    EOF
}}
"""
            file.write(secret_manager_string)
            file.close()
            print('updated aws_copy.tf')

            secret_manager_cmd = "docker-compose -f C:/Users/ALi/Desktop/code/main_etl/terraform/docker-compose_copy.yml run --rm terraform apply" # -auto-approve
            os.system(secret_manager_cmd)

class GoogleCloud:
    def __init__(self,google_cloud_json_credentials) -> None:
        credentials = service_account.Credentials.from_service_account_info(google_cloud_json_credentials)
        project = google_cloud_json_credentials['project_id']
        self.storage_client = storage.Client(project=project,credentials=credentials)
        
    def list_gc_bucket_files(self, gc_bucket_name, prefix=None, search_word_in_file_name=None):

        # if want to check out what else in the bucket, then remove prefix param
        files = self.storage_client.list_blobs(gc_bucket_name,prefix=prefix)

        # all install overview files
        if search_word_in_file_name:
            historical_files = [file.name for file in files if search_word_in_file_name in file.name]
            return historical_files

        return files

    def get_gc_file_content(self, gc_bucket_name,file_name,file_type=None):
        bucket = self.storage_client.bucket(gc_bucket_name)
        if file_type:
            if file_type == 'gz':
                blob = bucket.get_blob(file_name)
                data = BytesIO(blob.download_as_string())
                data.seek(0)
                return data
 
        else:
            blob = bucket.blob(file_name)
            content = blob.download_as_text()
            return content


class Aws:
    def __init__(self, aws_access_key,aws_secret_key) -> None:
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.s3_client = boto3.client('s3',aws_access_key_id=self.aws_access_key,aws_secret_access_key=self.aws_secret_key)

    def list_s3_bucket_files(self,s3_bucket: str,prefix: str=None,remove_text_from_file_name: str=False) -> list: # prefix is folder name
        
        if prefix:
            # all files in the the specified(prefix) folder
            bucket_files = self.s3_client.list_objects(Bucket=s3_bucket,Prefix=prefix)['Contents']
            
            # to remove certain text from the file names before returning the file list
            if remove_text_from_file_name:
                files = [bucket_file.get('Key').replace(remove_text_from_file_name,'') for bucket_file in bucket_files]
                return files
            
            # if not remove text from file name then return all files in the specified folder
            files = [bucket_file.get('Key') for bucket_file in bucket_files]
            return files

        # to get all files in the bucket
        all_files = [bucket_file.get('Key') for bucket_file in self.s3_client.list_objects(Bucket=s3_bucket)['Contents']]
        return all_files

    def list_s3_folders(self,s3_bucket,prefix):
        responses = self.s3_client. list_objects(Bucket=s3_bucket,Prefix=prefix,Delimiter='/')
        s3_folders = [response.get('Prefix') for response in responses.get('CommonPrefixes')]
        return s3_folders

    def get_latest_file_in_s3(self,s3_bucket: str, prefix: str=None):

        get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
        if prefix:
            bucket_files = self.s3_client.list_objects(Bucket=s3_bucket,Prefix=prefix)['Contents']
        else:
            bucket_files = self.s3_client.list_objects_v2(Bucket=s3_bucket)['Contents']
        last_added_file = max(bucket_files, key=lambda x: x['LastModified'])
        return last_added_file    


    def write_string_to_s3(self, file_name: str, string: str or None,s3_bucket:str):
        # self.s3_client.put_object(Bucket=s3_bucket,Key=file_name,Body=string) # key is the file name without the bucket name ex: google-play-store/stats/installs/your_file.csv
        
        string = BytesIO(string.encode())
        self.s3_client.upload_fileobj(string,Bucket=s3_bucket,Key=file_name)

        # the fastest way to upload local csv/txt to s3
    def write_local_file_to_s3(self, local_file_path: str, s3_bucket:str, s3_file_name:str): 
        file_content = open(local_file_path,'rb')
        self.s3_client.upload_fileobj(file_content,Bucket=s3_bucket,Key=s3_file_name)

        # fastest way to upload a dataframe to s3
    def write_dataframe_to_s3_by_bytesio(self,dataframe: pd.DataFrame, s3_bucket:str, s3_file_name:str,compression=None):
        # example: aws.write_dataframe_to_s3_by_bytesio(dataframe=df,s3_bucket=s3_bucket,s3_file_name=prefix+'test.csv.gz',compression='gzip')
        csv_buffer = BytesIO()
        if compression:
            dataframe.to_csv(csv_buffer,index=False,mode='wb',encoding='utf-8',compression=compression)
        else:
            dataframe.to_csv(csv_buffer,index=False,mode='wb',encoding='utf-8')
        csv_buffer.seek(0)
        self.s3_client.upload_fileobj(csv_buffer,Bucket=s3_bucket,Key=s3_file_name)

    def write_dataframe_to_s3_by_stringio(self,dataframe: pd.DataFrame, s3_bucket:str, s3_file_name:str):
        csv_buffer= StringIO()
        dataframe.to_csv(csv_buffer,index=False)
        self.s3_client.put_object(Bucket=s3_bucket,Key=s3_file_name,Body=csv_buffer.getvalue())

    def read_S3_file_content(self, s3_bucket: str, file_name: str) -> botocore.response.StreamingBody:
        response = self.s3_client.get_object(Bucket=s3_bucket, Key=file_name)
        status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
        if status == 200:
            # to see file content do: reponse.get('Body').read().decode()
            content = response.get("Body") 
            return content

        return f"Unsuccessful S3 get_object response. Status - {status}"

    def read_S3_file_content_into_dataframe(self, s3_bucket: str, file_name: str,chunksize=100000):
        # fastest way to read s3 file into pandas dataframe
        # 36 secs for 300 MB 
        data = self.read_S3_file_content(s3_bucket=s3_bucket,file_name=file_name)
        if chunksize:
            chunks = pd.read_csv(data,chunksize=chunksize)
            df = pd.concat(chunks)
        else:
            df = pd.read_csv(data)

        return df

    def read_S3_file_into_dataframe_by_s3fs(self,s3_bucket,prefix): 
        # need: pip install s3fs
        # 51.57 secs for 300 MB
        df = pd.read_csv(f's3://{s3_bucket}/{prefix}')
        return df

    def read_S3_file_into_dataframe_by_bytesio(self,s3_bucket,prefix):
        # 42.95 secs for 300 MB
        data = self.read_S3_file_content(s3_bucket=s3_bucket,file_name=prefix).read()
        bytes_file = BytesIO(data)
        df = pd.read_csv(bytes_file)
        return df

    def write_dataframe_to_s3_by_s3fs(self,df,s3_bucket,prefix):
        # need: pip install s3fs
        save_to =f's3://{s3_bucket}/{prefix}'
        df.to_csv(save_to)
        print(f'data has been uploaded to {save_to}')

class Snowflake:
    def __init__(self,snow_user,snow_password,snow_account, snow_warehouse,snow_database,snow_schema) -> None:
        self.snow_user = snow_user
        self.snow_password = snow_password
        self.snow_account = snow_account
        self.snow_warehouse = snow_warehouse
        self.snow_database = snow_database
        self.snow_schema = snow_schema
        self.con  = snowflake.connector.connect(user=snow_user,password=snow_password,account=snow_account,warehouse=snow_warehouse,database=snow_database,schema=snow_schema)

    def fix_df(self, df: pd.DataFrame, fix_dates_col=True) -> pd.DataFrame:
        df = df.rename(str.upper, axis="columns")
        df.columns = df.columns.str.replace(" ", "_").str.replace('[^a-zA-z0-9_]', '',regex=True)
        if fix_dates_col:
            cols = df.select_dtypes(include=['datetime64[ns]','datetime']).columns
            for col in cols:
                df[col] = df[col].dt.tz_localize('UTC')

        return df

    def execute_query(self,query:str):
        cursor = self.con.cursor()
        cursor.execute(query)
        cursor.close()

    def list_snowflake_loaded(self, snow_table:str) -> list:
        curs=self.con.cursor()
        snow_table = snow_table.upper()

        # get pre loaded (existing) files for specified table 
        try:
            contents = curs.execute("select S3_FILE_NAME from LOAD_STATUS where table_name='" + snow_table + "'").fetchall()
        except:
            contents = curs.execute("select FILE_NAME from LOAD_STATUS where table_name='" + snow_table + "'").fetchall()

        sf_files = [content[0] for content in contents]

        return sf_files
    
    def list_snowflake_dates(self,snow_table:str ,date_field:str, search_date_list: list=None) -> list:
        curs=self.con.cursor()

        date_field = date_field.upper().replace('-','_')
        snow_table = snow_table.upper().replace('-','_')

        if search_date_list:
            dates = ', '.join(f"'{date}'" for date in search_date_list)

            contents = curs.execute(f"select {date_field} from {snow_table} where {date_field} in ({dates}) ")
        else:
            contents = curs.execute(f"select {date_field} from {snow_table}")

        snowflake_dates = [content[0] for content in contents]
        return snowflake_dates
            
    def create_table(self, snow_database: str, snow_schema:str ,snow_table: str, dtype_str:str) -> None:
        try:
            sql_create_table = f"CREATE TABLE IF NOT EXISTS {snow_database}.{snow_schema}.{snow_table} ({dtype_str})"
            cur = self.con.cursor()
            cur.execute(sql_create_table)
            cur.close()
        except Exception as e:
            raise e

        print(f'database: {snow_database}, schema:{snow_schema}, table_name:{snow_table} has been created \n')
        return None

    def create_load_status_table(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "+ self.snow_database +"."+ self.snow_schema +"."+"LOAD_STATUS"+" (LOAD_DATE VARCHAR(100), SCHEMA_NAME VARCHAR(100), TABLE_NAME VARCHAR(100), S3_FILE_NAME TEXT)")
        cur.close()

    def update_load_status_table(self,snow_table:str,file_name:str):
        LOAD_DATE = str(datetime.datetime.now())
        cur = self.con.cursor()
        try:
            cur.execute("INSERT into LOAD_STATUS (LOAD_DATE, SCHEMA_NAME, TABLE_NAME, S3_FILE_NAME)VALUES('"+ LOAD_DATE+"', '"+self.snow_schema+"', '"+snow_table+"', '"+file_name+"' )")
        except:
            cur.execute("INSERT into LOAD_STATUS (LOAD_DATE, SCHEMA_NAME, TABLE_NAME, FILE_NAME)VALUES('"+ LOAD_DATE+"', '"+self.snow_schema+"', '"+snow_table+"', '"+file_name+"' )")
        cur.close()

    def get_data_in_dataframe(self,query:str) -> pd.DataFrame:
        cur = self.con.cursor()
        execute_query = cur.execute(query)
        data = cur.fetch_pandas_all()
        cur.close()
        return data
    
    def delete_data(self,s3_file_names: list, snow_tables: list):
        cur = self.con.cursor()
        s3_file_names = str(s3_file_names).replace('[','').replace(']','')
        for snow_table in snow_tables:
            try:
                cur.execute(f"""delete from "{self.snow_database}"."{self.snow_schema}"."{snow_table}" where S3_FILE_NAME in ({s3_file_names}) """)
            except:
                cur.execute(f"""delete from "{self.snow_database}"."{self.snow_schema}"."{snow_table}" where FILE_NAME in ({s3_file_names}) """)
        cur.close()

    def get_current_snowflake_col_info(self, snow_table, col_info_type = 'raw_data') -> dict:
        data_types = self.con.cursor().execute(f'show columns in {self.snow_database}.{self.snow_schema}.{snow_table};').fetchall()

        if col_info_type == 'raw_data':
            return data_types

        if col_info_type == 'columns': # -> ['column one','column two']
            cur_cols = []
            for data_type in data_types:
                column_name = data_type[2]
                # get current snowflake column names
                cur_cols.append(column_name)
            return cur_cols

        dtypes_dict = {}

        if col_info_type == 'all': # -> {column name:column type}
            for data_type in data_types:
                data_info = json.loads(data_type[3])
                column_name = data_type[2]
                column_type = data_info['type']
                dtypes_dict.update({column_name:column_type})
            return dtypes_dict

        if col_info_type =='TEXT': # ->  {text column: text length}
            for data_type in data_types:
                data_info = json.loads(data_type[3])
                if data_info['type']=='TEXT':
                    varchar_column_name = data_type[2]
                    current_varchar_column_length = data_info['length']
                    dtypes_dict.update({varchar_column_name:current_varchar_column_length})
            return dtypes_dict
        
        return dtypes_dict

    # date_field is if the data update in the same csv file in s3, and like the google play store data, then we need to specify date field in order to get new data
    def write_pandas_into_snowflake(self,df: pd.DataFrame,snow_table: str, update_load_status_table:bool = True, file_name:str = None, check_new_col:bool = False, check_varchar_size = False) -> None:
        """
        example:
        aws = Aws(aws_access_key=aws_access_key,aws_secret_key=aws_secret_key)
        file = aws.read_S3_file_content(s3_bucket=s3_bucket,file_name=file_name)
        df = pd.read_csv(file)
        schema_sf_lst = get_sf_col_type_from_dataframe(dataframe=df) 
        sf = Snowflake(snow_user=snow_user,snow_password=snow_password,snow_account = snow_account,snow_warehouse = snow_warehouse,snow_database = snow_database,snow_schema = snow_schema)
        sf.create_table(snow_database=snow_database,snow_schema=snow_schema,snow_table=snow_table,schema_sf_lst=schema_sf_lst)
        sf.write_pandas_into_snowflake(df=df,snow_table=snow_table,file_name=file_name)
        """

        snow_table = snow_table.upper()
        df = self.fix_df(df)

        if check_new_col:
            cur_cols = self.get_current_snowflake_col_info(snow_table=snow_table, col_info_type='columns')
            df_cols = df.columns

            new_cols = list(set(df_cols).difference(set(cur_cols)))
            
            # if there is new column , then recognize the data type and add the column into snowflake
            if new_cols:
                print('new_cols: ',new_cols)
                new_cols_df = df[new_cols]
                new_cols_dtypes_string, new_col_dtypes_dict = pandas_data_type_recognition(new_cols_df)
                for new_col in new_cols:
                    new_dtype = new_col_dtypes_dict[new_col]
                    add_col_query = f"alter table {self.snow_database}.{self.snow_schema}.{snow_table} add column {new_col} {new_dtype}"
                    self.execute_query(add_col_query)

        if check_varchar_size:
            # only for text column: if dataframe text column length greater than snowflake varchar length, then change table varchar length 
            varchar_cols_dict = self.get_current_snowflake_col_info(snow_table=snow_table,col_info_type='TEXT')
            for varchar_column_name, current_varchar_column_length in varchar_cols_dict.items():
                column_max_length = df[varchar_column_name].astype(str).str.len().max()
                if column_max_length > current_varchar_column_length:
                    query = f"alter table {snow_table} alter {varchar_column_name} set data type varchar({column_max_length});"
                    self.execute_query(query)

        try:
            write_pandas(conn=self.con, df=df, table_name=snow_table)
        except:
            engine = create_engine(URL(account = self.snow_account,user = self.snow_user,password = self.snow_password,database = self.snow_database,schema = self.snow_schema,warehouse = self.snow_warehouse))
            connection = engine.connect()
            df.to_sql(snow_table,con=connection,index=False,if_exists='append',method='multi',chunksize=100000)
            connection.close()
            engine.dispose()

        if update_load_status_table:
            if file_name:
                self.update_load_status_table(snow_table=snow_table,file_name=file_name)
                print(f"{file_name} loaded to {snow_table}:  updated load_status table \n --- --- ---")
                return None
            else:
                return 'need to give file name'
        else:
            print(f"{file_name} loaded to {snow_table}:  not updating load_status_table \n --- --- ---")

        return None

    def copy_s3_to_snowflake(self,columns_len: int,s3_bucket, s3_files, snow_table:str, aws_access_key:str, aws_secret_key:str, role:str=None, file_format:str=None,stage=None):
        # """
        # mainly use for etl: if using admin account, should specifiy role and stage otherwise will create default role and stage for you based on your username
        # if using for etl purpose, then no need to specify role and stage
        # """

        columns_str = '' # get column count ex: $1,$2,$3,$4,$5,$6...
        for i in range(1,columns_len-1): # minus one is to match the total columns count
            columns_str += f'${i},' 
        
        if file_format: 
            file_format_cmd = ""
        else:
            file_format_cmd = f"""create or replace file format {self.snow_user}_csvformat type = 'CSV' field_delimiter=',' skip_header =1, FIELD_OPTIONALLY_ENCLOSED_BY='"'; """
            file_format = file_format_cmd.split()[file_format_cmd.split().index('format')+1] # find the word after format

        if not role:
            role = f'RL_{self.snow_user}' # use default role

        if not stage:
            stage = f"{self.snow_user}_STAGE" # create default stage
            

        commands = [f'use role {role};',f'use database {self.snow_database};',f'use warehouse {self.snow_warehouse};',f'use schema {self.snow_schema};',
            file_format_cmd,
            f"""create stage if not exists {stage} url='s3://{s3_bucket}' """,
            ]
        
        for command in commands:
            self.execute_query(command)
        
        for s3_file in s3_files:
            cp_cmd = f"""
                copy into {snow_table}
                from (select {columns_str} metadata$filename, current_timestamp() from '@{stage}/{s3_file}')
                credentials=(aws_key_id='{aws_access_key}' aws_secret_key='{aws_secret_key}')   file_format={file_format};
                """
            print(cp_cmd)
            self.execute_query(cp_cmd)
            self.update_load_status_table(snow_table=snow_table,file_name=s3_file)
            print(f'{s3_file} loaded to snowflake and updated load status table')

    def create_user_and_role_for_etl(self,etl_user, etl_role, snow_table):
        # George's command
        # etl_user format: TRITON_PODCAST_ETL -> should be stored in secrets manager as snow_user
        # etl_role format: RL_TRITON_PODCAST_ETL
        commands = [
        """use role securityadmin;""",
        f"""create role if not exists {etl_role} comment = 'This role has all privileges on {snow_table}, purpose is Dataload';""",
        f"""grant all on schema "{self.snow_database}"."{self.snow_schema}" to role {etl_role};""",
        f"""create user {etl_user} password = '{self.snow_password}' default_role = {etl_role};""",
        f"""grant role {etl_role} to user {etl_user};""",
        f"""grant role {etl_role} to user WLI;""",
        f"""grant usage on database "{self.snow_database}" to role {etl_role};""",
        f"""grant usage on schema "{self.snow_database}"."{self.snow_schema}" to role {etl_role};""",
        f"""grant select,insert,delete,update on all tables in schema "{self.snow_database}"."{self.snow_schema}" to role {etl_role};""",
        f"""grant select,insert,delete,update on future tables in schema "{self.snow_database}"."{self.snow_schema}" to role {etl_role};""",
        f"""grant select on all tables in schema "{self.snow_database}"."{self.snow_schema}" to role sysadmin;""",
        f"""grant select on future tables in schema "{self.snow_database}"."{self.snow_schema}" to role sysadmin;""",
                   ]
        for command in commands:
            self.execute_query(command)

class Avro:
    def df_to_avro(source_file,dest_file):
        df = pd.read_csv(source_file)
        pdx.to_avro(dest_file, df)

    def read_avro_into_df(avro_file):
        df = pdx.from_avro(avro_file)
        return df

class Aws_Pyspark_Snowflake(Aws,Snowflake):
    """
    pyspark version: 3.2.1
    check spark.jars.packages here:
    https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-aws org.apache.hadoop:hadoop-aws:3.3.1
    https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-common org.apache.hadoop:hadoop-common:3.3.1
    
    pyspark version: 3.2.1
    to use pyspark with snowflake need to install the compatible two jars from the following first two links:
    https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/ 
    https://search.maven.org/search?q=a:spark-snowflake_2.12
    or use maven
    https://mvnrepository.com/artifact/net.snowflake/spark-snowflake net.snowflake:spark-snowflake_2.12:2.10.0-spark_3.1
    https://mvnrepository.com/artifact/net.snowflake/snowflake-jdbc net.snowflake:snowflake-jdbc:3.13.14

    spark avro maven:https://mvnrepository.com/artifact/org.apache.spark/spark-avro
    
    spark_df.Collect (Action) - Return all the elements of the dataset as an array at the driver program. 
    This is usually useful after a filter or other operation that returns a sufficiently small subset of the data.
    
    """
    def __init__(self,aws_access_key,aws_secret_key,snow_user,snow_password,snow_account,snow_database,snow_schema,snow_url,snow_warehouse) -> None:
        Aws.__init__(self,aws_access_key=aws_access_key,aws_secret_key=aws_secret_key)
        Snowflake.__init__(self,snow_user=snow_user,snow_password=snow_password,snow_account=snow_account,
                    snow_database=snow_database,snow_schema=snow_schema,snow_warehouse=snow_warehouse)

        # company_name.us-east-1.snowflakecomputing.com ()
        self.snow_url = snow_url 

        # initialize spark session
        # make large or repeated queries on the same dataframe run faster
        # when caching dataframe, spark groups records in batches of the size given and compresses each batch (if over 100 fields, pick up smaller size)
        self.spark = SparkSession.builder\
        .config('spark.master','local')\
        .config('spark.app.name','Aws_Pyspark_Snowflake')\
        .config('spark.jars.packages','org.apache.hadoop:hadoop-aws:3.3.1,org.apache.hadoop:hadoop-common:3.3.1,net.snowflake:snowflake-jdbc:3.13.14,net.snowflake:spark-snowflake_2.12:2.10.0-spark_3.1,org.apache.spark:spark-avro_2.12:3.2.1')\
        .getOrCreate()
        
        # aws configuration
        self.sc = self.spark.sparkContext
        self.sc._jsc.hadoopConfiguration().set('fs.s3a.access.key', aws_access_key)
        self.sc._jsc.hadoopConfiguration().set('fs.s3a.secret.key', aws_secret_key)
        
        # snowflake configuration
        self.SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"
        self.snowflake_options = {
        "sfUrl": self.snow_url,
        "sfUser": self.snow_user,
        "sfPassword": self.snow_password,
        "sfDatabase": self.snow_database,
        "sfSchema": self.snow_schema,
        "sfWarehouse": self.snow_warehouse}
    
    def config_avro_compression(self,compression='snappy'):
        # compression configuration for avro file (default is snappy): bzip2, deflate, uncompressed, xz, snappy, zstandard
        self.spark.conf.set("spark.sql.avro.compression.codec", compression) 
    
    def config_parquet_compression(self,compression='snappy'):
        # compression configuration for parquet file (default is snappy): gzip,snappy,uncompressed,brotli,lzo,lz4
        self.spark.conf.set("spark.sql.parquet.compression.codec",compression)
    
    def create_parallel_rdd(self,data):
        """
        example:
        data = []
        for idx, query_id in enumerate(query_ids):
            url = f'{triton_url}{query_id}/?start={start}&endBefore={endBefore}'
            temp_data = primary_api_call(url=url, user=triton_user, pw=triton_pw)
            print(temp_data)
            data += temp_data
        spark_rdd = aws_pyspark_snowflake.sc.parallelize(data).toDF()
        """
        spark_rdd = self.sc.parallelize(data).toDF()
        return spark_rdd
        
    def create_spark_dataframe(self,data):
        """
        example:
        for idx, query_id in enumerate(query_ids):
            url = f'{triton_url}{query_id}/?start={start}&endBefore={endBefore}'
            data = primary_api_call(url=url, user=triton_user, pw=triton_pw)
            if idx == 0:
                # # first run creates spark_df, then second run onwards, create temp_df and union spark_df with temp_df
                spark_df = aws_pyspark_snowflake.spark.createDataFrame(data=data)
            else:
                temp_df = aws_pyspark_snowflake.spark.createDataFrame(data=data)
                spark_df = spark_df.unionAll(temp_df)
        """
        
        df = self.spark.createDataFrame(data=data)
        return df
    
    def add_new_col(self,spark_df, col_name, col_value):
        spark_df = spark_df.withColumn(col_name,lit(col_value))
        return spark_df
    
    def run_query_on_spark_df(self,spark_df,temp_view,query):
        self.spark.catalog.dropTempView(temp_view)
        spark_df.createTempView(temp_view)
        spark_df = self.spark.sql(query)
        self.spark.catalog.dropTempView(temp_view)
        return spark_df
    
    def fix_spark_df(self,spark_df):
        NewColumns=(column.strip().replace(' ', '_').replace('(','').replace(')','') for column in spark_df.columns)
        spark_df = spark_df.toDF(*NewColumns)
        return spark_df
        
    def get_files_from_local_path(self,path_to_dir, suffix=".csv" ):
        filenames = os.listdir(path_to_dir)
        return [ path_to_dir + filename for filename in filenames if filename.endswith( suffix ) ]
        
    def read_s3_file_into_spark_df(self,s3_bucket,s3_file,format='csv'):
        spark_df = self.spark.read.format(format).option('header',True).load(f"s3a://{s3_bucket}/{s3_file}")

        return spark_df
    
    def read_s3_files_into_spark_df(self,s3_bucket,s3_folder,format='csv'):
        spark_df = self.spark.read.format(format).option('header',True).load(f"s3a://{s3_bucket}/{s3_folder}")

        return spark_df
    
    def read_local_file_into_spark_df(self,file, format='csv'):
        if format == 'csv':
            spark_df = self.spark.read.options(inferSchema='True',delimiter=',').option('header',True).csv(file)
        else:
            spark_df = self.spark.read.format(format).load(file)
            
        return spark_df
    
    def read_local_files_into_spark_df(self,file_list,format='csv'):
        """
        example:
        file_list = get_files_from_local_path(path_to_dir='triton_podcast_2021-11-01/',suffix='.avro')
        avro_spark_df = aws_pyspark_snowflake.read_local_files_into_spark_df(file_list=file_list,format='avro')
        avro_spark_df.show()
        """
        if format == 'csv':
            spark_df = self.spark.read.options(inferSchema='True',delimiter=',').option('header',True).csv(file_list)
        else:
            spark_df = self.spark.read.format(format).load(file_list)
            
        return spark_df
        
    def write_spark_df_to_local(self,spark_df,local_path,format='csv',partition_by=None):
        if partition_by:
            spark_df.write.format(format).partitionBy(partition_by).save(local_path)
        else:
            spark_df.write.format(format).save(local_path)
    
    def write_spark_df_to_s3(self,spark_df,s3_bucket,folder,format='csv',mode='append',partition_by=None):
        if partition_by:
            spark_df.write.format(format).option('header',True).partitionBy(partition_by).save(f's3a://{s3_bucket}/{folder}',mode=mode)
        else:
            # df.write.format('csv').option('header',True).save('s3a://s3_bucket/path/to/folder',mode='overwrite')
            spark_df.write.format(format).option('header',True).save(f's3a://{s3_bucket}/{folder}',mode=mode)

    def write_spark_df_to_snowflake(self,spark_df,snow_table,mode="append"):
        spark_df.write.format("snowflake") \
        .options(**self.snowflake_options) \
        .option("dbtable", snow_table).mode(mode).options(header=True) \
        .save()  
    
    def get_snowflake_data_into_spark_dataframe(self,query):
        df = self.spark.read.format(self.SNOWFLAKE_SOURCE_NAME).options(**self.snowflake_options).option('query',query).load()
        return df

