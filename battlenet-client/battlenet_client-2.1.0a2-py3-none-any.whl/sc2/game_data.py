from requests import Response

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .client import SC2Client


class LeagueData:
    def __init__(self, client: "SC2Client") -> None:
        self.__client = client

    def league_data(
        self,
        season_id: str,
        queue_id: str,
        team_type: str,
        league_id: str,
        locale: Optional[str] = None,
    ) -> Response:
        """Returns data for the specified season, queue, team, and league.

        queueId: the standard available queueIds are: 1=WoL 1v1, 2=WoL 2v2, 3=WoL 3v3, 4=WoL 4v4, 101=HotS 1v1,
            102=HotS 2v2, 103=HotS 3v3, 104=HotS 4v4, 201=LotV 1v1, 202=LotV 2v2, 203=LotV 3v3, 204=LotV 4v4,
            206=LotV Archon. Note that other available queues may not be listed here.

        teamType: there are two available teamTypes: 0=arranged, 1=random.

        leagueId: available leagueIds are: 0=Bronze, 1=Silver, 2=Gold, 3=Platinum, 4=Diamond, 5=Master, 6=Grandmaster.

        Args:
            locale (str): The locale to reflect in localized data.
            season_id (str): The season ID of the data to retrieve.
            queue_id (str): The queue ID of the data to retrieve.
            team_type (str): The team type of the data to retrieve.
            league_id (str): The league ID of the data to retrieve.

        Returns:
            dict: dict containing league data for specified season, queue, team, and league.
        """

        return self.__client.game_data(
            locale, "league", season_id, queue_id, team_type, league_id
        )
