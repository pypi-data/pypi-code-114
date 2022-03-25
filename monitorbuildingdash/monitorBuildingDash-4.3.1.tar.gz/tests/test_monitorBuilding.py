#!/bin/python
import importlib,re
import os,pandas as pd,glob,pickle
import dorianUtils.comUtils as comUtils
importlib.reload(comUtils)
from dorianUtils.utilsD import Utils
import time,datetime as dt,sys
start=time.time()
utils=Utils()
# ==============================================================================
#                           TESTS STREAMER
def testStreamer():
    streamer=comUtils.Streamer()
    t0 = pd.Timestamp('2021-08-12 05:00',tz='CET')
    t1 = t0+dt.timedelta(days=0,hours=23,minutes=59)
    folderday = folderparked_days + streamer.to_folderday(t0)
    localGetTags = lambda x:[k.split('/')[-1].split('.pkl')[0] for k in glob.glob(folderday+x)]
    pv         = localGetTags('*PV*JTW-00*')
    sls_global = localGetTags('*[EF]001*sys-JTW*')
    tags = sls_global+pv
    # def testLoadDataFolders():
    start=time.time()
    # dfs=sbc.loadtags_minutefolder(folderminute,tags)
    # df=sbc.streaming.dumy_period([t0,t1],sbc.folderPkl,pool=True)
    # df=sbc.streaming.load_parkedtags_period(tags,[t0,t1],sbc.folderPkl,pool=False)
    # df=sbc.streaming.load_parkedtags_period(tags,[t0,t1],sbc.folderPkl,pool=True)

    # df=streamer.load_parkedtags_daily(tags,t0,t1,folderparked_days)
    print('{:.2f} milliseconds'.format((time.time()-start)*1000))

# ==============================================================================
#                           TESTS WEBPAGE MONITORING
import monitorBuildingDash.screenBuilding as screenBuilding
importlib.reload(screenBuilding)
cfg = screenBuilding.ScreenBuildingComputer()
import plotly.express as px, plotly.graph_objects as go
# cfg.dbParameters['dbname']='bigbrother'
# cfg.dbParameters['host']='192.168.7.2'
# cfg.folderPkl='/home/sylfen/data/monitoring_daily/'

# def test_webpage_monitoring():
t1   = pd.Timestamp.now(tz='CET')
# t1 = pd.Timestamp('2022-02-22 10:01',tz='CET')
t0 = t1-pd.Timedelta(days=2)
tags=cfg.getTagsTU('pv')
# df = cfg.streamer.load_tag_daily(t0,t1,tags[0],cfg.folderPkl,rs='600s',rsMethod='forwardfill',timezone="CET")
df = cfg.getTags_sls_conso(t0,t1,rs='600s',units='kW')

# df = cfg.get_conso_prod_sls_lastValue()

# df  = cfg.conso2days_sls(t1)
# df2 = cfg.get_slsTotalEngie(t1,'mean')
# fig=cfg.fig_conso2days_sls(t1)
# fig.show()
sys.exit()
# df = cfg.consoweek_sls(t1)
# fig=cfg.fig_consoweek_sls(t1)

# t1 = pd.Timestamp('2022-01-10 10:01',tz='CET')
# t0 = t1-pd.Timedelta(days=20)
tags = cfg.tag_categories['SLS niveau1 puissances']
# df   = cfg._load_parked_tags(t0,t1,tags)
# df = cfg.loadtags_period(t0,t1,tags,'raw')
# df = cfg.consomonth_sls(t1)
# df = cfg.conso_sls_compteurs(['A007'],t1,t0)
# px.bar(df)
# fig=cfg.fig_consomonth_sls(t1)


# last_days = cfg.get_last_days_month_since_start(t1)
# tc = cfg.get_nearest_available_day(pd.Timestamp('2021-06-30',tz='CET'))


# t1 = pd.Timestamp('2021-12-29 23:59',tz='CET')
# t0 = t1-pd.Timedelta(days=1)
# df = cfg.loadtags_period(t0,t1,['C0000000d-F003-kWh-JTWH'],'raw')
# df = cfg.get_compteurs_sls_since_start(t1)
# df = cfg.track_energy_compteurs_months(t1,False)
# df = cfg.get_last_days_month_since_start(t1)
sys.exit()

# t1 = pd.Timestamp('2021-08-06 23:00',tz='CET')
# t1 = pd.Timestamp('2021-09-10 23:03',tz='CET')
tags = cfg.tag_categories['SLS compteurs']
# tags = tags[7:8]
# tags = tags[6:7]
# t0 = t1 - pd.Timedelta(hours=23)
# df = cfg._load_parked_tags(t0,t1,tags)
# df = cfg.loadtags_period(t0,t1,tags,'raw')
# df=cfg.get_compteurs_sls_since_start(t1)
fig=cfg.fig_consoyear(t1,mode='global')

# t1 = pd.Timestamp('2021-09-16 16:03',tz='CET')
# df = cfg.conso_repartition_sls(t1)
# fig = cfg.fig_repartitioncompteurs_sls(t1)
sys.exit()
# fig.show()

# ==============================================================================
#                           TESTS SCREENBUILDING
# tags=cfg.getUsefulTags('Puissances sls')
# folderminute=streamer.to_folderminute(t0)
# tags=sbc.getTagsTU('PV')+sbc.getTagsTU('B001')

def generateRandomData():
    dataparker = screenBuilding.DumpingClient_SB()
    t1 = dt.datetime(2021,12,17,19,35).astimezone()
    t0 = t1-dt.timedelta(days=0,hours=3,minutes=0)
    start = time.time()
    dffig = dataparker.generateRandomParkedData(t0,t1,4)
    # dffig = dataparker.generateRandomParkedData(t0,t1,10,tags)
    # pickle.dump(dffig,open('random_dffig.pkl','wb'))
    # pickle.load(open('random_dffig.pkl','rb'))
    print('generating data done in {:.2f} s'.format((time.time()-start)))
    dataparker.parkalltagsDF(df,True)

# def test_dfLoadparkedTags():
start = time.time()
# t1 = pd.Timestamp.now(tz='CET')
t1 = pd.Timestamp('2022-02-23 18:00',tz='CET')
t0 = t1-pd.Timedelta(days=6,hours=0)
# tags = pd.Series(cfg.alltags).sample(n=4).to_list()
tags = cfg.tag_categories['SLS niveau0 compteurs']
tags+= cfg.tag_categories['SLS niveau0 puissances']
# df = cfg.streamer.load_parkedtags_daily(tags,t0,t1,cfg.folderPkl)
# dfparked = cfg._load_parked_tags(t0,t1,tags)
# dfdb = cfg._load_database_tags(t0,t1,tags)

# df = cfg.loadtags_period(t0,t1,tags,rsMethod='raw',checkTime=False)
# df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs='60s')
rs = '60s'
# df = cfg.loadtags_period(t0,t1,tags,rsMethod='meanright',rs=rs,checkTime=True)
df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs=rs,checkTime=True)
comUtils.computetimeshow('loading',start)

# print('done in {:.2f} milliseconds'.format((time.time()-start)*1000))

def test_resampling():
    import plotly.express as px
    rs='10s'
    listTags = cfg.allTags.sample(n=2)
    df = cfg._dfLoadparkedTags(listTags,[t0,t1],rs='raw')
    dfraw = df.iloc[:,[0]]

    dfraw.columns = ['value']
    s = dfraw.iloc[:,[0]]

    dfs={}
    dfraw['variable']='raw'
    dfs['raw']=dfraw
    # ts['raw']='{:.3f}'.format((time.time()-start)*1000))

    methods={}
    start = time.time()
    methods['ffill'] ='s.ffill()'

    #######
    # if raw data have na values, without a ffill at the begining na will be propagated.
    #######

    # methods['interpolate']= "s.interpolate('time')" #works only on na values
    # methods['rsfill'] = "s.resample(rs).ffill()"
    # methods['rsfirst'] = "s.resample(rs).first()"#doesnt work
    # methods['rslast'] = "s.resample(rs).last()"#doesnt work
    # methods['rsmeanfill'] = "s.resample(rs).mean().ffill()" # horrible
    # methods['rsinterpolate'] = "pd.concat([s.resample(rs).asfreq(),s]).sort_index().interpolate('time').resample(rs).asfreq()"

    #######
    # fill na values of raw data (because of pivoted dataframe for example)
    #######
    #works as expected
    methods['fillrsfill']= "s.ffill().resample(rs).ffill()"
    # methods['rsinterpolate'] = "pd.concat([s.resample(rs).asfreq(),s]).sort_index().interpolate('time').resample(rs).asfreq()"

    #######
    # mean,max,min
    #######

    #add na data if missing values in between
    #incorrect because at t value given for what happend between t and t+1
    # methods['fillrsmax']  = "s.ffill().resample(rs).max()"
    #correct
    # methods['fillrsmaxright']  = "s.ffill().resample(rs,label='right',closed='right').max()"
    # methods['fillrsminright']  = "s.ffill().resample(rs,label='right',closed='right').min()"
    # very dangerous because data are not regularly spaced.
    # methods['fillrsmeanright']  = "s.ffill().resample(rs,label='right',closed='right').mean()"

    #######
    # fill first with rs 100ms for mean or rolling mean
    #######
    # methods['0.1fillrsfill']   = "s.resample('100ms').ffill().resample(rs).ffill()"
    # methods['fillrs0.1fill'] = "s.ffill().resample('100ms').ffill()"
    # way better because data are rergulary spaced. 100ms necessary to make sure that all datapoints are catched
    methods['fill0.1fillrsmeanright'] = "s.ffill().resample('100ms').ffill().resample(rs,label='right',closed='right').mean()"
    # maybe even more precise if the dynamic compression was too hard
    # methods['fill0.1interpolate_rsmeanright'] = "pd.concat([s.resample('100ms').asfreq(),s]).sort_index().interpolate('time').resample(rs,label='right',closed='right').mean()"

    #######
    # rolling mean
    #######
    # methods['fill0.1fillrsRollmean']="s.ffill().resample('100ms').ffill().rolling(rs).mean()"
    # methods['fillrsfillrsRollmean']="s.ffill().resample(rs).ffill().rolling(rs).mean()"
    methods['fillrsfill10rsRollmean']="s.ffill().resample(rs).ffill().rolling(str(int(rs[:-1])*10)+'s').mean()"
    methods['fillrsfill5rsRollmean']="s.ffill().resample(rs).ffill().rolling(str(int(rs[:-1])*5)+'s').mean()"
    # methods['fillrsfill5rsRollmeanGauss']="s.ffill().resample(rs).ffill().rolling(str(int(rs[:-1])*5)+'s',win_type='gaussian').mean(std=2)"
    # methods['fillrsfill5rsRollmeanTri']="s.ffill().resample(rs).ffill().rolling(str(int(rs[:-1])*5)+'s',win_type='triang').mean()"
    # methods['fillrsfillrsRollmean']="s.ffill().resample(rs).ffill().rolling(rs).mean()"
    # methods['fill0.1fillrsRollmean10first1']="s.ffill().resample('100ms').ffill().rolling('10s').mean().resample('1s').first()"


    for k,v in methods.items():
        start = time.time()
        dftmp = eval(v)
        ts=' - {:.3f} ms'.format((time.time()-start)*1000)
        dftmp['variable'] = k+ts
        dfs[k] = dftmp

    dft=pd.concat(dfs.values(),axis=0)

    fig=px.scatter(dft,y='value',color='variable',facet_row='variable')
    fig=fig.update_traces(mode='lines+markers',line_shape='linear',marker_size=10)
    fig.update_xaxes(tickvals=dfs[list(dfs.keys())[-1]].index,showticklabels=False)
    fig.show(config={'modeBarButtonsToAdd':['toggleSpikelines']})

def testSetInterval():
    from time import sleep
    import numpy as np

    def sleepabit():
        t0 = dt.datetime.now().astimezone()
        print('start time task : ',t0.strftime('%H:%M:%S:%f')[:-4])
        value =0.9+np.random.randint(0,20)/100
        print('duration task : ',value)
        print('')
        sleep(value)

    ## initialize a M:S:000 pétante ! #####
    now =dt.datetime.now().astimezone()
    time.sleep(1-now.microsecond/1000000)
    setTest=comUtils.SetInterval(1,sleepabit)
    setTest.start()

def testLoadAndpPlotCompuation():
    # generateRandomData()
    #### small computation test
    cfg.dbParameters={
        # 'host'     : "localhost",
        'host'     : "192.168.7.2",
        'port'     : "5432",
        'dbname'   : "bigbrother",
        'user'     : "postgres",
        'password' : "sylfenbdd"
        }
    t1 = pd.Timestamp.now('CET')
    t1 = t1-pd.Timedelta(hours=12,minutes=0)
    t0 = t1-pd.Timedelta(hours=15,minutes=0)
    start=time.time()
    tags = cfg.tag_categories['SLS niveau1 puissances']
    df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs='60s',checkTime=False)
    # df = cfg._load_database_tags(t0,t1,tags)
    print('')
    print('=============================================')
    print('full loading data in {:.2f} milliseconds'.format((time.time()-start)*1000))

    sys.exit()
    start=time.time()
    fig=cfg.plotTabSelectedData(df)
    print('generate figure in {:.2f} milliseconds'.format((time.time()-start)*1000))
    start=time.time()
    # fig=fig.add_trace(go.Scatter(x=df.index,y=np.random.randn(len(df))))
    # print('adding figure in {:.2f} milliseconds'.format((time.time()-start)*1000))
    start=time.time()
    fig=fig.update_traces(mode='lines+markers')
    fig.show()
    print('plot figure in {:.2f} milliseconds'.format((time.time()-start)*1000))

def testdoubleMultiUnitGraph():
    timeRange=['2021-12-20 09:15','2021-12-20 11:30']
    tags1=cfg.getUsefulTags('Temperatures du gv1a')[:3] + cfg.getTagsTU('GFC')[0:2]
    tags2=cfg.getUsefulTags('Temperatures du gv1a')[5:6] + cfg.getTagsTU('GFC')[3:4]
    tags3=cfg.getUsefulTags('Temperatures du gv1a')[7:] + cfg.getTagsTU('GFC')[5:] + ['SEH1.STB_HER_01_JTW_01_HC20']
    tags=tags1+tags2+tags3
    df=cfg.df_loadtagsrealtime(tags,timeRange,False,'forwardfill','60s')
    fig = cfg.doubleMultiUnitGraph(df,tags1,tags2,tags3)
    fig.show()

def testGraphs():
    start = time.time()
    # t1 = pd.Timestamp.now(tz='CET')
    t1 = pd.Timestamp('2022-02-17 18:00',tz='CET')
    t0 = t1-pd.Timedelta(days=0,hours=3)
    tags+= cfg.tag_categories['SLS niveau0 puissances']
    rs = '10s'
    df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs=rs,checkTime=True)
    comutils.computetimeshow('min max',start)
    # fig  = cfg.multiUnitGraphSB(df)
    fig = px.scatter(df)
    fig = cfg.graph_UnitsSubplots(df,facet_col_wrap=2)
    td   = cfg.toogle_tag_description(df.columns,'description')
    fig  = cfg.utils.customLegend(fig,td)
    fig.show()
    sys.exit()

    fig = cfg.update_lineshape_fig(fig,'default')
    fig = cfg.addTagEnveloppe(fig,tags[0],t0,t1,rs=rs)
    td  = cfg.toogle_tag_description(tags,'description')
    # fig = utils.customLegend(fig,td)
    fig.show()
