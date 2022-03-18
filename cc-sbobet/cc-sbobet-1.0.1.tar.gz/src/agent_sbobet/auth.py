import re

from api_helper import get_uri, captcha_solver
from . import settings


def get_vcode(session, hidck, domain):
    r = session.post(get_uri('WebRoot/Restricted/Security/passwordframe.aspx', domain), data={
        'cmd': 'ref',
        'HidCK': hidck,
    })

    url = re.findall(r"updateImgText\('([^']*)'\)", r.text)[0].replace('../../', 'WebRoot/')

    print(get_uri(url, domain))

    r = session.get(get_uri(url, domain))

    # print(r.text)

    return captcha_solver(r.content)


def force_change_password(session, domain, hidck, password1, password2, code):
    while True:
        vcode = ''

        while len(vcode) != 4:
            print('try to solve code')
            vcode = get_vcode(session, hidck, domain)

            # print('vcode', vcode)

        form_data = {
            'HidCK': hidck,
            'cmd': 'update',
            'currPwd': password1,
            'newPwd': password2,
            'confirmPwd': password2,
            'hidMsgEnabled': '0',
            'hidPwdEnabled': '1',
            'hidSecurityCodeEnabled': '0',
            'txtMsg': code,
            'txtSecurityCode': code,
            'vcode': vcode,
        }

        r = session.post(get_uri(settings.URI_PASSWORD_FRAME, domain), data=form_data)

        if 'Please enter a correct validation code' not in r.text:
            return r


def change_password(session, domain, old_password, new_password, code):
    r = session.get(get_uri('webroot/restricted/Security/password.aspx?p=1', domain))
    hidck = re.findall("HidCK.*value='([^']*)'", r.text)[0]
    return force_change_password(session, domain, hidck, old_password, new_password, code)
