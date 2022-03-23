import os,pickle,glob,pandas as pd
from multiprocessing import Pool

if 'sylfen' in os.getenv('HOME'):
    baseFolder = '/home/sylfen/data_ext/'
else:
    baseFolder='/home/dorian/data/sylfenData/'

# folderdata=baseFolder+'smallPower_daily/'
folderdata=baseFolder+'smallpower_daily_back/'


def applyCorrectFormat(d,cfg,newtz='CET',printag=False,debug=False):
    '''
    - format as pd.Series with name values and timestamp as index
    - remove index duplicates
    - convert timezone
    - apply correct datatype if bool,float or string
    '''
    print(d)
    tags = os.listdir(d)
    for t in tags:
        tagpath=d+'/'+t
        if printag:print(tagpath)
        try:
            df=pd.read_pickle(tagpath)
        except:
            print('pb loading',tagpath)
        if df.empty:
            print('dataframe empty for ',tagpath)
            return
        ##### --- make them format pd.Series with name values and timestamp as index----
        if not isinstance(df,pandas.core.series.Series):
            col_timestamp=[k for k in df.columns if 'timestamp' in k]
            df.set_index(col_timestamp)['value'].to_pickle(tagpath)
        ##### --- remove index duplicates ----
        df = df[~df.index.duplicated(keep='first')]
        ##### --- convert timezone----
        if isinstance(df.index.dtype,pd.DatetimeTZDtype):
            df.index = df.index.tz_convert(newtz)
        else:### for cases with changing DST at 31.10 or if it is a string
            df.index = [pd.Timestamp(k).astimezone(newtz) for k in df.index]
        #####----- apply correct datatype ------
        try:
            df = df.astype(cfg.dataTypes[cfg.dfplc.loc[t.strip('.pkl'),'DATATYPE']])
        except:
            print(t,' not in ',cfg.file_plc_xlsm)
        df.to_pickle(tagpath)

def correctTensions1_0737(d,cfg):
    '''format : pd.Series with name Value and timestampz as index'''
    # print(d)
    et_tags=cfg.getUsefulTags('tensions stacks')
    for t in et_tags:
        tagpath=d+'/'+t+'.pkl'
        try:
            print(tagpath)
            df=pickle.load(open(tagpath,'rb'))
            df=1.0737*df
            df.to_pickle(tagpath)
        except:
            print('pb loadding',tagpath)

def compute_calculated_tags_retro(d,calculatedTag,cfg):
    '''format : pd.Series with name Value and timestampz as index'''
    # ================================================
    # courant en valeur absolue et convention physique
    # ================================================

def remove_tags(d,tags):
    print(d)
    for t in tags:
        tagpath=d+'/'+t+'.pkl'
        try:
            os.remove(tagpath)
        except:
            print('no file :',tagpath)

import smallPowerDash.smallPower as smallPower
cfg = smallPower.SmallPowerComputer(rebuildConf=False)

# days=glob.glob(folderdata+'/*2022-25*')
# with Pool(15) as p:p.starmap(changedatatype,[(d,cfg) for d in days])
# correctTensions1_0737(folderdata+'2022-02-06',cfg)
# day='2022-02-14'
# day='2022-02-15'
# day='2022-02-16'
day='2022-02-23'
removedupplicates(folderdata+day)
assignTypeCorrect(folderdata+day,cfg)
# with Pool(25) as p:p.starmap(assignTypeCorrect,[(folderdata+d,cfg) for d in days])
