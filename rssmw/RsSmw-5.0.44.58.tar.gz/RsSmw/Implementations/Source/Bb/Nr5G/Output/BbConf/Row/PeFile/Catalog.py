from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, rowNull=repcap.RowNull.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:ROW<CH0>:PEFile:CATalog \n
		Snippet: value: List[str] = driver.source.bb.nr5G.output.bbConf.row.peFile.catalog.get(rowNull = repcap.RowNull.Default) \n
		No command help available \n
			:param rowNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Row')
			:return: nr_5_gcat_name_phy_exp: No help available"""
		rowNull_cmd_val = self._cmd_group.get_repcap_cmd_value(rowNull, repcap.RowNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:ROW{rowNull_cmd_val}:PEFile:CATalog?')
		return Conversions.str_to_str_list(response)
