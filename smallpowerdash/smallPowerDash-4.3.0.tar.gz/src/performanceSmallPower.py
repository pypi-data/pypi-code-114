import sys,re,importlib, numpy as np, time, datetime as dt

import dorianUtils.utilsD as ut
import dorianUtils.configFilesD as cfd
import plotly.express as px

importlib.reload(ut)
importlib.reload(cfd)

utils      = ut.Utils()

# baseFolder = '/home/sylfen/data/'
baseFolder   = '/home/dorian/data/sylfenData/'
# /home/sylfen/data/smallPower_pkl
import smallPowerDash.configFilesSmallPower as cfs
importlib.reload(cfs)
folderPkl = baseFolder + 'smallPower_pkl/'
cfg  = cfs.ConfigFilesSmallPower(folderPkl)

timeRange = ['2021-05-01 00:00','2021-05-01 23:59']

listTags = cfg.getUsefulTags('Pression ligne air')
# listTags = cfg.getUsefulTags('Débits lignes air')
rs = '60s'

cfg.dfPLC['newindex']=range(len(cfg.dfPLC))

df = cfg.loadFile('*04-28*')

start=time.time()
x=[]
for tag in df2.tag:
    x.append(list(cfg.dfPLC.newindex[cfg.dfPLC.TAG==tag])[0])

utils.printCTime(start)

def isin(x):return np.isin(x,listTags)

def numbatest():
    import numba

    @numba.jit
    def isin_plain(x,s):
        return x in s

    @numba.jit
    def apply_isin_numba(df,s):
        result = np.empty(len(df), dtype="short")
        for i in range(len(df)):
            result[i] = isin_plain(df.tag[i],s)
        return result

    def compute_numba(df,tlist):
        result = apply_isin_numba(df,tlist)
        return df[result]

    start=time.time()
    compute_numba(df,listTags)
    utils.printCTime(start)

    start=time.time()
    df.tag.isin(listTags)
    utils.printCTime(start)

def testModin():
    import modin.pandas as pd
    # import pandas as pd
    import os
    os.environ["MODIN_CPUS"] = "4"
    os.environ["MODIN_MEMORY"] = "10000000000"
    start=time.time()
    df2=df.tag.isin(listTags)
    utils.printCTime(start)

def aply_swifter_test():
    import swifter
    start=time.time()
    df.tag.apply(isin)
    utils.printCTime(start)

    start=time.time()
    df['tag'].swifter.apply(isin)
    utils.printCTime(start)

def pd_eval_test():
    start=time.time()
    df.tag.isin(listTags)
    utils.printCTime(start)

    start=time.time()
    pd.eval("df.tag.apply(isin)")
    utils.printCTime(start)

    start=time.time()
    pd.eval("df.tag.isin(listTags)")
    utils.printCTime(start)

def poolPickleload():
    start=time.time()
    df1 = cfg.DF_fromTagList(df,listTags)
    utils.printCTime(start)

    df2 = cfg.DF_fromTagList_pool(df,listTags)
    df2 = cfg.DF_fromTagList_process(df,listTags)
    df = df.drop_duplicates(subset=['timestampUTC', 'tag'], keep='last')
    df = df.pivot(index="timestampUTC", columns="tag", values="value")
    # df.duplicated(subset=['timestampUTC', 'tag'], keep=False)
    # df3=df.drop_duplicates()
    df=df.resample('60s').apply(np.nanmean)
    df.index=df.index.tz_convert('Europe/Paris')# convert utc to tzSel timezone
    utils.printCTime(start)

    start=time.time()
    df2 = cfg.DF_loadTimeRangeTags(timeRange,listTags,rs=rs,applyMethod='nanmean')
    utils.printCTime(start)
