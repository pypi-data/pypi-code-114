from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sinfo:
	"""Sinfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sinfo", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:SINFo:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.ehFlags.sinfo.get_state() \n
		Enables / disables the signaling of SyncInfo field for periodic advertisement. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:SINFo:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:SINFo:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.ehFlags.sinfo.set_state(state = False) \n
		Enables / disables the signaling of SyncInfo field for periodic advertisement. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:EHFLags:SINFo:STATe {param}')
