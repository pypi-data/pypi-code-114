from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cinfo:
	"""Cinfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cinfo", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:CINFo:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.ehFlags.cinfo.get_state() \n
		Activates the CTEInfo field in the extended header of Bluetooth LE advertising packets in the LE uncoded PHY. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:CINFo:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:CINFo:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.ehFlags.cinfo.set_state(state = False) \n
		Activates the CTEInfo field in the extended header of Bluetooth LE advertising packets in the LE uncoded PHY. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:CINFo:STATe {param}')
