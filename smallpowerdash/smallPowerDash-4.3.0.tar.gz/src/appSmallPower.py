#working with dorianUtilsModulaire==4_1
import time, os,importlib
start=time.time()
from dorianUtils.dccExtendedD import DccExtended

import dash, dash_auth, dash_html_components as html
import dash, dash_bootstrap_components as dbc
import smallPowerDash.smallPower as smallPower
import smallPowerDash.smallPowerTabs as sptabs
print('imports in {:.2f} milliseconds'.format((time.time()-start)*1000))

VALID_USERNAME_PASSWORD_PAIRS = {
    'smallpower': 'gggmnd',
}
# ==============================================================================
#                       START APP
# ==============================================================================
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                title='smallPower(dev)')
#***** secure app with password
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)
cfg  = smallPower.SmallPowerComputer(rebuildConf=True)

musTab = sptabs.TabMultiUnitSelectedTags_SP(app,cfg,realtime=False,tabname='explorateur')
musTab_RT = sptabs.TabMultiUnitSelectedTags_SP(app,cfg,realtime=True,baseid='must_sp_rt_',tabname='temps réel')
tabs = [musTab,musTab_RT]

dccE=DccExtended()
tabsLayout= dccE.createTabs(tabs)

### add modals
mdFile   = cfg.confFolder + 'logVersionSmallPower_user.md'
titleLog = 'SmallPower 4.2(log)'
modalLog = dccE.addModalLog(app,titleLog,mdFile)
modalErrors = [m.modalError for m in tabs]
app.layout = html.Div([html.Div(modalErrors+[modalLog]),html.Div(tabsLayout)])

app.run_server(port=45001,host='0.0.0.0',debug=True,use_reloader=False)
