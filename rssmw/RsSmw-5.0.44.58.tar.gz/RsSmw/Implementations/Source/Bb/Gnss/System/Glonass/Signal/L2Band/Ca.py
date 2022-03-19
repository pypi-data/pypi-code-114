from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ca:
	"""Ca commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ca", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:CA:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.system.glonass.signal.l2Band.ca.get_state() \n
		Enables the corresponding signal from the GNSS system in the corresponding RF band. \n
			:return: signal_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:CA:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, signal_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:CA:[STATe] \n
		Snippet: driver.source.bb.gnss.system.glonass.signal.l2Band.ca.set_state(signal_state = False) \n
		Enables the corresponding signal from the GNSS system in the corresponding RF band. \n
			:param signal_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(signal_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:CA:STATe {param}')
