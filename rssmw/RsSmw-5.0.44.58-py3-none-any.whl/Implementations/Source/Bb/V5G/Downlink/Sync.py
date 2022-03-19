from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 12 total commands, 0 Subgroups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	def get_epower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:EPOWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.sync.get_epower() \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:return: epower: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:EPOWer?')
		return Conversions.str_to_float(response)

	def set_epower(self, epower: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:EPOWer \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_epower(epower = 1.0) \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:param epower: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(epower)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:EPOWer {param}')

	def get_piq_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PIQSequence \n
		Snippet: value: str = driver.source.bb.v5G.downlink.sync.get_piq_sequence() \n
		No command help available \n
			:return: piq_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:PIQSequence?')
		return trim_str_response(response)

	def set_piq_sequence(self, piq_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PIQSequence \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_piq_sequence(piq_sequence = '1') \n
		No command help available \n
			:param piq_sequence: No help available
		"""
		param = Conversions.value_to_quoted_str(piq_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:PIQSequence {param}')

	# noinspection PyTypeChecker
	def get_pmodulation(self) -> enums.SyncModulationScheme:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PMODulation \n
		Snippet: value: enums.SyncModulationScheme = driver.source.bb.v5G.downlink.sync.get_pmodulation() \n
		No command help available \n
			:return: pmodulation: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:PMODulation?')
		return Conversions.str_to_scalar_enum(response, enums.SyncModulationScheme)

	def set_pmodulation(self, pmodulation: enums.SyncModulationScheme) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PMODulation \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_pmodulation(pmodulation = enums.SyncModulationScheme.IQFile) \n
		No command help available \n
			:param pmodulation: No help available
		"""
		param = Conversions.enum_scalar_to_str(pmodulation, enums.SyncModulationScheme)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:PMODulation {param}')

	def get_ppower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PPOWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.sync.get_ppower() \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:return: ppower: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:PPOWer?')
		return Conversions.str_to_float(response)

	def set_ppower(self, ppower: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PPOWer \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_ppower(ppower = 1.0) \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:param ppower: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(ppower)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:PPOWer {param}')

	def get_psequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PSEQuence \n
		Snippet: value: str = driver.source.bb.v5G.downlink.sync.get_psequence() \n
		No command help available \n
			:return: psequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:PSEQuence?')
		return trim_str_response(response)

	def set_psequence(self, psequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PSEQuence \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_psequence(psequence = '1') \n
		No command help available \n
			:param psequence: No help available
		"""
		param = Conversions.value_to_quoted_str(psequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:PSEQuence {param}')

	def get_pstate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PSTate \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.sync.get_pstate() \n
		No command help available \n
			:return: psync_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:PSTate?')
		return Conversions.str_to_bool(response)

	def set_pstate(self, psync_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:PSTate \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_pstate(psync_state = False) \n
		No command help available \n
			:param psync_state: No help available
		"""
		param = Conversions.bool_to_str(psync_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:PSTate {param}')

	def get_siq_sequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SIQSequence \n
		Snippet: value: str = driver.source.bb.v5G.downlink.sync.get_siq_sequence() \n
		No command help available \n
			:return: siq_sequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:SIQSequence?')
		return trim_str_response(response)

	def set_siq_sequence(self, siq_sequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SIQSequence \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_siq_sequence(siq_sequence = '1') \n
		No command help available \n
			:param siq_sequence: No help available
		"""
		param = Conversions.value_to_quoted_str(siq_sequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:SIQSequence {param}')

	# noinspection PyTypeChecker
	def get_smodulation(self) -> enums.SyncModulationScheme:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SMODulation \n
		Snippet: value: enums.SyncModulationScheme = driver.source.bb.v5G.downlink.sync.get_smodulation() \n
		No command help available \n
			:return: mod_scheme: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:SMODulation?')
		return Conversions.str_to_scalar_enum(response, enums.SyncModulationScheme)

	def set_smodulation(self, mod_scheme: enums.SyncModulationScheme) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SMODulation \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_smodulation(mod_scheme = enums.SyncModulationScheme.IQFile) \n
		No command help available \n
			:param mod_scheme: No help available
		"""
		param = Conversions.enum_scalar_to_str(mod_scheme, enums.SyncModulationScheme)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:SMODulation {param}')

	def get_spower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SPOWer \n
		Snippet: value: float = driver.source.bb.v5G.downlink.sync.get_spower() \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:return: spower: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:SPOWer?')
		return Conversions.str_to_float(response)

	def set_spower(self, spower: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SPOWer \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_spower(spower = 1.0) \n
		Set the power level of synchronization signal, particularly PSS, SSS and ESS. \n
			:param spower: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(spower)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:SPOWer {param}')

	def get_ssequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SSEQuence \n
		Snippet: value: str = driver.source.bb.v5G.downlink.sync.get_ssequence() \n
		No command help available \n
			:return: ssequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:SSEQuence?')
		return trim_str_response(response)

	def set_ssequence(self, ssequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SSEQuence \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_ssequence(ssequence = '1') \n
		No command help available \n
			:param ssequence: No help available
		"""
		param = Conversions.value_to_quoted_str(ssequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:SSEQuence {param}')

	def get_sstate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SSTate \n
		Snippet: value: bool = driver.source.bb.v5G.downlink.sync.get_sstate() \n
		No command help available \n
			:return: ssync_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:SSTate?')
		return Conversions.str_to_bool(response)

	def set_sstate(self, ssync_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:SSTate \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_sstate(ssync_state = False) \n
		No command help available \n
			:param ssync_state: No help available
		"""
		param = Conversions.bool_to_str(ssync_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:SSTate {param}')

	# noinspection PyTypeChecker
	def get_tx_antenna(self) -> enums.TxAntennaGnss:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:TXANtenna \n
		Snippet: value: enums.TxAntennaGnss = driver.source.bb.v5G.downlink.sync.get_tx_antenna() \n
		No command help available \n
			:return: tx_antenna: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:V5G:DL:SYNC:TXANtenna?')
		return Conversions.str_to_scalar_enum(response, enums.TxAntennaGnss)

	def set_tx_antenna(self, tx_antenna: enums.TxAntennaGnss) -> None:
		"""SCPI: [SOURce<HW>]:BB:V5G:DL:SYNC:TXANtenna \n
		Snippet: driver.source.bb.v5G.downlink.sync.set_tx_antenna(tx_antenna = enums.TxAntennaGnss.ALL) \n
		No command help available \n
			:param tx_antenna: No help available
		"""
		param = Conversions.enum_scalar_to_str(tx_antenna, enums.TxAntennaGnss)
		self._core.io.write(f'SOURce<HwInstance>:BB:V5G:DL:SYNC:TXANtenna {param}')
