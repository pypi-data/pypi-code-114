from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Simulation:
	"""Simulation commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("simulation", core, parent)

	# noinspection PyTypeChecker
	def get_count(self) -> enums.FreqConvExt:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:SIMulation:COUNt \n
		Snippet: value: enums.FreqConvExt = driver.source.frequency.converter.external.simulation.get_count() \n
		No command help available \n
			:return: count: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:SIMulation:COUNt?')
		return Conversions.str_to_scalar_enum(response, enums.FreqConvExt)

	def set_count(self, count: enums.FreqConvExt) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:SIMulation:COUNt \n
		Snippet: driver.source.frequency.converter.external.simulation.set_count(count = enums.FreqConvExt.M01) \n
		No command help available \n
			:param count: No help available
		"""
		param = Conversions.enum_scalar_to_str(count, enums.FreqConvExt)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:SIMulation:COUNt {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:SIMulation:STATe \n
		Snippet: value: bool = driver.source.frequency.converter.external.simulation.get_state() \n
		No command help available \n
			:return: sim_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:SIMulation:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, sim_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:CONVerter:EXTernal:SIMulation:STATe \n
		Snippet: driver.source.frequency.converter.external.simulation.set_state(sim_state = False) \n
		No command help available \n
			:param sim_state: No help available
		"""
		param = Conversions.bool_to_str(sim_state)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CONVerter:EXTernal:SIMulation:STATe {param}')
