from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cfactor:
	"""Cfactor commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfactor", core, parent)

	def get_actual(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CFACtor:ACTual \n
		Snippet: value: float = driver.source.bb.mccw.cfactor.get_actual() \n
		No command help available \n
			:return: actual: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CFACtor:ACTual?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.MccwCrestFactMode:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CFACtor:MODE \n
		Snippet: value: enums.MccwCrestFactMode = driver.source.bb.mccw.cfactor.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CFACtor:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MccwCrestFactMode)

	def set_mode(self, mode: enums.MccwCrestFactMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CFACtor:MODE \n
		Snippet: driver.source.bb.mccw.cfactor.set_mode(mode = enums.MccwCrestFactMode.CHIRp) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MccwCrestFactMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CFACtor:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CFACtor \n
		Snippet: value: float = driver.source.bb.mccw.cfactor.get_value() \n
		No command help available \n
			:return: cfactor: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:MCCW:CFACtor?')
		return Conversions.str_to_float(response)

	def set_value(self, cfactor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:MCCW:CFACtor \n
		Snippet: driver.source.bb.mccw.cfactor.set_value(cfactor = 1.0) \n
		No command help available \n
			:param cfactor: No help available
		"""
		param = Conversions.decimal_value_to_str(cfactor)
		self._core.io.write(f'SOURce<HwInstance>:BB:MCCW:CFACtor {param}')
