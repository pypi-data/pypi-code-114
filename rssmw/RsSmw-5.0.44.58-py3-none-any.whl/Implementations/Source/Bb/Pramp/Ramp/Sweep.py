from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:SWEep:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.sweep.get_time() \n
		Sets the time of one sweep cycle. \n
			:return: sweep_time: float Range: 1E-6 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:SWEep:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, sweep_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:SWEep:TIME \n
		Snippet: driver.source.bb.pramp.ramp.sweep.set_time(sweep_time = 1.0) \n
		Sets the time of one sweep cycle. \n
			:param sweep_time: float Range: 1E-6 to 20
		"""
		param = Conversions.decimal_value_to_str(sweep_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:SWEep:TIME {param}')
