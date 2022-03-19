from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pbrate:
	"""Pbrate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbrate", core, parent)

	def set(self, playback_rate: int, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:PBRate \n
		Snippet: driver.source.bb.nr5G.output.bbConf.row.pbrate.set(playback_rate = 1, rowNull = repcap.RowNull.Default) \n
		Defines the playback rate.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on [:SOURce<hw>]:BB:NR5G:OUTPut:BBConf:ROW<ch0>:VARiation. \n
			:param playback_rate: integer Per default, the playback rate is the same as the calculated sample rate but the value range also depends on the installed options. Range: 0 to 24e8
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.decimal_value_to_str(playback_rate)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:PBRate {param}')

	def get(self, rowNull=repcap.RowNull.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:PBRate \n
		Snippet: value: int = driver.source.bb.nr5G.output.bbConf.row.pbrate.get(rowNull = repcap.RowNull.Default) \n
		Defines the playback rate.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on [:SOURce<hw>]:BB:NR5G:OUTPut:BBConf:ROW<ch0>:VARiation. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: playback_rate: integer Per default, the playback rate is the same as the calculated sample rate but the value range also depends on the installed options. Range: 0 to 24e8"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:PBRate?')
		return Conversions.str_to_int(response)
