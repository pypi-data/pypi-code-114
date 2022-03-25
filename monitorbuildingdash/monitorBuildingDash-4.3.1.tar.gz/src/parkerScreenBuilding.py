#!/bin/python
import importlib, time,datetime as dt,sys,os,glob
import dorianUtils.comUtils as comUtils
import pickle,pandas as pd
from zipfile import ZipFile
from multiprocessing import Pool

importlib.reload(comUtils)
streaming=comUtils.Streamer()

start=time.time()
if 'sylfen' in os.getenv('HOME'):
    baseFolder = '/home/sylfen/data_ext/'
else:
    baseFolder='/home/dorian/data/sylfenData/'

FOLDERZIP = baseFolder+'monitoring_zip/'
folderparked_minutes =baseFolder+'monitoring_minutely/'
# folderparked_days=baseFolder+'monitoring_daily_back/'
folderparked_days=baseFolder+'monitoring_daily/'
listfiles = glob.glob(FOLDERZIP + '*.zip')
# listfiles = glob.glob(FOLDERZIP+'*2022-01-2*.zip')
listfiles.sort()

def read_csv_datetimeTZ(filename):
    start   = time.time()
    print("============================================")
    print('reading of file',filename)
    df = pd.read_csv(filename,parse_dates=['timestampz'],names=['tag','value','timestampz'])
    print('read in {:.2f} milliseconds'.format((time.time()-start)*1000))
    start = time.time()
    return df

def park_zipFile(f,pool=False):
    '''format of data in the zipFile should be 3 columns tag,value,timestampz with no header.'''
    start = time.time()
    try:
        """unzip the file """
        print(f)
        with ZipFile(f, 'r') as zipObj:
           zipObj.extractall(FOLDERZIP)
        """read the file to the correct format for parking"""
        df = read_csv_datetimeTZ(f.replace('.zip','.csv'))
        listTags=list(df.tag.unique())
        """park the file """
        # streaming.park_alltagsDF(df,folderparked_minutes,pool=False)
        streaming.park_DFday(df,folderparked_days,pool=pool)
        message=f+' parked in {:.2f} milliseconds'.format((time.time()-start)*1000)
        """move the .zip file to archives"""
        os.rename(f,FOLDERZIP+'/archives/'+f.split('/')[-1])
        """remove the .csv file"""
        os.remove(f.replace('.zip','.csv'))

    except:
        print()
        print('************************************')
        message=f+' failed to be parked'
        print(message)
        print('************************************')
        print()
    return message

# with Pool(4) as p:dfs=p.map(park_zipFile,listfiles)
# with Pool(8) as p:dfs=p.map(park_zipFile,listfiles[10:])
# with Pool(45) as p:dfs=p.map(park_zipFile,listfiles)
# dfs={f:park_zipFile(f,True) for f in listfiles}
# f=listfiles[-1]
# df = read_csv_datetimeTZ(f.replace('.zip','.csv'))
# importlib.reload(comUtils)
# streaming=comUtils.Streamer()
# streaming.park_DFday(df,folderparked_days,pool=False,showtag=False)

def parkExternalDatabase(d):
    import monitorBuildingDash.screenBuilding as screenBuilding
    import pandas as pd,numpy as np
    dbParameters = {
        'host'     : "192.168.1.44",
        'port'     : "5434",
        'dbname'   : "BigBrother",
        'user'     : "postgres",
        'password' : "sylfenBDD"
        }
    # dbParameters = {
    #     'host'     : "192.168.7.2",
    #     'port'     : "5432",
    #     'dbname'   : "bigbrother",
    #     'user'     : "postgres",
    #     'password' : "sylfenbdd"
    #     }
    dbparker = screenBuilding.ScreeningBuilding_dumper()
    dbparker.dbParameters=dbParameters
    # t1 = pd.Timestamp.now(tz='CET')
    t1 = pd.Timestamp(d+ ' 23:59:59',tz='CET')
    t0 = t1-pd.Timedelta(hours=t1.hour,minutes=t1.minute,seconds=t1.second)
    basename = '-00-00-Monitoring-RealTimeData.csv'
    dbparker.exportdb2zip(dbParameters,t0,t1,FOLDERZIP,basename=basename)
    pklfile=FOLDERZIP + (t0 + pd.Timedelta(days=1)).strftime(streaming.format_dayFolder)[:-1]+basename.replace('.csv','.pkl')
    df=pickle.load(open(pklfile,'rb'))
    df=df.reset_index()
    df=df.replace('null',np.nan)
    streaming.park_DFday(df,folderparked_days,pool=False,showtag=False)

# for d in pd.date_range(start='2022-02-19',end='2022-02-22'):
#     parkExternalDatabase(d.strftime('%Y-%m-%d'))
parkExternalDatabase('2022-02-28')
