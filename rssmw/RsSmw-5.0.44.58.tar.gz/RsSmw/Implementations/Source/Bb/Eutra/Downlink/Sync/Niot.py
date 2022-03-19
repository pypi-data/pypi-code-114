from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Niot:
	"""Niot commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("niot", core, parent)

	def get_nppwr(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:NPPWr \n
		Snippet: value: float = driver.source.bb.eutra.downlink.sync.niot.get_nppwr() \n
		Sets the power of the NPSS/NSSS allocations. \n
			:return: np_sync_power: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:NPPWr?')
		return Conversions.str_to_float(response)

	def set_nppwr(self, np_sync_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:NPPWr \n
		Snippet: driver.source.bb.eutra.downlink.sync.niot.set_nppwr(np_sync_power = 1.0) \n
		Sets the power of the NPSS/NSSS allocations. \n
			:param np_sync_power: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(np_sync_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:NPPWr {param}')

	def get_ns_pwr(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:NSPWr \n
		Snippet: value: float = driver.source.bb.eutra.downlink.sync.niot.get_ns_pwr() \n
		Sets the power of the NPSS/NSSS allocations. \n
			:return: ns_sync_power: float Range: -80 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:NSPWr?')
		return Conversions.str_to_float(response)

	def set_ns_pwr(self, ns_sync_power: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:NSPWr \n
		Snippet: driver.source.bb.eutra.downlink.sync.niot.set_ns_pwr(ns_sync_power = 1.0) \n
		Sets the power of the NPSS/NSSS allocations. \n
			:param ns_sync_power: float Range: -80 to 10
		"""
		param = Conversions.decimal_value_to_str(ns_sync_power)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:NSPWr {param}')

	# noinspection PyTypeChecker
	def get_tx_antenna(self) -> enums.EutraNbiotSimAnt:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:TXANtenna \n
		Snippet: value: enums.EutraNbiotSimAnt = driver.source.bb.eutra.downlink.sync.niot.get_tx_antenna() \n
		Defines on which antenna the NPSS/NSSS are transmitted. \n
			:return: np_ns_sync_tx_ant: NONE| ANT1| ANT2| ALL
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:TXANtenna?')
		return Conversions.str_to_scalar_enum(response, enums.EutraNbiotSimAnt)

	def set_tx_antenna(self, np_ns_sync_tx_ant: enums.EutraNbiotSimAnt) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:SYNC:NIOT:TXANtenna \n
		Snippet: driver.source.bb.eutra.downlink.sync.niot.set_tx_antenna(np_ns_sync_tx_ant = enums.EutraNbiotSimAnt.ALL) \n
		Defines on which antenna the NPSS/NSSS are transmitted. \n
			:param np_ns_sync_tx_ant: NONE| ANT1| ANT2| ALL
		"""
		param = Conversions.enum_scalar_to_str(np_ns_sync_tx_ant, enums.EutraNbiotSimAnt)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:SYNC:NIOT:TXANtenna {param}')
