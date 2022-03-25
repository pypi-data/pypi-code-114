import os,pickle,glob,pandas as pd
from multiprocessing import Pool

def tzconvert(d):
    print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        # print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            if isinstance(df.index.dtype,pd.DatetimeTZDtype):
                df.index = df.index.tz_convert('UTC')
            else:### for cases with changing DST 31.10 for example
                df.index = [pd.Timestamp(k).astimezone('UTC') for k in df.index]
        df.to_pickle(tagpath)

def correctFormat(d):
    '''format : pd.Series with name "Value" and timestampz as index'''
    print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        # print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            df.set_index('timestampUTC')['value'].to_pickle(tagpath)
            # df.set_index('timestampUTC').to_pickle(tagpath)

# def changedatatype(d,cfg):
def changedatatype(d):
    '''format : pd.Series with name Value and timestampz as index'''
    # print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        print(tagpath)
        try:
            dataype='float'
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            df=df.astype(dataype)
            if dataype=='bool':
                df=df.astype(int)
            df.to_pickle(tagpath)

def toFormattagvaluetimestamp(d):
    '''format : pd.Series with name Value and timestampz as index'''
    # print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            df.index.name = 'timestampUTC'
            df = df.reset_index()
            df['tag'] = t.split('.pkl')[0]
            df.to_pickle(tagpath)

def removedupplicates(d):
    '''format : pd.Series with name Value and timestampz as index'''
    # print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            df = df[~df.index.duplicated(keep='first')]
            df.to_pickle(tagpath)

def filterOnTime(d,timestamp):
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            df = df[df.index<timestamp]
            df.to_pickle(tagpath)

def assignTypeCorrect(d,cfg):
    '''format : pd.Series with name Value and timestampz as index'''
    # print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        print(tagpath)
        try:
            df=pickle.load(open(tagpath,'rb'))
        except:
            print('pb loadding',tagpath)
        if not df.empty:
            try:
                df = df.astype(cfg.dataTypes[cfg.dfplc.loc[t.replace('.pkl',''),'DATATYPE']])
                df.to_pickle(tagpath)
            except:
                print(t,' not in ',cfg.file_plc_xlsm)

def remove_tags(d,tags):
    print(d)
    for t in tags:
        tagpath=d+'/'+t+'.pkl'
        try:
            os.remove(tagpath)
        except:
            print('no file :',tagpath)

folderbase='/home/dorian/data/sylfenData/monitoring_daily/'
# with Pool() as p:p.map(tzconvert,days)
# with Pool(6) as p:p.map(correctFormat,days)
days = glob.glob(folderbase + '*2022-03-01*')
# days = glob.glob(folderbase + '*2022-01-28*')
# import monitorBuildingDash.screenBuilding as screenBuilding
# cfg = screenBuilding.ScreenBuildingComputer()

with Pool(2) as p:p.map(changedatatype,days)

# [correctFormat(d) for d in days]
# toFormattagvaluetimestamp('2022-02-09')
# changedatatype(folderbase+'2022-02-17',cfg)
# changedatatype(folderbase+'2022-02-08',cfg)
# filterOnTime(folderbase+'2022-02-17','2022-02-17T17:00:00+01:00')
