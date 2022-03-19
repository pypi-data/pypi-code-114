from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsmod:
	"""Nsmod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsmod", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NSMod:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.nsmod.get_state() \n
		No command help available \n
			:return: non_std_modulation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:NSMod:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, non_std_modulation: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NSMod:STATe \n
		Snippet: driver.source.bb.nr5G.nsmod.set_state(non_std_modulation = False) \n
		No command help available \n
			:param non_std_modulation: No help available
		"""
		param = Conversions.bool_to_str(non_std_modulation)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NSMod:STATe {param}')
