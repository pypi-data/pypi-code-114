from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clipping:
	"""Clipping commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clipping", core, parent)

	def get_level(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:LEVel \n
		Snippet: value: int = driver.source.bb.btooth.clipping.get_level() \n
		Sets the limit for level clipping. This value indicates at what point the signal is clipped. It is specified as a
		percentage, relative to the highest level. 100% indicates that clipping does not take place. \n
			:return: level: integer Range: 1 to 100, Unit: PCT
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:CLIPping:LEVel?')
		return Conversions.str_to_int(response)

	def set_level(self, level: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:LEVel \n
		Snippet: driver.source.bb.btooth.clipping.set_level(level = 1) \n
		Sets the limit for level clipping. This value indicates at what point the signal is clipped. It is specified as a
		percentage, relative to the highest level. 100% indicates that clipping does not take place. \n
			:param level: integer Range: 1 to 100, Unit: PCT
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:CLIPping:LEVel {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClipMode:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:MODE \n
		Snippet: value: enums.ClipMode = driver.source.bb.btooth.clipping.get_mode() \n
		The command sets the method for level clipping. \n
			:return: mode: VECTor| SCALar VECTor The reference level is the amplitude | i+jq |. SCALar The reference level is the absolute maximum of the I and Q values.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:CLIPping:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClipMode)

	def set_mode(self, mode: enums.ClipMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:MODE \n
		Snippet: driver.source.bb.btooth.clipping.set_mode(mode = enums.ClipMode.SCALar) \n
		The command sets the method for level clipping. \n
			:param mode: VECTor| SCALar VECTor The reference level is the amplitude | i+jq |. SCALar The reference level is the absolute maximum of the I and Q values.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClipMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:CLIPping:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.clipping.get_state() \n
		Activates level clipping. The value is defined with the command BB:BTO:CLIPping:LEVel, the mode of calculation with the
		command BB:BTO:CLIPping:MODE. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:BTOoth:CLIPping:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:CLIPping:STATe \n
		Snippet: driver.source.bb.btooth.clipping.set_state(state = False) \n
		Activates level clipping. The value is defined with the command BB:BTO:CLIPping:LEVel, the mode of calculation with the
		command BB:BTO:CLIPping:MODE. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:CLIPping:STATe {param}')
