from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Optimization:
	"""Optimization commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("optimization", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.BbImpOptMode:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:MODE \n
		Snippet: value: enums.BbImpOptMode = driver.source.bb.impairment.optimization.get_mode() \n
		Sets the optimization mode. \n
			:return: mode: FAST| | QHTable FAST Optimization by compensation for I/Q skew. QHTable Improved optimization by maintained speed.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IMPairment:OPTimization:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.BbImpOptMode)

	def set_mode(self, mode: enums.BbImpOptMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:MODE \n
		Snippet: driver.source.bb.impairment.optimization.set_mode(mode = enums.BbImpOptMode.FAST) \n
		Sets the optimization mode. \n
			:param mode: FAST| | QHTable FAST Optimization by compensation for I/Q skew. QHTable Improved optimization by maintained speed.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.BbImpOptMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:IMPairment:OPTimization:MODE {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:STATe \n
		Snippet: value: bool = driver.source.bb.impairment.optimization.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:IMPairment:OPTimization:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:IMPairment:OPTimization:STATe \n
		Snippet: driver.source.bb.impairment.optimization.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:IMPairment:OPTimization:STATe {param}')
