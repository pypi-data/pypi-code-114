#working with dorianUtilsModulaire==4_0
import time, os,importlib
start=time.time()
from dorianUtils.dccExtendedD import DccExtended
from dorianUtils.utilsD import Utils
import dash_html_components as html
import dash, dash_bootstrap_components as dbc
import smallPowerDash.smallPower as smallPower
import smallPowerDash.smallPowerTabs as sptabs
import dash_auth
VALID_USERNAME_PASSWORD_PAIRS = {
    'smallpower': 'gggmnd',
}
importlib.reload(smallPower)
importlib.reload(sptabs)
print('imports in {:.2f} milliseconds'.format((time.time()-start)*1000))
# ==============================================================================
#                       START APP
# ==============================================================================
utils = Utils()
dccE = DccExtended()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                title='smallPower(dev)')
#### secure app with password
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)
cfg = smallPower.SmallPowerComputer(rebuildConf=True)
# cfg.dbParameters['dbname']='jules'
# cfg.dbParameters['host']='192.168.7.2'

# stTab = sptabs.TabSelectedTags_SP(app,cfg,realtime=False,tabname='catégorie de tags')
# stTab_rt = sptabs.TabSelectedTags_SP(app,cfg,realtime=True,tabname='catégorie de tags temps réel',baseid='stsp_rt')
# muTab = sptabs.TabMultiUnit_SP(app,cfg,realtime=False,tabname='multi-échelles')
# muTab_RT = sptabs.TabMultiUnit_SP(app,cfg,realtime=True,baseid='mustp_rt_',tabname='temps réel multi-échelles')
musTab = sptabs.TabMultiUnitSelectedTags_SP(app,cfg,realtime=False,tabname='explorateur')
musTab_RT = sptabs.TabMultiUnitSelectedTags_SP(app,cfg,realtime=True,baseid='must_sp_rt_',tabname='temps réel')
# dmuTab_RT = sptabs.TabDoubleMultiUnits_SP(app,cfg,realtime=True,tabname='double échelles temps réel')
# tuTab = sptabs.TabUnitSelector_SP(app,cfg,realtime=False)
# indicatorTab = sptabs.IndicatorTab(app,cfg,realtime=False)
# analysisTab   = tabsD.AnalysisTab(app,cfg)

# tabs = [stTab,stTab_rt,muTab,muTab_RT,musTab,musTab_RT,dmuTab_RT]
# tabs = [muTab,muTab_RT,musTab,musTab_RT]
# tabs = [musTab,musTab_RT]
tabs = [musTab,musTab_RT]

tabsLayout= dccE.createTabs(tabs)

### add modals
mdFile   = cfg.confFolder + 'logVersionSmallPower_user.md'
titleLog = 'SmallPower 4.1(log)'
modalLog = dccE.addModalLog(app,titleLog,mdFile)
modalErrors = [m.modalError for m in tabs]
app.layout = html.Div([html.Div(modalErrors+[modalLog]),html.Div(tabsLayout)])

app.run_server(port=20000,host='0.0.0.0',debug=True,use_reloader=True)
