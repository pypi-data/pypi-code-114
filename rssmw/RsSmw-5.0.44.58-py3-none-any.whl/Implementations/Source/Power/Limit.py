from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limit", core, parent)

	def get_amplitude(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:LIMit:[AMPLitude] \n
		Snippet: value: float = driver.source.power.limit.get_amplitude() \n
		Limits the maximum RF output level in CW and sweep mode. It does not influence the 'Level' display or the response to the
		query [:SOURce<hw>]:POWer[:LEVel][:IMMediate][:AMPLitude]. \n
			:return: amplitude: float Range: depends on the installed options
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:LIMit:AMPLitude?')
		return Conversions.str_to_float(response)

	def set_amplitude(self, amplitude: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:LIMit:[AMPLitude] \n
		Snippet: driver.source.power.limit.set_amplitude(amplitude = 1.0) \n
		Limits the maximum RF output level in CW and sweep mode. It does not influence the 'Level' display or the response to the
		query [:SOURce<hw>]:POWer[:LEVel][:IMMediate][:AMPLitude]. \n
			:param amplitude: float Range: depends on the installed options
		"""
		param = Conversions.decimal_value_to_str(amplitude)
		self._core.io.write(f'SOURce<HwInstance>:POWer:LIMit:AMPLitude {param}')
