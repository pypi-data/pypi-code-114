from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpcc:
	"""Dpcc commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpcc", core, parent)

	def get_burst(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:BURSt \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.udtx.dpcc.get_burst() \n
		No command help available \n
			:return: burst: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:BURSt?')
		return Conversions.str_to_int(response)

	def set_burst(self, burst: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:BURSt \n
		Snippet: driver.source.bb.w3Gpp.mstation.udtx.dpcc.set_burst(burst = 1) \n
		No command help available \n
			:param burst: No help available
		"""
		param = Conversions.decimal_value_to_str(burst)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:BURSt {param}')

	def get_cycle(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:CYCLe \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.udtx.dpcc.get_cycle() \n
		No command help available \n
			:return: cycle: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:CYCLe?')
		return Conversions.str_to_int(response)

	def set_cycle(self, cycle: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:CYCLe \n
		Snippet: driver.source.bb.w3Gpp.mstation.udtx.dpcc.set_cycle(cycle = 1) \n
		No command help available \n
			:param cycle: No help available
		"""
		param = Conversions.decimal_value_to_str(cycle)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:CYCLe {param}')

	def get_offset(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:OFFSet \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.udtx.dpcc.get_offset() \n
		No command help available \n
			:return: offset: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:OFFSet?')
		return Conversions.str_to_int(response)

	def set_offset(self, offset: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:OFFSet \n
		Snippet: driver.source.bb.w3Gpp.mstation.udtx.dpcc.set_offset(offset = 1) \n
		No command help available \n
			:param offset: No help available
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:OFFSet {param}')

	def get_postamble(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:POSTamble \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.udtx.dpcc.get_postamble() \n
		No command help available \n
			:return: postamble: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:POSTamble?')
		return Conversions.str_to_int(response)

	def get_preamble(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:MSTation:UDTX:DPCC:PREamble \n
		Snippet: value: int = driver.source.bb.w3Gpp.mstation.udtx.dpcc.get_preamble() \n
		No command help available \n
			:return: preamble: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:MSTation:UDTX:DPCC:PREamble?')
		return Conversions.str_to_int(response)
