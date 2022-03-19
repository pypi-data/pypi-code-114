from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Variation:
	"""Variation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("variation", core, parent)

	def set(self, srate_variation: bool, rowNull=repcap.RowNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:VARiation \n
		Snippet: driver.source.bb.nr5G.output.bbConf.row.variation.set(srate_variation = False, rowNull = repcap.RowNull.Default) \n
		Activates sample rate variation. \n
			:param srate_variation: 0| 1| OFF| ON
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
		"""
		param = Conversions.bool_to_str(srate_variation)
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:VARiation {param}')

	def get(self, rowNull=repcap.RowNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:VARiation \n
		Snippet: value: bool = driver.source.bb.nr5G.output.bbConf.row.variation.get(rowNull = repcap.RowNull.Default) \n
		Activates sample rate variation. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: srate_variation: 0| 1| OFF| ON"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:VARiation?')
		return Conversions.str_to_bool(response)
