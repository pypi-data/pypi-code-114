from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpch:
	"""Dpch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpch", core, parent)

	def get_count(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:DPCH:COUNt \n
		Snippet: value: int = driver.source.bb.w3Gpp.pparameter.dpch.get_count() \n
		Sets the number of activated DPCHs. The maximum number is the ratio of the chip rate and the symbol rate (maximum 512 at
		the lowest symbol rate of 7.5 ksps) . \n
			:return: count: integer Range: 0 to 512 (Max depends on other settings)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:PPARameter:DPCH:COUNt?')
		return Conversions.str_to_int(response)

	def set_count(self, count: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:DPCH:COUNt \n
		Snippet: driver.source.bb.w3Gpp.pparameter.dpch.set_count(count = 1) \n
		Sets the number of activated DPCHs. The maximum number is the ratio of the chip rate and the symbol rate (maximum 512 at
		the lowest symbol rate of 7.5 ksps) . \n
			:param count: integer Range: 0 to 512 (Max depends on other settings)
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:DPCH:COUNt {param}')

	# noinspection PyTypeChecker
	def get_symbol_rate(self) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:DPCH:SRATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.pparameter.dpch.get_symbol_rate() \n
		This command sets the symbol rate of DPCHs. The setting takes effect only after execution of command
		BB:W3GPp:PPARameter:EXECute. \n
			:return: srate: D7K5| D15K| D30K| D60K| D120k| D240k| D480k| D960k
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:PPARameter:DPCH:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)

	def set_symbol_rate(self, srate: enums.SymbRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:DPCH:SRATe \n
		Snippet: driver.source.bb.w3Gpp.pparameter.dpch.set_symbol_rate(srate = enums.SymbRate.D120k) \n
		This command sets the symbol rate of DPCHs. The setting takes effect only after execution of command
		BB:W3GPp:PPARameter:EXECute. \n
			:param srate: D7K5| D15K| D30K| D60K| D120k| D240k| D480k| D960k
		"""
		param = Conversions.enum_scalar_to_str(srate, enums.SymbRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:DPCH:SRATe {param}')
