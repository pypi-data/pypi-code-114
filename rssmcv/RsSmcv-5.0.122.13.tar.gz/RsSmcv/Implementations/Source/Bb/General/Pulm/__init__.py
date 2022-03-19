from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulm:
	"""Pulm commands group definition. 9 total commands, 3 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulm", core, parent)

	@property
	def double(self):
		"""double commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_double'):
			from .Double import Double
			self._double = Double(self._core, self._cmd_group)
		return self._double

	@property
	def transition(self):
		"""transition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_transition'):
			from .Transition import Transition
			self._transition = Transition(self._core, self._cmd_group)
		return self._transition

	@property
	def video(self):
		"""video commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_video'):
			from .Video import Video
			self._video = Video(self._core, self._cmd_group)
		return self._video

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DELay \n
		Snippet: value: float = driver.source.bb.general.pulm.get_delay() \n
		Sets the pulse delay in microseconds. \n
			:return: pulm_delay: float Range: 50E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, pulm_delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:DELay \n
		Snippet: driver.source.bb.general.pulm.set_delay(pulm_delay = 1.0) \n
		Sets the pulse delay in microseconds. \n
			:param pulm_delay: float Range: 50E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(pulm_delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:DELay {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BasebandPulseMode:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:MODE \n
		Snippet: value: enums.BasebandPulseMode = driver.source.bb.general.pulm.get_mode() \n
		Sets the pulse mode. You can set for single or double pulse signals. \n
			:return: pulm_mode: SINGle| DOUBle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BasebandPulseMode)

	def set_mode(self, pulm_mode: enums.BasebandPulseMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:MODE \n
		Snippet: driver.source.bb.general.pulm.set_mode(pulm_mode = enums.BasebandPulseMode.DOUBle) \n
		Sets the pulse mode. You can set for single or double pulse signals. \n
			:param pulm_mode: SINGle| DOUBle
		"""
		param = Conversions.enum_scalar_to_str(pulm_mode, enums.BasebandPulseMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:MODE {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:PERiod \n
		Snippet: value: float = driver.source.bb.general.pulm.get_period() \n
		Defines the pulse period in microseconds. \n
			:return: puls_mod_per: float Range: 100E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, puls_mod_per: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:PERiod \n
		Snippet: driver.source.bb.general.pulm.set_period(puls_mod_per = 1.0) \n
		Defines the pulse period in microseconds. \n
			:param puls_mod_per: float Range: 100E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(puls_mod_per)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:PERiod {param}')

	def get_width(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:WIDTh \n
		Snippet: value: float = driver.source.bb.general.pulm.get_width() \n
		Sets the pulse width in microseconds. \n
			:return: pulm_width: float Range: 50E-9 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:WIDTh?')
		return Conversions.str_to_float(response)

	def set_width(self, pulm_width: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:WIDTh \n
		Snippet: driver.source.bb.general.pulm.set_width(pulm_width = 1.0) \n
		Sets the pulse width in microseconds. \n
			:param pulm_width: float Range: 50E-9 to 100
		"""
		param = Conversions.decimal_value_to_str(pulm_width)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:WIDTh {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:[STATe] \n
		Snippet: value: bool = driver.source.bb.general.pulm.get_state() \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:return: pulm_state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GENeral:PULM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, pulm_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GENeral:PULM:[STATe] \n
		Snippet: driver.source.bb.general.pulm.set_state(pulm_state = False) \n
		Activates the standard and deactivates all the other digital standards and digital modulation modes in the same path. \n
			:param pulm_state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(pulm_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GENeral:PULM:STATe {param}')

	def clone(self) -> 'Pulm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
