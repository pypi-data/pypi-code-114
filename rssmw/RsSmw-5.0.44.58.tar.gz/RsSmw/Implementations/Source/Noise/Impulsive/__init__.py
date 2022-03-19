from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Impulsive:
	"""Impulsive commands group definition. 7 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("impulsive", core, parent)

	@property
	def burst(self):
		"""burst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	def get_ci(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:CI \n
		Snippet: value: float = driver.source.noise.impulsive.get_ci() \n
		Specifies the ratio of the wanted signal (C) to the impulsive noise signal (I) . \n
			:return: ipls_ci: float Range: -35 to 60
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:CI?')
		return Conversions.str_to_float(response)

	def set_ci(self, ipls_ci: float) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:CI \n
		Snippet: driver.source.noise.impulsive.set_ci(ipls_ci = 1.0) \n
		Specifies the ratio of the wanted signal (C) to the impulsive noise signal (I) . \n
			:param ipls_ci: float Range: -35 to 60
		"""
		param = Conversions.decimal_value_to_str(ipls_ci)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:CI {param}')

	def get_frame(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:FRAMe \n
		Snippet: value: float = driver.source.noise.impulsive.get_frame() \n
		Sets the time intervals at which the bursts occur. \n
			:return: ipls_frame_duration: float Range: 0.1E-3 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:FRAMe?')
		return Conversions.str_to_float(response)

	def set_frame(self, ipls_frame_duration: float) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:FRAMe \n
		Snippet: driver.source.noise.impulsive.set_frame(ipls_frame_duration = 1.0) \n
		Sets the time intervals at which the bursts occur. \n
			:param ipls_frame_duration: float Range: 0.1E-3 to 1
		"""
		param = Conversions.decimal_value_to_str(ipls_frame_duration)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:FRAMe {param}')

	def get_max_space(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:MAXSpace \n
		Snippet: value: float = driver.source.noise.impulsive.get_max_space() \n
		If more than 1 pulse per burst are enabled ([:SOURce<hw>]:NOISe:IMPulsive:PULSee.g. 2) , sets the minimum/maximum spacing
		between 2 pulses within a burst. \n
			:return: ipls_space_max: float Range: 0.25E-6 to 0.01
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:MAXSpace?')
		return Conversions.str_to_float(response)

	def set_max_space(self, ipls_space_max: float) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:MAXSpace \n
		Snippet: driver.source.noise.impulsive.set_max_space(ipls_space_max = 1.0) \n
		If more than 1 pulse per burst are enabled ([:SOURce<hw>]:NOISe:IMPulsive:PULSee.g. 2) , sets the minimum/maximum spacing
		between 2 pulses within a burst. \n
			:param ipls_space_max: float Range: 0.25E-6 to 0.01
		"""
		param = Conversions.decimal_value_to_str(ipls_space_max)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:MAXSpace {param}')

	def get_min_space(self) -> float:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:MINSpace \n
		Snippet: value: float = driver.source.noise.impulsive.get_min_space() \n
		If more than 1 pulse per burst are enabled ([:SOURce<hw>]:NOISe:IMPulsive:PULSee.g. 2) , sets the minimum/maximum spacing
		between 2 pulses within a burst. \n
			:return: ipls_min_space: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:MINSpace?')
		return Conversions.str_to_float(response)

	def set_min_space(self, ipls_min_space: float) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:MINSpace \n
		Snippet: driver.source.noise.impulsive.set_min_space(ipls_min_space = 1.0) \n
		If more than 1 pulse per burst are enabled ([:SOURce<hw>]:NOISe:IMPulsive:PULSee.g. 2) , sets the minimum/maximum spacing
		between 2 pulses within a burst. \n
			:param ipls_min_space: float Range: 0.25E-6 to 0.01
		"""
		param = Conversions.decimal_value_to_str(ipls_min_space)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:MINSpace {param}')

	def get_pulse(self) -> int:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:PULSe \n
		Snippet: value: int = driver.source.noise.impulsive.get_pulse() \n
		Sets the number of noise pulses per burst. \n
			:return: ipls_pulse: integer Range: 1 to 65535
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:PULSe?')
		return Conversions.str_to_int(response)

	def set_pulse(self, ipls_pulse: int) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:PULSe \n
		Snippet: driver.source.noise.impulsive.set_pulse(ipls_pulse = 1) \n
		Sets the number of noise pulses per burst. \n
			:param ipls_pulse: integer Range: 1 to 65535
		"""
		param = Conversions.decimal_value_to_str(ipls_pulse)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:PULSe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:[STATe] \n
		Snippet: value: bool = driver.source.noise.impulsive.get_state() \n
		Enables or disables the impulsive noise generator. \n
			:return: impulsive_state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:NOISe:IMPulsive:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, impulsive_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:NOISe:IMPulsive:[STATe] \n
		Snippet: driver.source.noise.impulsive.set_state(impulsive_state = False) \n
		Enables or disables the impulsive noise generator. \n
			:param impulsive_state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(impulsive_state)
		self._core.io.write(f'SOURce<HwInstance>:NOISe:IMPulsive:STATe {param}')

	def clone(self) -> 'Impulsive':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Impulsive(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
