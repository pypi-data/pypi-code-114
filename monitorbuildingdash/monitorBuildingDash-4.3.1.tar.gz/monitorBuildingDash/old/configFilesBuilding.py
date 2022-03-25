import pytz,pandas as pd, numpy as np,datetime as dt,pickle, os, glob,re
from dorianUtils.configFilesD import ConfigDashTagUnitTimestamp,ConfigDashRealTime,ConfigFilesRealTimeCSV
from multiprocessing import Process, Queue, current_process,Pool
from scipy import integrate
from pandas.tseries.frequencies import to_offset
import plotly.express as px


class ConfigFilesBuilding(ConfigDashTagUnitTimestamp):
    # ==========================================================================
    #                       INIT FUNCTIONS
    # ==========================================================================

    def __init__(self,folderPkl,pklMeteo=None,folderFig=None,folderExport=None,encode='utf-8'):
        self.appDir  = os.path.dirname(os.path.realpath(__file__))
        self.confFolder = self.appDir +'/confFiles/'
        ConfigDashTagUnitTimestamp.__init__(self,folderPkl,self.confFolder)
        self.rsMinDefault   = 15
        self.listCompteurs  = pd.read_csv(self.confFolder+'/compteurs.csv')
        self.listVars       = self._readVariables()
        self.dfPLCMonitoring = self._buildDescriptionDFplcMonitoring()
        self.dfMeteoPLC     = self._loadPLCMeteo()
        self.dfPLC          = self._mergeMeteoMonitoringPLC()
        self.listUnits      = list(self.dfPLC.UNITE.unique())
        self.listCalculatedVars = None
        self.pklMeteo       = pklMeteo
        self.listFilesMeteo = self.utils.get_listFilesPklV2(self.pklMeteo)
        try :
            a=[k.split('/')[-1] for k in glob.glob(self.folderPkl + '/parkedData/*')]
            a.sort()
            self.listParked = a
        except: print('not folder parkedData in ',self.folderPkl)
        self.dfPLC= self.dfPLC.set_index('TAG')
        self.listCompteurs = [k.split('-')[1] for k in list(self.listCompteurs.Compteurs) if 'VIRTUAL' not in k]

    def _readVariables(self):
        x1=pd.ExcelFile(self.confFolder+'/variables.ods')
        return {s:pd.read_excel(self.confFolder+'/variables.ods',sheet_name=s) for s in x1.sheet_names}

    def exportToxcel(self,df):
        df.index = [t.astimezone(pytz.timezone('Etc/GMT-2')).replace(tzinfo=None) for t in df.index]
        df.to_excel(dt.date.today().strftime('%Y-%m-%d')+'.xlsx')

    def getListVarsFromPLC(self):
        def getListCompteursFromPLC(self,regExpTagCompteur='[a-zA-Z][0-9]+-\w+'):
            return list(np.unique([re.findall(regExpTagCompteur,k)[0] for k in self.dfPLC.TAG]))
        listVars = self.getTagsTU(getListCompteursFromPLC()[0])
        listVars = [re.split('(h-)| ',k)[2] for k in listVars]
        return listVars

    def _loadPLCMeteo(self):
        dfPLC       = pd.read_csv(self.appDir + '/confFiles/configurationMeteo.csv')
        dfPLC.TAG = dfPLC.TAG.apply(lambda x: x.replace('SIS','SIS-02'))
        return dfPLC

    def _buildDescriptionDFplcMonitoring(self):
        self.confFile = 'build from listVars.csv and listCompteurs.csv'
        tagDess,tagIds,unites=[],[],[]
        for c in self.listCompteurs.iterrows():
            compteurName = c[1][1]
            compteurId = c[1][0]
            if compteurId[0]=='C':
                listVars=self.listVars['triphase']
            elif compteurId[:2]=='PV':
                listVars=self.listVars['PV']
            elif compteurId[0]=='M':
                listVars=self.listVars['monophase']

            for v in listVars.iterrows():
                varName = v[1][1]
                varId = v[1][0]
                tagDess.append(compteurName + ' ' + varName)
                tagIds.append(compteurId + '-' + varId)
                # print(compteurId + '-' + varId)
                unites.append(v[1][2])
        dfPLC =  pd.DataFrame(data={'TAG':tagIds,'UNITE':unites,'DESCRIPTION':tagDess})
        # dfPLC['MIN']  = 0
        # dfPLC['MAX']  = 0
        # dfPLC['TYPE'] = 'float'
        return dfPLC

    def _mergeMeteoMonitoringPLC(self):
        tagToday    = self._getListMeteoTags()
        dfMeteoPLC  = self.dfMeteoPLC[self.dfMeteoPLC.TAG.isin(tagToday)]#keep only measured data not predictions
        dfPLC=pd.concat([self.dfPLCMonitoring,dfMeteoPLC])
        dfPLC.to_csv(self.confFolder+'/screenBuilding-10001-001-ConfigurationPLC.csv')
        return dfPLC

    def _getListMeteoTags(self):
        return list(self.dfMeteoPLC[self.dfMeteoPLC.TAG.str.contains('-[A-Z]{2}-01-')].TAG)

    def _getListMeteoTagsDF(self,df):
        return list(df[df.tag.str.contains('-[A-Z]{2}-01-')].tag.unique())

    # ==============================================================================
    #                   functions filter on dataFrame
    # ==============================================================================
    def loadFileMeteo(self,filename):
        if '*' in filename :
            filenames=self.utils.get_listFilesPklV2(self.pklMeteo,filename)
            if len(filenames)>0 : filename=filenames[0]
            else : return pd.DataFrame()
        df = pickle.load(open(filename, "rb" ))
        df.tag   = df.tag.apply(lambda x:x.replace('@',''))#problem with tag remove @
        df.tag   = df.tag.apply(lambda x:x.replace('_','-'))#
        tagToday = self._getListMeteoTagsDF(df)
        # tagToday = self._getListMeteoTags()
        # print(tagToday)
        # print(df.tag.unique())
        df       = df[df.tag.isin(tagToday)]#keep only measured data not predictions
        df.timestampUTC = pd.to_datetime(df.timestampUTC,utc=True)# convert datetime to utc
        return df

    def loadFileMonitoring(self,filename):
        return self.loadFile(filename)

    def _DF_fromTagList(self,df,tagList,rs):
        df = df.drop_duplicates(subset=['timestampUTC', 'tag'], keep='last')
        if not isinstance(tagList,list):tagList =[tagList]
        df = df[df.tag.isin(tagList)]
        if not rs=='raw':df = df.pivot(index="timestampUTC", columns="tag", values="value")
        else : df = df.sort_values(by=['tag','timestampUTC']).set_index('timestampUTC')
        return df

    def _loadDFTagsDayMeteoBuilding(self,datum,listTags,rs):
        realDatum = self.utils.datesBetween2Dates([datum,datum],offset=+1)[0][0]
        dfMonitoring  = self.loadFileMonitoring('*'+realDatum+'*')
        dfMeteo       = self.loadFileMeteo('*'+realDatum+'*')
        if not dfMonitoring.empty : dfMonitoring = self._DF_fromTagList(dfMonitoring,listTags,rs)
        if not dfMeteo.empty : dfMeteo = self._DF_fromTagList(dfMeteo,listTags,rs)
        if rs=='raw':
            df = pd.concat([dfMonitoring,dfMeteo],axis=1)
            # tmp = list(df.columns);tmp.sort();df=df[tmp]
        df = pd.concat([dfMonitoring,dfMeteo],axis=0)
        return df
        # return dfMonitoring

    # ==========================================================================
    #                       COMPUTATIONS FUNCTIONS
    # ==========================================================================
    def computePowerEnveloppe(self,timeRange,compteur = 'EM_VIRTUAL',rs='auto'):
        listTags = self.getTagsTU(compteur+'.+[0-9]-JTW','kW')
        df = self.DF_loadTimeRangeTags(timeRange,listTags,rs='5s')
        L123min = df.min(axis=1)
        L123max = df.max(axis=1)
        L123moy = df.mean(axis=1)
        L123sum = df.sum(axis=1)
        df = pd.concat([df,L123min,L123max,L123moy,L123sum],axis=1)

        from dateutil import parser
        ts=[parser.parse(t) for t in timeRange]
        deltaseconds=(ts[1]-ts[0]).total_seconds()
        if rs=='auto':rs = '{:.0f}'.format(max(1,deltaseconds/1000)) + 's'
        df = df.resample(rs).apply(np.mean)
        dfmin = L123min.resample(rs).apply(np.min)
        dfmax = L123max.resample(rs).apply(np.max)
        df = pd.concat([df,dfmin,dfmax],axis=1)
        df.columns=['L1_mean','L2_mean','L3_mean','PminL123_mean','PmaxL123_mean',
                    'PmoyL123_mean','PsumL123_mean','PminL123_min','PmaxL123_max']
        return df

    def _integratePowerCol(self,df,tag,pool):
        print(tag)
        x1=df[df.tag==tag]
        if not x1.empty:
            timestamp=x1.index
            x1['totalSecs']=x1.index.to_series().apply(lambda x: (x-x1.index[0]).total_seconds())/3600
            x1=pd.DataFrame(integrate.cumulative_trapezoid(x1.value,x=x1.totalSecs))
            x1.index=timestamp[1:]
            x1.columns=[tag]
        return x1

    def compute_kWhFromPower(self,timeRange,compteurs=['B001'],rs='raw'):
        generalPat='('+'|'.join(['(' + c + ')' for c in compteurs])+')'
        listTags = self.getTagsTU(generalPat+'.*sys-JTW')

        df = self.DF_loadTimeRangeTags(timeRange,listTags,rs=rs,applyMethod='mean',pool=True)
        dfs=[]
        for tag in listTags:
            dftmp = self._integratePowerCol(df,tag,True)
            if not dftmp.empty:dfs.append(dftmp)

        try : df=pd.concat(dfs,axis=1)
        except : df = pd.DataFrame()
        return df.ffill().bfill()

    def compute_kWhFromCompteur(self,timeRange,compteurs=['B001']):
        generalPat='('+'|'.join(['(' + c + ')' for c in compteurs])+')'
        listTags = self.getTagsTU(generalPat+'.+kWh-JTWH')
        df = self.DF_loadTimeRangeTags(timeRange,listTags,rs='raw',applyMethod='mean')
        df = df.drop_duplicates()
        dfs=[]
        for tag in listTags:
            x1=df[df.tag==tag]
            dfs.append(x1['value'].diff().cumsum()[1:])
        try :
            df = pd.concat(dfs,axis=1)
            df.columns = listTags
        except : df = pd.DataFrame()
        return df.ffill().bfill()

    def plot_compare_kwhCompteurvsPower(self,timeRange,compteurs=['B001'],rs='600s'):
        dfCompteur = self.compute_kWhFromCompteur(timeRange,compteurs)
        dfPower = self.compute_kWhFromPower(timeRange,compteurs)
        df = self.utils.prepareDFsforComparison([dfCompteur,dfPower],
                            ['energy from compteur','enery from Power'],
                            group1='groupPower',group2='compteur',
                            regexpVar='\w+-\w+',rs=rs)

        fig=px.line(df,x='timestamp',y='value',color='compteur',line_dash='groupPower',)
        fig=self.utils.quickLayout(fig,'energy consumed from integrated power and from energy counter',ylab='kWh')
        fig.update_layout(yaxis_title='energy consommée en kWh')
        return fig

    def energyPeriodBarPlot(self,timeRange,period='1d',compteurs = ['A003','B001']):
        dfCompteur   = self.compute_kWhFromCompteur(timeRange,compteurs)
        df = dfCompteur.resample(period).first().diff()[1:]
        fig = px.bar(df,title='répartition des énergies consommées par compteur')
        fig.update_layout(yaxis_title='énergie en kWh')
        fig.update_layout(bargap=0.5)
        return fig
    # ==========================================================================
    #                       for website monitoring
    # ==========================================================================
    def generateFilename(self,proprietaire='MJ',client='*',batiment='*',local='*'):
        return '-'.join([proprietaire,client,batiment,local])

    def getListTagsAutoConso(self,compteurs):
        pTotal = [self.getTagsTU(k + '.*sys-JTW')[0] for k in compteurs]
        pvPower = self.getTagsTU('PV.*-JTW-00')[0]
        listTagsPower = pTotal + [pvPower]
        energieTotale = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in compteurs]
        pvEnergie = self.getTagsTU('PV.*-JTWH-00')[0]
        listTagsEnergy = energieTotale + [pvEnergie]
        return pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy

    def computeAutoConso(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.DF_loadTimeRangeTags(timeRange,listTagsPower,'600s','mean')
        df = self.DF_loadTimeRangeTags_cfd(timeRange,listTagsPower,'600s','mean')
        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k+'.*sys-JTW')[0] for k in ['GENERAL','E001','F001',]]
            df['puissance totale'] = df[g] + df[f] - df[e] + df[pvPower]
        elif formula=='sum-pv':
            df['puissance totale'] = df[pTotal].sum(axis=1) - df[pvPower]
        elif formula=='sum':
            df['puissance totale'] = df[pTotal].sum(axis=1)

        df['diffPV']=df[pvPower]-df['puissance totale']
        dfAutoConso = pd.DataFrame()
        df['zero'] = 0
        dfAutoConso['part rSoc']     = 0
        dfAutoConso['part batterie'] = 0
        dfAutoConso['part Grid']     = -df[['diffPV','zero']].min(axis=1)
        dfAutoConso['Consommation du site']      = df['puissance totale']
        dfAutoConso['surplus PV']    = df[['diffPV','zero']].max(axis=1)
        dfAutoConso['part PV']       = df[pvPower]-dfAutoConso['surplus PV']
        # dfAutoConso['Autoconsommation'] = df[pvPower]-dfAutoConso['PV surplus']
        return dfAutoConso

    def consoPowerWeek(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.DF_loadTimeRangeTags(timeRange,listTagsPower,'1H','mean')
        df = self.DF_loadTimeRangeTags_cfd(timeRange,listTagsPower,'1H','mean')

        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k+'.*sys-JTW')[0] for k in ['GENERAL','E001','F001',]]
            df['puissance totale'] = df[g] + df[f] - df[e] + df[pvPower]
        elif formula=='sum-pv':
            df['puissance totale'] = df[pTotal].sum(axis=1) - df[pvPower]
        elif formula=='sum':
            df['puissance totale'] = df[pTotal].sum(axis=1)

        df = df[['puissance totale',pvPower]]
        df.columns = ['consommation bâtiment','production PV']
        return df

    def compute_EnergieMonth(self,timeRange,compteurs,formula='g+f-e+pv'):
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        # df = self.DF_loadTimeRangeTags(timeRange,listTagsEnergy,rs='raw',applyMethod='mean')
        df = self.DF_loadTimeRangeTags_cfd(timeRange,listTagsEnergy,rs='raw',applyMethod='mean')
        df = df.drop_duplicates()

        df=df.pivot(columns='tag',values='value').resample('1d').first().ffill().bfill()
        newdf=df.diff().iloc[1:,:]
        newdf.index = df.index[:-1]
        if formula=='g+f-e+pv':
            g,e,f = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in ['GENERAL','E001','F001',]]
            newdf['energie totale'] = newdf[g] + newdf[f] - newdf[e] + newdf[pvEnergie]
        elif formula=='sum-pv':
            newdf['energie totale'] = newdf[pTotal].sum(axis=1) - newdf[pvEnergie]
        elif formula=='sum':
            newdf['energie totale'] = newdf[energieTotale].sum(axis=1)

        newdf = newdf[['energie totale',pvEnergie]]
        newdf.columns = ['kWh consommés','kWh produits']
        return newdf

    def get_compteur(self,timeDate,compteurs,formula='g+f-e+pv'):
        timeRange = [k.isoformat() for k in [timeDate - dt.timedelta(seconds=600),timeDate]]
        pTotal,pvPower,listTagsPower,energieTotale,pvEnergie,listTagsEnergy = self.getListTagsAutoConso(compteurs)
        df = self.DF_loadTimeRangeTags_cfd(timeRange,listTagsEnergy,rs='20s',applyMethod='mean')
        g,e,f = [self.getTagsTU(k + '.*kWh-JTWH')[0] for k in ['GENERAL','E001','F001',]]
        if formula=='g+f-e+pv':
            df['energie totale'] = df[g] + df[f] - df[e] + df[pvEnergie]
        elif formula=='sum':
            df['energie totale'] = df[energieTotale].sum(axis=1)
        return df.iloc[-1,:]

class ConfigFilesBuildingRealTime(ConfigDashRealTime):
    def __init__(self,connParameters=None):
        self.appDir  = os.path.dirname(os.path.realpath(__file__))
        if not connParameters : connParameters ={
            'host'     : "192.168.1.44",
            'port'     : "5434",
            'dbname'   : "BigBrother",
            'user'     : "postgres",
            'password' : "SylfenBDD"
        }
        self.connParameters=connParameters
        confFolder = self.appDir +'/confFiles/'
        ConfigDashRealTime.__init__(self,confFolder,self.connParameters)

    def parseDataBaseTags(self):
        conn = self.connectToDB()
        import dorianUtils.utilsD as utilsD
        db = utilsD.DataBase()
        df = db.readSQLdataBase(conn,"",secs=60)
        lTags = df.tag.unique()
        listUnits = np.unique(['-'.join(s.split('-')[3:]) for s in lTags])
        return lTags,listUnits

class ConfigFilesBuildingRealTimeCSV(ConfigFilesRealTimeCSV):
    def __init__(self,folderRT):
        self.appDir  = os.path.dirname(os.path.realpath(__file__))
        confFolder = self.appDir +'/confFiles/'
        ConfigFilesRealTimeCSV.__init__(self,folderRT,confFolder)
