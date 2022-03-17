from __future__ import annotations

from .constants import operator_dict


class Operator:
    def __init__(self, data: dict):
        self.name: str = data.get("statsDetail")
        self.matches_played: int = data.get("matchesPlayed")
        self.rounds_played: int = data.get("roundsPlayed")
        self.minutes_played: int = data.get("minutesPlayed")
        self.matches_won: int = data.get("matchesWon")
        self.matches_lost: int = data.get("matchesLost")
        self.rounds_won: int = data.get("roundsWon")
        self.rounds_lost: int = data.get("roundsLost")
        self.kills: int = data.get("kills")
        self.assists: int = data.get("assists")
        self.death: int = data.get("death")
        self.headshots: int = data.get("headshots")
        self.melee_kills: int = data.get("meleeKills")
        self.team_kills: int = data.get("teamKills")
        self.opening_kills: int = data.get("openingKills")
        self.opening_deaths: int = data.get("openingDeaths")
        self.trades: int = data.get("trades")
        self.opening_kill_trades: int = data.get("openingKillTrades")
        self.opening_death_trades: int = data.get("openingDeathTrades")
        self.revives: int = data.get("revives")
        self.distance_travelled: int = data.get("distanceTravelled")
        self.win_loss_ratio: float = data.get("winLossRatio")
        self.kill_death_ratio: float = round((data.get("killDeathRatio").get("value") * 100), 2)
        self.headshot_accuracy: float = round((data.get("headshotAccuracy").get("value") * 100), 2)
        self.kills_per_round: float = round((data.get("killsPerRound").get("value") * 100), 2)
        self.rounds_with_a_kill: float = round((data.get("roundsWithAKill").get("value") * 100), 2)
        self.rounds_with_multi_kill: float = round((data.get("roundsWithMultiKill").get("value") * 100), 2)
        self.rounds_with_opening_kill: float = round((data.get("roundsWithOpeningKill").get("value") * 100), 2)
        self.rounds_with_opening_death: float = round((data.get("roundsWithOpeningDeath").get("value") * 100), 2)
        self.rounds_with_kost: float = round((data.get("roundsWithKOST").get("value") * 100), 2)
        self.rounds_survived: float = round((data.get("roundsSurvived").get("value") * 100), 2)
        self.rounds_with_an_ace: float = round((data.get("roundsWithAnAce").get("value") * 100), 2)
        self.rounds_with_clutch: float = round((data.get("roundsWithClutch").get("value") * 100), 2)
        self.time_alive_per_match: float = data.get("timeAlivePerMatch")
        self.time_dead_per_match: float = data.get("timeDeadPerMatch")
        self.distance_per_round: float = data.get("distancePerRound")

        self.health: int = self._get_from_operators_const("health")
        self.armor: int = self._get_from_operators_const("armor")
        self.unit: int = self._get_from_operators_const("unit")
        self.country_code: int = self._get_from_operators_const("country_code")
        self.year_introduced: int = self._get_from_operators_const("year")
        self.icon_url: int = self._get_from_operators_const("icon_url")

    def _get_from_operators_const(self, what: str) -> str | int | list:
        return operator_dict.get(self.name.lower(), None).get(what, "Missing Data")

    def __repr__(self) -> str:
        return str(vars(self))


class OperatorsGameMode:
    def __init__(self, data: dict):
        self.attacker: list = [Operator(operator) for operator in data.get("teamRoles", {}).get("attacker", {})]
        self.defender: list = [Operator(operator) for operator in data.get("teamRoles", {}).get("defender", {})]

    def __repr__(self) -> str:
        return str(vars(self))


class Operators:
    def __init__(self, data: dict):
        self.all: OperatorsGameMode = OperatorsGameMode(data.get("platforms").get("PC").get("gameModes").get("all", {}))
        self.casual: OperatorsGameMode = OperatorsGameMode(data.get("platforms").get("PC").get("gameModes").get("casual", {}))
        self.ranked: OperatorsGameMode = OperatorsGameMode(data.get("platforms").get("PC").get("gameModes").get("ranked", {}))
        self.unranked: OperatorsGameMode = OperatorsGameMode(data.get("platforms").get("PC").get("gameModes").get("unranked", {}))

    def __repr__(self) -> str:
        return str(vars(self))
