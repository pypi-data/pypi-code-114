from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Conflict:
	"""Conflict commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conflict", core, parent)

	def get(self, rowNull=repcap.RowNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:CONFlict \n
		Snippet: value: bool = driver.source.bb.nr5G.output.bbConf.row.conflict.get(rowNull = repcap.RowNull.Default) \n
		Queries if there are conflicts caused by mismatch between the nominal sample rate, playback rate and sample rate in the
		given row. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: conflict: 1| ON| 0| OFF"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:CONFlict?')
		return Conversions.str_to_bool(response)
