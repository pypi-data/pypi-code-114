from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Avrl:
	"""Avrl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("avrl", core, parent)

	def get(self, rowNull=repcap.RowNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:POWer:BBConf:ROW<CH0>:AVRL \n
		Snippet: value: float = driver.source.bb.nr5G.output.power.bbConf.row.avrl.get(rowNull = repcap.RowNull.Default) \n
		Queries the available basebands with their average power. \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: pow_per_bb_rel_lvl: float Range: -80 to 10"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:POWer:BBConf:ROW{rowNull_cmd_val}:AVRL?')
		return Conversions.str_to_float(response)
