import os

class DirX:
    def Directory():
        str_x = os.getcwd().split('/')
        if str_x[2] == 'frankie':
            if str_x[3] == 'Library':
                Directory = '/Users/frankie/Library/Mobile Documents/com~apple~CloudDocs/TradingProject/'
            elif str_x[3] == 'PycharmProjects':
                Directory = '/Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/'
            else:
                raise ValueError('Frankie_dir must exist')
        elif str_x[2] == 'alessandroborsatti':
            if str_x[3] == 'Library':
                Directory = '/Users/alessandroborsatti/Library/Mobile Documents/com~apple~CloudDocs/TradingProject/'
            elif str_x[3] == 'PycharmProjects':
                Directory = '/Users/alessandroborsatti/PycharmProjects/PycharmProjectsShared/TradingProject/'
            else:
                raise ValueError('AB_dir must exist')
        else:
            raise ValueError('Directory must exist')
        return [Directory]

    def DirectoryLocal():
        str_x = os.getcwd().split('/')
        if str_x[2] == 'frankie':
            Directory_Local = '/Users/frankie/PycharmProjects/PycharmProjectsShared/TradingProject/'
        elif str_x[2] == 'alessandroborsatti':
            Directory_Local = '/Users/alessandroborsatti/PycharmProjects/PycharmProjectsShared/TradingProject/'
        else:
            raise ValueError('Local Dir must exist')
        return Directory_Local

    def DirectoryCloud():
        str_x = os.getcwd().split('/')
        if str_x[2] == 'frankie':
            Directory_Local = '/Users/frankie/Library/Mobile Documents/com~apple~CloudDocs/TradingProject/'
        elif str_x[2] == 'alessandroborsatti':
            Directory_Local = '/Users/alessandroborsatti/Library/Mobile Documents/com~apple~CloudDocs/TradingProject/'
        else:
            raise ValueError('Local Dir must exist')
        return Directory_Local

    Dir_Exp_Run=DirectoryLocal()

    def FileOrder(Mininbars): # integer needed
        Fldict = {1:'-A-',5:'-B-',10:'-C-',15:'-D-',30:'-E-'}
        FileOrder = (Fldict.get(Mininbars))
        return FileOrder

    def DivByZero_int(a,b):
        if b==0.0:
            Res=0
        elif b==0.0 and a==0.0:
            Res=0
        else:
            Res=a/b
        return Res

    def DivByZero_float(a,b):
        if b==0.0:
            Res=0.0
        elif b==0.0 and a==0.0:
            Res=0.0
        else:
            Res=a/b
        return Res

    def RunCSV_Saver(fromdate, DirectoryTrigger):
        dataTF_list = ['1min', '5min', '10min', '15min', '30min']
        for i in range(len(dataTF_list)):
            try:
                import pandas as pd
                print(dataTF_list[i] + ' Processing')
                dataname_P = Directory + 'CME_MINI_NQ1!Actual_'+ dataTF_list[i] +'.parquet'
                DATA = pd.read_parquet(dataname_P)
                print(dataTF_list[i] + ' parquet present')
                DATA = DATA.loc[DATA.index > fromdate]

                dataname_Run = DirectoryTrigger + 'CME_MINI_NQ1!Actual_'+ dataTF_list[i] +'_RUN.csv'

                DATA.to_csv(dataname_Run, sep=',' )
                print(dataTF_list[i] + ' Saved')
                print('-')
            except:
                print(dataTF_list[i] + ' parquet Missing')
        return RunCSV_Saver