from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:GAP:CONFig:STATe \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.niot.gap.config.get_state() \n
		If activated, a gap between the NPDCCH and NPDSCH with the specified duration is applied. \n
			:return: gap_config: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:NIOT:GAP:CONFig:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, gap_config: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:NIOT:GAP:CONFig:STATe \n
		Snippet: driver.source.bb.eutra.downlink.niot.gap.config.set_state(gap_config = False) \n
		If activated, a gap between the NPDCCH and NPDSCH with the specified duration is applied. \n
			:param gap_config: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(gap_config)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:NIOT:GAP:CONFig:STATe {param}')
