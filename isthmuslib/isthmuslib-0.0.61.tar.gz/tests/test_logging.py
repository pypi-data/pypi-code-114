import pytest
import pathlib

from src.isthmuslib.logging import auto_extract_from_text, auto_extract_from_file


def test_foo():
    s: str = """It was the best of times, [@@@] it was the worst [<<x=5>>]of times, it was the age of"
    s += "wisdom, [<<y='foo'>>] it was the age of foolishness, [@@@] it was the epoch of belief, it was the epoch of "
    s += "incredulity, [<<y='bar'>>] it was the season of Light, it was the season of Darkness, """

    print(auto_extract_from_text(s, parallelize=False))


def test_extraction():
    path_to_test_file = pathlib.Path.cwd() / '..' / 'data' / 'local_only' / 'reference_logs_1.txt'
    s = auto_extract_from_file(path_to_test_file, parallelize=False)
    print(s)

@pytest.mark.skip(reason='lengthy')
def test_foo_2():
    s: str = """
    @@ AT: 2022-03-13T16:20:09.308774+0000 | LEVEL: INFO | IN: __main__.<module>
    
    primary bot main logging to: /home/ubuntu/logs/local_only/bot_logs.txt

    
    @@ AT: 2022-03-13T16:20:10.907204+0000 | LEVEL: INFO | IN: config.import_me_dynamic_config.<module>
    
    Auto switcher: using GL instance ID: research_1_c
    
    
    @@ AT: 2022-03-13T16:20:10.907491+0000 | LEVEL: INFO | IN: config.import_me_dynamic_config.<module>
    
    Auto switcher: using parameters preset tighter on research_1_c
    
    
    @@ AT: 2022-03-13T16:20:10.907627+0000 | LEVEL: INFO | IN: config.import_me_dynamic_config.<module>
    
    Auto switcher: using credentials preset perpetuals_control_1_c on research_1_c
    
    
    @@ AT: 2022-03-13T16:20:11.763187+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    Starting up primary bot at address [<<address=0x57E4D5Bda719497C7389496724cd65496126f17D>>] at [<<boot_time=1647188411.7629402>>]
    
    (Bot and logic version [<<commit='2f1ef54'>>])
    
    [<<strategy_parameters=StrategyParameters(buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2)>>]
    
    [<<dydx_parameters=DydxParameters(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>)>>]
    
    
    @@ AT: 2022-03-13T16:20:12.684280+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.35979858799998965>>]
    [<<get_state_time_sec=0.5597386240000333>>]
    [<<process_time_sec=0.0002803610000228218>>]
    
    
    @@ AT: 2022-03-13T16:20:12.684573+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188412.6839797>>]
    [<<spot=2571.9>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:12.684782+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:12.684940+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:12.685299+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    [<<follow_down_at=None>>]
    [<<follow_up_at=None>>]
    [<<infer_anchors_on_init=True>>]
    
    
    @@ AT: 2022-03-13T16:20:12.685442+0000 | LEVEL: INFO | IN: __main__.<module>
    
    No orders to be placed at this time 
    [<<dydx_order=None>>]
    
    
    @@ AT: 2022-03-13T16:20:12.685568+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    [<<heartbeat_remaining_sec=4.078871470000081>>] (so now bot will sleep for remainder of the heartbeat)
    
    
    @@ AT: 2022-03-13T16:20:17.590790+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.2639374330000237>>]
    [<<get_state_time_sec=0.5579511279998997>>]
    [<<process_time_sec=8.208000008380623e-05>>]
    
    
    @@ AT: 2022-03-13T16:20:17.591074+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188417.590681>>]
    [<<spot=2572.55>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:17.591269+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:17.591416+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:17.591722+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    [<<follow_down_at=None>>]
    [<<follow_up_at=None>>]
    [<<infer_anchors_on_init=True>>]
    
    
    @@ AT: 2022-03-13T16:20:17.591859+0000 | LEVEL: INFO | IN: __main__.<module>
    
    No orders to be placed at this time 
    [<<dydx_order=None>>]
    
    
    @@ AT: 2022-03-13T16:20:17.591982+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    [<<heartbeat_remaining_sec=4.176805535999961>>] (so now bot will sleep for remainder of the heartbeat)
    
    
    @@ AT: 2022-03-13T16:20:23.098812+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.7537844380000251>>]
    [<<get_state_time_sec=0.5716816950000521>>]
    [<<process_time_sec=8.412900001530943e-05>>]
    
    
    @@ AT: 2022-03-13T16:20:23.099099+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188423.0986984>>]
    [<<spot=2572.1499999999996>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:23.099304+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:23.099481+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:23.099800+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    [<<follow_down_at=None>>]
    [<<follow_up_at=None>>]
    [<<infer_anchors_on_init=True>>]
    
    
    @@ AT: 2022-03-13T16:20:23.099950+0000 | LEVEL: INFO | IN: __main__.<module>
    
    No orders to be placed at this time 
    [<<dydx_order=None>>]
    
    
    @@ AT: 2022-03-13T16:20:23.100091+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    [<<heartbeat_remaining_sec=3.673137001999976>>] (so now bot will sleep for remainder of the heartbeat)
    
    
    @@ AT: 2022-03-13T16:20:27.860127+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.2685081460000447>>]
    [<<get_state_time_sec=0.8143379769999228>>]
    [<<process_time_sec=8.502100001805957e-05>>]
    
    
    @@ AT: 2022-03-13T16:20:27.860404+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188427.8600097>>]
    [<<spot=2571.6000000000004>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:27.860610+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:27.860762+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:27.861070+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    [<<follow_down_at=None>>]
    [<<follow_up_at=None>>]
    [<<infer_anchors_on_init=True>>]
    
    
    @@ AT: 2022-03-13T16:20:27.861211+0000 | LEVEL: INFO | IN: __main__.<module>
    
    No orders to be placed at this time 
    [<<dydx_order=None>>]
    
    
    @@ AT: 2022-03-13T16:20:27.861345+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    [<<heartbeat_remaining_sec=3.915813451999952>>] (so now bot will sleep for remainder of the heartbeat)
    
    
    @@ AT: 2022-03-13T16:20:32.617231+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.29259670900000856>>]
    [<<get_state_time_sec=0.5431655460000684>>]
    [<<process_time_sec=8.277999995698337e-05>>]
    
    
    @@ AT: 2022-03-13T16:20:32.617524+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188432.61712>>]
    [<<spot=2571.45>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:32.617928+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:32.618109+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:32.618625+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    [<<follow_down_at=None>>]
    [<<follow_up_at=None>>]
    [<<infer_anchors_on_init=True>>]
    
    
    @@ AT: 2022-03-13T16:20:32.618795+0000 | LEVEL: INFO | IN: __main__.<module>
    
    No orders to be placed at this time 
    [<<dydx_order=None>>]
    
    
    @@ AT: 2022-03-13T16:20:32.619031+0000 | LEVEL: INFO | IN: __main__.<module>
    
    
    [<<heartbeat_remaining_sec=4.162323491000052>>] (so now bot will sleep for remainder of the heartbeat)
    
    
    @@ AT: 2022-03-13T16:20:37.823067+0000 | LEVEL: INFO | IN: __main__.<module>
    
    TIMING PROFILE:
    [<<get_spot_time_sec=0.27195281900003465>>]
    [<<get_state_time_sec=0.765084168000044>>]
    [<<process_time_sec=8.38739999835525e-05>>]
    
    
    @@ AT: 2022-03-13T16:20:37.823355+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [@@@]
    ***next_iteration***
    [<<timestamp=1647188437.8229544>>]
    [<<spot=2571.55>>]
    [<<current_equity=100.003404>>]
    [<<position=NONE>>]
    Will buy at $2565.47 or $2578.33
    
    
    @@ AT: 2022-03-13T16:20:37.823582+0000 | LEVEL: INFO | IN: __main__.<module>
    
    [<<dydx_account=DydxAccount(market=<Market.ETHUSD: 1>, order_type=<OrderType.MARKET: 1>, post_only=False, expiration_sec=500.0, limit_fee=0.0015, time_in_force=<TimeInForce.FILL_OR_KILL: 2>, side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404, buy_half_width_prct=0.25, sell_fallback_dist_prct=0.75, follow_prct=0.5, follow_lag_sec=60.0, action_trigger_offset_prct=100.0, period_sec=86400.0, sleep_sec=1200.0, heartbeat_sec=5.0, leverage=1.5, infer_anchors_on_init=True, buy_longs=True, buy_shorts=True, buffer_usd=3.0, trade_before_follow=True, never_retreat=True, quantum_decimals=2, follow_anchor_spot=None, follow_anchor_timestamp=None, action_anchor_spot=2571.9, action_anchor_timestamp=1647188412.6839797, create_long_at=2578.32975, create_short_at=2565.4702500000003, close_long_at=2559.0405, close_short_at=2584.7594999999997, follow_down_at=None, follow_up_at=None, initial_state_hash=None, verbose=True)>>]
    
    
    @@ AT: 2022-03-13T16:20:37.823781+0000 | LEVEL: INFO | IN: __main__.<module>
    
    From account state [<<current_state=PositionState(side=<Side.NONE: 0>, size_eth=None, entered_timestamp=None, entered_price=None, equity_usd=100.003404)>>],
    
    orders to execute: [<<dydx_orders=[]>>]
    
    
    @@ AT: 2022-03-13T16:20:37.824135+0000 | LEVEL: INFO | IN: __main__.<module>
    
    Instance state:
    [<<side_string=none>>]
    [<<size_eth=None>>]
    [<<equity_usd=100.003404>>]
    [<<action_anchor_spot=2571.9>>]
    [<<action_anchor_timestamp=1647188412.6839797>>]
    [<<close_long_at=2559.0405>>]
    [<<close_short_at=2584.7594999999997>>]
    [<<create_long_at=2578.32975>>]
    [<<create_short_at=2565.4702500000003>>]
    [<<entered_price=None>>]
    [<<entered_timestamp=None>>]
    [<<follow_anchor_spot=None>>]
    [<<follow_anchor_timestamp=None>>]
    """

    print(auto_extract_from_text(s, parallelize=2))
