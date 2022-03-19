from pytz import timezone as tz
from datetime import datetime
from pprint import pprint

from data_verifier.model.metro import DelhiMetro
from data_verifier.base import BaseResposne
from data_verifier.exceptions.exception import VerificationError

class DelhiMetroClass(BaseResposne):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'Host': 'backend.delhimetrorail.com',
        'Origin': 'https://www.delhimetrorail.com',
        'Referer': 'https://www.delhimetrorail.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    list_all_line_url="https://backend.delhimetrorail.com/api/v2/en/line_list"
    station_code_url='https://backend.delhimetrorail.com/api/v2/en/station_by_keyword/all/{}'
    station_by_line_url='https://backend.delhimetrorail.com/api/v2/en/station_by_line/{}'
    station_brief_detail_url='https://backend.delhimetrorail.com/api/v2/en/station_brief_detail/{}'
    least_distance_destination_url='https://backend.delhimetrorail.com/api/v2/en/station_route/{}/{}/least-distance/{}'
    minimum_interchange_destination_url = 'https://backend.delhimetrorail.com/api/v2/en/station_route/{}/{}/minimum-interchange/{}'

    def __init__(self,to_verify:DelhiMetro, **kwargs):
        super().__init__(to_verify)
        self.task = kwargs.get('task')

    def query_info(self):
        if self.task == 'check':
            if len(self._get_station_code())>0:
                return True
            return False

        elif self.task == 'station_code':
            return self._get_station_code()

        elif self.task == 'station_by_line':
            return self._get_station_by_line()
        elif self.task == 'station_detail':
            return self._station_brief_details()
        elif self.task == 'get_all_line':
            return self._list_all_lines()
        elif self.task == 'least_distance':
            return self._least_distance_destination()
        elif self.task == 'min_interchange':
            return self._minimum_interchange_destination()


    def _get_station_code(self):
        '''This will give station code with parameter as name, also it can that input station name is correct or not'''

        response = self.smart_request('GET',self.station_code_url.format(self.to_verify.keyword),headers=self.headers)

        if not response.ok:
            raise VerificationError("Failed to get response")
        return response.json()

    def _get_station_by_line(self):
        '''This will list all the stations available on a particular line'''

        response = self.smart_request('GET', self.station_by_line_url.format(self.to_verify.line_code), headers=self.headers)

        if not response.ok:
            raise VerificationError("Failed to get response")
        return response.json()

    def _list_all_lines(self):
        '''This will list all the lines that are present in delhi metro station'''

        response = self.smart_request('GET', self.list_all_line_url,
                                      headers=self.headers)

        if not response.ok:
            raise VerificationError("Failed to get response")
        return response.json()

    def _station_brief_details(self):
        '''This will list all the details of the station with station code'''

        response = self.smart_request("GET",self.station_brief_detail_url.format(self.to_verify.station_code),headers=self.headers)

        if not response.ok:
            raise VerificationError("Failed to get response")
        return response.json()

    def _least_distance_destination(self):
        '''This will list all the details of the station with station code'''
        response = self.smart_request("GET", self.least_distance_destination_url.format(self.to_verify.start_station_code,self.to_verify.final_station_code,datetime.now().isoformat()),
                                      headers=self.headers)

        if not response.ok:
            raise VerificationError(response.text)
        return response.json()

    def _minimum_interchange_destination(self):
        '''This will list all the details of the station with station code'''

        response = self.smart_request("GET", self.minimum_interchange_destination_url.format(self.to_verify.start_station_code,self.to_verify.final_station_code,datetime.now().isoformat()),
                                      headers=self.headers)

        if not response.ok:
            raise VerificationError(response.text)
        return response.json()

    @classmethod
    def extract_data(cls,db_ob:DelhiMetro,**kwargs):
        return cls(db_ob,**kwargs).query_info()


def template(data:dict):
    route=data.get('route')
    path='Start : {}, End : {} \nFare : {}, Total Time : {}'.format(data.get('from'),data.get('to'),data.get('fare'),data.get('total_time'))
    for i in route:
        path+='\n\n=> **{}** from: {} to: {}'.format(i.get('line'),i.get('start'),i.get('end'))
        for j in i.get('path'):
            path+='\n\t-> {}'.format(j.get('name'))

    return path

def test():
    dm = DelhiMetro()
    dm.keyword = input("Start Station: ")
    if DelhiMetroClass.extract_data(dm,task='check'):
        dm.start_station_code=DelhiMetroClass.extract_data(dm,task='station_code')[0].get('station_code')
    else:
        return "Start Station not found, try again"

    dm.keyword = input("Final Station: ")
    if DelhiMetroClass.extract_data(dm, task='check'):
        dm.final_station_code = DelhiMetroClass.extract_data(dm, task='station_code')[0].get('station_code')
    else:
        return "Final Station not found, try again"

    return template(DelhiMetroClass.extract_data(dm,task='min_interchange'))

if __name__== '__main__':
    while True:
        print(test())