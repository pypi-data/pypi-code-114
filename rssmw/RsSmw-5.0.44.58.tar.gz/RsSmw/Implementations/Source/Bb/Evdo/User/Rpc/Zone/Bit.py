from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bit:
	"""Bit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bit", core, parent)

	def set(self, bit: int, userIx=repcap.UserIx.Default, zoneNull=repcap.ZoneNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:ZONE<CH0>:BIT \n
		Snippet: driver.source.bb.evdo.user.rpc.zone.bit.set(bit = 1, userIx = repcap.UserIx.Default, zoneNull = repcap.ZoneNull.Default) \n
		The Reverse Power Control (RPC) pattern is defined in form of table with four zones (zone 0 .. 3) . For each zone, a bit
		and a count can be defined. This parameter defines the RPC bits sent within the specific zone of the RPC Pattern. \n
			:param bit: 0| 1 Range: 0 to 1
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param zoneNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zone')
		"""
		param = Conversions.decimal_value_to_str(bit)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		zoneNull_cmd_val = self._cmd_group.get_repcap_cmd_value(zoneNull, repcap.ZoneNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:ZONE{zoneNull_cmd_val}:BIT {param}')

	def get(self, userIx=repcap.UserIx.Default, zoneNull=repcap.ZoneNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:ZONE<CH0>:BIT \n
		Snippet: value: int = driver.source.bb.evdo.user.rpc.zone.bit.get(userIx = repcap.UserIx.Default, zoneNull = repcap.ZoneNull.Default) \n
		The Reverse Power Control (RPC) pattern is defined in form of table with four zones (zone 0 .. 3) . For each zone, a bit
		and a count can be defined. This parameter defines the RPC bits sent within the specific zone of the RPC Pattern. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:param zoneNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Zone')
			:return: bit: 0| 1 Range: 0 to 1"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		zoneNull_cmd_val = self._cmd_group.get_repcap_cmd_value(zoneNull, repcap.ZoneNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:ZONE{zoneNull_cmd_val}:BIT?')
		return Conversions.str_to_int(response)
