import numpy as np # Version 1.21.5
import pandas as pd # Version  1.3.5
from sqlalchemy import create_engine, Integer
import warnings

def is_processed_data(target_data, add_data, host, dbname, username, password, schema, old_table, port, chunks, depth, need_merge_table):
    print('func'+str(depth))
    db_info = "postgresql://" + username + ":" + password + "@" + host + ":" + port + "/" + dbname
    engine = create_engine(db_info) # set yours
    data = pd.read_sql('SELECT * FROM {schema}.{table_name} order by seq_no asc'.format(schema = schema, table_name = old_table), engine, chunksize = chunks)
    # concat data
    data_list = []
    processed_list = []
    
    for chunk in data :
        data_list.append(chunk)
    data = pd.concat(data_list)
    
    data = pd.DataFrame(data)
    
    for target in list(add_data):
        if target in data.columns:
            print(target)
            for i in range(data.seq_no.max()):
                if data[data.seq_no == i].iloc[0][target] != None :
                    data.loc[(data.seq_no == i),target] = target_data[target](data[data.seq_no == i].iloc[0][target])
            processed_list.append(data[target])
    if processed_list :
        processed_list.append(data['seq_no'])
        if depth > 0:
            processed_list.append(data['raw_data'])
        
        merge_Data = pd.concat(processed_list, axis = 1)
        
        try :
            print('make table'+str(depth))
            merge_Data.to_sql(name= need_merge_table+str(depth),

                                      con = engine,

                                      if_exists = 'replace',

                                      index = False,

                                      chunksize = chunks,

                                      dtype={"seq_no": Integer()})
        except :
            print('The table exists.')


def target_data_saved(target_data, host, dbname, username, password, schema, target_table, port, old_table, chunks, need_merge_table):
    import psycopg2
    conn_p = psycopg2.connect(host = host,
                              dbname = dbname,
                              user = username,
                              password = password,
                              port = int(port))

    cur_p = conn_p.cursor()
    cur_p.execute("CREATE TABLE IF NOT EXISTS {schema}.{target_table} (no Serial, target TEXT);".format(schema = schema, target_table = target_table))
    conn_p.commit()
    
    cur_p.execute("select target from {schema}.{target_table};".format(schema = schema, target_table = target_table))
    data = cur_p.fetchall()
    exists_columns = []

    for v in data:
        exists_columns.append(v[0])
    add_data = set(target_data.keys()) - set(exists_columns)

    if add_data :

        cur_p.execute("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table_name}')".format(schema = schema, table_name = old_table+str(0)))
        is_table = cur_p.fetchall()[0][0]
        while not is_table :
            warnings.warn(old_table + ' is not exists' )
            print('The \'old_table\' you set does not exist. If not necessary, press enter.')
            print('Input old_table you want to set :', end=' ')
            old_table = input()
            if old_table == '':
                break
            cur_p.execute("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table_name}')".format(schema = schema, table_name = old_table+str(0)))
            is_table = cur_p.fetchall()[0][0]

        #cur_p.execute("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table_name}')".format(schema = schema, table_name = old_table+str(index)))
        for add in list(add_data):
            cur_p.execute("INSERT INTO {schema}.{table_name} (target) VALUES ('{data}') ".format(schema = schema, table_name = target_table, data = add))
            conn_p.commit()
            
        depth = 100
        for index in range(depth):
            #Existence of old table
            cur_p.execute("select exists (select from information_schema.tables where table_schema = '{schema}' and table_name = '{table_name}')".format(schema = schema, table_name = old_table+str(index)))
            if cur_p.fetchall()[0][0]:
                print(index)
                is_processed_data(target_data, add_data, host, dbname, username, password, schema, old_table+str(index), port, chunks, index, need_merge_table)
            else :
                break
            
    conn_p.close()
