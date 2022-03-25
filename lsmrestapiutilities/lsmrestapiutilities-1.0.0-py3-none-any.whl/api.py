from http.client import responses
from .consts import URL

import requests

class RESTAPI :
    def __init__(self, api_key) :
        self.api_key = api_key
    
    def request(self, api_url, params={}) :
        args = {'Authorization' : self.api_key}
        for key, value in params.items() :
            if key not in args :
                args[key] = value
        response = requests.get(
            URL['base'].format(
                url=api_url
            ),
            headers=args
        )
        
        return response.json()

    def custom_filtered_request(self, endpoint, filter) :
        api_url = URL[endpoint].format(url=filter)
        return self.request(api_url)

    def custom_request(self, url) :
        api_url = URL['base'].format(url=url)
        return self.request(api_url)



    def get_summoner_by_name(self, summoner_name) :
        api_url = URL['summoners'].format(url='?name={name}'.format(name=summoner_name))
        return self.request(api_url)

    def get_summoner_by_id(self, id) :
        api_url = URL['summoners'].format(url='?id={id}'.format(id=id))
        return self.request(api_url)

    def get_summoner_by_account_id(self, account_id) :
        api_url = URL['summoners'].format(url='?accountid={id}'.format(id=account_id))
        return self.request(api_url)

    def get_summoner_by_puuid(self, puuid) :
        api_url = URL['summoners'].format(url='?puuid={id}'.format(id=puuid))
        return self.request(api_url)

    def get_summoner_by_level(self, level) :
        api_url = URL['summoners'].format(url='?summonerlevel={level}'.format(level=level))
        return self.request(api_url)


    
    def get_map_by_id(self, id) :
        api_url = URL['maps'].format(url='?mapid={id}'.format(id=id))
        return self.request(api_url)

    def get_map_by_name(self, name) :
        api_url = URL['maps'].format(url='?mapname={name}'.format(name=name))
        return self.request(api_url)



    def get_rune_by_id(self, id) :
        api_url = URL['runes'].format(url='?runeid={id}'.format(id=id))
        return self.request(api_url)

    def get_rune_by_name(self, name) :
        api_url = URL['runes'].format(url='?name={name}'.format(name=name))
        return self.request(api_url)

    def get_rune_by_style(self, style) :
        api_url = URL['runes'].format(url='?style={style}'.format(style=style))
        return self.request(api_url)



    def get_runestyle_by_id(self, id) :
        api_url = URL['runestyles'].format(url='?styleid={id}'.format(id=id))
        return self.request(api_url)

    def get_runestyle_by_name(self, name) :
        api_url = URL['runestyles'].format(url='?name={name}'.format(name=name))
        return self.request(api_url)



    def get_queue_by_id(self, id) :
        api_url = URL['queues'].format(url='?queueid={id}'.format(id=id))
        return self.request(api_url)

    def get_queue_by_map(self, map) :
        api_url = URL['queues'].format(url='?map={map}'.format(map=map))
        return self.request(api_url)

    

    def get_champion_by_id(self, id) :
        api_url = URL['champions'].format(url='?championid={id}'.format(id=id))
        return self.request(api_url)

    def get_champion_by_name(self, name) :
        api_url = URL['champions'].format(url='?name={name}'.format(name=name))
        return self.request(api_url)



    def get_championmastery_by_summonerid(self, summonerid) :
        api_url = URL['championmasteries'].format(url='?summonerid={id}'.format(id=summonerid))
        return self.request(api_url)

    def get_championmastery_by_championid(self, championid) :
        api_url = URL['championmasteries'].format(url='?championid={id}'.format(id=championid))
        return self.request(api_url)



    def get_league_by_leagueid(self, leagueid) :
        api_url = URL['leagues'].format(url='?leagueid={id}'.format(id=leagueid))
        return self.request(api_url)

    def get_league_by_queue(self, queue) :
        api_url = URL['leagues'].format(url='?queuetype={queue}'.format(queue=queue))
        return self.request(api_url)

    def get_league_by_tier(self, tier) :
        api_url = URL['leagues'].format(url='?tier={tier}'.format(tier=tier))
        return self.request(api_url)

    def get_league_by_rank(self, rank) :
        api_url = URL['leagues'].format(url='?rank={rank}'.format(rank=rank))
        return self.request(api_url)

    def get_league_by_summonerid(self, summonerid) :
        api_url = URL['leagues'].format(url='?summonerid={id}'.format(id=summonerid))
        return self.request(api_url)

    def get_league_by_summonername(self, summonername) :
        api_url = URL['leagues'].format(url='?summonername={name}'.format(name=summonername))
        return self.request(api_url)

    

    def get_item_by_id(self, id) :
        api_url = URL['items'].format(url='?itemid={id}'.format(id=id))
        return self.request(api_url)

    def get_item_by_name(self, name) :
        api_url = URL['items'].format(url='?name={name}'.format(name=name))
        return self.request(api_url)


    
    def get_match_by_id(self, id) :
        api_url = URL['matches'].format(url='?matchid={id}'.format(id=id))
        return self.request(api_url)

    def get_match_by_mapid(self, mapid) :
        api_url = URL['matches'].format(url='?mapid={id}'.format(id=mapid))
        return self.request(api_url)

    def get_match_by_queueid(self, queueid) :
        api_url = URL['matches'].format(url='?queueid={id}'.format(id=queueid))
        return self.request(api_url)

    def get_match_by_gameversion(self, gameversion) :
        api_url = URL['matches'].format(url='?gameversion={version}'.format(version=gameversion))
        return self.request(api_url)

    def get_match_by_gamemode(self, gamemode) :
        api_url = URL['matches'].format(url='?gamemode={mode}'.format(mode=gamemode))
        return self.request(api_url)

    def get_match_by_gamename(self, gamename) :
        api_url = URL['matches'].format(url='?gamename={name}'.format(name=gamename))
        return self.request(api_url)

    

    def get_matchteam_by_matchid(self, id) :
        api_url = URL['matchteams'].format(url='?matchid={id}'.format(id=id))
        return self.request(api_url)

    def get_matchteam_by_teamid(self, teamid) :
        api_url = URL['matchteams'].format(url='?teamid={id}'.format(id=teamid))
        return self.request(api_url)

    def get_matchteam_by_matchid_and_teamid(self, id, teamid) :
        api_url = URL['matchteams'].format(url='?matchid={id}&teamid={teamid}'.format(id=id, teamid=teamid))
        return self.request(api_url)

    

    def get_matchparticipant_by_matchid(self, matchid) :
        api_url = URL['matchparticipants'].format(url='?matchid={id}'.format(id=matchid))
        return self.request(api_url)

    def get_matchparticipant_by_summonerid(self, summonerid) :
        api_url = URL['matchparticipants'].format(url='?summonerid={id}'.format(id=summonerid))
        return self.request(api_url)

    def get_matchparticipant_by_puuid(self, puuid) :
        api_url = URL['matchparticipants'].format(url='?puuid={id}'.format(id=puuid))
        return self.request(api_url)

    def get_matchparticipant_by_matchid_and_summonerid(self, matchid, summonerid) :
        api_url = URL['matchparticipants'].format(url='?matchid={id}&summonerid={summonerid}'.format(id=matchid, summonerid=summonerid))
        return self.request(api_url)

    def get_matchparticipant_by_matchid_and_puuid(self, matchid, puuid) :
        api_url = URL['matchparticipants'].format(url='?matchid={id}&puuid={puuid}'.format(id=matchid, puuid=puuid))
        return self.request(api_url)

    

    def get_summonerspell_by_key(self, key) :
        api_url = URL['summonerspells'].format(url='?spellkey={key}'.format(key=key))
        return self.request(api_url)

    def get_summonerspell_by_id(self, id) :
        api_url = URL['summonerspells'].format(url='?spellid={id}'.format(id=id))
        return self.request(api_url)

    def get_summonerspell_by_name(self, name) :
        api_url = URL['summonerspells'].format(url='?name={name}'.format(name=name))
        return self.request(api_url)