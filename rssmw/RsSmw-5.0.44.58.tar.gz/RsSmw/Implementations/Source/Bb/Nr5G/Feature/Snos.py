from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snos:
	"""Snos commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snos", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:FEATure:SNOS:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.feature.snos.get_state() \n
		No command help available \n
			:return: separate_num_output: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:FEATure:SNOS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, separate_num_output: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:FEATure:SNOS:STATe \n
		Snippet: driver.source.bb.nr5G.feature.snos.set_state(separate_num_output = False) \n
		No command help available \n
			:param separate_num_output: No help available
		"""
		param = Conversions.bool_to_str(separate_num_output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:FEATure:SNOS:STATe {param}')
