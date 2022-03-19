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
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:LEVel \n
		Snippet: value: int = driver.source.bb.gbas.clipping.get_level() \n
		Sets the limit for clipping. \n
			:return: level: integer Range: 1 to 100
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:CLIPping:LEVel?')
		return Conversions.str_to_int(response)

	def set_level(self, level: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:LEVel \n
		Snippet: driver.source.bb.gbas.clipping.set_level(level = 1) \n
		Sets the limit for clipping. \n
			:param level: integer Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:CLIPping:LEVel {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClipMode:
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:MODE \n
		Snippet: value: enums.ClipMode = driver.source.bb.gbas.clipping.get_mode() \n
		Sets the clipping mode. \n
			:return: mode: VECTor| SCALar
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:CLIPping:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClipMode)

	def set_mode(self, mode: enums.ClipMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:MODE \n
		Snippet: driver.source.bb.gbas.clipping.set_mode(mode = enums.ClipMode.SCALar) \n
		Sets the clipping mode. \n
			:param mode: VECTor| SCALar
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClipMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:CLIPping:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:STATe \n
		Snippet: value: bool = driver.source.bb.gbas.clipping.get_state() \n
		Enables/disable clipping. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GBAS:CLIPping:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:GBAS:CLIPping:STATe \n
		Snippet: driver.source.bb.gbas.clipping.set_state(state = False) \n
		Enables/disable clipping. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:GBAS:CLIPping:STATe {param}')
