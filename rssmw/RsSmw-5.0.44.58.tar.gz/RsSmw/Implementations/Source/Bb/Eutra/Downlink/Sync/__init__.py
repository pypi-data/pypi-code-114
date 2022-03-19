from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 10 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def niot(self):
		"""niot commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_niot'):
			from .Niot import Niot
			self._niot = Niot(self._core, self._cmd_group)
		return self._niot

	def get_ppower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PPOWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.sync.get_ppower() \n
		Sets the power of the primary synchronization signal (P-SYNC) . \n
			:return: ppower: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PPOWer?')
		return Conversions.str_to_float(response)

	def set_ppower(self, ppower: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PPOWer \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_ppower(ppower = 1.0) \n
		Sets the power of the primary synchronization signal (P-SYNC) . \n
			:param ppower: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(ppower)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PPOWer {param}')

	def get_psequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PSEQuence \n
		Snippet: value: str = driver.source.bb.eutra.downlink.sync.get_psequence() \n
		No command help available \n
			:return: psequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PSEQuence?')
		return trim_str_response(response)

	def set_psequence(self, psequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PSEQuence \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_psequence(psequence = '1') \n
		No command help available \n
			:param psequence: No help available
		"""
		param = Conversions.value_to_quoted_str(psequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PSEQuence {param}')

	def get_pstate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PSTate \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.sync.get_pstate() \n
		No command help available \n
			:return: psync_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PSTate?')
		return Conversions.str_to_bool(response)

	def set_pstate(self, psync_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:PSTate \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_pstate(psync_state = False) \n
		No command help available \n
			:param psync_state: No help available
		"""
		param = Conversions.bool_to_str(psync_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:PSTate {param}')

	def get_spower(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SPOWer \n
		Snippet: value: float = driver.source.bb.eutra.downlink.sync.get_spower() \n
		Sets the power of the secondary synchronization signal (S-SYNC) . \n
			:return: spower: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SPOWer?')
		return Conversions.str_to_float(response)

	def set_spower(self, spower: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SPOWer \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_spower(spower = 1.0) \n
		Sets the power of the secondary synchronization signal (S-SYNC) . \n
			:param spower: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(spower)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SPOWer {param}')

	def get_ssequence(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SSEQuence \n
		Snippet: value: str = driver.source.bb.eutra.downlink.sync.get_ssequence() \n
		No command help available \n
			:return: ssequence: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SSEQuence?')
		return trim_str_response(response)

	def set_ssequence(self, ssequence: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SSEQuence \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_ssequence(ssequence = '1') \n
		No command help available \n
			:param ssequence: No help available
		"""
		param = Conversions.value_to_quoted_str(ssequence)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SSEQuence {param}')

	def get_sstate(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SSTate \n
		Snippet: value: bool = driver.source.bb.eutra.downlink.sync.get_sstate() \n
		No command help available \n
			:return: ssync_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SSTate?')
		return Conversions.str_to_bool(response)

	def set_sstate(self, ssync_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:SSTate \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_sstate(ssync_state = False) \n
		No command help available \n
			:param ssync_state: No help available
		"""
		param = Conversions.bool_to_str(ssync_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:SSTate {param}')

	# noinspection PyTypeChecker
	def get_tx_antenna(self) -> enums.TxAntennaGnss:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:TXANtenna \n
		Snippet: value: enums.TxAntennaGnss = driver.source.bb.eutra.downlink.sync.get_tx_antenna() \n
		Defines on which antenna port the P-/S-SYNC is transmitted. The available values depend on the number of configured
		antennas. \n
			:return: tx_antenna: NONE| ANT1| ANT2| ANT3| ANT4| ALL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:TXANtenna?')
		return Conversions.str_to_scalar_enum(response, enums.TxAntennaGnss)

	def set_tx_antenna(self, tx_antenna: enums.TxAntennaGnss) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:TXANtenna \n
		Snippet: driver.source.bb.eutra.downlink.sync.set_tx_antenna(tx_antenna = enums.TxAntennaGnss.ALL) \n
		Defines on which antenna port the P-/S-SYNC is transmitted. The available values depend on the number of configured
		antennas. \n
			:param tx_antenna: NONE| ANT1| ANT2| ANT3| ANT4| ALL
		"""
		param = Conversions.enum_scalar_to_str(tx_antenna, enums.TxAntennaGnss)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:TXANtenna {param}')

	def clone(self) -> 'Sync':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sync(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
