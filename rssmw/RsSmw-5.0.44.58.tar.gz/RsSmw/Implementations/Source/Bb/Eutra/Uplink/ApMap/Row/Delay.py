from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Delay:
	"""Delay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("delay", core, parent)

	def set(self, ul_bb_delay: int, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:APMap:ROW<BBID>:DELay \n
		Snippet: driver.source.bb.eutra.uplink.apMap.row.delay.set(ul_bb_delay = 1, rowNull = repcap.RowNull.Default) \n
		In advanced configuration with coupled sources, delays the signal of the selected cell. This result in signal delay
		between the generated baseband signals. \n
			:param ul_bb_delay: integer Range: 0 to 70000, Unit: ns
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(ul_bb_delay)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:UL:APMap:ROW{rowNull_cmd_val}:DELay {param}')

	def get(self, rowNull=repcap.RowNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:UL:APMap:ROW<BBID>:DELay \n
		Snippet: value: int = driver.source.bb.eutra.uplink.apMap.row.delay.get(rowNull = repcap.RowNull.Default) \n
		In advanced configuration with coupled sources, delays the signal of the selected cell. This result in signal delay
		between the generated baseband signals. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: ul_bb_delay: integer Range: 0 to 70000, Unit: ns"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:UL:APMap:ROW{rowNull_cmd_val}:DELay?')
		return Conversions.str_to_int(response)
