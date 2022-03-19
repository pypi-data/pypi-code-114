from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, count: int, userIx=repcap.UserIx.Default, zoneNull=repcap.ZoneNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:ZONE<CH0>:COUNt \n
		Snippet: driver.source.bb.evdo.user.rpc.zone.count.set(count = 1, userIx = repcap.UserIx.Default, zoneNull = repcap.ZoneNull.Default) \n
		The Reverse Power Control (RPC) pattern is defined in form of table with four zones (zone 0 .. 3) . For each zone, a bit
		and a count can be defined. This parameter defines the number of RPC bits sent within the specific zone of the RPC
		Pattern. \n
			:param count: integer Range: 1 to 128
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param zoneNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zone')
		"""
		param = Conversions.decimal_value_to_str(count)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		zoneNull_cmd_val = self._cmd_group.get_repcap_cmd_value(zoneNull, repcap.ZoneNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:ZONE{zoneNull_cmd_val}:COUNt {param}')

	def get(self, userIx=repcap.UserIx.Default, zoneNull=repcap.ZoneNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:ZONE<CH0>:COUNt \n
		Snippet: value: int = driver.source.bb.evdo.user.rpc.zone.count.get(userIx = repcap.UserIx.Default, zoneNull = repcap.ZoneNull.Default) \n
		The Reverse Power Control (RPC) pattern is defined in form of table with four zones (zone 0 .. 3) . For each zone, a bit
		and a count can be defined. This parameter defines the number of RPC bits sent within the specific zone of the RPC
		Pattern. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param zoneNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zone')
			:return: count: integer Range: 1 to 128"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		zoneNull_cmd_val = self._cmd_group.get_repcap_cmd_value(zoneNull, repcap.ZoneNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:ZONE{zoneNull_cmd_val}:COUNt?')
		return Conversions.str_to_int(response)
