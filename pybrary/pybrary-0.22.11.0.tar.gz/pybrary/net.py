from urllib.request import urlopen

from .shell import shell
from . import logger, debug, error

def get_ip_adr():
    url = 'http://api.ipify.org'
    with urlopen(url, timeout=1) as resp:
        if resp.status==200:
            adr = resp.read().decode().strip()
            debug('ip adr : %s', adr)
            return True, adr
        else:
            error('%s %s', resp.status, resp.reason)
            return False, resp.reason


def check_vuln(adr):
    cmd = f'nmap -Pn --script vuln {adr}'
    print('cmd:', cmd)
    ret, out, err = shell(cmd)
    print('ret:', ret)
    print('out:', out)
    print('err:', err)

def check_malware(adr):
    cmd = f'nmap -sV --script=http-malware-host {adr}'
    print('cmd:', cmd)
    ret, out, err = shell(cmd)
    print('ret:', ret)
    print('out:', out)
    print('err:', err)

