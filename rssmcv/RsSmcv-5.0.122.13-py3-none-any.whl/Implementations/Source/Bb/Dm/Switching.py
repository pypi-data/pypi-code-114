from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Switching:
	"""Switching commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("switching", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SourceInt:
		"""SCPI: [SOURce<HW>]:BB:DM:SWITching:SOURce \n
		Snippet: value: enums.SourceInt = driver.source.bb.dm.switching.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SWITching:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_source(self, source: enums.SourceInt) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SWITching:SOURce \n
		Snippet: driver.source.bb.dm.switching.set_source(source = enums.SourceInt.EXTernal) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SWITching:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DM:SWITching:STATe \n
		Snippet: value: bool = driver.source.bb.dm.switching.get_state() \n
		Enables switching between a modulated and an unmodulated signal. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DM:SWITching:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DM:SWITching:STATe \n
		Snippet: driver.source.bb.dm.switching.set_state(state = False) \n
		Enables switching between a modulated and an unmodulated signal. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DM:SWITching:STATe {param}')
