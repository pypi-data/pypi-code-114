import dorianUtils.comUtils as com
import importlib, pandas as pd
import glob,os
# importlib.reload(com)
if 'sylfen' in os.getenv('HOME'):
    baseFolder = '/home/sylfen/data_ext/'
    CONFFOLDER='/home/sylfen/.venv/venv_smallpower/lib/python3.8/site-packages/smallPowerDash/confFiles/'
else:
    CONFFOLDER='/home/dorian/sylfen/exploreSmallPower/smallPowerDash/confFiles/'

FILE_PLC_XLSM = glob.glob(CONFFOLDER+'*ALPHA*.xlsm')[0]
PLC_BECKHOFF  = CONFFOLDER + 'plc_smallpower.pkl'
dfplc =pd.read_excel(FILE_PLC_XLSM,sheet_name='FichierConf_Jules',index_col=0)

beckhoff=com.Opcua_Client(device_name='beckhoff',endpointUrl='opc.tcp://10.10.38.100',port=4840,
                dfplc=dfplc,
                nameSpace="ns=4;s=GVL.")

certif_path = CONFFOLDER + 'my_cert.pem'
key_path    = CONFFOLDER + 'my_private_key.pem'
sslString   = 'Basic256Sha256,Sign,' + certif_path + ',' + key_path
beckhoff.client.set_security_string(sslString)
beckhoff.client.set_user("Alpha")
beckhoff.client.set_password("Alpha$01")
beckhoff.client.connect() #====>cause problem with multiprocessing

nodes_SN={k:v for k,v in beckhoff.nodesDict.items() if 'SN' in k }
beckhoff.collectData(nodes_SN)
