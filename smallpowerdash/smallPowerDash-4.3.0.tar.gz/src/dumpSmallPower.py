#!/bin/python
######      IMPORTANT  FOR OPCUA        #####
# GENERATE A PRIVATE KEY AND A CERTIF WITH COMMAND
## openssl req -x509 -newkey rsa:4096 -keyout <key.pem> -out <cert.pem> -days 7200 -nodes
## or take an existing certif/key pair
# do not forget to change pg_hba.conf and restart server +
# change password of uer postgres with :
# alter user <postgres> password '<newpassword>';

import importlib
import os
import dorianUtils.comUtils as comUtils
import time,datetime as dt,sys
importlib.reload(comUtils)
import smallPowerDash.smallPower as smallPower
importlib.reload(smallPower)
start=time.time()
dumperSmallPower = smallPower.SmallPower_dumper()

dumperSmallPower.park_database()

# dumperSmallPower.start_dumping()

# ==============================================================================
#                           TESTS
import pandas as pd
beckhoff=dumperSmallPower.devices['beckhoff']
def testInsert_intodb():
    start = time.time()
    quickTags = dumperSmallPower.dumpInterval['beckhoff'][0.1].argsAction[1]
    slowTags = dumperSmallPower.dumpInterval['beckhoff'][1].argsAction[1]
    beckhoffclient = dumperSmallPower.devices['beckhoff']
    tags=quickTags
    # d=beckhoffclient.collectData(tags)
    c=beckhoffclient.insert_intodb(dumperSmallPower.dbParameters,tags)
    c=beckhoffclient.insert_intodb(dumperSmallPower.dbParameters,slowTags)
    # df=pd.DataFrame(d).T
    print('insert into database done in {:.2f} milliseconds'.format((time.time()-start)*1000))

def test_calculatedtags():
    # sys.exit()
    d  = beckhoff.compute_calculated_tags()
    df = pd.DataFrame(d).T
    df.columns=['value','timestamp']
    tagnames = pd.Series(dict((v,k) for k,v in beckhoff.tags_calculated.iteritems()))
    df['description'] = df.reset_index()['index'].apply(lambda x:tagnames[x]).to_list()
    df = df.reset_index().set_index('description')[['value','timestamp','index']]
    # dumperSmallPower.insert_calctags_intodb()

def testCreateFolders():
    t1=dt.datetime(2021,11,10,10,30)
    # t0=t1-dt.timedelta(days=0,hours=0,minutes=15)#single day-hour
    # t0=t1-dt.timedelta(days=0,hours=5,minutes=15)#single day
    # t0=t1-dt.timedelta(days=1,hours=5,minutes=15)#2 days
    t0=t1-dt.timedelta(days=2,hours=5,minutes=15)#more than 2 days
    foldersCreated=streaming.foldersaction(t0,t1,dumperSmallPower.folderPkl,streaming.createminutefolder)

def testparktagfromdb():
    tag = 'SEH0.JT_02.JTVA_HC20'
    t1 = dt.datetime(2021,11,10,10,29,59)
    t0 = t1-dt.timedelta(days=0,hours=0,minutes=2,seconds=59)

    #feed db with random data
    dbconn = dumperSmallPower.connect2db()
    dumperSmallPower.feed_db_random_data(t0,t1,[tag])

    #parkage
    foldersCreated=streaming.foldersaction(t0,t1,dumperSmallPower.folderPkl,streaming.createminutefolder)
    sqlQ ="select * from realtimedata;"
    # df = pd.read_sql_query(sqlQ,dbconn,parse_dates=['timestampz'],dtype={'value':'float'})
    df = pd.read_sql_query(sqlQ,dbconn,parse_dates=['timestampz'])
    dbconn.close()
    dfs=dumperSmallPower.parktagfromdb(t0,t1,df,tag,'no')

    # quick load data parked minute check
    import pickle
    foldermin=dumperSmallPower.folderPkl + t0.strftime(streaming.dayFolderFormat) + '/10/'
    dfout1=pickle.load(open(foldermin + '28/' + tag + '.pkl','rb'))

def testparktagallfromdb():
    dumperSmallPower.parkingTime=60*2
    t1 = dt.datetime.now().astimezone()
    t0 = t1-dt.timedelta(minutes=5)
    ### # flushdb first
    # dumperSmallPower.flushdb(5,full=True)
    #feed db with random data
    start = time.time()
    # df = dumperSmallPower.generateRandomParkedData(t0,t1)
    dumperSmallPower.feed_db_random_data(t0,t1)
    print('fed in {:.2f} milliseconds'.format((time.time()-start)*1000))
    start = time.time()
    #parkage
    dfs = dumperSmallPower.parkallfromdb()
    print('parked in {:.2f} milliseconds'.format((time.time()-start)*1000))
    # sys.exit()

    # quick load data parked minute check
    import pickle
    tag = pd.Series(dumperSmallPower.allTags).sample(n=1).squeeze()
    folderminute = dumperSmallPower.folderPkl + t0.strftime(streaming.dayFolderFormat + '/%H/%M/')
    dfout1 = pickle.load(open(folderminute + tag + '.pkl','rb'))
    d2=dumperSmallPower.folderPkl + '2021-12-10/12/27/'
    pickle.load(open(d2 + tag + '.pkl','rb'))

def test_justparkallfromdb():
    import pickle, pandas as pd
    dfs = dumperSmallPower.parkallfromdb()
    tag = pd.Series(dumperSmallPower.allTags).sample(n=1).squeeze()
    foldermin=dumperSmallPower.folderPkl+'2021-12-10/13/'
    df=pickle.load(open(foldermin + '10' '/' + tag + '.pkl','rb'))
    df.index=df.index.tz_convert('CET')
    df

def testSetInterval():
    from time import sleep
    import numpy as np
    def sleepabit(initValue=0.9):
        t0 = dt.datetime.now().astimezone()
        print('start time task : ',t0.strftime('%H:%M:%S:%f')[:-4])
        value =initValue+np.random.randint(0,20)/100
        print('duration task : ',value)
        print('')
        sleep(value)

    ## initialize a M:S:000 pétante ! #####
    now =dt.datetime.now().astimezone()
    time.sleep(1-now.microsecond/1000000)
    setTest=comUtils.SetInterval(1,sleepabit,0.99)
    setTest.start()

def testStaticCompressionOnMonitoringData():
    # s=df.iloc[:,0]
    # s2=streaming.staticCompressionTag(s,s.std(),method='reduce')

    s=streaming.generateRampPlateau(nbpts=200)
    precs=np.logspace(-2,0,6)*5
    results = streaming.testCompareStaticCompression(s,precs)

def test_reconnection():
    dfplc=dumperSmallPower.dfPLC
    tags = list(dfplc.index[dfplc['FREQUENCE_ECHANTILLONNAGE']==0.1])
    quickNodes = {t:dumperSmallPower.nodesDict[t] for t in tags}
    for k in range(2):
            # d=dumperSmallPower.collectData(quickNodes)
            c=dumperSmallPower.insert_intodb(quickNodes)
            time.sleep(0.2)

def checkTimes():
    dict2pdf = lambda d:pd.DataFrame.from_dict(d,orient='index').squeeze().sort_values()
    s_collect = dict2pdf(dumperSmallPower.collectingTimes)
    s_insert  = dict2pdf(dumperSmallPower.insertingTimes)

    p = 1. * np.arange(len(s_collect))
    ## first x axis :
    tr1 = go.Scatter(x=p,y=df,name='collectingTime',col=1,row=1)
    ## second axis
    tr2 = go.Scatter(x=p,y=df,name='collectingTime',col=1,row=2)
    title1='cumulative probability density '
    title2='histogramm computing times '
    # fig.update_layout(titles=)
