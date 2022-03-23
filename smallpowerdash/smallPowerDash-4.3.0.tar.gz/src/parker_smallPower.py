#!/bin/python
import importlib, time,datetime as dt,sys,os,glob
import dorianUtils.comUtils as comUtils
import pickle,pandas as pd
from zipfile import ZipFile
from multiprocessing import Pool

importlib.reload(comUtils)
streamer=comUtils.Streamer()

if 'sylfen' in os.getenv('HOME'):
    baseFolder = '/home/sylfen/data_ext/'
else:
    baseFolder='/home/dorian/data/sylfenData/'

FOLDERZIP = baseFolder + 'smallPower_zip_hourly/'
# FOLDERZIP_DAILY = baseFolder + 'smallPower_zip/'
start=time.time()
# folderparked_minutes =baseFolder+'smallPower_minutely/'
# FOLDERPARKED_DAYS=baseFolder+'smallPower_daily/'
FOLDERPARKED_DAYS=baseFolder+'smallpower_daily_back/'
FOLDERPARKED_HOURS=baseFolder+'smallPower_hourly/'
# FOLDERPARKED_DAYS = '/data1/smallpower_daily'
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
        # streamer.park_alltagsDF(df,folderparked_minutes,pool=False)
        streamer.park_DFday(df,FOLDERPARKED_DAYS,pool=pool)
        message=f+' parked in {:.2f} milliseconds'.format((time.time()-start)*1000)
    except:
        print()
        print('************************************')
        message=f+' failed to be parked'
        print(message)
        print('************************************')
        print()
    return message

def park_zip_hour_folder(filezip_hour):
    '''format of data in the zipFile should be 3 columns tag,value,timestampz with no header.'''
    start = time.time()
    #### unzip the file
    # try:
    with ZipFile(filezip_hour, 'r') as zipObj:
       zipObj.extractall(FOLDERZIP)
    ###read the file
    f_csv=filezip_hour.replace('.zip','.csv')
    df = read_csv_datetimeTZ(f_csv)
    ###remove the csv
    os.remove(f_csv)
    ###park the file
    streamer.park_DF_hour(df,FOLDERPARKED_HOURS,pool=False)
    message=filezip_hour+' parked in {:.2f} milliseconds'.format((time.time()-start)*1000)
    # except:
    #     print()
    #     print('************************************')
    #     message = filezip_hour+' failed to be parked'
    #     print(message)
    #     print('************************************')
    #     print()
    return message

def park_hourly2dayly(day,FOLDERPARKED_DAYS,showtag=False):
    """ -day :'ex : 2022-02-15' """
    listhours=glob.glob(FOLDERPARKED_HOURS+day+'/*')
    listhours.sort()
    listTags = os.listdir(listhours[0])
    folderday=FOLDERPARKED_DAYS +'/'+ day+ '/'
    if not os.path.exists(folderday):os.mkdir(folderday)
    for tag in listTags:
        if showtag:print(tag)
        dfs=[pd.read_pickle(hour+'/' + tag) for hour in listhours]
        pd.concat(dfs).to_pickle(folderday + tag)


listhoursfiles=glob.glob(FOLDERZIP+'/*2022-02-24*')
# park_zip_hour_folder(listhoursfiles[0])
with Pool(24) as p:p.map(park_zip_hour_folder,listhoursfiles)

# day='2022-02-24'
# park_hourly2dayly(day,True)
days=['2022-02-'+str(k) for k in range(25,29)]

with Pool(3) as p:p.map(park_hourly2dayly,days)

#####################
#   PARK EXTERNAL   #
#   DATABASE        #
#####################
def parkExternalDatabase():
    import smallPowerDash.smallPower as smallPower
    import pandas as pd
    dbParameters = {
        'host'     : "192.168.1.44",
        'host'     : "192.168.7.2",
        'port'     : "5434",
        'dbname'   : "Jules",
        'user'     : "postgres",
        'password' : "sylfenBDD"
        }
    dbparker = smallPower.SmallPower_dumper()
    dbparker.dbParameters=dbParameters
    t1 = pd.Timestamp.now(tz='CET')
    # t1 = pd.Timestamp('2022-02-09 23:59:59',tz='CET')
    t0 = t1-pd.Timedelta(hours=t1.hour,minutes=t1.minute,seconds=t1.second)
    basename='-00-00-x-RealTimeData.csv'
    dbparker.exportdb2zip(dbParameters,t0,t1,FOLDERZIP,basename=basename)
    pklfile=FOLDERZIP + (t0 + pd.Timedelta(days=1)).strftime(streamer.format_dayFolder).split('/')[0]+basename.replace('.csv','.pkl')
    df = pickle.load(open(pklfile,'rb')).reset_index()
    streamer.park_DFday(df,FOLDERPARKED_DAYS,pool=False,showtag=True)
    # streamer.dummy_daily()
# parkExternalDatabase()
