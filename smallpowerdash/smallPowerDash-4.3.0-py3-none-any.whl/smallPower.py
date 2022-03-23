#!/bin/python
# #######################
# #   GLOBAL VARIABLES  #
# # COMPUTER DEPENDENT  #
# #######################
import os,sys, time, datetime as dt,importlib,pickle,glob,re
import pandas as pd,numpy as np
from dorianUtils.utilsD import Utils
import dorianUtils.comUtils as comUtils
importlib.reload(comUtils)
import socket

# ==============================================================================
#                           CONFIGURATION
# ==============================================================================

PARKING_TIME = 60*10 #### in seconds
NAMESPACE_BECKHOFF = "ns=4;s=GVL."

DB_PARAMETERS = {
    'host'     : "localhost",
    'port'     : "5432",
    'dbname'   : "jules",
    'user'     : "postgres",
    'password' : "sylfenbdd"
}
if 'sylfen' in os.getenv('HOME'):
    baseFolder   = '/home/sylfen/data_ext/'
    ENDPOINTURL  = 'opc.tcp://10.10.38.100'
    PORT_BECKHOFF= 4840
else:
    baseFolder    = '/home/dorian/data/sylfenData/'
    # ENDPOINTURL   = 'localhost'
    ENDPOINTURL  = 'opc.tcp://10.10.38.100'
    PORT_BECKHOFF= 4840
    # PORT_BECKHOFF = 65000
    DB_PARAMETERS['dbname']="juleslocal"

FOLDERPKL  = baseFolder + 'smallPower_daily/'
FileSystem = comUtils.FileSystem
fs         = FileSystem()
appdir     = os.path.dirname(os.path.realpath(__file__))
parentdir  = fs.getParentDir(appdir)
CONFFOLDER          = parentdir + 'smallPowerDash/confFiles/'
FILECONF_SMALLPOWER = CONFFOLDER + 'smallpower_configfiles.ods'

######################################
##### INITIALIZATION OF DEVICES ######
######################################
def _load_material_constants():
    dfConstants = pd.read_excel(FILECONF_SMALLPOWER,sheet_name='constants',index_col=1)
    # cst = comUtils.EmptyClass()
    cst = {}
    for k in dfConstants.index:
        # setattr(cst,k,dfConstants.loc[k].value)
        cst[k]=dfConstants.loc[k].value
    return cst,dfConstants

# listFiles = glob.glob(CONFFOLDER + '*devices*.ods')
# file_devices = listFiles[0]
# v_devices  = re.findall('_v\d+',file_devices)[0]
# df_devices = pd.read_excel(file_devices,index_col=0,sheet_name='devices')

FILE_PLC_XLSM = glob.glob(CONFFOLDER+'*ALPHA*.xlsm')[0]
PLC_BECKHOFF  = CONFFOLDER + 'plc_smallpower.pkl'
load_plc_beckhoff = lambda :pd.read_excel(FILE_PLC_XLSM,sheet_name='FichierConf_Jules',index_col=0)

class Beckhoff_client(comUtils.Opcua_Client):
    def __init__(self):
        comUtils.Opcua_Client.__init__(self,
                    device_name = 'beckhoff',
                    endpointUrl = ENDPOINTURL,
                    port        = PORT_BECKHOFF,
                    dfplc       = fs.load_confFile(PLC_BECKHOFF,load_plc_beckhoff,False),
                    nameSpace   = NAMESPACE_BECKHOFF)
        if '10.10.38.100' in self.endpointUrl:
            certif_path = CONFFOLDER + 'my_cert.pem'
            key_path    = CONFFOLDER + 'my_private_key.pem'
            sslString = 'Basic256Sha256,Sign,' + certif_path + ',' + key_path
            try :
                self.client.set_security_string(sslString)
                self.client.set_user("Alpha")
                self.client.set_password("Alpha$01")
                print('security check succeeded!')
            except:
                print('security check FAILED -> impossible to connect to beckhoff')
        self.currentTime = pd.Timestamp.now(tz='UTC')
        # ######################
        # tags for computation #
        # and calculatedTags   #
        # ######################
        tags_for_computation={
            'vanneBF'     : self.getTagsTU('l300.*ECV')[0],
            'air_in_ft'   : self.getTagsTU('l138.*FT')[0],
            'air_out_ft'  : self.getTagsTU('l118.*FT')[0],
            'air_out_pt'  : self.getTagsTU('GFD_02.*PT')[0],
            'air_in_tt'   : self.getTagsTU('HTBA.*HEX_02.*TT.*01')[0],
            'air_stack_tt': self.getTagsTU('GFC_02.*TT')[0],
            'air_balayage_tt' : self.getTagsTU('HPB.*HEX_02.*TT.*02')[0],
            'n2_in_air'       : self.getTagsTU('l301.*FT')[0],
            'fuel_in_ft'      : self.getTagsTU('l041.*FT.*HM05')[0],
            'h2_in_ft'        : self.getTagsTU('l041.*FT')[0],
            'fuel_out_ft'     : self.getTagsTU('l025.*FT.*HM05')[0],
            'fuel_out_pt'     : self.getTagsTU('GFD_01.*PT')[0],
            'fuel_in_tt'      : self.getTagsTU('HTBF.*HEX_01.*TT.*01')[0],
            'fuel_stack_tt'   : self.getTagsTU('GFC_01.*TT')[0],
            'n2_in_fuel'      : self.getTagsTU('l303.*FT.*HM05')[0],
            # 'water_in_ft' : self.getTagsTU('l213.*FT.*HM05')[0],
            'power_total' :'SEH0.JT_01.JTW_HC20',
            'T_stacks'    :'SEH1.STB_TT_02.HM05',
            # 'L032' : self.getTagsTU('l032.*FT'),#NO
            # 'L303' : self.getTagsTU('l303.*FT'),#NO
            # 'L025' : self.getTagsTU('l025.*FT'),#NF
            'h2_cold_loop_ft'   : self.getTagsTU('l032.*FT')[0],
            'power_chauffant_1' : self.getTagsTU('STK_HER.*01.*JTW')[0],
            'power_chauffant_2' : self.getTagsTU('STK_HER.*02.*JTW')[0],
            'power_chauffant_3' : self.getTagsTU('STK_HER.*03.*JTW')[0],
            }
        ### complete dictionnaries for stack currents
        for k in range(1,5):
            basetag='SEH1.STK_ALIM_0'+str(k)+'.IT'
            tag_hm05,tag_hr29 = basetag+'_HM05',basetag+'_HR29'
            tags_for_computation['current_stack_measure'+ str(k)] = tag_hm05
            tags_for_computation['current_stack_command'+ str(k)] = tag_hr29

        cal_tags      = pd.read_excel(FILECONF_SMALLPOWER,sheet_name='calculated_tags',index_col=0)
        self.tags_calculated = cal_tags['calculated_tag'].squeeze()
        # sys.exit()
        ### complete dictionnaries for rendement_gv tags
        tags_gv = pd.concat([pd.Series(self.get_tags_gv_rendement(k)) for k in ['a','b']]).drop_duplicates()
        self.tags_for_computation = pd.concat([pd.Series(tags_for_computation),tags_gv]).sort_index()
        self.cst,_ = _load_material_constants()

    def get_tags_allpowers(self):
        return {
            'power_stk_her':['SEH1.STB_STK_00_HER_00_JTW_00_HC01'],
            'power_enceinte':['SEH1.STB_HER_00_JTW_00_HC01'],
            'power_gv1a':self.getTagsTU('STG_01a.*JTW'),
            'power_gv1b':self.getTagsTU('STG_01b.*JTW'),
            'alim_stacks':self.getTagsTU('STK_ALIM.*JTW'),
            'power_pumps':self.getTagsTU('PMP.*JTW'),
            'power_blowers':self.getTagsTU('BLR.*JTW'),
        }
    def get_tags_gv_rendement(self,gv='a'):
        tags={}
        power_gv = self.getTagsTU('stg.*'+gv+'.*JTW')
        for k,tag in enumerate(power_gv):
            tags['power_gv_'+gv+'_'+str(k+1)] = tag
        tags['ft_in_gv_'+gv] = self.getTagsTU('l213.*'+gv+'.*FT')[0]
        tags['tt_in_gv'] = self.getTagsTU('GWPBH_TT')[0]
        tags['tt_out_gv'] = self.getTagsTU('L036.*TT')[0]
        return tags

# ###################
#   computations of #
#       new tags    #
# ###################
    def low_pass_filter(self,x,x_1,alpha):
        '''
        x     : value at time t
        x_1   : value at time t-1
        alpha : coefficient cutoff frequency between 0 and 1
        '''
        return alpha*x+(1-alpha)*x_1
    def o2_stack_alim(self,I_conventionnel):
        ## o2out has the sign of I_conventionnel
        o2_out       = I_conventionnel*25/(4*self.cst['FAR']) ##25 cells
        o2_out_Nlmin = o2_out*self.cst['vlm']*60
        return o2_out_Nlmin
    def fuites_air(self,mode,o2_stack,air_in,air_out,n2_in):
        '''
        o2_stack is negative in electrolysis and positive in fuel cell mode
        Débit entrée – Débit sortie +/- fonction du courant
        Si le courant = 0 alors Si débit azote >0 alors on est en BF, sinon on est en BO
        '''
        if mode=='BF':fuiteAir = n2_in
        else:fuiteAir = air_in - o2_stack - air_out
        return fuiteAir
    def h2_stack_out(self,I_conventionnel):
        ## o2out has the sign of I_conventionnel
        h2_out       = I_conventionnel*25/(2*self.cst['FAR']) ##25 cells
        h2_out_Nlmin = h2_out*self.cst['vlm']*60
        return h2_out_Nlmin
    def detect_modehub(self,I_conventionel,vanneN2):
        '''4 modes:
        - SOEC, I>0
        - SOFC I>0
        - BF, I=0, vanneN2(NF) is False
        - BO, tout le reste.
        '''
        if I_conventionel < -0.01:mode='SOEC'
        elif I_conventionel > 0.01 : mode='SOFC'
        else:
            if not vanneN2:mode='BF'
            else:mode='BO'
        return mode
    def fuites_fuel(self,mode,h2stack,fuel_in,fuel_out,n2_in_fuel):
        '''
        - mode : got from self.detect_modehub
        - h2stack is taken always positive for the formula
        '''
        h2stack = np.abs(h2stack)
        if mode=='SOEC':
            fuitefuel = fuel_in + h2stack - fuel_out
        elif mode=='SOFC':
            fuitefuel = fuel_in - h2stack
        elif mode=='BF':
            fuitefuel = n2_in_fuel + fuel_in
        else:
            fuitefuel = fuel_in - fuel_out
        return fuitefuel
    def rendement_sys(self,mode,power_sys,h2_produced):
        '''power_sys in kW and h2 produced or consumed(proportionel to the stacks current) in the stack Nl/min'''
        #conversion in mol/s
        h2_mols  = np.abs(h2_produced/60/22.4)
        #take the power
        h2_power_chimique = h2_mols*self.cst['PCImol_H2']
        #remove extra power not from the system
        rendement=0
        total_power = power_sys-1000
        if mode=='SOEC':
            if total_power>0:
                rendement = h2_power_chimique/total_power
        elif mode=='SOFC':
            if h2_power_chimique>0:
                rendement = -total_power/h2_power_chimique
        return rendement*100
    def rendement_gv(self,FT_IN_GV,TT_IN_GV,TT_OUT_GV,power_elec_chauffe):
        '''
        - FT_IN_GV should be in g/min
        '''
        debitEau_gs = FT_IN_GV/60
        #calcul
        power_chauffe_eau_liq = max(0,debitEau_gs*self.cst['Cp_eau_liq']*(100-TT_IN_GV))
        power_vapo_eau        = debitEau_gs*self.cst['Cl_H2O']
        power_chauffe_vap     = max(0,debitEau_gs*self.cst['Cp_eau_vap']*(TT_OUT_GV-100))
        power_total_chauffe = power_chauffe_eau_liq + power_vapo_eau +  power_chauffe_vap
        # print(power_total_chauffe,power_elec_chauffe)
        if not power_elec_chauffe==0:
            return power_total_chauffe/power_elec_chauffe*100
        else:
            return np.nan

    def pertes_thermiques_stack(self,air_in_tt,air_in_ft,air_stack_tt,fuel_in_tt,fuel_in_ft,fuel_stack_tt,puissance_four):
        '''
        - _ft variables are volumetric flows in Nl/min
        - balayage should be added !
        '''
        # cp_fuel,M_fuel = self.dfConstants.loc['Cp_' + fuel,'value'],self.dfConstants.loc['Mmol_' + fuel,'value']
        cp_fuel,M_fuel = self.cst['Cp_H2'],self.cst['Mmol_H2']
        cp_air,M_air = self.cst['Cp_air'],self.cst['Mmol_Air']

        surchauffe_Air  = (air_stack_tt-air_in_tt)*cp_air*M_air*air_in_ft/22.4/60
        surchauffe_Fuel = (fuel_stack_tt-fuel_in_tt)*cp_fuel*M_fuel*fuel_in_ft/22.4/60
        # surchauffe_AirBalayage = (air_stack_tt-air_in_tt)*cp_air*M_air*debitAirBalayage_mols/22.4/60

        total_puissance_surchauffe_gaz = surchauffe_Air + surchauffe_Fuel
         # + surchauffe_AirBalayage
        if total_puissance_surchauffe_gaz>0:
            return puissance_four/total_puissance_surchauffe_gaz
        # return total_puissance_surchauffe_gaz/puissance_four
        else:
            return np.nan

    def compute_calculated_tags(self):
        '''
        - d_values  --> dictionnary of tag value used for computation tag_var:value
        - d_tags_hc --> dictionnary of calculated tag/value tag:[value,timestamp]
        '''
        ### gather first all values of tags needed for computation
        d_values = self.collectData(self.tags_for_computation.to_list())
        ### rename the keys with those of tags_for_computation
        tagnames = pd.Series(dict((v,k) for k,v in self.tags_for_computation.iteritems()))
        d_values  = {tagnames[tag]:v[0] for tag,v in d_values.items()}
        for k,v in d_values.items(): print(k.ljust(50),v)
        d_tags_hc = {}
        # ================================================
        # courant en valeur absolue et convention physique
        # ================================================
        now = pd.Timestamp.now(tz='UTC')
        for current_tag_name in [k for k in df.columns if 'current_stack' in k]:
            tag_current=beckhoff.tags_for_computation[current_tag_name]
            d_tags_hc[tag_current + '.HC09'] = [np.abs(d_values[current_tag_name]),now.isoformat()]
            d_tags_hc[tag_current + '.HC13'] = [-d_values[current_tag_name],now.isoformat()]
        #
        #
        # for k in range(1,5):
        #     #### courant en valeur absolue
        #     basetag='SEH1.STK_ALIM_0'+str(k)+'.IT'
        #     tag_hm05,tag_hr29 = basetag+'_HM05',basetag+'_HR29'
        #     d_tags_hc[tag_hm05 + '.HC09']=[np.abs(d_values['current_stack_measure'+str(k)]),now.isoformat()]
        #     d_tags_hc[tag_hr29 + '.HC09']=[np.abs(d_values['current_stack_command'+str(k)]),now.isoformat()]
        #
        #     #### convention physique
        #     d_tags_hc[tag_hm05 + '.HC13'] = d_tags_hc[tag_hm05+'.HC09'].copy()
        #     d_tags_hc[tag_hr29 + '.HC13'] = d_tags_hc[tag_hr29+'.HC09'].copy()
        #     #### if mode SOEC --> invert sign
        #     if d_values['current_stack_measure1']>0:
        #         d_tags_hc[tag_hm05+'.HC13'][0] = -d_tags_hc[tag_hm05+'.HC13'][0]
        #         d_tags_hc[tag_hr29+'.HC13'][0] = -d_tags_hc[tag_hr29+'.HC13'][0]

        # ======================
        #  courants total stack
        # ======================
        # valeur absolute
        d_tags_hc['I_absolue'] = [sum([v[0] for k,v in d_tags_hc.items() if 'IT_HM05.HC09' in k]),now.isoformat()]
        #convention physique
        I_conventionel = sum([v[0] for k,v in d_tags_hc.items() if 'IT_HM05.HC13' in k])
        d_tags_hc['I_conventionel'] = [I_conventionel,now.isoformat()]

        # ======================
        #       modehub
        # ======================
        modehub = self.detect_modehub(I_conventionel,d_values['vanneBF'])

        # ======================
        #       fuite air
        # ======================
        now_air = pd.Timestamp.now(tz='UTC')
        #--- o2 out of stack
        o2_out_alim = self.o2_stack_alim(I_conventionel)
        o2_out_hm05 = d_values['air_out_ft'] - d_values['air_in_ft']
        #--- fuites
        air_in,air_out,n2_in = [d_values[t] for t in ['air_in_ft','air_out_ft','n2_in_air']]
        fuite_air            = self.fuites_air(modehub,o2_out_alim,air_in,air_out,n2_in)
        fuite_air_gfd        = fuite_air/d_values['air_out_pt']

        # ======================
        #       fuite fuel
        # ======================
        now_fuel = pd.Timestamp.now(tz='UTC')
        #--- h2 out of stack
        h2_out_alim = self.h2_stack_out(I_conventionel)
        h2_out_hm05 = d_values['fuel_out_ft'] - d_values['h2_in_ft']
        #--- fuites
        fuel_in,fuel_out,n2_in_fuel=[d_values[t] for t in ['h2_in_ft','fuel_out_ft','n2_in_fuel']]
        fuite_fuel = self.fuites_fuel(modehub,h2_out_alim,fuel_in,fuel_out,n2_in_fuel)
        fuite_fuel_gfd = fuite_fuel/d_values['fuel_out_pt']

        # ======================
        #   rendement systeme
        # ======================
        now_rendement = pd.Timestamp.now(tz='UTC')
        rendement_sys = self.rendement_sys(d_values['power_total'],h2_out_alim)
        # rendement_sys = self.rendement_sys(d_values['power_total'],h2_out_hm05)

        # ======================
        #   rendement gv
        # ======================
        TT_IN_GV,TT_OUT_GV = [d_values[t] for t in ['tt_in_gv','tt_out_gv']]
        ## gv1a
        power_tags = [k for k in self.tags_for_computation.index if 'power_gv_a' in k]
        power_elec_chauffe = sum([d_values[t] for t in power_tags])
        rendement_gv_a = self.rendement_gv(d_values['ft_in_gv_a'],TT_IN_GV,TT_OUT_GV,power_elec_chauffe)
        ## gv1b
        rendement_gv_b = self.rendement_gv(d_values['ft_in_gv_b'],TT_IN_GV,TT_OUT_GV,d_values['power_gv_b_1'])

        # ============================
        #   pertes thermiques stack
        # ============================
        now_pertes_stack = pd.Timestamp.now(tz='UTC')
        air_in_tt,air_in_ft,air_stack_tt  = [d_values[t] for t in ['air_in_tt','air_in_ft','air_stack_tt']]
        fuel_in_tt,h2_in_ft,fuel_stack_tt,h2_cold_loop_ft = [d_values[t] for t in ['fuel_in_tt','h2_in_ft','fuel_stack_tt','h2_cold_loop_ft']]
        puissance_four                    = sum([d_values['power_chauffant_'+str(k)] for k in [1,2,3]])
        fuel_in_ft   = h2_in_ft + h2_cold_loop_ft
        pertes_stack = self.pertes_thermiques_stack(air_in_tt,air_in_ft,air_stack_tt,fuel_in_tt,fuel_in_ft,fuel_stack_tt,puissance_four)

        # ======================
        #   compteurs, cumul
        # ======================
        now_cumul = pd.Timestamp.now(tz='UTC')
        durationh = (now - self.currentTime).total_seconds()/3600
        self.currentTime = now #### update the current time
        # ------ tps fonctionnement T>600°C
        tps_T600 = self.tag_buffered['tps_T600']
        if d_values['T_stacks'] > 600: tps_T600+= durationh

        # ------ h2 production/SOEC
        tps_SOEC          = self.tag_buffered['tps_SOEC']
        tps_SOFC          = self.tag_buffered['tps_SOFC']
        cumul_h2_produced = self.tag_buffered['cumul_h2_produced']
        cumul_h2_consumed = self.tag_buffered['cumul_h2_consumed']
        nbTransitions     = self.tag_buffered['nbTransitions']
        if I_conventionel<-0.01:
            tps_SOEC+= durationh
            cumul_h2_produced+= h2_out_hm05*durationh*60/1000
        if I_conventionel>0.01:
            tps_SOFC+= durationh
            cumul_h2_consumed+= h2_in*durationh*60/1000

        if not modehub==self.tag_buffered['modehub']:
            if modehub=='SOEC' or modehub =='SOFC':
                nbTransitions=+1

        # ======================
        #   apply lowpassfilter
        # ======================
        fuite_air      = self.low_pass_filter(fuite_air,self.tag_buffered['fuite_air'],0.005)
        fuite_air_gfd  = self.low_pass_filter(fuite_air_gfd,self.tag_buffered['fuite_air_gfd'],0.005)
        fuite_fuel     = self.low_pass_filter(fuite_fuel,self.tag_buffered['fuite_fuel'],0.005)
        fuite_fuel_gfd = self.low_pass_filter(fuite_fuel_gfd,self.tag_buffered['fuite_fuel_gfd'],0.005)
        rendement_sys  = self.low_pass_filter(rendement_sys,self.tag_buffered['rendement_sys'],0.005)
        rendement_gv_a = self.low_pass_filter(rendement_sys,self.tag_buffered['rendement_gv_a'],0.005)
        rendement_gv_b = self.low_pass_filter(rendement_sys,self.tag_buffered['rendement_gv_b'],0.005)
        pertes_stack = self.low_pass_filter(pertes_stack,self.tag_buffered['pertes_stack'],0.005)

        # ======================
        #       update all
        # ======================
        d_tags_hc['modehub']           = [modehub,now.isoformat()]
        d_tags_hc['o2_out_alim']       = [np.abs(o2_out_alim),now_air.isoformat()]
        d_tags_hc['o2_out_hm05']       = [o2_out_hm05,now_air.isoformat()]
        d_tags_hc['fuite_air']         = [fuite_air,now_air.isoformat()]
        d_tags_hc['fuite_air_gfd']     = [fuite_air_gfd,now_air.isoformat()]
        d_tags_hc['h2_out_alim']       = [np.abs(h2_out_alim),now_fuel.isoformat()]
        d_tags_hc['h2_out_hm05']       = [h2_out_hm05,now_fuel.isoformat()]
        d_tags_hc['fuite_fuel']        = [fuite_fuel,now_fuel.isoformat()]
        d_tags_hc['fuite_fuel_gfd']    = [fuite_fuel_gfd,now_fuel.isoformat()]
        d_tags_hc['rendement_sys']     = [rendement_sys,now_rendement.isoformat()]
        d_tags_hc['rendement_gv_a']    = [rendement_gv_a,now_rendement.isoformat()]
        d_tags_hc['rendement_gv_b']    = [rendement_gv_b,now_rendement.isoformat()]
        d_tags_hc['pertes_stack']      = [pertes_stack,now_pertes_stack.isoformat()]
        d_tags_hc['tps_T600']          = [tps_T600,now_cumul.isoformat()]
        d_tags_hc['tps_SOEC']          = [tps_SOEC,now_cumul.isoformat()]
        d_tags_hc['tps_SOFC']          = [tps_SOFC,now_cumul.isoformat()]
        d_tags_hc['cumul_h2_produced'] = [cumul_h2_produced,now_cumul.isoformat()]
        d_tags_hc['cumul_h2_consumed'] = [cumul_h2_consumed,now_cumul.isoformat()]
        d_tags_hc['nbTransitions']     = [nbTransitions,now_cumul.isoformat()]

        self.tag_buffered = {tagvar:value[0] for tagvar,value in d_tags_hc.items()}
        # rename the keys of d_tags_hc
        d_tags_hc = {self.tags_calculated[tagvar]:val for tagvar,val in d_tags_hc.items()}
        return d_tags_hc


# ##############
#       old    #
# ##############
    def _get_tags_Istacks(self):
        return {
            'Istacks' : self.getTagsTU('STK.*IT.*HM05'),
            }
    def i_total(self,Istacks):
        return sum(Istacks)
    def fuelmodeNicolas(self,dvvv):
        # NF: False<==>fermé ; NO: False<==>ouvert
        # NF: False<==>ouvert ; NO True<==>fermé
        modeFuel = []
        # Gonflage :
        # L035 ou L040 fermées et L039 fermée et L027(NO) fermée
        if (not dvvv['vanne35'] or not dvvv['vanne40']) and (not dvvv['vanne39']) and (dvvv['vanne27']):
            modeFuel.append('gonflage')

            # Boucle fermée recirculation à froid (mode pile):
            # L026(NO) et L029 fermées, L027(NO) ouverte, L035 OU L040 fermées
            if (dvvv['vanne26']) and (not dvvv['vanne29']) and (not dvvv['vanne27']) and (not dvvv['vanne35']) or (not dvvv['vanne40']):
                modeFuel.append('recircuFroidPile')

                # Boucle ouverte (fonctionnement électrolyse ou boucle ouverte pendant les transitions) :
                # (L035 ET L040 ouvertes) ou L026(NO) ouverte ou L029 ouverte
                if (dvvv['vanne35'] and dvvv['vanne40']) or (not dvvv['vanne26']) or (dvvv['vanne29']):
                    modeFuel.append('bo_electrolyse')

                    # Fonctionnement mode gaz naturel :
                    # - L027(NO) fermée, L039 ouverte
                    if (dvvv['vanne27'] and dvvv['vanne39']):
                        modeFuel.append('gaz_nat')
                        return modeFuel
    def verifDebitmetre(self,L032,L303,L025):
        # Vérif débitmètres ligne fuel BF = L032 FT – L303 – L025
        return L032-L303-L025
    def get_tags_modeFuel(self):
        return {
                'vanne26' : self.getTagsTU('l026.*ECV'),#NO
                'vanne27' : self.getTagsTU('l027.*ECV'),#NO
                'vanne29' : self.getTagsTU('l029.*ECV'),#NF
                'vanne35' : self.getTagsTU('l035.*ECV'),#NF
                'vanne39' : self.getTagsTU('l039.*ECV'),#NF
                'vanne40' : self.getTagsTU('l040.*ECV'),#NF
        }
    def coefFuitesFuel(self,Itotal,modefuel,L303,L041,L032,L025):
        '''
        Gonflage :
        - L035 ou L040 fermées et L039 fermée et L027 fermée
        - fuites fuel BF = L303 + L041 (+ Somme i x 25 / 2F)  note : normalement dans ce mode le courant est nul.
        Boucle fermée recirculation à froid (mode pile)
        - L026 et L029 fermées, L027 ouverte, L035 OU L040 fermées
        - fuites fuel BF = L303 + L041 + Somme i x 25 / 2F
        Boucle ouverte (fonctionnement électrolyse ou boucle ouverte pendant les transitions) :
        - (L035 ET L040 ouvertes) ou L026 ouverte ou L029 ouverte
        - fuite ligne fuel BO = L303 + L041 + Somme i x 25 / 2F – L025
        Fonctionnement mode gaz naturel :
        - L027 fermée, L039 ouverte
        - fuites fuel BO = (L032 – L303) x 4 + L303 + L041 + Somme i x 25 / 2F – L025
        En résumé : trois calculs possibles du débit de fuite fuel
        Le même calcul pour les cas 1 et 2 qui sont « fermés »
        Un calcul pour le mode ouvert électrolyse ou boucle ouverte pendant les transitions
        Un calcul pour le mode gaz naturel.
        '''
        #############################
        # compute Hydrogen production
        #############################
        PH2mols = Itotal*25/(2*self.cst['FAR']) ##25 cells
        PH2Nlmin = PH2mols*self.cst['vlm']*60
        #############################
        # mode fuel
        #############################
        if modefuel=='gonflage' or modefuel=='recircuFroidPile':
            fuitesFuel = L303 + L041 + PH2Nlmin
        elif modefuel=='bo_electrolyse':
            fuitesFuel = L303 + L041 + PH2Nlmin - L025
        elif modefuel=='gaz_nat':
            fuitesFuel = (L032 - L303)*4 + L303 + L041 + PH2Nlmin - L025
        return fuitesFuel

DEVICES={'beckhoff':Beckhoff_client()}
# ==============================================================================
#                           CONFIGURATIONS
VisualisationMaster_daily = comUtils.VisualisationMaster_daily
Configurator = comUtils.Configurator
SuperDumper_daily = comUtils.SuperDumper_daily
VersionManager_daily = comUtils.VersionManager_daily
# sys.exit()

class Config_extender():
    def __init__(self):
        cfg = Configurator(FOLDERPKL,DB_PARAMETERS,DEVICES,PARKING_TIME)
        self.utils   = Utils()
        self.devices = cfg.devices
        self.devices['beckhoff'].file_plc_xlsm = FILE_PLC_XLSM
        self.file_plc_xlsm = FILE_PLC_XLSM
        self.file_conf  = FILECONF_SMALLPOWER
        self.usefulTags = pd.read_excel(self.file_conf,sheet_name='useful_tags',index_col=0)
        self.confFolder  = CONFFOLDER
        self.freqCalctags = 1
        ### add the calculated tags in the plc ###
        plcCalctags = pd.read_excel(self.file_conf,sheet_name='calculated_tags',index_col=1).iloc[:,1:]
        self.dfplc  = pd.concat([cfg.dfplc,plcCalctags],axis=0)
        self.alltags  = list(self.dfplc.index)
        self.listUnits = self.dfplc.UNITE.dropna().unique().tolist()


import psycopg2
class SmallPower_dumper(SuperDumper_daily,Config_extender):
    def __init__(self):
        SuperDumper_daily.__init__(self,FOLDERPKL,DB_PARAMETERS,DEVICES,PARKING_TIME)
        Config_extender.__init__(self)
        self.devices['beckhoff'].client.connect() #====>cause problem with multiprocessing

        #### initialize lowpass tags (to get the first correct initial value)
        tag_buffered={}
        folderlastday = self.daysnotempty.max().strftime(self.format_dayFolder)
        for var,tag in self.devices['beckhoff'].tags_calculated.to_dict().items():
            try:
                val = pickle.load(open(folderlastday+tag,'rb')).median()
            except:
                print('tag : ',tag,' not in the folder :',folderlastday)
                val = 0
            tag_buffered[var] = val
        self.devices['beckhoff'].tag_buffered=tag_buffered
        print()
        print('initialization of low pass tags done!')
        print()

        ### interval for calculated tags
        self.calcTags_dumper = comUtils.SetInterval(self.freqCalctags,self.insert_calctags_intodb)

    def insert_calctags_intodb(self):
        if self.devices['beckhoff'].isConnected:
            data={}
            try :
                connReq = ''.join([k + "=" + v + " " for k,v in self.dbParameters.items()])
                dbconn = psycopg2.connect(connReq)
            except :
                print('problem connecting to database ',self.dbParameters)
                return
            cur  = dbconn.cursor()
            start=time.time()
            try :
                data = self.devices['beckhoff'].compute_calculated_tags()
            except:
                print(comUtils.timenowstd(),' : souci computing new tags')
                return
            for tag in data.keys():
                sqlreq = "insert into realtimedata (tag,value,timestampz) values ('"
                value = data[tag][0]
                if value==None:
                    value = 'null'
                value=str(value)
                sqlreq+= tag +"','" + value + "','" + data[tag][1]  + "');"
                sqlreq=sqlreq.replace('nan','null')
                cur.execute(sqlreq)
            dbconn.commit()
            cur.close()
            dbconn.close()

    def start_dumping(self):
        self.calcTags_dumper.start()
        SuperDumper_daily.start_dumping(self)

    def stop_dumping(self):
        self.calcTags_dumper.stop()
        SuperDumper_daily.stop_dumping(self)

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from PIL import Image
class SmallPowerComputer(VisualisationMaster_daily,Config_extender):
    def __init__(self,rebuildConf=True):
        VisualisationMaster_daily.__init__(self,FOLDERPKL,DB_PARAMETERS,DEVICES,PARKING_TIME)
        Config_extender.__init__(self)
        self.imgpeintre  = Image.open(CONFFOLDER + '/pictures/peintrepalette.jpeg')
        self.sylfenlogo  = Image.open(CONFFOLDER +  '/pictures/logo_sylfen.png')
        self.file_conf_pkls = CONFFOLDER +  'smallpower_conffiles.pkl'
        self.colorPalettes   = self._loadcolorPalettes()
        conf_pkls = self.fs.load_confFile(self.file_conf_pkls,self.load_confFiles,rebuildConf)
        self.cst,self.dfConstants,self.enumModeHUB,self.dftagColorCode,self.unitDefaultColors = conf_pkls
        self.colorshades    = list(self.colorPalettes.keys())
        self.enumModeHUB_simple = {k:v for k,v in self.enumModeHUB.items() if 'undefined' not in v}


    def load_confFiles(self):
        cst,dfConstants = _load_material_constants()
        enumModeHUB     = self._load_enum_hubmodes()
        dftagColorCode,unitDefaultColors    = self._buildColorCode()
        return cst,dfConstants,enumModeHUB,dftagColorCode,unitDefaultColors
    ###########################
    #  GENERATOR CONF FILES   #
    ###########################
    def _load_enum_hubmodes(self):
        enumModeHUB = pd.read_excel(self.file_plc_xlsm,sheet_name='Enumérations',skiprows=1).iloc[:,1:3].dropna()
        enumModeHUB=enumModeHUB.set_index(enumModeHUB.columns[0]).iloc[:,0]
        enumModeHUB.index=[int(k) for k in enumModeHUB.index]
        for k in range(100):
            if k not in enumModeHUB.index:
                enumModeHUB.loc[k]='undefined'
        enumModeHUB = enumModeHUB.sort_index()
        enumModeHUB = enumModeHUB.to_dict()
        return enumModeHUB

    def _loadcolorPalettes(self):
        colPal = pickle.load(open(CONFFOLDER+'palettes.pkl','rb'))
        colPal['reds']     = colPal['reds'].drop(['Misty rose',])
        colPal['greens']   = colPal['greens'].drop(['Honeydew',])
        colPal['blues']    = colPal['blues'].drop(['Blue (Munsell)','Powder Blue','Duck Blue','Teal blue'])
        colPal['magentas'] = colPal['magentas'].drop(['Pale Purple','English Violet'])
        colPal['cyans']    = colPal['cyans'].drop(['Azure (web)',])
        colPal['yellows']  = colPal['yellows'].drop(['Light Yellow',])
        ### manual add colors
        colPal['blues'].loc['Indigo']='#4B0082'

        #### shuffle them so that colors attribution is random
        for c in colPal.keys():
            colPal[c]=colPal[c].sample(frac=1)
        return colPal

    def _buildColorCode(self):
        unitDefaultColors = pd.read_excel(self.file_conf,sheet_name='units_colorCode',index_col=0)
        dftagColorCode = pd.read_excel(self.file_conf,sheet_name='tags_color_code',index_col=0,keep_default_na=False)
        from plotly.validators.scatter.marker import SymbolValidator
        raw_symbols = pd.Series(SymbolValidator().values[2::3])
        listLines = pd.Series(["solid", "dot", "dash", "longdash", "dashdot", "longdashdot"])
        allHEXColors=pd.concat([k['hex'] for k in self.colorPalettes.values()])
        ### remove dupplicates index (same colors having different names)
        allHEXColors=allHEXColors[~allHEXColors.index.duplicated()]

        def assignRandomColor2Tag(tag):
            unitTag  = self.getUnitofTag(tag).strip()
            # print(unitDefaultColors)
            # sys.exit()
            shadeTag = unitDefaultColors.loc[unitTag].squeeze()
            color = self.colorPalettes[shadeTag]['hex'].sample(n=1)
            return color.index[0]

        # generate random color/symbol/line for tags who are not in color_codeTags
        listTags_wo_color=[k for k in self.alltags if k not in list(dftagColorCode.index)]
        d = {tag:assignRandomColor2Tag(tag) for tag in listTags_wo_color}
        dfRandomColorsTag = pd.DataFrame.from_dict(d,orient='index',columns=['colorName'])
        dfRandomColorsTag['symbol'] = pd.DataFrame(raw_symbols.sample(n=len(dfRandomColorsTag),replace=True)).set_index(dfRandomColorsTag.index)
        dfRandomColorsTag['line'] = pd.DataFrame(listLines.sample(n=len(dfRandomColorsTag),replace=True)).set_index(dfRandomColorsTag.index)
        # concatenate permanent color_coded tags with color-random-assinged tags
        dftagColorCode = pd.concat([dfRandomColorsTag,dftagColorCode],axis=0)
        # assign HEX color to colorname
        dftagColorCode['colorHEX'] = dftagColorCode.apply(lambda x: allHEXColors.loc[x['colorName']],axis=1)
        return dftagColorCode,unitDefaultColors

    # ==============================================================================
    #                   COMPUTATION FUNCTIONS/INDICATORS
    # ==============================================================================
    def getModeHub(self,t0,t1,*args,**kwargs):
        modeSystem = 'SEH1.Etat.HP41'
        dfmodeHUB = self.loadtags_period(t0,t1,[modeSystem],*args,**kwargs)
        # dfmodeHUB = dfmodeHUB.dropna().astype(int)
        dfmodeHUB.columns=['value']
        dfmodeHUB['mode hub']=dfmodeHUB.applymap(lambda x:self.enumModeHUB[x])
        return dfmodeHUB

    def repartitionPower(self,t0,t1,*args,expand='groups',groupnorm='percent',**kwargs):
        dfs=[]
        armoireTotal = self.getTagsTU('SEH0\.JT.*JTW_')
        dfPtotal = self.loadtags_period(armoireTotal,timeRange,*args,**kwargs)

        if expand=='tags':
            puissancesTotales = self.getTagsTU('JTW_00')
            powertags = self.getTagsTU('JTW')
            powertags = [t for t in powertags if t not in armoireTotal+puissancesTotales]
            df = self.loadtags_period(powertags,timeRange,*args,**kwargs)
            # fig = px.area(df,x='timestamp',y='value',color='tag',groupnorm=groupnorm)
            fig = px.area(df,groupnorm=groupnorm)
        elif expand=='groups':
            pg = {}
            pg['armoire'] = self.getTagsTU('EPB.*JTW')
            pg['enceinte thermique'] = self.getTagsTU('STB_HER.*JTW.*HC20')
            pg['chauffant stack'] = self.getTagsTU('STB_STK.*JTW.*HC20')
            pg['alim stack'] = self.getTagsTU('STK_ALIM.*JTW')
            pg['chauffant GV'] = self.getTagsTU('STG.*JTW')
            pg['blowers'] = self.getTagsTU('BLR.*JTW')
            pg['pompes'] = self.getTagsTU('PMP.*JTW')
            d = pd.DataFrame.from_dict(pg,orient='index').melt(ignore_index=False).dropna()['value']
            d = d.reset_index().set_index('value')
            allTags = list(d.index)

            df = self.loadtags_period(allTags,timeRange,*args,**kwargs)
            df = df.melt(value_name='value',var_name='tag',ignore_index=False)
            df['group']=df.tag.apply(lambda x:d.loc[x])
            fig=px.area(df,x=df.index,y='value',color='group',groupnorm=groupnorm,line_group='tag')
            fig.update_layout(legend=dict(orientation="h"))
            try:
                for k in dfPtotal.columns:
                    fig.add_traces(go.Scatter(x=dfPtotal.index,y=dfPtotal[k],name=k,
                        mode='lines+markers',marker=dict(color='blue')))
            except:
                print('total power not available')
            fig.update_layout(yaxis_title='power in W')
            self.standardLayout(fig)
        return fig,None

    def bilan_echangeur(self,t0,t1,tagDebit='L400',echangeur='CND_03',**kwargs):
        cdn1_tt = self.getTagsTU(echangeur + '.*TT')
        debitEau = self.getTagsTU(tagDebit + '.*FT')
        listTags = cdn1_tt + debit
        if isinstance(timeRange,list) :
            df   = self.loadtags_period(listTags,timeRange,**kwargs)
        if df.empty:
            return df
        debitEau_gs = df[debitEau]*1000/3600
        deltaT = df[cdn3_tt[3]]-df[cdn3_tt[1]]
        puissance_echangee = debitEau_gs*self.cst['Cp_eau_liq']*deltaT
        varUnitsCalculated = {
            'debit eau(g/s)':{'unit':'g/s','var':debitEau_gs},
            'delta température ' + echangeur:{'unit':'°C','var':deltaT},
            'puissance echangée ' + echangeur:{'unit':'W','var':puissance_echangee},
        }
        return df, varUnitsCalculated

    def bilan_valo(self,t0,t1,*args,**kwargs):
        '''
        - timeRange : int if realTime==True --> ex : 60*30*2
        [str,str] if not realtime --> ex : ['2021-08-12 9:00','2020-08-13 18:00']
        '''
        debit_eau = self.getTagsTU('L400.*FT')#kg/h
        cdn1_tt = self.getTagsTU('CND_01.*TT')
        cdn3_tt = self.getTagsTU('CND_03.*TT')
        hex1_tt = self.getTagsTU('HPB_HEX_01')
        hex2_tt = self.getTagsTU('HPB_HEX_02')
        vannes  = self.getTagsTU('40[2468].*TV')
        vanne_hex1, vanne_hex2, vanne_cdn3, vanne_cdn1 = vannes

        t_entree_valo='_TT_02.HM05'
        t_sortie_valo='_TT_04.HM05'
        listTags = debit_eau + cdn1_tt + cdn3_tt + hex1_tt + hex2_tt + vannes

        if isinstance(timeRange,list) :
            df   = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if df.empty:
            return df

        debitEau_gs = df[debit_eau].squeeze()*1000/3600
        nbVannes = df[vannes].sum(axis=1)##vannes NF 0=fermée
        debitUnitaire = debitEau_gs/nbVannes

        deltaT = df[cdn3_tt[3]]-df[cdn3_tt[1]]
        echange_cnd3 = debitUnitaire*self.cst['Cp_eau_liq']*deltaT

        varUnitsCalculated = {
            'debit eau(g/s)':{'unit':'g/s','var':debitEau_gs},
            'nombres vannes ouvertes':{'unit':'#','var':nbVannes},
            'debit eau unitaire':{'unit':'g/s','var':debitUnitaire},
            'delta température':{'unit':'°C','var':deltaT},
            'puissance echange condenseur 3':{'unit':'W','var':echange_cnd3},
        }
        return df, varUnitsCalculated

    def rendement_GV(self,t0,t1,*args,activePower=True,wholeDF=False,**kwargs):
        '''
        - activePower : active or apparente power
        - timeRange : int if realTime==True --> ex : 60*30*2
        [str,str] if not realtime --> ex : ['2021-08-12 9:00','2020-08-13 18:00']'''

        debit_eau = self.getTagsTU('L213_H2OPa.*FT')#g/min
        if activePower:p_chauffants = self.getTagsTU('STG_01a.*JTW')
        else: p_chauffants = self.getTagsTU('STG_01a.*JTVA')
        t_entree_GV = self.getTagsTU('GWPBH_TT')
        t_sortie_GV = self.getTagsTU('L036.*TT')
        TT07 = self.getTagsTU('STG_01a.*TT_02')

        listTags = debit_eau+p_chauffants+t_entree_GV + t_sortie_GV+TT07
        df = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if df.empty:
            return df
        df = df[listTags]
        debitEau_gs = df[debit_eau].squeeze()/60

        #calcul
        power_chauffe_eau_liq = debitEau_gs*self.cst['Cp_eau_liq']*(100-df[t_entree_GV].squeeze())
        power_chauffe_eau_liq = power_chauffe_eau_liq.apply(lambda x :max(0,x))
        power_vapo_eau = debitEau_gs*self.cst['Cl_H2O']
        power_chauffe_vap = debitEau_gs*self.cst['Cp_eau_vap']*(df[t_sortie_GV].squeeze()-100)
        power_chauffe_vap = power_chauffe_vap.apply(lambda x :max(0,x))
        power_total_chauffe = power_chauffe_eau_liq + power_vapo_eau +  power_chauffe_vap
        power_elec_chauffe = df[p_chauffants].sum(axis=1)
        rendement_GV = power_total_chauffe/power_elec_chauffe*100
        rendement_GV_rollmean= rendement_GV.rolling('3600s').mean()
        varUnitsCalculated = {
            'puissance chauffe eau liquide':{'unit':'W','var':power_chauffe_eau_liq},
            'puissance vaporisation eau':{'unit':'W','var':power_vapo_eau},
            'puissance chauffe vaporisation':{'unit':'W','var':power_chauffe_vap},
            'puissance totale de chauffe':{'unit':'W','var':power_total_chauffe},
            'puissance electrique de chauffe':{'unit':'W','var':power_elec_chauffe},
            'rendement GV':{'unit':'%','var':rendement_GV},
            'rendement GV (moyennes)':{'unit':'%','var':rendement_GV},
        }
        return df,varUnitsCalculated

    def pertes_thermiques_stack(self,t0,t1,*args,fuel='N2',activePower=True,**kwargs):
        air_in = self.getTagsTU('HTBA.*HEX_02.*TT.*01')[0]
        air_balayage = self.getTagsTU('HPB.*HEX_02.*TT.*02')[0]
        fuel_in_stack = self.getTagsTU('HTBF.*HEX_01.*TT.*01')[0]
        air_stack_tt = self.getTagsTU('GFC_02.*TT')[0]
        fuel_stack_tt = self.getTagsTU('GFC_01.*TT')[0]
        debitAir = self.getTagsTU('l138.*FT')[0]
        debitFuel = self.getTagsTU('l032.*FT')[0]
        p_chauffants = self.getTagsTU('STK_HER.*JTW')

        listTags = [air_in,air_balayage,fuel_in_stack,air_stack_tt,fuel_stack_tt,debitAir,debitFuel]+p_chauffants

        if isinstance(timeRange,list) :
            df   = self.loadtags_period(listTags,timeRange,**kwargs)
        if df.empty:
            return df
        df = df[listTags]
        cp_fuel,M_fuel = self.dfConstants.loc['Cp_' + fuel,'value'],self.dfConstants.loc['Mmol_' + fuel,'value']
        cp_air,M_air = self.cst['Cp_air'],self.cst['Mmol_Air']
        debitAir_mols = df[debitAir].squeeze()/22.4/60
        debitAirBalayage_mols = df[debitAir].squeeze()/22.4/60
        debitFuel_mols = df[debitFuel].squeeze()/22.4/60
        surchauffe_Air  = (df[air_stack_tt]-df[air_in])*cp_air*M_air*debitAir_mols
        surchauffe_Fuel = (df[fuel_stack_tt]-df[fuel_in_stack])*cp_fuel*M_fuel*debitFuel_mols
        surchauffe_AirBalayage = (df[air_stack_tt]-df[air_in])*cp_air*M_air*debitAirBalayage_mols
        total_puissance_surchauffe_gaz = surchauffe_Air + surchauffe_Fuel + surchauffe_AirBalayage
        puissance_four = df[p_chauffants].sum(axis=1)
        pertes_stack = puissance_four/total_puissance_surchauffe_gaz

        varUnitsCalculated = {
            'debit air(mol/s)':{'unit':'mol/s','var':debitAir_mols},
            'debit fuel(mol/s)':{'unit':'mol/s','var':debitFuel_mols},
            'surchauffe air':{'unit':'W','var':surchauffe_Air},
            'surchauffe fuel':{'unit':'W','var':surchauffe_Fuel},
            'surchauffe air balayage':{'unit':'W','var':surchauffe_AirBalayage},
            'total puissance surchauffe gaz':{'unit':'W','var':total_puissance_surchauffe_gaz},
            'puissance four':{'unit':'W','var':puissance_four},
            'pertes stack':{'unit':'W','var':pertes_stack},
        }
        return df,varUnitsCalculated

    def rendement_blower(self,t0,t1,*args,activePower=True,**kwargs):
        debitAir = self.getTagsTU('138.*FT')
        pressionAmont_a,pressionAmont_b = self.getTagsTU('131.*PT')
        pressionAval = self.getTagsTU('138.*PT')[0]
        puissanceBlowers = self.getTagsTU('blr.*02.*JT')
        t_aval = self.getTagsTU('l126')
        listTags = debitAir+[pressionAmont_a,pressionAmont_b]+[pressionAval]+t_aval+puissanceBlowers

        df   = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if not df.empty:
            df = df[listTags]
            debitAirNm3 = df[debitAir]/1000/60
            deltaP2a_Pa = (df[pressionAval]-df[pressionAmont_a])*100
            deltaP2b_Pa = (df[pressionAval]-df[pressionAmont_b])*100
            deltaP_moyen = (deltaP2a_Pa + deltaP2b_Pa)/2
            p_hydraulique = debitAirNm3.squeeze()*deltaP_moyen
            p_elec = df[puissanceBlowers].sum(axis=1)
            rendement_blower = p_hydraulique/p_elec

        varUnitsCalculated = {
            'debit air(Nm3/s)':{'unit':'Nm3/s','var':debitAirNm3},
            'deltap blower a':{'unit':'Pa','var':deltaP2a_Pa},
            'deltap blower b':{'unit':'Pa','var':deltaP2b_Pa},
            'deltap moyen':{'unit':'mbarg','var':deltaP_moyen},
            'puissance hydraulique':{'unit':'W','var':deltaP_moyen},
            'puissance electrique':{'unit':'W','var':p_elec},
            'rendement blower':{'unit':'%','var':rendement_blower},
            }
        return df,varUnitsCalculated

    def rendement_pumpRecircuFroid(self,t0,t1,*args,activePower=True,**kwargs):
        ### compliqué débit amont
        debitAmont   = self.getTagsTU('303.*FT')+''#???
        debitAval = self.getTagsTU('L032.*FT')
        t_aval = self.getTagsTU('L032.*TT')
        pressionAval = ''#???
        puissancePump = self.getTagsTU('gwpbh.*pmp_01.*JTW')
        listTags = debitAmont + debitAval +t_aval + pressionAval + puissancePump
        df   = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if df.empty:
            return df
        df = df[listTags]
        dfPump = pd.DataFrame()
        dfPump['debit eau total(Nm3/s)'] = (df['debit eau1(g/min)']+df['debit eau2(g/min)'])/1000000/60
        Pout = df['pressionAval(mbarg)']*100
        dfPump['puissance hydraulique(W)'] = dfPump['debit eau total(Nm3/s)']*dfPump['pression sortie(Pa)']
        dfPump['rendement pompe'] = dfPump['puissance hydraulique(W)']/df['puissance pump(W)']*100
        dfPump['cosphiPmp'] = df['puissance pump(W)']/(df['puissance pump(W)']+df['puissance pump reactive (VAR)'])
        varUnitsCalculated = {

        }
        df.columns=[k + ' : ' + l  for k,l in zip(df.columns,listTags)]
        df = pd.concat([df,dfPump],axis=1)
        return df,varUnitsCalculated

    def cosphi(self,t0,t1,*args,**kwargs):
        extVA = 'JTVA_HC20'
        extVAR ='JTVAR_HC20'
        extW ='JTW'
        tagsVA = self.getTagsTU(extVA)
        tagsVAR = self.getTagsTU(extVAR)
        tagsJTW = self.getTagsTU(extW)
        racineVA = [tag.split(extVA)[0] for tag in tagsVA]
        racineVAR = [tag.split(extVAR)[0] for tag in tagsVAR]
        racineW = [tag.split(extW)[0] for tag in tagsJTW]
        tags4Cosphi = list(set(racineVA)&set(racineW))

        jtvas,jtws=[],[]
        for t in tags4Cosphi:
            jtvas.append([tag for tag in tagsVA if t in tag][0])
            jtws.append([tag for tag in tagsJTW if t in tag][0])

        listTags = jtvas + jtws
        if isinstance(timeRange,list):
            df = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if df.empty:
            return df
        cosphi = {t:{'unit':'cosphi','var':df[jtva].squeeze()/df[jtw].squeeze()} for jtva,jtw,t in zip(jtvas,jtws,tags4Cosphi)}
        # cosphi = {jtva+'/'+jtw:{'unit':'cosphi','var':df[jtva].squeeze()/df[jtw].squeeze()} for jtva,jtw in zip(jtvas,jtws)}
        return df,cosphi

    def fuitesAir(self,t0,t1,*args,**kwargs):
        airAmont = self.getTagsTU('l138.*FT')[0]
        airAval = self.getTagsTU('l118.*FT')[0]
        Istacks = self.getTagsTU('STK.*IT.*HM05')
        Tfour = self.getTagsTU('STB_TT_02')[0]
        pressionCollecteur = self.getTagsTU('GFC_02.*PT')[0]
        pressionDiffuseur = self.getTagsTU('GFD_02.*PT')[0]

        listTags =[airAmont,airAval]+Istacks+[Tfour]+[pressionCollecteur,pressionDiffuseur]
        df = self.loadtags_period(t0,t1,listTags,*args,**kwargs)

        if df.empty:
            return pd.DataFrame()
        df = df[listTags]

        # sum courant stacks
        Itotal = df[Istacks].sum(axis=1)
        # production O2
        F = self.dfConstants.loc['FAR'].value
        Po2mols = Itotal*25/(4*F) ##25 cells
        Po2Nlmin = Po2mols*22.4*60
        # fuite air
        # QairAval = df[airAval] + Po2Nlmin
        QairAval = df[airAval] - Po2Nlmin
        fuiteAir = df[airAmont]-(QairAval)
        txFuite = fuiteAir/df[airAmont]*100
        coefficientDeFuite = fuiteAir/df[pressionDiffuseur]

        dfmodeHUB=self.getModeHub(t0,t1,*args,**kwargs)
        # dfmodeHUB=self.getModeHub(timeRange,rs=rs)

        varUnitsCalculated = {
            'courrant stacks total':{'unit':'A','var':Itotal},
            'production O2(mol/s)':{'unit':'mol/s','var':Po2mols},
            'production O2(Nl/min)':{'unit':'Nl/min','var':Po2Nlmin},
            'flux air aval(aval + production O2)':{'unit':'Nl/min','var':QairAval},
            'fuite air':{'unit':'Nl/min','var':fuiteAir},
            'taux de fuite air':{'unit':'%','var':txFuite},
            'coefficient de fuite':{'unit':'N/min/mbar','var':coefficientDeFuite},
            'mode hub':{'unit':'mode hub','var':dfmodeHUB['value']}
        }
        # update mode and hovers
        listTexts={'mode hub':dfmodeHUB['mode hub']}
        return df,varUnitsCalculated,listTexts

    def postItotal(self,t0,t1,*args,**kwargs):
        tagscurrent = self.devices['beckhoff']._get_tags_Istacks()
        df = self.loadtags_period(t0,t1,self.utils.flattenList(tagscurrent.values()),*args,**kwargs)
        return df[list(tagscurrent.values())[0]].apply(lambda x:self.devices['beckhoff'].i_total(x),axis=1)

    def post_fuitesAir(self,t0,t1,alpha=0.005,rsMethod='forwardfill',rs='60s'):
        beckhoff=self.devices['beckhoff']
        tagsfuite     = {k:v[0] for k,v in beckhoff.get_tags_fuiteair().items()}
        df            = self.loadtags_period(t0,t1,list(tagsfuite.values()),rs='1s',rsMethod='forwardfill')
        df['itotal']  = self.postItotal(t0,t1,rs='1s',rsMethod='forwardfill')
        df = df.rename(columns={v:k for k,v in tagsfuite.items()})
        coeffuiteAir = df.apply(lambda x:beckhoff.coefFuitesAir(x['itotal'],x['airAval'],x['airAmont'],x['pressionDiffuseur']),axis=1)
        ### apply lowpass filter
        coeffuiteAir = pd.Series(self.utils.lowpass(coeffuiteAir,alpha),index=coeffuiteAir.index)
        coeffuiteAir.name='coef fuite air'
        return eval(self.methods[rsMethod].replace('df','coeffuiteAir'))

    def fuitesFuel(self,t0,t1,*args,**kwargs):
        '''
        Gonflage :
        - L035 ou L040 fermées et L039 fermée et L027 fermée
        - fuites fuel BF = L303 + L041 (+ Somme i x 25 / 2F)  note : normalement dans ce mode le courant est nul.
        Boucle fermée recirculation à froid (mode pile)
        - L026 et L029 fermées, L027 ouverte, L035 OU L040 fermées
        - fuites fuel BF = L303 + L041 + Somme i x 25 / 2F
        Boucle ouverte (fonctionnement électrolyse ou boucle ouverte pendant les transitions) :
        - (L035 ET L040 ouvertes) ou L026 ouverte ou L029 ouverte
        - fuite ligne fuel BO = L303 + L041 + Somme i x 25 / 2F – L025
        Fonctionnement mode gaz naturel :
        - L027 fermée, L039 ouverte
        - fuites fuel BO = (L032 – L303) x 4 + L303 + L041 + Somme i x 25 / 2F – L025
        En résumé : trois calculs possibles du débit de fuite fuel
        Le même calcul pour les cas 1 et 2 qui sont « fermés »
        Un calcul pour le mode ouvert électrolyse ou boucle ouverte pendant les transitions
        Un calcul pour le mode gaz naturel.
        '''

        vanne26 = self.getTagsTU('l026.*ECV')[0]#NO
        vanne27 = self.getTagsTU('l027.*ECV')[0]#NO
        vanne29 = self.getTagsTU('l029.*ECV')[0]#NF
        vanne35 = self.getTagsTU('l035.*ECV')[0]#NF
        vanne39 = self.getTagsTU('l039.*ECV')[0]#NF
        vanne40 = self.getTagsTU('l040.*ECV')[0]#NF
        vannes = [vanne26,vanne27,vanne29,vanne35,vanne39,vanne40]
        Istacks = self.getTagsTU('STK.*IT.*HM05')

        L025=self.getTagsTU('l025.*FT')[0]
        L032=self.getTagsTU('l032.*FT')[0]
        L041=self.getTagsTU('l041.*FT')[0]
        L303=self.getTagsTU('l303.*FT')[0]
        Tfour = self.getTagsTU('STB_TT_02')
        pressionStacks = self.getTagsTU('GF[CD]_01.*PT')

        debits =[L303,L041,L032,L025]
        listTags = vannes+Istacks+debits+pressionStacks+Tfour

        start = time.time()
        df = self.loadtags_period(listTags,timeRange,*args,**kwargs)
        if df.empty:
            print('no data could be loaded')
            return pd.DataFrame()

        print('loading data in {:.2f} milliseconds'.format((time.time()-start)*1000))
        #############################
        # compute Hydrogen production
        #############################

        Itotal = df[Istacks].sum(axis=1)
        F = self.dfConstants.loc['FAR'].value
        PH2mols = Itotal*25/(2*F) ##25 cells
        PH2Nlmin = PH2mols*22.4*60

        #############################
        # dtermine mode fuel
        #############################

        # convert vannes to bool
        for v in vannes:df[v]=df[v].astype(bool)
        dfModes={}
        # ~df[vanne]==>fermé si NF mais df[vanne]==>ouvert si NO
        # Gonflage :
        # L035 ou L040 fermées et L039 fermée et L027(NO==>0:ouvert) fermée
        dfModes['gonflage'] = (~df[vanne35] | ~df[vanne40]) & (~df[vanne39]) & (df[vanne27])
        # fuites fuel BF = L303 + L041 (+ Somme i x 25 / 2F)  note : normalement dans ce mode le courant est nul.

        # Boucle fermée recirculation à froid (mode pile):
        # L026(NO) et L029 fermées, L027(NO) ouverte, L035 OU L040 fermées
        dfModes['recircuFroidPile']=(df[vanne26]) & (~df[vanne29]) & (~df[vanne27]) & (~df[vanne35]) | (~df[vanne40])
        # fuites fuel BF = L303 + L041 + Somme i x 25 / 2F
        fuitesFuelBF = df[L303] + df[L041] + PH2Nlmin

        # Boucle ouverte (fonctionnement électrolyse ou boucle ouverte pendant les transitions) :
        # (L035 ET L040 ouvertes) ou L026(NO) ouverte ou L029 ouverte
        dfModes['bo_electrolyse']=(df[vanne35] & df[vanne40]) | (~df[vanne26]) | (df[vanne29])
        # - fuites fuel BO = (L032 – L303) x 4 + L303 + L041 + Somme i x 25 / 2F – L025
        fuitesFuelBO = df[L303] + df[L041] + PH2Nlmin - df[L025]
        # Fonctionnement mode gaz naturel :
        # - L027(NO) fermée, L039 ouverte
        dfModes['gaz_nat']=(df[vanne27] & df[vanne39])
        fuitesFuelBO_GN = (df[L032] - df[L303])*4 + df[L303] + df[L041] + PH2Nlmin - df[L025]
        # - fuites fuel BO = (L032 – L303) x 4 + L303 + L041 + Somme i x 25 / 2F – L025

        # check wether they are multiple modes or exclusive modes
        dfModeFuel= [v.apply(lambda x: k+'/' if x==True else '') for k,v in dfModes.items()]
        dfModeFuel = pd.concat(dfModeFuel,axis=1).sum(axis=1).apply(lambda x : x[:-1])
        modesFuel = {v:k for k,v in enumerate(dfModeFuel.unique())}
        modeFuelInt = dfModeFuel.apply(lambda x:modesFuel[x])

        #determine if pileBF or pileBO
        pileBF = [k for k in modesFuel.keys() if 'recircuFroidPile' in k or 'gonflage' in k]
        pileBF = dfModeFuel.apply(lambda x: True if x in pileBF else False)
        dfs=pd.concat([fuitesFuelBO,fuitesFuelBF],axis=1)
        dfs.columns=['BO','BF']
        dfs['pileBF'] = pileBF

        #get fuel fuites in either mode
        fuitesFuel =dfs.apply(lambda x: x['BO'] if x['pileBF'] else x['BF'],axis=1)

        # Vérif débitmètres ligne fuel BF = L032 FT – L303 – L025
        verifDebitmetre = df[L032]-df[L303]-df[L025]

        # get mode Hub
        dfmodeHUB=self.getModeHub(timeRange,**kwargs)

        # define names and scales
        varUnitsCalculated ={
            'courrant stacks total':{'unit':'A','var':Itotal},
            'production H2(mol/s)':{'unit':'mol/s','var':PH2mols},
            'production H2(Nl/min)':{'unit':'Nl/min','var':PH2Nlmin},
            'fuites fuel BF':{'unit':'Nl/min','var':fuitesFuelBF},
            'fuites fuel BO':{'unit':'Nl/min','var':fuitesFuelBO},
            'fuites fuel':{'unit':'Nl/min','var':fuitesFuel},
            'debit 32 - 303 - 25':{'unit':'Nl/min','var':verifDebitmetre},
            'pile BF':{'unit':'etat Pile BF','var':pileBF.astype(int)},
            'mode_Fuel':{'unit':'etat mode Fuel','var':modeFuelInt},
            'mode hub':{'unit':'mode hub','var':dfmodeHUB['value']}
            }

        listTexts={'mode_Fuel':dfModeFuel,'mode hub':dfmodeHUB['mode hub']}
        print('figure computed in in {:.2f} milliseconds'.format((time.time()-start)*1000))
        return df,varUnitsCalculated,listTexts

    def compute_continuousMode_hours(df,modus=10):
        '''10:soec,20:sofc'''
        # df_modes= pd.DataFrame.from_dict(self.enumModeHUB,orient='index',columns=['mode'])
        # df_modes[df_modes['mode']==modus]
        ## fill the data every 1 minute
        dfmode=df.resample('60s',closed='right').ffill()
        ## keep only data for the corresponding mode
        dfmode=dfmode[dfmode['value']==modus]
        ## compute delta times
        deltas=dfmode.reset_index()['timestampUTC'].diff().fillna(pd.Timedelta('0 minutes'))
        ## sum the delta only if they are smaller than 1minute and 1 second
        return deltas[deltas<pd.Timedelta('1 minute,1 second')].sum()

    def compute_H2_produced(df,modus=10):
        tag_mode=['SEH1.Etat.HP41']
        tagDebitH2 = cfg.getTagsTU('L025.*FT.*HM05')
        tagsCurrent = cfg.getTagsTU('alim.*IT_HM05')

        df_etathp41=self.loadtags_period(t0,t1,tag_mode)
        dfmode = df_etathp41.resample('10s',closed='right').ffill()
        dfmode = dfmode[dfmode['value']==10]
        df_debitH2 = self.loadtags_period(t0,t1,tagDebitH2)[['value']]
        I_stacks = self.loadtags_period(t0,t1,tagsCurrent)
        Itotal = I_stacks.sum(axis=1).drop_duplicates()
        Itotal = Itotal.resample('10s').ffill().loc[dfmode.index]
        PH2mol_s = Itotal*25/(2*cfg.cst['FAR']) ##25 cells
        PH2Nlmin = PH2mol_s*22.4*60
        df_debit = df_debitH2.resample('10s').ffill().loc[dfmode.index] ##Nl/min
        H2_produit =(df_debit/60).sum()*10/1000 #Nm3
        H2_produit_I =(PH2Nlmin/60).sum()*10/1000 #Nm3

    def get_I_V_cara():
        tag_mode=['SEH1.Etat.HP41']
        tagsCurrent=cfg.getTagsTU('alim.*IT_HM05')
        tagsVoltage=cfg.getTagsTU('alim.*ET_HM05')
        df_etathp41=readbourinparkedtags(folderpkl,tag_mode,t0,t1)
        df_stack_sn=readbourinparkedtags(folderpkl,tagsStack_sn,t0,t1)
        h_soec,h_sofc=[compute_continuousMode_hours(df_etathp41,m) for m in [10,20]]
        df_cara = df_cara.reset_index().drop_duplicates().set_index('timestampUTC')
        df_cara = processdf(cfg,df_cara,rs = '60s')
        df_cara.to_pickle('df_cara.pkl')

    def plot_I_V_cara():
        ### filter time electrolysis
        tagsCurrent=cfg.getTagsTU('alim.*IT_HM05')
        tagsVoltage=cfg.getTagsTU('alim.*ET_HM05')
        df_cara=pickle.load(open('df_cara.pkl','rb'))
        df2 = df_cara.resample('300s').mean()
        fig=go.Figure()
        for i,v in zip(tagsCurrent,tagsVoltage):
            x=df2[i]
            y=df2[v]
            x=-x[x.abs()>0.1]
            x=x[x<24]
            x=x[x>-60]
            y=y[x.index]
            fig.add_trace(go.Scatter(x=x,y=y,name=i))

        fig.update_traces(mode='markers')
        fig.update_xaxes(title_text='Current (A)')
        fig.update_yaxes(range=[-5,50],title_text='Voltage (V DC)')
        fig.show()

    # ==============================================================================
    #                   graphic functions
    # ==============================================================================
    def toogle_tag_description(self,tagsOrDescriptions,toogleto='tag'):
        '''
        -tagsOrDescriptions:list of tags or description of tags
        -toogleto: you can force to toogleto description or tags ('tag','description')
        '''
        current_names = tagsOrDescriptions
        ### automatic detection if it is a tag --> so toogle to description
        areTags = True if current_names[0] in self.dfplc.index else False
        dictNames=dict(zip(current_names,current_names))
        if toogleto=='description'and areTags:
            newNames  = [self.dfplc.loc[k,'DESCRIPTION'] for k in current_names]
            dictNames = dict(zip(current_names,newNames))
        elif toogleto=='tag'and not areTags:
            newNames  = [self.dfplc.index[self.dfplc.DESCRIPTION==k][0] for k in current_names]
            dictNames = dict(zip(current_names,newNames))
        return dictNames

    def update_lineshape_fig(self,fig,style='default'):
        if style=='default':
            fig.update_traces(line_shape="linear",mode='lines+markers')
            for trace in fig.data:
                name        = trace.name
                dictname    = self.toogle_tag_description([name],'tag')
                tagname     = dictname[name]
                if 'ECV' in tagname or '.HR36' in tagname or self.getUnitofTag(tagname) in ['ETAT','CMD','Courbe']:
                    trace.update(line_shape="hv",mode='lines+markers')

        elif style in ['markers','lines','lines+markers']:
            fig.update_traces(line_shape="linear",mode=style)
        elif style =='stairs':
            fig.update_traces(line_shape="hv",mode='lines')
        return fig

    def updatecolortraces(self,fig):
        for tag in fig.data:
            tagcolor = self.dftagColorCode.loc[tag.name,'colorHEX']
            # print(tag.name,colName,tagcolor)
            tag.marker.color = tagcolor
            tag.line.color = tagcolor
            tag.marker.symbol = self.dftagColorCode.loc[tag.name,'symbol']
            tag.line.dash = self.dftagColorCode.loc[tag.name,'line']

    def updatecolorAxes(self,fig):
        for ax in fig.select_yaxes():
            titleAxis = ax.title.text
            if not titleAxis==None:
                unit    = titleAxis.strip()
                axColor = self.unitDefaultColors.loc[unit].squeeze()[:-1]
                # print(axColor)
                # sys.exit()
                ax.title.font.color = axColor
                ax.tickfont.color   = axColor
                ax.gridcolor        = axColor

    def plotIndicator(self,df,varUnitsCalculated,listTexts={}):
        if isinstance(df,type(go.Figure())):
            return df

        dfCalc = pd.concat([pd.DataFrame(s['var']) for s in varUnitsCalculated.values()],axis=1)
        dfCalc.columns = list(varUnitsCalculated.keys())
        unitGroups={}
        unitGroups.update({k:v['unit'] for k,v in varUnitsCalculated.items()})
        df2_plot=pd.concat([dfCalc,df])
        unitGroups.update({t:self.getUnitofTag(t) for t in df.columns})

        fig = self.utils.multiUnitGraph(df2_plot,unitGroups)
        # fig = self.multiUnitGraphSP(df2_plot,unitGroups)
        fig = self.standardLayout(fig)
        # update mode and hovers
        vanneTags=[k for k in df.columns if 'ECV' in k]
        fig.for_each_trace(
            lambda trace: trace.update(line_shape="hv") if trace.name in vanneTags else (),
        )
        hovertemplatemode='<b>%{y:.2f}' + '<br>     mode:%{text}'
        for k,v in listTexts.items():
            fig.update_traces(selector={'name':k},
                    hovertemplate=hovertemplatemode,
                    text=v,line_shape='hv')
        return fig

    def multiUnitGraphShades(self,df):
        tagMapping = {t:self.getUnitofTag(t) for t in df.columns}
        fig = self.utils.multiUnitGraph(df,tagMapping)
        dfGroups = self.utils.getLayoutMultiUnit(tagMapping)[1]
        listCols = dfGroups.color.unique()
        for k1,g in enumerate(listCols):
            colname = self.colorshades[k1]
            shades = self.colorPalettes[colname]['hex']
            names2change = dfGroups[dfGroups.color==g].index
            fig.update_yaxes(selector={'gridcolor':g},
                        title_font_color=colname[:-1],gridcolor=colname[:-1],tickfont_color=colname[:-1])
            shade=0
            for d in fig.data:
                if d.name in names2change:
                    d['marker']['color'] = shades[shade]
                    d['line']['color']   = shades[shade]
                    shade+=1
            fig.update_yaxes(showgrid=False)
            fig.update_xaxes(showgrid=False)

        # fig.add_layout_image(dict(source=self.imgpeintre,xref="paper",yref="paper",x=0.05,y=1,
        #                             sizex=0.9,sizey=1,sizing="stretch",opacity=0.5,layer="below"))
        # fig.update_layout(template="plotly_white")
        fig.add_layout_image(
            dict(
                source=self.sylfenlogo,
                xref="paper", yref="paper",
                x=0., y=1.02,
                sizex=0.12, sizey=0.12,
                xanchor="left", yanchor="bottom"
            )
        )
        return fig

    def multiUnitGraphSP(self,df,tagMapping=None,**kwargs):
        if not tagMapping:tagMapping = {t:self.getUnitofTag(t) for t in df.columns}
        # print(tagMapping)
        fig = self.utils.multiUnitGraph(df,tagMapping,**kwargs)
        self.standardLayout(fig)
        self.updatecolorAxes(fig)
        self.updatecolortraces(fig)
        return fig

    def doubleMultiUnitGraph(self,df,tags1,tags2,*args,**kwargs):
        fig = VisualisationMaster_daily.multiMultiUnitGraph(self,df,tags1,tags2,*args,**kwargs)
        self.updatecolorAxes(fig)
        self.updatecolortraces(fig)
        self.standardLayout(fig,h=None)
        return fig

    def minmaxFigure(self,t0,t1,tags,rs='600s',subplot=True):
        hex2rgb = lambda h,a:'rgba('+','.join([str(int(h[i:i+2], 16)) for i in (0, 2, 4)])+','+str(a)+')'
        df = self.loadtags_period(t0,t1,tags,rsMethod='forwardfill',rs='100ms',checkTime=True)
        dfmean=df.resample(rs,closed='right').mean()
        dfmin=df.resample(rs,closed='right').min()
        dfmax=df.resample(rs,closed='right').max()

        if subplot:rows=len(df.columns)
        else:rows=1
        fig = make_subplots(rows=rows, cols=1,shared_xaxes=True,vertical_spacing = 0.02)

        for k,tag in enumerate(df.columns):
            hexcol=self.dftagColorCode.loc[tag,'colorHEX']
            col = hex2rgb(hexcol.strip('#'),0.3)
            x = list(dfmin.index) + list(np.flip(dfmax.index))
            y = list(dfmin[tag])+list(np.flip(dfmax[tag]))
            if subplot:row=k+1
            else:row=1
            # fig.add_trace(go.Scatter(x=x,y=y,fill='toself',fillcolor=col,mode='markers+lines',marker={'color':'black'},name=tag+'_minmax'),row=row,col=1)
            fig.add_trace(go.Scatter(x=x,y=y,fill='toself',fillcolor=col,mode='none',marker={'color':'black'},name=tag+'_minmax'),row=row,col=1)
            fig.add_trace(go.Scatter(x=dfmean.index,y=dfmean[tag],mode='markers+lines',marker={'color':hexcol},name=tag),row=row,col=1)
        return fig

    def addTagEnveloppe(self,fig,tag_env,t0,t1,rs):
        hex2rgb = lambda h,a:'rgba('+','.join([str(int(h[i:i+2], 16)) for i in (0, 2, 4)])+','+str(a)+')'
        df    = self.loadtags_period(t0,t1,[tag_env],rsMethod='forwardfill',rs='100ms')
        dfmin = df.resample(rs,label='right',closed='right').min()
        dfmax = df.resample(rs,label='right',closed='right').max()
        hexcol= self.dftagColorCode.loc[tag_env,'colorHEX']
        col = hex2rgb(hexcol.strip('#'),0.3)
        x = list(dfmin.index) + list(np.flip(dfmax.index))
        y = list(dfmin[tag_env])  + list(np.flip(dfmax[tag_env]))
        ### retrieve yaxis
        correctidx=[k for k in self.toogle_tag_description([k.name for k in fig.data],'tag').values()].index(tag_env)
        fig.add_trace(go.Scatter(x=x,y=y,fill='toself',fillcolor=col,mode='none',name=tag_env + '_minmax',yaxis=fig.data[correctidx]['yaxis']
            # line_shape='hv'
            ))
        return fig

class SmallPower_VM(VersionManager_daily,Config_extender):
    def __init__(self,**kwargs):
        Config_extender.__init__(self)
        VersionManager_daily.__init__(self,FOLDERPKL,CONFFOLDER + "/PLC_config/",pattern_plcFiles='*ALPHA*.xlsm',**kwargs)
        self.all_not_ds_history = list(pd.concat([pd.Series(dfplc.index[~dfplc.DATASCIENTISM]) for dfplc in self.df_plcs.values()]).unique())
        self.versionsStart = {
            '2.10':'2021-05-27',
            '2.13':'2021-06-21',
            '2.14':'2021-06-23',
            '2.15':'2021-06-29',
            '2.16':'2021-07-01',
            '2.18':'2021-07-07',
            '2.20':'2021-08-02',
            '2.21':'2021-08-03',
            '2.22':'2021-08-05',
            '2.24':'2021-09-23',
            '2.26':'2021-09-30',
            '2.27':'2021-10-07',
            '2.28':'2021-10-12',
            '2.29':'2021-10-18',
            '2.30':'2021-11-02',
            '2.31':'2021-11-08',
            '2.32':'2021-11-24',
            '2.32':'2021-11-24',
            '2.34':'2021-11-25',
            '2.35':'2021-11-25',
            '2.36':'2021-11-29',
            '2.37':'2021-12-09',
            '2.40':'2021-12-14',
            '2.42':'2022-01-10',
        }

    def load_PLC_versions(self):
        print('Start reading all .xlsm files....')
        df_plcs = {}
        for f,v in self.dicVersions.items():
            print(f)
            df_plcs[v] = pd.read_excel(f,sheet_name='FichierConf_Jules',index_col=0)
        print('')
        print('concatenate tags of all dfplc verion')
        all_tags_history = list(pd.concat([pd.Series(dfplc.index[dfplc.DATASCIENTISM]) for dfplc in df_plcs.values()]).unique())
        return df_plcs,all_tags_history

    def remove_notds_tags(self,*args,**kwargs):
        self.streamer.remove_tags_daily(self.all_not_ds_history,self.folderData,*args,**kwargs)
