from datetime import date, datetime

from .constants import *

class PlayerStats():
    def __init__(self, gen=DEFAULTINFO, over=DEFAULTOVER, game=DEFAULTGAME):
        total = calculate_total(game)
        self.lastLoginName = gen["lastLoginName"]
        self.lastLoginTimeRaw = gen["lastLoginTime"]
        self.lastLoginTime = datetime.fromtimestamp(self.lastLoginTimeRaw).strftime("%I:%M %p on %B %d, %Y")
        self.role = gen["role"]
        self.level = over["level"]
        self.weightedwins = over["weightedwins"]
        self.xp = over["exp"]
        self.wins = total["wins"]
        self.finals = total["finals"]
        self.kills = total["kills"]
        self.beds = total["beds"]

    def generalInfo(self):
        print(f'''General Info:
Last Login Name: {self.lastLoginName}
Last Login Time: {self.lastLoginTime}
Rank: {self.role}''')

        # print(f"{VOXYLBASE}{VOXYLINFO.format(self.uuid, VOXYLAPI.format(self.key))}")
        # getapi = requests.get(f"{VOXYLBASE}{VOXYLINFO.format(self.uuid, VOXYLAPI.format(self.key))}").json()
        # if getapi["success"] != True:
        #     return None
        # return getapi

    def generalStats(self):
        print(f'''General Stats:
Level: {self.level}
XP: {self.xp}
Weighted Wins: {self.weightedwins}''')

        # getapi = requests.get(f"{VOXYLBASE}{VOXYLOVERALL.format(self.uuid, VOXYLAPI.format(self.key))}").json()
        # if getapi["success"] != True:
        #     return None
        # return getapi

    def overallGameStats(self):
        print(f'''Overall Game Stats:
Total Wins: {self.wins}
Total Finals: {self.finals}
Total Kills: {self.kills}
Total Beds Destroyed: {self.beds}''')

        # getapi = requests.get(f"{VOXYLBASE}{VOXYLGAME.format(self.uuid, VOXYLAPI.format(self.key))}").json()
        # if getapi["success"] != True:
        #     return None
        # return getapi

class WeightedLevelLBPlayer(PlayerStats):
    def __init__(self, placing, gen=DEFAULTINFO, over=DEFAULTOVER, game=DEFAULTGAME):
        super().__init__()
        self.placing = placing
        total = calculate_total(game)
        self.lastLoginName = gen["lastLoginName"]
        self.lastLoginTimeRaw = gen["lastLoginTime"]
        self.lastLoginTime = datetime.fromtimestamp(self.lastLoginTimeRaw).strftime("%I:%M %p on %B %d, %Y")
        self.role = gen["role"]
        self.level = over["level"]
        self.weightedwins = over["weightedwins"]
        self.xp = over["exp"]
        self.wins = total["wins"]
        self.finals = total["finals"]
        self.kills = total["kills"]
        self.beds = total["beds"]

class TechniqueLBPlayer(PlayerStats):
    def __init__(self, placing, time, subtime, gen=DEFAULTINFO, over=DEFAULTOVER, game=DEFAULTGAME):
        super().__init__()
        self.placing = placing
        self.time = time
        self.subtime = subtime
        total = calculate_total(game)
        self.lastLoginName = gen["lastLoginName"]
        self.lastLoginTimeRaw = gen["lastLoginTime"]
        self.lastLoginTime = datetime.fromtimestamp(self.lastLoginTimeRaw).strftime("%I:%M %p on %B %d, %Y")
        self.role = gen["role"]
        self.level = over["level"]
        self.weightedwins = over["weightedwins"]
        self.xp = over["exp"]
        self.wins = total["wins"]
        self.finals = total["finals"]
        self.kills = total["kills"]
        self.beds = total["beds"]

def calculate_total(data):
    wins = 0
    finals = 0
    kills = 0
    beds = 0
    for i in data:
        try:
            wins += data[i]["wins"]
        
        except:
            pass

        try:
            finals += data[i]["finals"]
        
        except:
            pass

        try:
            kills += data[i]["kills"]
        
        except:
            pass

        try:
            beds += data[i]["beds"]
        
        except:
            pass
    
    return {"wins": wins, "finals": finals, "kills": kills, "beds": beds}