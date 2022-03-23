import re
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, Integer
import psycopg2
import time
import psutil

def Check_list(df, df_list, page):

    # Check if there is a column containing 'list' in the item name
    df_columns_list = []
    for i in range(len(df.columns)): 
        if 'list' in df.columns[i]:
            df_columns_list.append(df.columns[i])
    # If an item name including 'list' exists
    if df_columns_list:    
        
        di = df[df_columns_list].reset_index(drop=True)
        df1 = pd.DataFrame([di[df_columns_list[i]] for i in range(len(df_columns_list))])
        df1 = df1.T
        ## Fill with NaN data None
        df1 = df1.fillna(np.nan).replace([np.nan], [None])
        
        # Unpacking the data of items in a list
        unpakaged_list = []
        list_name = []
        
        for i in range(len(df1.columns)):
            seq = page
            for v in range(len(df1[df1.columns[i]])):
                # Data with 'list' in the item name is labeled and indexed by the data list name and order in the unpacked list
                if df1[df1.columns[i]][v] != None :
                    # Combined into a list of Json type data bound in the list column
                    df[df1.columns[i]][v] = df1.columns[i] + '_' + str(seq)
                
                    for t in range(len(df1[df1.columns[i]][v])):
                        list_name.append(df1.columns[i]+ '_' +str(seq))
                        unpakaged_list.append(df1[df1.columns[i]][v][t])
                    seq += 1
        # Change to DataFrame with Listed Data                
        df2 = pd.DataFrame(unpakaged_list, index = list_name)
        df_list.append(df.fillna(np.nan).replace([np.nan], [None]))
        return Check_list(df2, df_list, page + len(df2))
    else :
        return df_list.append(df.fillna(np.nan).replace([np.nan], [None]))
    

# Set target_Data item alias/anonymization
def anonymization(df_list, target_data):
    
    for i in range(len(df_list)):

        for v in range(len(df_list[i].columns)):

            for key, value in target_data.items():

                if key == df_list[i].columns[v]:

                    for k in range(len(df_list[i][key])):
                        if df_list[i][key][k] != None:
                            print(df_list[i][key][k] + ' -> ' + value(df_list[i][key][k]))
                            df_list[i][key][k] = value(df_list[i][key][k])
                                
                                
# For expected personal information data, pseudonymized/anonymized processing after data search
def Value_check(df_list):

    # social security number
    privacy_re = re.compile(r'(\d{6}[-]\d{1})(\d{6})')

    # Mobile phone number data
    tel_re = re.compile(r'(\d{3}[-]\d{3,4}[-])(\d{4})')
    
    # Email data identification
    email_re = re.compile(r'[\w]+@[\w.]+')

    for i in range(len(df_list)):
        # number of columns
        for v in range(len(df_list[i].columns)):
            # number of rows
            for c in range(len(df_list[i])):
                
                if df_list[i][df_list[i].columns[v]][c] != None:

                    # Check if value is in social security number format
                    if privacy_re.match(str(df_list[i][df_list[i].columns[v]][c])):
                        print(df_list[i][df_list[i].columns[v]][c] + ' -> ' + privacy_re.sub('\g<1>******', df_list[i][df_list[i].columns[v]][c]))
                        df_list[i][df_list[i].columns[v]][c] = privacy_re.sub('\g<1>******', df_list[i][df_list[i].columns[v]][c])

                     # Check if value is in mobile phone number format
                    if tel_re.match(str(df_list[i][df_list[i].columns[v]][c])):
                        print(df_list[i][df_list[i].columns[v]][c] + '->' + tel_re.sub('\g<1>####', df_list[i][df_list[i].columns[v]][c]))
                        df_list[i][df_list[i].columns[v]][c] = tel_re.sub('\g<1>####', df_list[i][df_list[i].columns[v]][c])


                    # Check if values is in email format
                    if email_re.match(str(df_list[i][df_list[i].columns[v]][c])):
                        print(df_list[i][df_list[i].columns[v]][c] + '->' + email_re.sub('*****@*****', df_list[i][df_list[i].columns[v]][c]))
                        df_list[i][df_list[i].columns[v]][c] = email_re.sub('*****@*****', df_list[i][df_list[i].columns[v]][c])


def Input_Data(df_list, username, password, host, port, dbname, table, schema, chunks):

    # save as DB
    db_info = "postgresql://" + username + ":" + password + "@" + host + ":" + port + "/" + dbname
    engine = create_engine(db_info) # set yours
  
    for i in range(len(df_list)):
        if not df_list[i].empty:
            
            if (not 'raw_data' in df_list[i].columns) and (i > 0):
                df_list[i].insert(1,'raw_data',df_list[i].index)
                print('raw_data')
            
            try :
                
                df_list[i].to_sql(name = table+str(i),

                                  con = engine,

                                  schema = schema,

                                  if_exists = 'append', # {'fail', 'replace', 'append'), default 'fail

                                  index = False,
                                  
                                  chunksize = chunks,
                                  
                                  dtype={"seq_no": Integer()})
                print('saved Data' + str(i))
            except:
                print('merge new columns ' + table+str(i))
               
                data_list = []
                data = pd.read_sql('SELECT * FROM {schema}.{table_name}'.format(schema = schema, table_name = table+str(i)), engine, chunksize=chunks)
                print('Import existing table')

                # Gathering scattered data
                for chunk in data :
                    data_list.append(chunk)
                data = pd.concat(data_list)
                print('data processed')
                input_data = pd.concat([data, df_list[i]])
                print('input_concat_data')
                ### After assembling the column of the processed data and the column of the newly processed data, it is stored in the db
                input_data.to_sql(name= table+str(i),
                                  
                                  con = engine,

                                  schema = schema,
                                  
                                  if_exists = 'replace',
                                  
                                  index = False,
                                  
                                  chunksize = chunks,
                                  
                                  dtype={"seq_no": Integer()})
                print('saved')
        else :
            
            break

# Main function executed for anonymous/pseudonym processing
def main(host_r, dbname_r, user_r, password_r, table_r, column_r, seq_no, port_r, host_p, dbname_p, user_p, password_p, port_p, table, n, chunksize, schema_r, schema_p, target_data):
    conn_r = psycopg2.connect(host = host_r,
                              dbname = dbname_r,
                              user = user_r,
                              password = password_r,
                              port = port_r)
    
    cur_r = conn_r.cursor()
    cur_r.execute("SELECT count(*) FROM {tablename};".format(tablename = table_r))
    data_c = cur_r.fetchall()
    # Check the total number of incoming data
    mydata_count = data_c[0][0]

    conn_p = psycopg2.connect(host = host_p,
                              dbname = dbname_p,
                              user = user_p,
                              password = password_p,
                              port = port_p)
    cur_p = conn_p.cursor()
    
    cur_p.execute("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table}')".format(schema = schema_p, table = table+str(0)))

    processing_time = 0
    processing_row = 0
    # Whether an anonymous table exists
    if cur_p.fetchall()[0][0]:
        # when the table exists
        cur_p.execute("select count(*) from {old_table}".format(old_table = table+str(0)))
        processed_row = cur_p.fetchall()
        processed_count = processed_row[0][0]
        
        print('Start processing' + str(mydata_count - processed_count) + 'rows')
        if mydata_count > processed_count:

            # Set the depth of the list to be put together by merging the data and set the size to 100.
            conn_p.close()

            # Anonymize the data to be processed by truncating n rows
            for c in range(processed_count, mydata_count, +n):
                # Start time
                start = time.time()
                # Import data
                cur_r.execute("select {column} from {table_name} order by {seq_no} asc OFFSET {start} limit {end}".format(column = column_r,
                                                                                                                       seq_no = seq_no,
                                                                                                                       table_name = table_r,
                                                                                                                       start = c ,
                                                                                                                       end = n))
                
                data = cur_r.fetchall()
                res_list = []

                if type(data[0][0]) == str:
                    for d in data:
                        # When the data to be loaded is in str json format
                        res_list.append(eval(d[0]))
                else :
                    for d in data:
                        # When the data to be loaded is in the json format of the dictionary
                        res_list.append(d[0])

                df = pd.DataFrame(res_list)
                df_list = []

                # Execution of Anonymity/Pseudonymization function
                Check_list(df, df_list, processed_count + c)
                anonymization(df_list, target_data)
                Value_check(df_list)

                for k in range(len(df_list)):
                    if k == 0:
                        df_list[k].insert(0,'seq_no',[ seq for seq in range(c, c + len(df_list[k].index)) ])
                    else :
                        df_list[k].insert(0,'seq_no',[ seq for seq in range(len(df_list[k].index))])
                
                Input_Data(df_list, user_p, password_p, host_p, port_p, dbname_p, table, schema_p, chunksize)

                processing_time += time.time() - start
                processing_row += len(df_list[0].index)
                p = psutil.Process()
                rss = p.memory_info().rss / 2 ** 20 # Bytes to MB

                print("number of rows processed " + str(processing_row) + "row, processing time :", processing_time)               
                print(f"memory usage: {rss: 10.5f} MB")
            # Store processed data in DB
            conn_r.close()
            
        else :
            return print('There is not enough data to process.')

    else : 
        # Terminate the database connection within the instance
        conn_p.close()
        print('Start processing ' + str(mydata_count) + 'rows')

        for c in range(0, mydata_count, +n):

            start = time.time()
            cur_r.execute("select {column} from {table_name} order by {seq_no} asc OFFSET {start} limit {end}".format(column = column_r,
                                                                                                                   seq_no = seq_no,
                                                                                                                   table_name = table_r,
                                                                                                                   start = c,
                                                                                                                   end = n))
            
            data = cur_r.fetchall()
            res_list = []

            if type(data[0][0]) == str:
                for d in data:
                    # When the data to be loaded is in str json format
                    res_list.append(eval(d[0]))
            else :
                for d in data:
                    # When the data to be loaded is in the json format of the dictionary
                    res_list.append(d[0])

            df = pd.DataFrame(res_list)
            df_list = []
            # Execution of Anonymity/Pseudonymization function
            Check_list(df, df_list, c)
            anonymization(df_list, target_data)
            Value_check(df_list)

       
            # Store processed data in DB
            for k in range(len(df_list)):

                if k == 0:
                    df_list[k].insert(0,'seq_no',[ seq for seq in range(c, c + len(df_list[k].index))])

                else :
                    df_list[k].insert(0,'seq_no',[ seq for seq in range(len(df_list[k].index))])

            Input_Data(df_list, user_p, password_p, host_p, port_p, dbname_p, table, schema_p, chunksize)

            processing_time += time.time() - start
            processing_row += len(df_list[0].index)
            p = psutil.Process()
            rss = p.memory_info().rss / 2 ** 20 # Bytes to MB

            print(f"memory usage: {rss: 10.5f} MB")
            print("number of rows processed " + str(processing_row) + " row, processing time :", processing_time)
        conn_r.close()