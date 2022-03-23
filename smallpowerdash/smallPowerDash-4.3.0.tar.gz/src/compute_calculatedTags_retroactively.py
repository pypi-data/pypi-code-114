import os,sys,pickle,glob,pandas as pd,numpy as np
import importlib
import time
##############
#  FUNCTIONS  #
##############
computetimeshow=lambda x,y:print(x + ' in {:.2f} ms'.format((time.time()-y)*1000))
from scipy.signal import butter, lfilter, freqz
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y
def alphaFilter(y, alpha):
    newy=[y[0]]
    for t in range(1,len(y)):
        newy.append(alpha*y[t]+(1-alpha)*newy[t-1])
    return newy
def cutoff2alpha(cutoff,fs):
    dt    = 1/fs
    alpha = 2*np.pi*dt / (dt + 1 / (2 * np.pi * cutoff))
    # alpha = dt / (dt + 1 / (2 * np.pi * cutoff))
    return alpha
def alpha2cutoff(alpha,dt):
    fs = 1/dt
    fc = alpha/(2*np.pi*dt*(1-alpha))
    return fc

####################
#  INITIALIZATION  #
####################
if 'sylfen' in os.getenv('HOME'):
    baseFolder = '/home/sylfen/data_ext/'
else:
    baseFolder='/home/dorian/data/sylfenData/'

folderdata=baseFolder+'smallPower_daily/'

import smallPowerDash.smallPower as smallPower
importlib.reload(smallPower)
cfg = smallPower.SmallPowerComputer(rebuildConf=True)

start=time.time()
LISTDAYS=pd.date_range(start='2022-02-14',end='2022-02-27',tz='CET')
# LISTDAYS=pd.date_range(start='2022-02-14',end='2022-02-15',tz='CET')
'''format : pd.Series with name Value and timestampz as index'''
beckhoff     = cfg.devices['beckhoff']
TAGS_CALC = beckhoff.tags_calculated
TAGS_FC      = pd.Series(dict((v,k) for k,v in beckhoff.tags_for_computation.iteritems()))
MODES_HUB={
    'SOEC':0,
    'SOFC':1,
    # 'BO':10,
    # 'BF':20,
    # 'stop':30,
    'BO':np.nan,
    'BF':np.nan,
    'stop':np.nan
}
### initialization of TAG_BUFFER_LASTDAY_VALUE
TAG_BUFFER_LASTDAY_VALUE =pd.Series({t:0 for t in TAGS_CALC.index})
TAG_BUFFER_LASTDAY_VALUE['modehub']='stop'
TAG_BUFFER_LASTDAY_VALUE.name = LISTDAYS[0]-pd.Timedelta(days=1)-pd.Timedelta(microseconds=1)
TAG_BUFFER_LASTDAY_VALUE = pd.DataFrame(TAG_BUFFER_LASTDAY_VALUE).T

start1=time.time()
###########################
#    BACK UP THE DATA IN  #
#       A ZIP FILE        #
###########################
for d in LISTDAYS:
    print()
    print(d.strftime('%d %b %H:%M:%S').rjust(50))
    # print(TAG_BUFFER_LASTDAY_VALUE.T)
    ###########################
    # LOAD THE DATA FOR A DAY #
    ###########################
    start=time.time()
    listtags_computation=beckhoff.tags_for_computation.to_list()
    t0 = d
    t1 = t0+pd.Timedelta(days=1)-pd.Timedelta(microseconds=1)
    df = cfg.loadtags_period(t0,t1,listtags_computation,rs='1s',rsMethod='forwardfill')
    # cfg.streamer.zip_day(cfg.folderPkl+d.strftime(cfg.format_dayFolder),'smallpower',baseFolder+'smallPower_daily_zip/')
    # dfparked = cfg.streamer.load_parkedtags_daily(t0,t1,listtags_computation,cfg.folderPkl,pool=True,rs='1s',rsMethod='forwardfill')
    # df = dfparked.pivot(values='value',columns='tag').sort_index()
    ##### rename df column names
    df.columns=[TAGS_FC[k] for k in df.columns]
    computetimeshow('loading data',start)
    # ================================================
    # courant en valeur absolue et convention physique
    # ================================================
    start=time.time()
    dfcalc=pd.DataFrame()
    for current_tag_name in [k for k in df.columns if 'current_stack' in k]:
        tag_current=beckhoff.tags_for_computation[current_tag_name]
        dfcalc[tag_current + '.HC09'] = df[current_tag_name].abs()
        dfcalc[tag_current + '.HC13'] = -df[current_tag_name]

    dfcalc['I_absolue']      = dfcalc[[k for k in dfcalc.columns if 'IT_HM05.HC09' in k]].sum(axis=1)
    dfcalc['I_conventionel'] = dfcalc[[k for k in dfcalc.columns if 'IT_HM05.HC13' in k]].sum(axis=1)
    computetimeshow('computing currents',start)

    # ======================
    #       modehub
    # ======================
    start=time.time()
    dfmode = pd.concat([dfcalc['I_conventionel'],df['vanneBF']],axis=1)
    dfcalc['modehub']=dfmode.apply(lambda x:beckhoff.detect_modehub(x['I_conventionel'],x['vanneBF']),axis=1)
    computetimeshow('mode hub',start)

    # ======================
    #       fuite air
    # ======================
    start=time.time()
    #--- o2 out of stack
    dfcalc['o2_out_alim'] = dfcalc['I_conventionel'].apply(beckhoff.o2_stack_alim)
    dfcalc['o2_out_hm05'] = df['air_out_ft']-df['air_in_ft']
    #--- fuites
    dffuite       = pd.concat([dfcalc[['modehub','o2_out_alim']], df[['air_in_ft','air_out_ft','n2_in_air']]],axis=1)
    dfcalc['fuite_air']     = dffuite.apply(lambda x:beckhoff.fuites_air(x['modehub'],x['o2_out_alim'],x['air_in_ft'],x['air_out_ft'],x['n2_in_air']),axis=1)
    dfcalc['fuite_air_gfd'] = dfcalc['fuite_air']/df['air_out_pt'].ffill().bfill()
    computetimeshow('fuites air',start)
    # ======================
    #       fuite fuel
    # ======================
    start=time.time()
    #--- h2 out of stack
    dfcalc['h2_out_alim'] = dfcalc['I_conventionel'].apply(beckhoff.h2_stack_out)
    dfcalc['h2_out_hm05'] = df['fuel_out_ft']-df['h2_in_ft']
    #--- fuites
    dffuite        = pd.concat([dfcalc[['modehub','h2_out_alim']], df[['h2_in_ft','fuel_out_ft','n2_in_fuel']]],axis=1)
    dfcalc['fuite_fuel']     = dffuite.apply(lambda x:beckhoff.fuites_fuel(x['modehub'],x['h2_out_alim'],x['h2_in_ft'],x['fuel_out_ft'],x['n2_in_fuel']),axis=1)
    dfcalc['fuite_fuel_gfd'] = dfcalc['fuite_fuel'].bfill()/df['fuel_out_pt'].ffill().bfill()
    computetimeshow('fuites fuel',start)

    def apply_df_functon(df,dfcalc,varargnames):
        '''varargnames should have the names of the arguments '''
        dft=df[[k for k in varargnames if k in df.columns]]
        dfc=df[[k for k in varargnames if k in dfc.columns]]
        df_fun=pd.concat([dft,dfc],axis=1)
        return df_fun.apply(lambda x:beckhoff.rendement_sys(*[x[k] for k in varargnames]),axis=1)
    # ======================
    #   rendement systeme
    # ======================
    start=time.time()
    df_rendement = pd.concat([df['power_total'],dfcalc[['modehub','h2_out_alim']]],axis=1)
    dfcalc['rendement_sys'] = df_rendement.apply(lambda x:beckhoff.rendement_sys(x['modehub'],x['power_total'],x['h2_out_alim']),axis=1)
    computetimeshow('rendements systeme',start)
    # ======================
    #   rendement gv       #
    # ======================
    start=time.time()
    df_gv = df[['tt_in_gv','tt_out_gv']]
    for gv1 in ['a','b']:
        df_gv1 = pd.DataFrame()
        df_gv1['power_elec_chauffe'] = df[[k for k in df.columns if 'power_gv_' + gv1 in k]].sum(axis=1)
        df_gv1=pd.concat([df_gv1,df_gv,df[['ft_in_gv_' + gv1]]],axis=1)
        # dfcalc.loc[:,('rendement_gv_' + gv1)] = df_gv1.apply(lambda x:beckhoff.rendement_gv(x['ft_in_gv_'+gv1],x['tt_in_gv'],x['tt_out_gv'],x['power_elec_chauffe']),axis=1)
        dfcalc['rendement_gv_' + gv1] = df_gv1.apply(lambda x:beckhoff.rendement_gv(x['ft_in_gv_'+gv1],x['tt_in_gv'],x['tt_out_gv'],x['power_elec_chauffe']),axis=1)

    computetimeshow('rendements gv',start)
    # ============================
    #   pertes thermiques stack
    # ============================
    start=time.time()
    df_pertes_stack = pd.DataFrame()
    df_pertes_stack['fuel_in_ft'] = df['h2_in_ft'] + df['h2_cold_loop_ft']
    df_pertes_stack['puissance_four'] = df[['power_chauffant_'+str(k) for k in [1,2,3]]].sum(axis=1)
    df_pertes_stack = pd.concat([df_pertes_stack,df[['air_in_tt','air_in_ft','air_stack_tt','fuel_in_tt','fuel_stack_tt']]],axis=1)
    dfcalc['pertes_stack'] = df_pertes_stack.apply(lambda x:beckhoff.pertes_thermiques_stack(x['air_in_tt'],
                                x['air_in_ft'],x['air_stack_tt'],x['fuel_in_tt'],x['fuel_in_ft'],x['fuel_stack_tt'],x['puissance_four']),axis=1)
    computetimeshow('pertes thermiques stack',start)
    # ======================
    #   compteurs, cumul
    # ======================
    start=time.time()
    # ------ tps fonctionnement T>600°C
    tps_T600 = df['T_stacks'].apply(lambda x:1 if x>600 else 0)
    dfcalc['tps_T600'] = TAG_BUFFER_LASTDAY_VALUE['tps_T600'][0]+tps_T600.cumsum()/3600

    # ------ h2 production/SOEC
    tps_SOEC = dfcalc['I_conventionel'].apply(lambda x:1 if x<-0.01 else 0)
    dfcalc['tps_SOEC']          = TAG_BUFFER_LASTDAY_VALUE['tps_SOEC'][0]+tps_SOEC.cumsum()/3600
    dfcalc['cumul_h2_produced'] = TAG_BUFFER_LASTDAY_VALUE['cumul_h2_produced'][0] + dfcalc['h2_out_hm05']*60/1000*tps_SOEC.cumsum()/3600
    # ------ h2 consommation/SOFC
    tps_SOFC = dfcalc['I_conventionel'].apply(lambda x:1 if x>0.01 else 0)
    dfcalc['tps_SOFC']          = TAG_BUFFER_LASTDAY_VALUE['tps_SOFC'][0] + tps_SOFC.cumsum()/3600
    dfcalc['cumul_h2_consumed'] = TAG_BUFFER_LASTDAY_VALUE['cumul_h2_consumed'][0] + df['h2_in_ft']*60/1000*tps_SOFC.cumsum()/3600
    # transitions
    transitions = pd.concat([TAG_BUFFER_LASTDAY_VALUE['modehub'],dfcalc['modehub']]).apply(lambda x:MODES_HUB[x])
    dfcalc['nbTransitions'] = TAG_BUFFER_LASTDAY_VALUE['nbTransitions'][0] + transitions.ffill().bfill().diff().apply(lambda x:1 if x==1 else 0).cumsum()
    computetimeshow('cumuls',start)

    # ======================
    #   check indicators
    # def checkIndicator():
    ### total current
    df_verif = pd.concat([dfcalc,df],axis=1)
    df_verif[['I_absolue']+[t for t in df_verif.columns if 'HM05.HC09' in t]]
    df_verif[['I_conventionel']+[t for t in df_verif.columns if 'HM05.HC13' in t]]
    ### mode hub
    df_verif[['modehub','I_conventionel','vanneBF']]
    ### fuites air
    df_verif[['o2_out_alim','o2_out_hm05','I_conventionel']]
    df_verif[['fuite_air','o2_out_alim','fuel_out_pt','fuite_air_gfd']]
    ### fuites fuel
    df_verif[['fuite_fuel','h2_out_alim','h2_out_hm05','fuel_out_pt','fuite_fuel_gfd']]

    # ======================
    #   apply lowpassfilter
    # ======================
    start=time.time()
    filtered_tags = {
        'fuite_air':0.001,
        'fuite_air_gfd':0.001,
        'fuite_fuel':0.001,
        'fuite_fuel_gfd':0.001,
        'rendement_sys':0.001,
        'rendement_gv_a':0.001,
        'rendement_gv_b':0.001,
        'pertes_stack':0.001
    }

    start=time.time()
    for tag,alpha in filtered_tags.items():
        dt = 1##seconds
        fs = 1/dt
        cutoff = alpha2cutoff(alpha,dt)
        period_cut=1/cutoff/60### min
        # dfcalc[t] = butter_lowpass_filter(dfcalc[tag], cutoff, fs, order=1)
        stag = pd.concat([TAG_BUFFER_LASTDAY_VALUE[tag],dfcalc[tag]]).ffill()
        dfcalc[tag] = alphaFilter(stag, alpha)[1:]


    # df_verif = pd.concat([dfcalc,df],axis=1)
    # df_verif[['fuite_air','fuite_air_lpf','o2_out_alim','o2_out_hm05']]
    computetimeshow('apply low pass filters',start)
    # ======================
    #### update the buffer for the next day
    TAG_BUFFER_LASTDAY_VALUE = pd.DataFrame(dfcalc.iloc[-1,:]).T
    # rename the keys of d_tags_hc
    dfcalc.columns = [TAGS_CALC[tagvar] for tagvar in dfcalc.columns]
    ## park the data
    start=time.time()
    folderday=cfg.folderPkl+cfg.streamer.to_folderday(d)
    for tag in dfcalc.columns:
        # print(tag)
        dftag=dfcalc[tag]
        dftag.name='value'
        dftag.to_pickle(folderday + tag + '.pkl')
    computetimeshow('parking',start)
    computetimeshow('TOTAL',start1)


import plotly.express as px
# dff = dfcalc.iloc[:,16:].resample('60s').ffill()
tags  = TAGS_CALC[16:40]
del tags['tps_GN']
# t0,t1 = LISTDAYS[0],LISTDAYS[-1]+pd.Timedelta(hours=23)
# t0,t1 = pd.Timestamp('2022-02-14',tz='CET'),pd.Timestamp('2022-02-17 00:00',tz='CET')
t0,t1 = pd.Timestamp('2022-02-14',tz='CET'),pd.Timestamp('2022-02-20 00:00',tz='CET')

tags=tags[['h2_out_hm05','h2_out_alim','I_conventionel']]
dff = cfg.loadtags_period(t0,t1,tags.to_list(),rs='600s',rsMethod='meanright')
dff = dff[tags]
# fig.write_image('/home/dorian/sylfen/log_work/cool.png',width=5500,height=700)
fig = cfg.multiUnitGraphSP(dff)
fig = cfg.addTagEnveloppe(fig,'SEH1.STB_H2_FT.HC20',t0,t1,'600s')
td  = {k:k+':'+v for k,v in  cfg.toogle_tag_description(dff.columns,'description').items()}
# fig = cfg.utils.customLegend(fig,td)
fig.update_layout(legend=dict(yanchor="bottom",y=1.01,xanchor="left",x=0.01),
font_size=30,font_family="Calibri")

folderPictures='/home/dorian/sylfen/reports/rapportsAlpha/rapportGuillaumeDorian/figures/'
fig.write_image(folderPictures+'cool2.png',width=2500)
# fig.show()
