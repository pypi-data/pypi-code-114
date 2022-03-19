"""
 - position sizing, ...


Current Price | Price Movement Estimation | Capital Needed | Capital At Risk | Leverage | Volume
--------------|---------------------------|----------------|-----------------|----------|-------
$1            | 10*e-4                    | $10*e+4        | $100            | 100      | 10*e+6
$1            | 10*e-4                    | $10*e+4        | $100            | 10       | 10*e+5
$1            | 10*e-4                    | $10*e+3        | $10             | 10       | 10*e+4

Formulas:
 - Volume * Price Movement Estimation = Capital At Risk
 - Volume * Current Price = Capital Needed  * Leverage
 - Volume = dividable by Micro/Micro/complete lot
Notes:
    - where is leverage in calculation? -> it impacts volume and implies if trade is even possible
    - what if broker does nt work with micro? -> then position size will be zero and throw exception (if position size too small)

"""
import math

import backtrader as bt
from .utils import *
from moosir_common.live_traders.core import PredictionTypeConstants

LOT_SIZE = 100000
MINI_LOT_SIZE = 10000
MICRO_LOT_SIZE = 1000

PIP_CONST = 0.0001
PIP_IN_DOLLAR = LOT_SIZE * PIP_CONST
# todo: just for now lower to small pips
# RISK_IN_PIP = (CASH_TOTAL * RISK_PORTFOLIO) / PIP_IN_DOLLAR

# RISK_PORTFOLIO = 0.01  # what % of your portfolio wanna risk
PIP_VALUE = 10


class PositionTypeConstants:
    POSITION_LONG = "LONG"
    POSITION_NONE = "NONE"
    POSITION_SHORT = "SHORT"


class BrokerMinLotSizeConstants:
    """
    - these are used for decimal points rounding for position size in lot
    - i.e. micro lot will be converted to 0.01 decimal point of lot
    - e.x. 2 micro lot = 0.02 lot

    """
    COMPLETE_LOT = 0
    MINI_LOT = 1
    MICRO_LOT = 2


class OrderPosition:
    def __init__(self, position_size_lot, trail_amount, price, leverage_used):
        # self.position_size = position_size
        self.position_size_lot = position_size_lot
        self.trail_amount = trail_amount
        self.price = price
        self.leverage_used = leverage_used


# todo: why it needs to know abt trader stuff!!
class RiskManager:
    def __init__(self,
                 broker_leverage: int = 10,
                 initial_cash: float = 10000.0,
                 risk_p_trade_perc: float = 0.01,
                 max_loss_tollerance: int = 1,
                 broker_min_lot: int = BrokerMinLotSizeConstants.MICRO_LOT,
                 average_price: float = 1,
                 average_stop_loss_pips: int = 10):

        assert 0 < risk_p_trade_perc < 1, "risk per trader percentage must be between 0 and 1"
        assert initial_cash > 1, "initial cash must be greater than 1"
        assert broker_leverage >= 1, "leverage must be greater than or equal to 1"
        assert broker_min_lot in [BrokerMinLotSizeConstants.COMPLETE_LOT,
                                  BrokerMinLotSizeConstants.MINI_LOT,
                                  BrokerMinLotSizeConstants.MICRO_LOT], "broker min lot is not valid " \
                                                                        "lot multiplier "
        self.risk_p_trade_perc = risk_p_trade_perc
        self.broker_leverage = broker_leverage
        self.broker_min_lot = broker_min_lot

        self.initial_cash = initial_cash
        used_capital_orig, _, b = self.find_perc_init_cap_can_be_used(average_price=average_price,
                                                                 average_stop_loss_pips=average_stop_loss_pips)
        used_capital_inc_loss = self.find_capital_to_use_by_max_loss(cash_used=used_capital_orig,
                                                                     max_loss_in_row=max_loss_tollerance - 1)
        self.capital_used_perc = b
        self.initial_cash_to_use = used_capital_inc_loss
        self.average_price = average_price
        self.average_stop_loss_pips = average_stop_loss_pips

    def calculate_order(self, current_price, stop_loss_price_move_pips, current_cash) -> OrderPosition:
        """

        :param current_price: current price
        :param stop_loss_price_move_pips:
            - (absolute) pips that triggers stop-loss (no matter buy or sell)
            - your estimation about price movement in opposite direction
        :param current_cash: it is the cash not portfolio value (i.e. no open open position values)
        :return:
        :exceptions:
            - volume to buy is zero
            - leverage is not enough
        """
        assert stop_loss_price_move_pips > 0, "price movement needs to be in absolute format (i.e. positive)"
        assert current_price > 0, "current price must be greater than 0"
        assert current_cash > 0, "current cash must be greater than 0"

        cash = self.initial_cash_to_use
        risk_per_trade_cash = self.risk_p_trade_perc * cash

        price_move_cash = PIP_CONST * stop_loss_price_move_pips
        position_size = int(risk_per_trade_cash / price_move_cash)

        # to be max on micro measure, cant do less than micro
        position_size_lot = round_decimals_down(position_size / LOT_SIZE,
                                                self.broker_min_lot)

        if position_size_lot <= 0:
            raise Exception(f"position size is {position_size_lot}. (stop loss pip: {stop_loss_price_move_pips}, "
                            f"broker min lot: {self.broker_min_lot}, init cash: {self.initial_cash})")

        cash_for_position_size = current_price * position_size
        leverage_needed = cash_for_position_size / current_cash
        # todo: how about current cash? might be lower than
        if leverage_needed > self.broker_leverage:
            raise Exception(
                f"leverage needed ({leverage_needed}) is higher than current leverage {self.broker_leverage}")

        trail_amount = 1 * stop_loss_price_move_pips * PIP_CONST
        result = OrderPosition(position_size_lot=position_size_lot,
                               trail_amount=trail_amount,
                               price=current_price,
                               leverage_used=leverage_needed)
        return result

    def calculate_trade_type(self, existing_position, signal: PredictionTypeConstants) -> PositionTypeConstants:
        """
        - does not trade if existing position is open!!!! if allowed, it can change position size, ... in other funcs
        """
        if existing_position:
            return PositionTypeConstants.POSITION_NONE

        if signal == PredictionTypeConstants.FLAT:
            return PositionTypeConstants.POSITION_NONE

        if signal == PredictionTypeConstants.HIGH or signal == PredictionTypeConstants.VERY_HIGH:
            return PositionTypeConstants.POSITION_LONG

        if signal == PredictionTypeConstants.LOW or signal == PredictionTypeConstants.VERY_LOW:
            return PositionTypeConstants.POSITION_SHORT

    def make_orders_long(self, strategy, position_size, price, trail_amount, is_bracket_order=True):
        if is_bracket_order:
            take_profit_price = price + 2 * trail_amount
            stop_loss_price = price - trail_amount

            strategy.buy_bracket(limitprice=take_profit_price,
                                 stopprice=stop_loss_price,
                                 size=position_size,
                                 exectype=bt.Order.Market)
        else:
            # todo: might cause prob when next bar is too big up or down!!!
            strategy.buy(size=position_size, exectype=bt.Order.Limit, price=price)
            #
            # # trailing
            strategy.sell(
                size=position_size
                , exectype=bt.Order.StopTrailLimit
                , trailamount=trail_amount
                , trailpercent=0.0
            )

    def make_orders_short(self, strategy, position_size, price, trail_amount, is_bracket_order=True):

        if is_bracket_order:
            take_profit_price = price - 2 * trail_amount
            stop_loss_price = price + trail_amount

            strategy.sell_bracket(limitprice=take_profit_price,
                                  stopprice=stop_loss_price,
                                  size=position_size,
                                  exectype=bt.Order.Market)
        else:
            # todo: might cause prob when next bar is too big up or down!!!
            strategy.sell(size=position_size, exectype=bt.Order.Limit, price=price)
            #
            # # trailing
            strategy.buy(
                size=position_size
                , exectype=bt.Order.StopTrailLimit
                , trailamount=trail_amount
                , trailpercent=0.0
            )

    # todo: dont know why min lot size that the broker can work with, has no impact here?!!!
    def find_perc_init_cap_can_be_used(self, average_price, average_stop_loss_pips):
        """
        Note
            - if wanna use L=1 (or not enough leverage given your capital)
            - you need to provide cap by yourself
            - i.e. part of the original capital needs to be saved as leverage!!!
            - i.e. you have money with broker, but only part of it is in trade/models/...
        Calculation:
            Cn: Capital needed
            C: Capital used
            Co: original capital (not all of this can be used, needs to help with leverage shortage)
            b: percentage of original capital that can be used (to find)
            Pm: price movement
            P: current price
            V: volume
            a: perc at risk (0<>1)
            L: leverage

            V = (a*C)/Pm and V = (Cn*L)/P
            => V = (a*b*Co)/Pm and V = (Cn*L)/P
            => Co = Cn # because this is the worst case if no leverage
            => b = (Pm * L)/ (P * a)
        """

        b = (average_stop_loss_pips * PIP_CONST * self.broker_leverage) / (average_price * self.risk_p_trade_perc)
        if b > 1:
            # i.e. more than enough leverage available to use
            b = 1

        if b <= 0:
            raise Exception(f"Wrong calculation of percentage of capital can be used: b: {b})")

        used_capital = b * self.initial_cash
        reserved_cap = (1 - b) * self.initial_cash

        return used_capital, reserved_cap, b

    def find_max_consecutive_loss_number(self, average_price, average_stop_loss_pips):

        cash_needed_avg = (average_price * self.risk_p_trade_perc) / (
                    self.broker_leverage * average_stop_loss_pips * PIP_CONST)

        loss_n = (1 - cash_needed_avg) / self.risk_p_trade_perc
        loss_n = int(loss_n) + 1
        if loss_n < 0:
            loss_n = 1

        return loss_n

    # todo: check out the test, it underutilize the capital based on the loss
    # check out the test when loss in the row is higher than max_loss defined!!!
    def find_capital_to_use_by_max_loss(self, cash_used,  max_loss_in_row):
        cash = cash_used * (1 - max_loss_in_row * self.risk_p_trade_perc)
        return cash
