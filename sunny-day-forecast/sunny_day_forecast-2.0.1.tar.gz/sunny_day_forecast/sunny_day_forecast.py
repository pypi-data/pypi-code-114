import requests, pprint

class Weather:
    """Creates a Weather object getting an apikey as input
    and either a city name of lat and lon coordinates.
    
    Package use example:
    
    # Create a weather object using a city name.
    # The api key below is not guaranteed to work.
    
    """
    
    def __init__(self, apikey, city=None, lat=None, lon=None): # 40.41, -3.70
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon
        if self.city:
            url = f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={self.apikey}&units=imperial'
            response = requests.get(url)
            self.data = response.json()
        elif self.lat and self.lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={self.apikey}&units=imperial"
            response = requests.get(url)
            self.data = response.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")

    
    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a list of dict
        """
        try:
            return self.data['list'][0:4] #Next 12 hours, 3 hours gap
        except KeyError:
            raise ValueError(self.data.get('message')) # {'cod': '404', 'message': 'city not found'}, we can also use ValueError here

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every 3 hours
            for the next 12 hours as a list of dict
        """
        simplified_li = list()
        for element in self.data['list'][0:4]:
            simplified_dict = dict()
            simplified_dict['Date_Time'] = element.get('dt_txt')
            simplified_dict['Temp_imperial']= element.get('main').get('temp')
            simplified_dict['Sky_conditions'] = element.get('weather')[0].get('description')
            icon = element.get('weather')[0].get('icon')
            simplified_dict['Icon'] = f'http://openweathermap.org/img/wn/{icon}@2x.png'
            simplified_li.append(simplified_dict)
        return simplified_li
    
    
# weather = Weather(apikey="95c0c347ba74892adb7e8d9d7ec7de2d" , city="Madrid", lat = 6.23, lon=3.60) 
# # # weather = self ...... so we can do weather.data
# # w = weather.next_12h()
# sw = weather.next_12h_simplified()
# pprint.pprint(sw)