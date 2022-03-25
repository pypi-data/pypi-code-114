import time, os, importlib
start=time.time()
import dorianUtils.dccExtendedD as dccExtendD
import dash_html_components as html
import dash, dash_bootstrap_components as dbc
import monitorBuildingDash.screenBuilding as screenBuilding
import monitorBuildingDash.screenBuildingTabs as sbtabs
from dorianUtils import dashTabsD as tabsD
import dash_auth
VALID_USERNAME_PASSWORD_PAIRS = {
    'monitoring': 'sls_actiparc',
}

print('imports in {:.2f} milliseconds'.format((time.time()-start)*1000))
# ==============================================================================
#                       START APP
# ==============================================================================
dccE = dccExtendD.DccExtended()
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                title='monitoring EMS')
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

cfg = screenBuilding.ScreenBuildingComputer()
cfg.dbParameters={
    'host'     : "localhost",
    'port'     : "5432",
    'dbname'   : "bigbrother",
    'user'     : "postgres",
    'password' : "sylfenbdd"
    }

musTab    = sbtabs.TabMultiUnitSelectedTags_SB(app,cfg,realtime=False,tabname='explorateur')
musTab_RT = sbtabs.TabMultiUnitSelectedTags_SB(app,cfg,realtime=True,baseid='must_sp_rt_',tabname='temps réel')

tabs = [musTab,musTab_RT]

tabsLayout= dccE.createTabs(tabs)

### add modals
mdFile   = cfg.confFolder + 'screeningBuilding_user.md'
titleLog = 'Monitoring EMS 4.3(log)'
modalLog = dccE.addModalLog(app,titleLog,mdFile)
modalErrors = [m.modalError for m in tabs]
app.layout = html.Div([html.Div(modalErrors+[modalLog]),html.Div(tabsLayout)])

# port=20000
port=35000
app.run_server(host='0.0.0.0',port=port,debug=False,use_reloader=False)
