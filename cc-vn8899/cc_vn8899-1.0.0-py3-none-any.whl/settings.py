import os

VN8899_AGENT_DOMAIN = os.getenv('VN8899_AGENT_DOMAIN', 'http://www.vn8899a.info/')

CAPTCHA_URL = 'backstage/rand.action'
LOGIN_URL = 'login.action'
WELCOME_URL = 'welcome.action'
REPORT_URL = 'report/rptPL.action'

MAX_CAPTCHA_TRY = 5
MAX_LOGIN_TRY = 10

DATE_FORMAT = '{:%Y-%m-%d}'
