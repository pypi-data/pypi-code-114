from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LteCell:
	"""LteCell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lteCell", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:LTECell:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.lteCell.get_state() \n
		In in-band mode, defines how the LTE channels are handled. If enabled, all LTE channels are deactivated. However, LTE
		reference signals are still transmitted. \n
			:return: lte_cell: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:LTECell:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, lte_cell: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:LTECell:STATe \n
		Snippet: driver.source.bb.eutra.downlink.niot.lteCell.set_state(lte_cell = False) \n
		In in-band mode, defines how the LTE channels are handled. If enabled, all LTE channels are deactivated. However, LTE
		reference signals are still transmitted. \n
			:param lte_cell: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(lte_cell)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:LTECell:STATe {param}')
