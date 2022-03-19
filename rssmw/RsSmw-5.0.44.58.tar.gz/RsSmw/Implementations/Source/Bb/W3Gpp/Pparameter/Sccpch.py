from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sccpch:
	"""Sccpch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sccpch", core, parent)

	# noinspection PyTypeChecker
	def get_symbol_rate(self) -> enums.SymbRate:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:SCCPch:SRATe \n
		Snippet: value: enums.SymbRate = driver.source.bb.w3Gpp.pparameter.sccpch.get_symbol_rate() \n
		The command sets the symbol rate of S-CCPCH. The setting takes effect only after execution of command
		BB:W3GPp:PPARameter:EXECute. \n
			:return: srate: D15K| D30K| D60K| D120k| D240k| D480k| D960k
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:PPARameter:SCCPch:SRATe?')
		return Conversions.str_to_scalar_enum(response, enums.SymbRate)

	def set_symbol_rate(self, srate: enums.SymbRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:SCCPch:SRATe \n
		Snippet: driver.source.bb.w3Gpp.pparameter.sccpch.set_symbol_rate(srate = enums.SymbRate.D120k) \n
		The command sets the symbol rate of S-CCPCH. The setting takes effect only after execution of command
		BB:W3GPp:PPARameter:EXECute. \n
			:param srate: D15K| D30K| D60K| D120k| D240k| D480k| D960k
		"""
		param = Conversions.enum_scalar_to_str(srate, enums.SymbRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:SCCPch:SRATe {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:SCCPch:STATe \n
		Snippet: value: bool = driver.source.bb.w3Gpp.pparameter.sccpch.get_state() \n
		Activates/deactivates the S-CCPCH. \n
			:return: state: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:W3GPp:PPARameter:SCCPch:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:PPARameter:SCCPch:STATe \n
		Snippet: driver.source.bb.w3Gpp.pparameter.sccpch.set_state(state = False) \n
		Activates/deactivates the S-CCPCH. \n
			:param state: 1| ON| 0| OFF
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:W3GPp:PPARameter:SCCPch:STATe {param}')
