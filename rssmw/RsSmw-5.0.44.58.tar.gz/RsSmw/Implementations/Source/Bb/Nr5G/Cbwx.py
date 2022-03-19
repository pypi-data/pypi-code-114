from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbwx:
	"""Cbwx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbwx", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CBWX:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.cbwx.get_state() \n
		No command help available \n
			:return: bw_extension: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:CBWX:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, bw_extension: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CBWX:STATe \n
		Snippet: driver.source.bb.nr5G.cbwx.set_state(bw_extension = False) \n
		No command help available \n
			:param bw_extension: No help available
		"""
		param = Conversions.bool_to_str(bw_extension)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:CBWX:STATe {param}')
