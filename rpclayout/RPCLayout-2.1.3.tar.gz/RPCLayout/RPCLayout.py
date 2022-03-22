'''
This script was made by neokeee 2022.
Easier Layout of Discord rich presence for API.JSON.
Author: @neokeee & @etherlesss
Last Update: 21/03/22
'''

from datetime import datetime
import requests as r
import psutil, time, os, platform, subprocess

http_errors = {
    "error-response": "<Response [500]>",
    "badgateway-response": "<Response [502]>",
    "failed-response": "<Response [400]>",
    "rejected-response": "<Response [403]>",
    "unauthorize-response": "<Response [401]>",
    "notfound-response": "<Response [404]>",
    "timeout-response": "<Response [408]>",
}

def __http_response__(string, dict):
    '''
    Kill program, http error response.
    '''
    print(string, dict)
    exit()

# req for mac m1
def isMac():
    return platform.system() == "Darwin"

def getProcessorMac():
    return subprocess.check_output(['sysctl','-n','machdep.cpu.brand_string']).decode('utf-8')

def isM1():
    return getProcessorMac() == "Apple M1\n"

class RPCLayout():
    def _isM1():
        return getProcessorMac() == "Apple M1\n"
    def _system(self):
        '''
        Return the operating system
        Darwin: MACOSX
        '''
        if platform.system() == "Windows":
            return "Windows"
        elif platform.system() == "Darwin":
            print(isM1())
            return "Darwin"
        
    def _getpid(self):
        '''
        Returns the program PID, use it for Presence.update(pid=_getpid())
        '''
        return os.getpid()
    def timestamp(self):
        '''
        TimeStamp made by etherlesss.
        '''
        now = datetime.utcnow()
        elapsed = int((now - datetime(1970, 1, 1)).total_seconds())
        return elapsed
    def _detectGame(self, gameExe):
        '''
        :param str gameExe: Game or program (MacOS supported!)
        Find the program.exe and returns True if the function found it, return False if function don't found it
        '''
        game = gameExe in (p.name() for p in psutil.process_iter())
        return game
    def _waitingForOpen(self, game = str):
        '''
        :param str game: game or program. Recieves a string.
    
        This function active a while loop with a time.sleep(2) until the game start.
        '''
        waitingGame = True
        while waitingGame:
            if game is True or game is False:
                print('Game cannot be a boolean!')
                break
            if self._detectGame(game) is True:
                waitingGame = False
                break
            time.sleep(2)
    def request_api(self, url):
        '''
        :param str url: API URL, must be in json format.
        
        Load HTTP GET with requests and take the information converting the body in json.
        '''
        req = r.get(url)
        if http_errors["error-response"] in str(req):
            print("Error in API:", http_errors["error-response"])
            exit()
        elif http_errors["failed-response"] in str(req):
            __http_response__("An error ocurred loading API:", http_errors["failed-response"])
        elif http_errors["rejected-response"] in str(req):
            __http_response__("The server has recieved the request but refuses to authorize it:", http_errors["rejected-response"])
        elif http_errors["timeout-response"] in str(req):
            __http_response__("Timeout:", http_errors["timeout-response"])
        elif http_errors["badgateway-response"] in str(req):
            __http_response__("Server error response code indicates that the server, while acting as a gateway or proxy, received an invalid response from the upstream server:", http_errors["badgateway-response"])
        elif http_errors["unauthorize-response"] in str(req):
            __http_response__("Unauthorize:", http_errors["unauthorize-response"])
        elif http_errors["notfound-response"] in str(req):
            __http_response__("HTTP Not found:", http_errors["notfound-response"])
        data = req.json()
        return data
    def _checkGameIsClosed(self, game):
        '''
        :param str game: Game
        
        Returns a boolean when the game is closed.
        '''
        if game is True or game is False:
            print('Game cannot be a boolean!')
            exit()
        if self._detectGame(game) is False:
            return True
        else:
            pass
        
    def destroy(self, rpc, text=""):
        '''
        :param str text: If want put error handler.
        :param pypresence.Presence rpc: RCP class for close the rcp and destroy the program.
        Destroy RPC and Program when something happen.
        '''
        if text=="":
            pass
        else:
            print(text)
            time.sleep(2)
        rpc.close()
        exit()