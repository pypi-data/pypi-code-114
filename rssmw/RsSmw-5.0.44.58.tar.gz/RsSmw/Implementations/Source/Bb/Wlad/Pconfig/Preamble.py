from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:PREamble:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.preamble.get_state() \n
		Activates/deactivates the preamble and signal fields of the frames in the frame block. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:PREamble:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:PREamble:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.preamble.set_state(state = False) \n
		Activates/deactivates the preamble and signal fields of the frames in the frame block. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:PREamble:STATe {param}')
