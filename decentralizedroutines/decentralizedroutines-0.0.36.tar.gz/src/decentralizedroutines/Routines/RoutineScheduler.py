import os
from pathlib import Path
import glob
import pandas as pd
import numpy as np
from datetime import datetime
import subprocess

import userconfig

class RoutineScheduler:

    def __init__(self,logger):
        self.logger=logger
        self.LoadSchedule()
        self.RefreshLogs()

    def LoadSchedule(self):
        self.schedule=[]
        today = datetime.now().date()
        year = today.timetuple()[0]
        month = today.timetuple()[1]
        day = today.timetuple()[2]        
        # create schedule
        schedpath = Path(userconfig.data['source_directory'])
        schedpath = schedpath / 'Routines/Schedule.xlsx'
        _sched = pd.read_excel(schedpath)
        sched = pd.DataFrame()
        for i,s in _sched.iterrows():
            runtimes = s['Run Times'].split(',')
            for t in runtimes:
                hour = int(t.split(':')[0])
                minute = int(t.split(':')[1])
                dttm = datetime(year,month,day,hour,minute)
                s['Run Times'] = pd.Timestamp(dttm)
                sched = sched.append(s)            
        sched = sched.sort_values(by=['Run Times','Name','Order']).reset_index(drop=True)
        sched['status'] = np.nan
        self.schedule = sched
        return sched

    def ReadLogs(self):
        today = datetime.now().date()
        year = today.timetuple()[0]
        month = today.timetuple()[1]
        day = today.timetuple()[2]        

        # refresh logs
        logsdir = userconfig.getLogsDirectory(userconfig.data)
        lenlogsdir = len(str(logsdir))

        files = glob.glob(str(logsdir) + "/**/*.log", recursive = True)
        # f=files[0]
        df = pd.DataFrame()
        for f in files:
            routine = f[lenlogsdir+1:].replace('.log','.py')
            try:
                _df = pd.read_csv(f,header=None,sep=';')
                _df.columns = ['type','hour','message']
                _df['routine'] = routine
                df = df.append(_df)
            except:
                pass
            
        return df

    def RefreshLogs(self):
        today = datetime.now().date()
        year = today.timetuple()[0]
        month = today.timetuple()[1]
        day = today.timetuple()[2]        

        df = self.ReadLogs()        
        sched = self.schedule
        if not df.empty:
            df = df[df['hour'].notnull()]
            df['time'] = [datetime(year, month, day,\
                int(h.split(':')[0]),int(h.split(':')[1]),int(h.split(':')[2])) \
                for h in df['hour']]
                        
            err = df[df['message']=='ROUTINE ERROR!'].reset_index(drop=True).sort_values(by='time')
            #err = df[df['type']=='ERROR'].reset_index(drop=True).sort_values(by='time')
            i=0
            for i in err.index:
                r = err.iloc[i]
                idx = sched['Script']==r['routine']
                idx = (idx) & (r['time']>=sched['Run Times'])
                if idx.any():
                    ids = idx[::-1].idxmax()
                    sched.loc[ids,'status'] = 'ERROR'
                    idx = sched.loc[idx,'status'].isnull()
                    idx = idx.index[idx]
                    sched.loc[idx,'status'] = 'EXPIRED'
            
            compl = df[df['message']=='ROUTINE COMPLETED!'].reset_index(drop=True).sort_values(by='time')
            i=0
            for i in compl.index:
                r = compl.iloc[i]
                idx = sched['Script']==r['routine']
                idx = (idx) & (r['time']>=sched['Run Times'])
                if idx.any():
                    ids = idx[::-1].idxmax()
                    sched.loc[ids,'status'] = 'COMPLETED'
                    idx = sched.loc[idx,'status'].isnull()
                    idx = idx.index[idx]
                    sched.loc[idx,'status'] = 'EXPIRED'
            
            #TODO COMPLETED WITH ERRORS!

        self.schedule = sched
        return sched

    def getPendingRoutines(self):
        pending = self.schedule[self.schedule['status'].isnull()]
        pending = pending[~pending['Script'].duplicated()]
        return pending

    def RunPendingRoutines(self):   
        today = datetime.now().date()
        year = today.timetuple()[0]
        month = today.timetuple()[1]
        day = today.timetuple()[2]        

        sched = self.schedule
        logger = self.logger
        # run pending routines
        pythonenv=userconfig.data['python']
        idx = sched['status'].isnull()
        runsched = sched[idx]
        idx = runsched['Run Times']<=pd.Timestamp.today()
        runsched = runsched[idx]
        urunroutine = runsched['Name'][idx].unique()
        if len(urunroutine)>0:
            # r = urunroutine[0]            
            for r in urunroutine:
                logger.info('Running routine %s ...' % (r))
                runnow = runsched[runsched['Name']==r]
                runnow = runnow[~runnow.duplicated('Script')].sort_values('Order')
                s = runnow.iloc[0]
                wait = runnow.shape[0]>1
                for i,s in runnow.iterrows():
                    logger.info('Executing process %s ...' % (s['Script']))
                    processpath = userconfig.getProcessPath('\\'+s['Script'])
                    env = os.environ.copy()
                    env['PYTHONPATH'] = userconfig.data['source_directory']
                    if wait:
                        sched.loc[i,'status'] = 'RUNNING'
                        # os.system('start /wait cmd /C '+pythonenv+' '+processpath)           
                        subprocess.call(pythonenv+' '+processpath,env=env)
                    else:
                        sched.loc[i,'status'] = 'RUNNING'                        
                        # os.system('start cmd /C '+pythonenv+' '+processpath)
                        subprocess.Popen([pythonenv,processpath],env=env)                                                
                    logger.info('Executing process %s DONE!' % (s['Script']))
                
                logger.info('Running routine %s DONE!' % (r))



