from . import efficiencylike
from typing import Tuple
import datetime



class Efficiency(efficiencylike.Efficiencylike):
    """Class for managing team efficiency properties. Should usually be used to compose a 
    team class.
    """
    possessions : float
    team : efficiencylike.Teamalog
    league : efficiencylike.Divisionalog
    recency : float
    mu : float = .01

    @classmethod
    def eff(cls, pts : float, possesions : float)->float:
        """Computes efficiency, pts/possesions.

        Args:
            pts (float): the points scored by a team.
            possesions (float): the number of possesions.

        Returns:
            float: the efficiency.
        """
        return pts/possesions

    @classmethod
    def adjem(cls, oeff : float, navg: float)->float:
        """Computes adjusted efficiency margin, efficiency - avg.

        Args:
            oeff (float): the offensive efficiency of the team.
            navgo (float): the league average offensive efficiency.

        Returns:
            float: the adjusted efficiency margin.
        """
        return oeff - navg

    @classmethod
    def kadjeff(cls, eff : float, navg : float, op_adj : float)->float:
        """Computes the adjusted efficiency.

        KenPom:
        I compute an adjusted offensive efficiency for each game 
        by multiplying the team’s raw offensive efficiency by the 
        national average efficiency and dividing by the opponent’s 
        adjusted defensive efficiency.

        We can use the same formula for adjusted offensive and defensive efficiencies.

        Args:
            eff (float): the efficiency of the team.
            navg (float): the nav.
            op_adj (float): the adjusted efficiency for the opponent for the opposite function (defense | offense).

        Returns:
            float: the adjusted offensive efficiency.
        """
        return (eff * navg)/op_adj


    def __init__(self, team : efficiencylike.Teamalog, league : efficiencylike.Divisionalog, controller : efficiencylike.Controlleralog):
        """Takes pts and possesions to initialize recency.

        Args:
            pts (float): A team's pts.
            possesions (float): A team's possessions.
            recency (float): The recency to use for a 
        """
        self.team = team
        self.league = league
        self.controller = controller
    
    def get(self, date : datetime.datetime)->None:
        """Gets self using the controller.
        """
        self.controller.get(self, date)

    def get_oeff(self)->float:
        """Gets the team's offensive efficiency.

        Returns:
            float: the team's offensive efficiency.
        """
        return Efficiency.eff(self.team.pts, self.possessions)

    def get_deff(self)->float:
        """Gets the team's deffensive efficiency.

        Returns:
            float: the team's defensive efficiency.
        """
        return Efficiency.eff(self.team.pts_against, self.possessions)


    def next_adjusted_koeff(self, opponent : efficiencylike.Efficiencylike)->float:
        """Gets the next adjusted offensive efficiency value.

        Args:
            opponent (EfficiencyTeamlike): is the opponent played in the game used to update the value.

        Returns:
            float: the next adjusted offensive efficiency value.
        """
        return Efficiency.kadjeff(self.get_oeff(), self.league.avg_oeff, opponent.radjdeff)

    def next_adjusted_kdeff(self, opponent : efficiencylike.Efficiencylike)->float:
        """Gets the next adjusted defensive efficiency value.

        Args:
            opponent (EfficiencyTeamlike): is the opponent played in the game used to update the value.

        Returns:
            float: the next adjusted deffensive efficiency value.
        """
        return Efficiency.kadjeff(self.team.pts_against, self.league.avg_deff, opponent.radjoeff)

    @classmethod
    def badjeff(cls, pppg : float, oe : float, de : float, navg : float)->Tuple[float, float]:
        """Computes the recency adjusted effiency

        Args:
            pppg (float): the points scored in the game by the offensive tema
            oe (float): the offensive efficiency of the offensive team before the game.
            de (float): the defensive efficiency of the defensive team before the game.
            ppp (float): the national average points per game.
            recency (float, opptional): the recency wait applied to the adjusted efficiency calculation. Defaults to .2.

        Returns:
            Tuple[float, float]: _description_
        """
        oe = pppg/(de/navg)
        de = pppg/(oe/navg)
        return (oe, de)

    @classmethod
    def radjeff(cls, pppg : float, oe : float, de : float, navg : float, recency : float =.2)->Tuple[float, float]:
        """Computes the recency adjusted effiency

        Args:
            pppg (float): the points scored in the game by the offensive tema
            oe (float): the offensive efficiency of the offensive team before the game.
            de (float): the defensive efficiency of the defensive team before the game.
            ppp (float): the national average points per game.
            recency (float, opptional): the recency wait applied to the adjusted efficiency calculation. Defaults to .2.

        Returns:
            Tuple[float, float]: _description_
        """
        loe = oe
        moe = oe
        lde = de
        mde = de
        while moe > Efficiency.mu or mde > Efficiency.mu:
            loe = oe
            lde = de
            oe = (oe * (1 - recency) + (pppg/(de/navg)) * recency)
            de = (de * (1 - recency) + (pppg/(oe/navg)) * recency)
            moe = loe - oe
            mde = lde - de
        return (oe, de)

    def biupdate_kadjeff(self, opponent : efficiencylike.Efficiencylike)->None:
        """Updates kadjeff for team and its opponent.
        Args:
            opponent (float): 
            points_for (float): the points scored by the home team in the contest (self.team).
            points_against (float): the points scored by the away team in the contest
        """
        next_kadjoeff = self.next_adjusted_koeff(opponent)
        next_kadjdeff = self.next_adjusted_kdeff(opponent)

        o_next_kadjoeff = self.next_adjusted_koeff(self)
        o_next_kadjdeff = self.next_adjusted_kdeff(self)

        self.kadjoeff = next_kadjoeff
        self.kadjdeff = next_kadjdeff

        opponent.kadjoeff = o_next_kadjoeff
        opponent.kadjdeff = o_next_kadjdeff

    def biupdate_badjeff(self, opponent : efficiencylike.Efficiencylike, pppf : float, pppa : float)->None:
        """Updates the badjeff value of the 

        Args:
            opponent (EfficiencyTeamlike): _description_
            pppf (float): _description_
            pppa (float): _description_
        """

        next_badjoeff, o_next_badjdeff = \
            Efficiency.badjeff(pppf, self.badjoeff, opponent.badjdeff, self.league.ppp)
        next_badjdeff, o_next_badjoeff = \
            Efficiency.badjeff(pppa, opponent.badjoeff, self.badjdeff, self.league.ppp)
        
        self.badjoeff = next_badjoeff
        self.badjdeff = next_badjdeff

        opponent.badjoeff = o_next_badjoeff
        opponent.badjdeff = o_next_badjdeff

    def biupdate_radjeff(self, opponent : efficiencylike.Efficiencylike, pppf : float, pppa : float, recency : float = .2)->None:
        """_summary_

        Args:
            opponent (EfficiencyTeamlike): _description_
            pppf (float): _description_
            pppa (float): _description_
        """

        next_radjoeff, o_next_radjdeff = \
            Efficiency.radjeff(pppf, self.badjoeff, opponent.badjdeff, self.league.ppp, recency)
        next_radjdeff, o_next_radjoeff = \
            Efficiency.radjeff(pppa, opponent.badjoeff, self.badjdeff, self.league.ppp, recency)
        
        self.radjoeff = next_radjoeff
        self.radjdeff = next_radjdeff

        opponent.radjoeff = o_next_radjoeff
        opponent.radjdeff = o_next_radjdeff

    def serialize(self, date : datetime.datetime)->None:
        """Serializes just this effiency model.
        """
        self.controller.serialize(self, date)

    def biupdate_and_serialize(self, opponent : efficiencylike.Efficiencylike, pppf : float, pppa : float, date : datetime.datetime, recency : float = .2)->None:
        """Performs a biupdate then serializes this efficiency and the opponent's.

        Args:
            opponent (EfficiencyTeamlike): 
            pppf (float): _description_
            pppa (float): _description_
            recency (float, optional): _description_. Defaults to .2.
        """
        self.biupdate_kadjeff(opponent)
        self.biupdate_badjeff(opponent, pppf, pppa)
        self.biupdate_radjeff(opponent, pppf, pppa, recency)
        self.serialize(date)

    