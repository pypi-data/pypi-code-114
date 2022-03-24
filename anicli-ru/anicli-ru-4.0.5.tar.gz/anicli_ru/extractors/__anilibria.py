from anicli_ru.base import *
import re


class Anime(BaseAnimeHTTP):
    """API method write in snake_case style.
    For details see docs on https://github.com/anilibria/docs/blob/master/api_v2.md"""
    BASE_URL = "https://api.anilibria.tv/v2/"

    def api_request(self, *, api_method: str, request_method: str = "POST", **kwargs) -> dict:
        """
        :param str api_method: Anilibria api method
        :param str request_method: requests send method type. Default "POST"
        :param kwargs: any requests.Session kwargs
        :return: json response
        """
        resp = self.request(request_method, self.BASE_URL + api_method, **kwargs)
        return resp.json()

    @staticmethod
    def _kwargs_pop_data(kwargs, **params) -> dict:
        data = kwargs.pop("data") if kwargs.get("data") else {}
        data.update(params)
        return data

    def search_titles(self, *, search: str, limit: int = -1, **kwargs) -> dict:
        """searchTitles method

        :param search:
        :param limit:
        :param kwargs:
        :return:
        """
        data = self._kwargs_pop_data(kwargs, search=search, limit=limit)
        return self.api_request(api_method="searchTitles", data=data, **kwargs)

    def get_updates(self, *, limit: int = -1, **kwargs) -> dict:
        """getUpdates method

        :param limit:
        :param kwargs:
        :return:
        """
        data = self._kwargs_pop_data(kwargs, limit=limit)
        return self.api_request(api_method="getUpdates", data=data, **kwargs)

    def search(self, q: str) -> ResultList[BaseAnimeResult]:
        r = self.search_titles(search=q)
        return
        return AnimeResult.parse(r)

    def ongoing(self, *args, **kwargs) -> ResultList[BaseOngoing]:
        r = self.get_updates()
        return
        return Ongoing.parse(r)

    def episodes(self, *args, **kwargs) -> ResultList[BaseEpisode]:
        raise NotImplementedError("...")

    def players(self, *args, **kwargs) -> ResultList[BasePlayer]:
        raise NotImplementedError("...")


class Parser(BaseParserObject):

    id: int
    code: str
    names: dict
    type: dict
    genres: list
    season: dict
    description: str
    blocked: dict
    player: dict


    """example response
    
    {
    "id": 8500,
    "code": "nanatsu-no-taizai-kamigami-no-gekirin",
    "names": {
        "ru": "Семь смертных грехов: Гнев богов ТВ-3",
        "en": "Nanatsu no Taizai: Kamigami no Gekirin TV-3",
        "alternative": null
    },
    "updated": 1585249972,
    "last_change": 1642539074,
    "type": {
        "full_string": "TV (24 эп.), 25 мин.",
        "code": 1,
        "string": "TV",
        "series": 24,
        "length": "25 мин"
    },
    "genres": [
        "Магия",
        "Приключения",
        "Сверхъестественное",
        "Сёнен",
        "Экшен"
    ],
    "season": {
        "string": "осень",
        "code": 4,
        "year": 2019,
        "week_day": 5
    },
    "description": "Продолжение аниме «Семь смертных грехов» расскажет нам о том, как Грехи продолжают противостояние с Десятью Заповедями. Мелиодасу и Элизабет предстоит вновь испытать свою судьбу в новых приключениях и сражениях, а также открыть секрет этого мира.",
    "in_favorites": 10134,
    "blocked": {
        "blocked": false,
        "bakanim": false
    },
    "player": {
        "alternative_player": "//kodik.info/serial/19248/803944eb832adacd4d4bec7d4221f941/720p?translations=false",
        "host": "de6.libria.fun",
        "series": {
            "first": 1,
            "last": 24,
            "string": "1-24"
        },
        "playlist": {
            "1": {
                "serie": 1,
                "created_timestamp": 1570809272,
                "hls": {
                    "fhd": "/videos/media/ts/8500/1/1080/6a6fc29f9428b2dcc8ce74ad21bb1cca.m3u8",
                    "hd": "/videos/media/ts/8500/1/720/8e5d9ba9e79d80ca6b6db6e6e375b4bb.m3u8",
                    "sd": "/videos/media/ts/8500/1/480/93048587fb765c9f2077ca7adad9457e.m3u8"
                }
            },
            ...
        }
    },
    "torrents": {
        "series": {
            "first": 1,
            "last": 24,
            "string": "1-24"
        },
        "list": [
            {
                "torrent_id": 10725,
                "series": {
                    "first": 1,
                    "last": 24,
                    "string": "1-24"
                },
                "quality": {
                    "string": "WEBRip 1080p",
                    "type": "WEBRip",
                    "resolution": 1080,
                    "encoder": "h264",
                    "lq_audio": false
                },
                "leechers": 0,
                "seeders": 0,
                "downloads": 10070,
                "total_size": 35521275317,
                "url": "/public/torrent/download.php?id=10725",
                "uploaded_timestamp": 1590483840,
                "metadata": null,
                "raw_base64_file": null
            },
    """

    @classmethod
    def parse(cls, response: dict) -> ResultList:
        pass


class AnimeResult(BaseAnimeResult):
    ANIME_HTTP = Anime()
    REGEX = {"url": re.compile("foo (.*?)"),
             "title": re.compile("bar (.*?)")}

    url: str
    title: str

    def __str__(self):
        return f"{self.title}"


class Ongoing(BaseOngoing):
    ANIME_HTTP = Anime()
    REGEX = {}

    def __str__(self):
        return


class Player(BasePlayer):
    ANIME_HTTP = Anime()
    REGEX = {"url": re.compile("url (.*?)")}
    url: str

    def __str__(self):
        return


class Episode(BaseEpisode):
    ANIME_HTTP = Anime()
    REGEX = {}

    def __str__(self):
        return ""
