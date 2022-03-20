class LBRY_Channel():
    def __init__(self,claim,LBRY_api):
        self._LBRY_api = LBRY_api
        error_occured = False

        if not 'value_type' in claim:
            raise ValueError('malformed claim')
        if claim["value_type"] == "repost":
            claim = claim["reposted_claim"]
        self.raw = claim
        if claim["value_type"] != "channel":
            raise ValueError('This not a channel')

        if 'claim_id' in claim:
            self.id = claim['claim_id']
        elif 'channel_id' in claim:
            self.id = claim['channel_id']
        else:
            print('Error parsing channel claim, id not found')
            error_occured = True

        try:
            self.name = claim['name']
        except KeyError as err:
            print('Error parsing channel claim, name not found')
            error_occured = True
            self.name = 'Anonymous'

        if 'canonical_url' in claim:
            self.url = claim['canonical_url']
        elif 'permanent_url' in claim:
            self.url = claim['permanent_url']
        else:
            print('Error finding url in channel claim:')
            error_occured = True
            self.url = ''

        try:
            self.thumbnail = claim['value']['thumbnail']['url']
        except KeyError:
            self.thumbnail = ''

        if 'value' in claim:
            self.title = claim['value']['title'] if 'title' in claim['value'] else ''
            self.description = claim['value']['description'] if 'description' in claim['value'] else ''
        else:
            self.title = ''
            self.description = ''

        if error_occured:
            print(claim)

        self.pubs_feed = self.get_pubs_feed()

    def __str__(self):
        return f"LBRY_Channel({self.name})"
    
    def get_pubs_feed(self):
        return self._LBRY_api.channels_feed([self.id])

    def refresh_feed(self):
        self.pubs_feed = self.get_pubs_feed()

    def follow(self):
        self._LBRY_api.add_sub_url(self.raw['permanent_url'])

    def unfollow(self):
        self._LBRY_api.remove_sub_url(self.raw['permanent_url'])

    @property
    def is_followed(self):
        return self.raw['permanent_url'] in self._LBRY_api.subs_urls

class LBRY_Channel_Err(LBRY_Channel):
    def __init__(self):
        self.name = 'Error'
        self.id = '0'
        self.url = ''
        self.title = ''
        self.description = ''
        self.pubs = []
        self.pubs_feed = iter([])

    def __str__(self):
        return f"Errored LBRY_Channel({self.name})"
    
    def get_pubs_feed(self):
        return iter([])

