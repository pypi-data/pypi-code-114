#!/bin/python
import importlib,sys,datetime as dt
import time,sys,os
import pickle
import pandas as pd
import smallPowerDash.smallPower as smallPower
import plotly.graph_objects as go,plotly.express as px
import numpy as np,datetime as dt
# import dorianUtils.configFilesD as cfd
import dorianUtils.utilsD as utilsD
import dorianUtils.comUtils as comutils

importlib.reload(smallPower)
# importlib.reload(cfd)
# importlib.reload(utilsD)

# ==============================================================================
#                           TESTS
cfg = smallPower.SmallPowerComputer(rebuildConf=False)
# cfg.dbParameters['dbname']='jules'
# cfg.dbParameters['host']='192.168.7.2'

def generateRandomData():
    dataparker = smallPower.DumpingClient_SP()
    t1 = dt.datetime(2021,12,17,19,35).astimezone()
    t0 = t1-dt.timedelta(days=0,hours=3,minutes=0)
    start = time.time()
    df = dataparker.generateRandomParkedData(t0,t1,4)
    # df = dataparker.generateRandomParkedData(t0,t1,10,tags)
    # pickle.dump(df,open('random_df.pkl','wb'))
    # pickle.load(open('random_df.pkl','rb'))
    print('generating data done in {:.2f} s'.format((time.time()-start)))
    dataparker.parkalltagsDF(df,True)

def getQuickData():
    start = time.time()
    t0 = pd.Timestamp('2022-02-24 00:00',tz='CET')
    t1 = pd.Timestamp('2022-02-24 23:59',tz='CET')
    tags = cfg.getTagsTU('STG.*TT_03')
    df = cfg.loadtags_period(t0,t1,tags,rsMethod='meanright',rs='1H',checkTime=False)
    # fig=cfg.multiUnitGraphSP(df)
    # fig.show()
    # df.index=[k.isoformat() for k in df.index]
    # df.to_excel('data_2022_16_02.xlsx')
    # pickle.dump(fig,open('fig.pkl','rb'))

# def test_dfLoadparkedTags():
start = time.time()
# t1 = pd.Timestamp.now(tz='CET')-pd.Timedelta(hours=1)
t1 = pd.Timestamp.now(tz='CET')
t0 = pd.Timestamp('2022-02-01 00:00',tz='CET')
t1 = pd.Timestamp('2022-02-28 23:59',tz='CET')
tags=cfg.getTagsTU('gfd')
tags=[tags[0]]


# dftag = cfg.streamer.load_tag_daily(t0,t1,tags[0],cfg.folderPkl,'raw','60s','CET',rmwindow='3000s',showTag=False,debug=True)
# dfparked = cfg.streamer.load_parkedtags_daily(t0,t1,tags,cfg.folderPkl,pool=True,rsMethod='forwardfill',rs='3600s')
# dfdb = cfg._load_database_tags(t0,t1,tags,rsMethod='raw',checkTime=False)
# dfdb = cfg._load_database_tags(t0,t1,tags,pool=False,rsMethod='forwardfill',rs='10s')
# dfparked = cfg.streamer.load_parkedtags_daily(t0,t1,tags,cfg.folderPkl,pool=True,rsMethod='raw')
# df=dfparked.pivot(values='value',columns='tag').sort_index()
# dfparked = cfg.streamer.load_parkedtags_daily(t0,t1,tags,cfg.folderPkl,pool=True,rsMethod='forwardfill',rs='10s',showTag=False)
# df = cfg.loadtags_period(t0,t1,tags,rsMethod='meanright',rs='auto',checkTime=True)
# df = cfg.loadtags_period(t0,t1,tags,rsMethod='raw',checkTime=False,rs='60s')
# df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs='3600s',checkTime=True)
# cfg.multiUnitGraphSP(df).show()

def test_post_calculatedTags():
    t1 = pd.Timestamp('2022-02-16 17:20',tz='CET')
    # t1 = t1-pd.Timedelta(hours=2)
    t0 = t1-pd.Timedelta(days=0,hours=0,minutes=20)

    alphas=np.linspace(0.001,0.2,20)
    df=cfg.post_fuitesAir(t0,t1,rs='30s',rsMethod='forwardfill',alpha=0.001)

    # dff=pd.DataFrame([cfg.utils.lowpass(coeffuiteAir,k) for k in alphas],
    #     index=['alpha : '+str(k) for k in alphas],
    #     columns=coeffuiteAir.index).T
    fig=px.scatter(df)
    fig.update_traces(mode='lines+markers')
    fig.show()
    comutils.computetimeshow(start)

def test_minMax_legend():
    start=time.time()
    t1 = pd.Timestamp.now(tz='CET')
    t1 = pd.Timestamp('2022-02-17 11:27',tz='CET')
    # t1 = t1-pd.Timedelta(hours=2)
    # t0 = t1-pd.Timedelta(days=0,hours=2,minutes=0)
    t0 = t1-pd.Timedelta(days=0,hours=0,minutes=7)
    rs='10s'
    tags = cfg.getTagsTU('GFC_0.*PT')
    tags+=['SEH1.HPB_STG_01a_TT_03.HM05']
    tags+=['SEH01.L118_O2_ECV2_01.HO00']
    tags+=['SEH1.STB_STK_04.HER_01.HO00']
    # df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs=rs,checkTime=False)
    df = cfg.loadtags_period(t0,t1,tags,rsMethod='meanright',rs=rs,checkTime=True)
    fig = cfg.multiUnitGraphSP(df)

    # td   = cfg.toogle_tag_description(tags,'description')
    # fig  = utilsD.Utils().customLegend(fig,td)
    fig  = cfg.update_lineshape_fig(fig,'standard')
    fig = cfg.addTagEnveloppe(fig,tags[1],t0,t1,rs=rs)
    fig.show()
    sys.exit()
    comutils.computetimeshow('min max',start)

    #### remove all min max traces
    idxs=[]
    for k,trace in enumerate(fig.data):
        if '_minmax' in trace.name:
            idxs.append(k)

    fig.data=[fig.data[k] for k in range(len(fig.data)) if k not in idxs]
    fig.show()

def test_resampling():
    import plotly.express as px
    rs='10s'
    listTags = streamVisu.allTags.sample(n=2)
    df = streamVisu._dfLoadparkedTags(listTags,[t0,t1],rs='raw')
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

def test_dfLoadDataBaseTags():
    start=time.time()
    # df = pd.read_sql_query("select * from realtimedata where tag='kWh_B001'",dbconn,parse_dates=['timestampz'],index_col='timestampz')
    # df = pd.read_sql_query("select * from realtimedata where tag in ('kWh_B001','kWh_A003');",dbconn,parse_dates=['timestampz'],index_col='timestampz')

    t1 = pd.Timestamp.now(tz=streamVisu.local_tzname)
    t0=t1-dt.timedelta(seconds=10*60)# only db
    timeRange = [k.isoformat() for k in [t0,t1]]
    print(timeRange)
    tags = list(streamVisu.allTags.sample(n=5))
    df = streamVisu._dfLoadDataBaseTags(tags,t0,t1,'2s')
    print(df)
    print('done in {:.2f} milliseconds'.format((time.time()-start)*1000))

def test_SetInterval():
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

def test_LoadAndpPlotCompuation():
    # generateRandomData()
    #### small computation test
    t1 = pd.Timestamp.now('CET')
    # t1 = pd.Timestamp('2021-12-17 18:00',tz='CET')
    t0 = t1-dt.timedelta(hours=0,minutes=5)
    timeRange=[t.isoformat()for t in [t0,t1]]
    start=time.time()
    # df=cfg.df_loadtagsrealtime(tags,t0,t1,True,'forwardfill','60s')
    df=cfg.df_loadtagsrealtime(tags,t0,t1,True,'raw','60s')
    print('')
    print('=============================================')
    print('full loading data in {:.2f} milliseconds'.format((time.time()-start)*1000))

    # sys.exit()
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

def test_graphs_functions():
    start = time.time()
    # t1 = pd.Timestamp.now(tz='CET')
    t1 = pd.Timestamp('2022-02-15',tz='CET')
    t0 = t1-pd.Timedelta(days=0,hours=20)
    tags1 = pd.Series(cfg.alltags).sample(n=6).to_list()
    tags2=cfg.getTagsTU('GFC_0.*PT')
    tags2+=cfg.getTagsTU('STG.*1a_TT')
    tags2+=['SEH1.STB_HER_02_JTW_01_HC20']
    df = cfg.loadtags_period(t0,t1,tags1+tags2,rsMethod='forwardfill',rs='300s',checkTime=True)

    fig  = cfg.graph_UnitsSubplots(df,facet_col_wrap=2)

    td   = cfg.toogle_tag_description(df.columns,'description')
    fig  = utilsD.Utils().customLegend(fig,td)
    fig.show()
    # sys.exit()
    # df = cfg.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs='60s',pool=False,checkTime=True)
    # df = cfg.loadtags_period(t0,t1,tags,rsMethod='max',rs='60s',checkTime=True)
    # cfg.doubleMultiUnitGraph(df,tags1,tags2).show()

def test_Indicator():
    import smallPowerDash.smallPowerTabs as sptabs
    import dash
    importlib.reload(sptabs)
    start = time.time()
    t1 = pd.Timestamp.now(tz='CET')
    t0 = t1-pd.Timedelta(days=0,hours=10)
    # tabIndicator = sptabs.RealTimeIndicatorTab(dash.Dash(),cfg)
    # df=tabIndicator.selectIndicator('fuites air',t0,t1,rsMethod='forwardfill',rs='60s')
    # modehub=cfg.getModeHub(t0,t1,rsMethod='forwardfill',rs='60s')
    # modehub=cfg.getModeHub(t0,t1,rsMethod='raw')
    df = cfg.fuitesAir(t0,t1,rsMethod='forwardfill',rs='60s')
    sys.exit()
    df = cfg.fuitesFuel(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.rendement_GV(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.rendement_blower(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.bilan_valo(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.bilan_condenseur(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.pertes_thermiques_stack(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.cosphi(t0,t1,rsMethod='forwardfill',rs='60s')
    df = cfg.repartitionPower(t0,t1,rsMethod='forwardfill',rs='60s',expand='tags')
    df = cfg.repartitionPower(t0,t1,rsMethod='forwardfill',rs='60s',expand='groups',groupnorm=None)
    fig = cfg.plotIndicator(*df)
    # fig.show()
