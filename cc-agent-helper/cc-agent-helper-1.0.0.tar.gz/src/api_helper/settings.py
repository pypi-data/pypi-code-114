import os

DEFAULT_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

WIN_LOSE_MONGODB_URL = os.getenv('WIN_LOSE_MONGODB_URL', os.getenv('MONGODB_URL', ''))
TICKET_MONGODB_URL = os.getenv('TICKET_MONGODB_URL', os.getenv('MONGODB_URL', ''))

CAPTCHA_API = os.getenv('CAPTCHA_API', 'https://ocr.cockreative.com/')
