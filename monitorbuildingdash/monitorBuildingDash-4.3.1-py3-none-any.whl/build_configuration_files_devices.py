import dorianUtils.comUtils as comUtils
import importlib, os,glob,re,pandas as pd,sys
import xml.etree.ElementTree as ET

REBUILD={
'vmuc':True,
'gtc_alstom':True,
'smartlogger':True,
'site_sls':True,
}

importlib.reload(comUtils)
fs = comUtils.FileSystem()
appdir    = os.path.dirname(os.path.realpath(__file__))
PARENTDIR = fs.getParentDir(appdir)
CONFFOLDER = PARENTDIR+'monitorBuildingDash/confFiles/'

file_devices = glob.glob(CONFFOLDER + '*devices*.ods')[0]
v_devices    = re.findall('_v\d+',file_devices)[0]
df_devices   = pd.read_excel(file_devices,index_col=0,sheet_name='devices')
VARIABLES    = pd.read_excel(file_devices,index_col=0,sheet_name='variables')
COMPTEURS    = pd.read_excel(file_devices,index_col=0,sheet_name='compteurs')
dictCat      = df_devices.category.to_dict()

UNITS_DICT = {'kW':'JTW','kWh':'JTWH','kVA':'JTVA','kvar':'JTVar','kvarh':'JTVarH','kVAh':'JTVAH'}
#################################################
#   build full name of compteurs for categories #
#################################################
COMPTEURS['fullname']=list(COMPTEURS.reset_index().apply(lambda x:dictCat[x['device']] + '-' + x['pointComptage']+'-',axis=1))
for cat in ['C','PV']:
    devices = list(df_devices[df_devices.category==cat].index)
    locCompteurs = COMPTEURS[COMPTEURS.device.isin(devices)].reset_index()
    if not locCompteurs.empty:
        compteursNumber = locCompteurs.reset_index().index.to_series().apply(lambda x:'{:x}'.format(x+1).zfill(8))
        fullnames       = cat + compteursNumber + '-' + locCompteurs['pointComptage']
        COMPTEURS.loc[locCompteurs['pointComptage'],'fullname'] = list(fullnames)

###############
#  FUNCTIONS  #
###############

def makemodebus_mapUnique(modebus_map):
    '''make modebus_map unique'''
    uniquemodebus_map = []
    for tag in modebus_map['id'].unique():
        dup=modebus_map[modebus_map['id']==tag]
        ### privilege on IEEE754 strcuture if duplicates
        rowFloat = dup[dup['type']=='IEEE754']
        if len(rowFloat)==1:
            uniquemodebus_map.append(rowFloat)
        else :
            uniquemodebus_map.append(dup.iloc[[0]])
    uniquemodebus_map=pd.concat(uniquemodebus_map).set_index('id')
    return uniquemodebus_map

def build_plc_from_modebus_map(modebus_map):
    dfplc = pd.DataFrame()
    dfplc['DESCRIPTION'] = modebus_map.apply(lambda x:VARIABLES.loc[x['description'],'description']+ ' ' + COMPTEURS.loc[x['point de comptage'],'description'],axis=1)
    dfplc['UNITE']       = modebus_map['unit'].apply(lambda x:UNITS_DICT[x])
    # dfplc.index    = modebus_map.index
    dfplc['MIN']      = -200000
    dfplc['MAX']      = 200000
    dfplc['DATATYPE'] = 'REAL'
    dfplc['DATASCIENTISM'] = True
    dfplc['PRECISION'] = 0.01
    dfplc['VAL_DEF'] = 0
    return dfplc

def getSizeOf(typeVar,f=1):
    if typeVar == 'IEEE754':return 2*f
    elif typeVar == 'INT64': return 4*f
    elif typeVar == 'INT32': return 2*f
    elif typeVar == 'INT16': return 1*f
    elif typeVar == 'INT8': return f/2

def parseXML_VMUC(xmlpath):
    def findInstrument(meter):
        df=[]
        for var in meter.iter('var'):
            df.append([var.find('varaddr').text,
                int(var.find('varaddr').text[:-1],16),
                var.find('vartype').text,
                getSizeOf(var.find('vartype').text,1),
                getSizeOf(var.find('vartype').text,2),
                var.find('vardesc').text,
                var.find('scale').text,
                var.find('unit').text]
                )
        df = pd.DataFrame(df)
        df.columns=['adresse','intAddress','type','size(mots)','size(bytes)','description','scale','unit']
        df['slave_unit'] = meter.find('addrTCP').text
        df['point de comptage']=meter.find('desc').text
        return df

    tree = ET.parse(xmlpath)
    root = tree.getroot()
    dfs=[]
    for meter in root.iter('meter'):
        dfs.append(findInstrument(meter))
    df=pd.concat(dfs)
    df['id']=[re.sub('[\( \)]','_',k) + '_' + l for k,l in zip(df['description'],df['point de comptage'])]
    df['slave_unit'] = pd.to_numeric(df['slave_unit'],errors='coerce')
    df['scale'] = pd.to_numeric(df['scale'],errors='coerce')
    return df

################W######
#        VMUC         #
################W######
vmuc_file_xml_   = CONFFOLDER + 'vmuc_ModbusTCP_Map_2022_01_10.xml'
if REBUILD['vmuc']:
    vmuc_modebus_map = parseXML_VMUC(vmuc_file_xml_)
    vmuc_modebus_map = makemodebus_mapUnique(vmuc_modebus_map)
    ############ keep only variables of interest
    var_vmuc = ['kW sys','kWh','kW L1', 'kW L2', 'kW L3','kVA L1', 'kVA L2', 'kVA L3','kWh L1', 'kWh L2', 'kWh L3']
    vmuc_modebus_map = vmuc_modebus_map[vmuc_modebus_map.description.isin(var_vmuc)]
    ############# appliquer la convention de nommage pour la definition des tags
    vmuc_modebus_map.index=vmuc_modebus_map.apply(lambda x:COMPTEURS.loc[x['point de comptage'],'fullname']+'-'+x['description']+'-'+UNITS_DICT[x['unit']],axis=1)
    ############## build plc file from modebusmap
    print('')
    print('building PLC configuration file of ' + 'VMUC'  +' from its modebus_map')
    print('*******************')
    vmuc_plc = build_plc_from_modebus_map(vmuc_modebus_map)
    ### save configuration files
    vmuc_modebus_map.to_pickle(CONFFOLDER+'/vmuc_modebus_map.pkl')
    vmuc_plc.to_pickle(CONFFOLDER+'/vmuc_plc.pkl')

################W######
#    GTC_ALSTOM       #
################W######
def parse_object_name(x):
    reg_exp=r"(?P<description>[\w\s°]+) (?P<address>[0-9A-F]{4}h) (?P<unitname>\w+) (?P<unit>Wh?) / PASSERELLE MODBUS (?P<passerelle>[\w\s]+)"
    m=re.match(reg_exp, x)
    if m is None:
        # return [x,'','','']
        return [x,'']
    else:
        # return [m.group('description'),m.group('address'),m.group('unitname'),m.group('unit'),m.group('passerelle')]
        return [m.group('description'),m.group('unit')]

def build_gtc_modebus_map(df_gtc,debug=False):
    len_parsed_df = df_gtc['object-name'].apply(lambda x:len(parse_object_name(x)))
    parsed_df     = df_gtc['object-name'].apply(lambda x:parse_object_name(x))
    idxbugs=len_parsed_df[len_parsed_df==0].index
    parsed_df = parsed_df.drop(idxbugs)
    modebusmap=pd.DataFrame(parsed_df.tolist(), index= parsed_df.index,columns=['description','unit'])
    modebusmap['adresse']     = df_gtc.loc[modebusmap.index,'Adresse MODBUS']
    modebusmap['intAddress']  = modebusmap['adresse']
    modebusmap['type']        = 'IEEE754'
    modebusmap['size(mots)']  = 2
    modebusmap['size(bytes)'] = modebusmap['size(mots)']*2
    modebusmap['scale']       = 1/1000
    modebusmap['slave_unit']  = 1
    modebusmap['unit']  = 'k'+modebusmap['unit']
    if debug:
        print(idxbugs)
        int(df_gtc.loc[idxbugs[0],'object-name'])
        return idxbugs
    return modebusmap
if REBUILD['gtc_alstom']:
    gtc_alstom_file = CONFFOLDER + 'ALSTOM_MODBUS_MBA_SYLFEN_V2.xlsx'
    df_gtc = pd.read_excel(gtc_alstom_file,sheet_name='ALSTOM_MODBUS_MBA_SYLFEN')
    gtc_modebus_map = build_gtc_modebus_map(df_gtc)
    ############ keep only variables of interest
    gtc_modebus_map = gtc_modebus_map[gtc_modebus_map['description'].str.contains('(TD)|(TGBT)')]

    ############# appliquer la convention de nommage pour la definition des tags
    df_compteurs_desc = COMPTEURS[COMPTEURS.device=='gtc_alstom'].reset_index().set_index('description')
    desc2fullname   = df_compteurs_desc['fullname'].to_dict()
    desc2ptComptage = df_compteurs_desc['pointComptage'].to_dict()
    gtc_modebus_map.index                = gtc_modebus_map.apply(lambda x:desc2fullname[x['description']] + '-' + UNITS_DICT[x['unit']],axis=1)
    gtc_modebus_map['point de comptage'] = gtc_modebus_map.apply(lambda x:desc2ptComptage[x['description']],axis=1)
    gtc_modebus_map['description']       = gtc_modebus_map['unit']
    ############## build plc file from modebusmap
    print('')
    print('building PLC configuration file of ' + 'GTC_ALSTOM'  +' from its modebus_map')
    print('*******************')
    gtc_plc = build_plc_from_modebus_map(gtc_modebus_map)
    ### save configuration files
    gtc_modebus_map.to_pickle(CONFFOLDER+'/gtc_alstom_modebus_map.pkl')
    gtc_plc.to_pickle(CONFFOLDER+'/gtc_alstom_plc.pkl')

################W######
#    SMARTLOGGER      #
################W######
if REBUILD['smartlogger']:
    sl_modebusmap = pd.DataFrame()
    sl_modebusmap['adresse']     = [40525,40560]
    sl_modebusmap['intAddress']  = sl_modebusmap['adresse']
    sl_modebusmap['type']        = 'INT32'
    sl_modebusmap['size(mots)']  = 2
    sl_modebusmap['size(bytes)'] = 4
    sl_modebusmap['description'] = ['kW','kWh']
    sl_modebusmap['scale']       = [1/1000,1/10]
    sl_modebusmap['unit']        = ['kW','kWh']
    sl_modebusmap['slave_unit']  = 1
    sl_modebusmap['point de comptage'] = 'centrale SLS 80kWc'
    sl_modebusmap.index = sl_modebusmap['point de comptage']+'-'+sl_modebusmap['description']
    ############# appliquer la convention de nommage pour la definition des tags
    sl_modebusmap.index=sl_modebusmap.apply(lambda x:COMPTEURS.loc[x['point de comptage'],'fullname']+'-'+x['description']+'-'+UNITS_DICT[x['unit']],axis=1)

    ############## build plc file from modebusmap
    print('')
    print('building PLC configuration file of ' + 'SMARTLOGGER'  +' from its modebus_map')
    print('*******************')
    sl_plc = build_plc_from_modebus_map(sl_modebusmap)

    sl_modebusmap.to_pickle(CONFFOLDER+'/smartlogger_modebus_map.pkl')
    sl_plc.to_pickle(CONFFOLDER+'/smartlogger_plc.pkl')

################W######
#    SITE SLS      #
################W######
if REBUILD['site_sls']:
    sitesls_mbmap = pd.DataFrame()
    sitesls_mbmap['adresse']     = [4198,4200,4246,4300]
    sitesls_mbmap['intAddress']  = sitesls_mbmap['adresse']
    sitesls_mbmap['type']        = 'UINT32'
    sitesls_mbmap['size(mots)']  = 2
    sitesls_mbmap['size(bytes)'] = 4
    sitesls_mbmap['unit']       = ['kW','kW','kWh','kWh']
    sitesls_mbmap['scale']       = 1
    sitesls_mbmap['slave_unit']  = 20
    sitesls_mbmap['description'] = ['puissance_soutirage','puissance_injection','energie_soutirage','energie_injection']
    sitesls_mbmap['point de comptage'] = 'siteSLS'
    sitesls_mbmap.index = sitesls_mbmap['point de comptage']+'-'+sitesls_mbmap['description']
    ############# appliquer la convention de nommage pour la definition des tags
    sitesls_mbmap.index=sitesls_mbmap.apply(lambda x:COMPTEURS.loc[x['point de comptage'],'fullname']+'-'+x['description']+'-'+UNITS_DICT[x['unit']],axis=1)

    ############## build plc file from modebusmap
    print('')
    print('building PLC configuration file of ' + 'SITESLS'  +' from its modebus_map')
    print('*******************')
    sitesls_plc = build_plc_from_modebus_map(sitesls_mbmap)

    sitesls_mbmap.to_pickle(CONFFOLDER+'/site_sls_modebus_map.pkl')
    sitesls_plc.to_pickle(CONFFOLDER+'/site_sls_plc.pkl')

    sys.exit()
