'''
This script was made by neokeee 2022.
Easier Layout of Discord rich presence for API JSON.
Author: @neokeee & @etherlesss
Last Update: 20/03/22
'''

from datetime import datetime
import requests as r
import psutil, time

class RPCLayout():
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
    def _waitingForOpen(self, game):
        '''
        :param bool game: game or program. Recieves boolean.
        
        This function active a while loop with a time.sleep(2) until the game start.
        '''
        waitingGame = True
        while waitingGame:
            if game is True:
                waitingGame = False
                break
            time.sleep(2)
    def request_api(self, url):
        '''
        :param str url: API URL, must be in json format.
        '''
        error_response = "<Response [500]>"
        failed_response = "<Response [400]>"
        reject_response = "<Response [403]>"
        req = r.get(url)
        if error_response in str(req):
            print("Error in API:", error_response)
            exit()
        elif failed_response in str(req):
            print("An error ocurred loading API:", failed_response)
            exit()
        elif reject_response in str(req):
            print('The server has recieved the request but refuses to authorize it:', reject_response)
            exit()
        data = req.json()
        return data
    def _checkGameIsClosed(self, game):
        '''
        :param bool game: Game
        
        Returns a boolean when the game is closed.
        '''
        if game is False:
            return True
        else:
            pass