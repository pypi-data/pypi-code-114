from ..utils import _AutomaticClient, Number
from .response import *


class CurrentWeatherAPIException(Exception):
    pass


class CurrentWeather(_AutomaticClient):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    async def get(self, coords: tuple[Number, Number]) -> CurrentWeatherStatus:
        params = {"appid": self.appid, "lat": coords[0], "lon": coords[1]}
        async with self.client.get(self.BASE_URL, params=params) as resp:
            resp = await resp.json()
            if "cod" in resp and "message" in resp:
                raise CurrentWeatherAPIException(resp["cod"], resp["message"])
            if "rain" in resp:
                for key in resp["rain"].keys():
                    resp["rain"][f"_{key}"] = resp["rain"][key]
                    del resp["rain"][key]
            return CurrentWeatherStatus(**resp)
