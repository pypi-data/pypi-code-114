from pywifi import PyWiFi
from subprocess import getstatusoutput
from bluetooth import discover_devices

version = 4
class Wifi():
    def Scan(self):
        results = []
        scan = PyWiFi().interfaces()[0]
        scan.scan()
        scan = scan.scan_results()
        for i in scan:
            if [i.ssid,i.bssid] not in results:
                results.append([i.ssid,i.bssid])
        return results
    def ConnectStatus(self):
        connectstatus = PyWiFi().interfaces()[0]
        if connectstatus.status() in [4,2]:
            return True
        else:
            return False
    def ConnectName(self):
        status, output = getstatusoutput("netsh WLAN show interfaces")
        for i in output.split('\n'):
            if i.find('    SSID                   : ') != -1:
                return i.split('    SSID                   : ')[1]

class Bluetooth():
    def Scan(self):
        results = []
        scan = discover_devices(lookup_names=True)
        for(addr,name) in scan:
            if addr not in results:
                results.append([name,addr])
        return results