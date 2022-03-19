import os

SBOBET_AGENT_DOMAIN = os.getenv('SBOBET_AGENT_DOMAIN', 'http://agent.sbobetsg.com/')
SBOBET_DOMAIN = os.getenv('SBOBET_DOMAIN', 'https://konduangdee.com')

DEFAULT_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

URI_PASSWORD_FRAME = 'WebRoot/Restricted/Security/passwordframe.aspx'

