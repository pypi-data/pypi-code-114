# from math import sqrt
from hybridvut.tools.units import convert_unit
from hybridvut.tools.RAS import RAS_U
from hybridvut.tools.iomath import calc_Z_y, calc_F_mult, calc_footprint
from hybridvut.tools.utils import (
    aggregate,
    monetize,
    harmonize_inds_coms_in_regions,
)
from hybridvut.hybridizations import hybridize

# import numpy as np
# import pandas as pd
# import numpy.matlib
import logging

# import numpy.linalg

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class VUT(object):
    """Make and Use table object including other matrices.

    Attributes
    __________
    V: pd.DataFrame
        Make Table (Industry x Product)
    U: pd.DataFrame
        Use Table (Product x Industry)
    F: pd.DataFrame
        Environmental extension (Intervention x Industry)
    F_Y: pd.DataFrame
        Environmental extension for final demand (Intervention x Demand Category)
    Q: pd.DataFrame
        Characterization factors of the interventions (Impact x Intervention)
    """

    def __init__(self, V=None, U=None, F=None, Q=None, F_Y=None):
        self.V = V
        self.U = U
        self.F = F
        self.Q = Q
        self.F_Y = F_Y

    # utils functions
    def aggregate(self, mapping_reg=None, mapping_com=None, mapping_ind=None):
        """Aggregate regions of the specified system and according to regional mapping.

        Parameters
        ----------
        mapping_reg : dict
            specifies name of new regions its aggregated subregions.
            {'new_reg0': ['reg0'],
            'new_reg1': ['reg1', 'reg2'],}
        mapping_com : dict
            specifies name of new commodities its aggregated commodities.
            {'new_com0': ['com0'],
            'new_com1': ['com1', 'com2'],}
        mapping_ind : dict
            specifies name of new industries its aggregated industries.
            {'new_ind0': ['ind0'],
            'new_ind1': ['ind1', 'ind2'],}
        Returns
        -------
        self.V : pd.DataFrame
            aggregated Make matrix
        self.U : pd.DataFrame
            aggregated Use matrix
        self.F : pd.DataFrame
            aggregated Extension matrix
        self.F_Y : pd.DataFrame
            aggregated Extension matrix for Demand categories

        TODO: include region checks for mapping (number); allow industry/commodity aggregation
        """
        return aggregate(self, mapping_reg, mapping_com, mapping_ind)

    def monetize(self, price_vector):
        """Monetize the Make and Use tables of a system.

        Currently only for dataframes without unit index.
        Parameters
        ----------
            price_vector : pd.DataFrame
                Price vector of the commodities (same MultiIndex as in V and U)
        Returns
        _______
            self.V : pd.DataFrame
                Make matrix in monetary units.
            self.U : pd.DataFrame
                Use matrix in monetary units.
        """
        return monetize(self, price_vector)

    def harmonize_inds_coms_in_regions(self):
        """Harmonize the number of commodities and industries among regions.

        Returns
        -------
            self.V : pd.DataFrame
                Make matrix with same commodities/ industries among regions.
            self.U : pd.DataFrame
                Use matrix with same commodities/ industries among regions.
            self.F : pd.DataFrame
                Factor intervention matrix with same industries among regions.
        """
        return harmonize_inds_coms_in_regions(self)

    # iomath functions
    def RAS_U(self, q, x, y, v, n, include_e_v=False):
        """Simple iterative fitting procedure for matrix U.

        Fits the matrix U so that its sum over columns equals q-y,
        and its sum over rows equals x-v.
        IN INPUT-OUTPUT ECONOMICS THIS IS CALLED RAS.

        Parameters
        ----------
        q: pd.Series
            Total output of commodities
        x: pd.Series
            Total output of industries
        y: pd.Series
            Total demand of commodities
        v: pd.Series
            Total value added of industries
        n: int
            Maximum number of iterations
        Returns
        -------
        pd.DataFrame
            Rased matrix U
        """
        return RAS_U(self, q, x, y, v, n, include_e_v)

    def calc_Z_y(self, tech_assumption="industry", requirements="com-by-com"):
        """This function calculates the transaction matrix Z and final demand y.

        This is done only based on the hybridized Make and Use Tables.
        TODO: Allow Commodity technology assumption!
        Parameters
        ----------
            tech_assumption : str
                Specifies the technology assumption to create the Z matrix.
                'industry' for Industry technology assumption
                'commodity' for commodity technology asssumption (only possible if number
                of industries is  equal to number of commodities)
            requirements : str
                Specifies the dimension of the transaction matrix Z.
                'com-by-com' for commodity-by-commodity requirements
                'ind-by-ind' for industry-by-industry requirements
        Returns
        -------
            Z : pd.DataFrame
                Transaction Matrix
            y : pd.DataFrame
                Final demand vector
        """
        return calc_Z_y(self, tech_assumption, requirements)

    def calc_F_mult(
        self,
        tech_assumption="industry",
        raw_factors="per-ind",
        multipliers="per-com",
        impacts=False,
        contribution=None,
    ):
        """This function calculates the Factor multipliers for the hybridized system.

        The equations are used from Lenzen and Rueda-Cantuche (2012):
        'A note on the use of supply-use tables in impact analyses'
        TODO: Implement 'commodity' and 'mixed' tech_assumptions for Factor matrix.
        Parameters
        ----------
        tech_assumption : str
            Specifies the technology assumption for calculating th e multipliers.
            'industry' for industry technology assumption
            'commodity' for commodity technology assumption
        raw_factors : str
            Specifies explicitely the factors of matrix F.
            'per-ind' for factors in F are defined per unit of industry output.
            'per-com' for factors in F are defined per unit of commodity output.
            Usually the Factor matrix is defined as factor per industry output.
        multipliers : str
            Specifies the nature of the calculated multipliers.
            'per-com' for multipliers per commodity
            'per-ind' for multipliers per industry
        impacts : bool
            If True, multiplieres for impact categories are determined, by using Q.
        contribution : dict with lists of str
            If not not None, contribution analysis is done chosen process (commodity).
            Keys need to be "category" and "ind_or_com":
            {"category": ['filter_intervention_or_impact'], "ind_or_com": ['filter_commodity_or_process']}
            Filtering is based on str.contains()
            To chose all, use {"category": [''], "ind_or_com": ['$']}, but might be time consuming.
        Returns
        -------
        F_mult : pd.DataFrame
            Multiplier Matrix
        """
        return calc_F_mult(
            self, tech_assumption, raw_factors, multipliers, impacts, contribution
        )

    def calc_footprint(
        self,
        responsibility="consumption",
        raw_factors="per-ind",
        multipliers="per-ind",
        sum_over_sectors=True,
    ):
        """Calculates footprints of countries depending on responsibility perspective.

        Equations based on Marques et al. (2012) Income-based environmental responsibility.
        TODO: Implement 'per-com' factor matrix
        Parameters
        ----------
        responsibility : str
            Specifies the responsibility perspective to be taken.
            'consumption' for consumption-based responsibility
            'income' for income-based responsibility
            'production' for production-based responsibility
        raw_factors : str
             Stressor relation of factor matrix F.
            'per-ind'
        multipliers : str
             Specifies the technology construct of the A matrix (ind-by-ind or com-by-com)
            'per-ind' or 'per-com'
             TODO: 'per-com' currently only for consupmtion-based perspective.
        sum_over_sectors : bool
            If True, the footprint is aggregated to the regional level.
            Otherwise, sector contribution is visible.
        Returns
        -------
        footprint : pd.DataFrame
            Interventions per country matrix
        """
        return calc_footprint(
            self, responsibility, raw_factors, multipliers, sum_over_sectors
        )

    # units functions
    def convert_unit(self, current, to, matrix, factor=None):
        """This function converts the current unit to another.

        Parameters
        ----------
        current : str
            Current unit to be converted, e.g. 'kg'
        to : str
            Target unit, e.g. 't'
        matrix : str
            'V' for Make matrix of total system
            'U' for Use matrix of total system
            'F' for Factor matrix of total system
            'Q' for Characterization matrix of total system
        factor = float
            Own factor for unit conversion
            Take care that values of Q are impact per intervention!
            E.g, from impact '(per) M.EUR' of intervention to '(per) EUR',
            requires factor = 1/1000000.
        Returns
        -------
        df : pd.DataFrame
            Matrix with converted units
        """
        return convert_unit(self, current, to, matrix, factor)


class HybridTables(object):
    """Foreground and background Make and Use Tables.

    The class provides functions for hybridization of a foreground system (Messageix)
    with a background system (e.g. Exiobase) represented as Make and Use Tables.
    Furthermore diagnostic features are provided for those systems.

    Attributes
    ----------
    foreground: hybridvut.VUT
        Foreground system
    background: hybridvut.VUT
        Background system
    total: hybridvut.VUT
        Total hybridized system
    """

    def __init__(
        self,
        foreground=None,
        background=None,
        #        total=None,
    ):
        self.foreground = foreground
        self.background = background
        self.total = VUT()

    # main function
    def hybridize(
        self,
        H=None,
        H1=None,
        HF=None,
        message_exiobase=False,
        check_negative_U=False,
        delete_trade_in_reg=None,
        RAS=False,
    ):
        """Hybridize the foreground and background sytems.

        V and U are determined based on V_back, U_back, V_for and U_for.
        The hybridization procedure assumes that the background system
        fully represents the world economy.
        TODO: Replace hard-coding when setting emissions of Exiobase to zero.

        Parameters
        ----------
        H : pd.DataFrame
            Concordance matrix (industries_back x industries_for)
            Assigns a process of the foreground system to the industry
            of the background system. Entry 1, if concordance, else 0.
        H1 : pd.DataFrame
            Concordance matrix (commodities_for x commodities_back)
            Assigns a commodity of the foreground system to the commodity
            of the background system. Entry 1, if concordance, else 0.
        HF : pd.DataFrame
            Concordance matrix for extensions (intervention_back x intervention_for)
            Assigns an intervantio of the background system to the intervention of
            the foreground system. Entry 1, if concordance, else 0.
        message_exiobase : bool
            If True, it is assumed that all associated commodities (H1) of the background
            system are covered by the foreground system; and hence removed from the background
            (this is also assumed for the traded commodities).
            Furthermore, to determine the F matrix all GHG emissions of the background
            Exiobase system in regard to the energy system are set to 0.
            This is necessary since the GHG accounting in Message is done on the
            extraction site.
            If False, the hybridization is fully done based on monetary ratios for all commodities;
            and the hybridized F matrix is determined by using H.
        check_negative_U : bool
            If True, a check on the hybridized U matrix is carried out for negative
            elements. If there are negative elements, these are set to zero; and
            a RAS procedure based on the hybridized V matrix is done.
        delete_trade_in_reg : dict
            Mapping to delete traded commodities between countries.
            Is required for example when using massage-exiobase models.
            e.g. {'from_reg_1': ['to_reg_1', 'to_reg_2'], 'from_reg_2': ...}
            RAS is done afterwards.
        RAS : bool
            If True, the use table is rased during the hybridization process.
            Only for message_exiobase relevant.
        T : pd.DataFrame (hidden)
            Weighting factor matrix (commodities_back x industries_for)
            Includes the share of used background commodity in the new
            considerred foreground process in comparison to foreground ref
            industry. (simple assumption here is:
            based on x_i_for / (x_i_for + x_i_back)
        T1 : pd.DataFrame (hidden)
            Weighting factor matrix (commodities_for x industries_back)
            Includes the share of used foreground commodity in the old
            background process in comparison to the background ref commodity.
            (simple assumption here is: based on x_c_for / (x_c_for + x_c_back)

        Returns
        -------
        self.total.V : pd.DataFrame
            Make matrix V of total hybridized system
        self.total.U : pd.DataFrame
            Use matrix U of total hybridized system
        self.total.F : pd.DataFrame
            Extension matrix F of total hybridized system
        self.total.Q : pd.DataFrame
            Characterization matrix Q of total hybridized system
        """
        return hybridize(
            self,
            H,
            H1,
            HF,
            message_exiobase,
            check_negative_U,
            delete_trade_in_reg,
            RAS,
        )
