from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtxId:
	"""MtxId commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtxId", core, parent)

	def get_mid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MTXid:MID \n
		Snippet: value: int = driver.source.bb.atsm.mtxId.get_mid() \n
		Sets the market ID for the transmission. \n
			:return: market_id: integer Range: 0 to 511
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:MTXid:MID?')
		return Conversions.str_to_int(response)

	def set_mid(self, market_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MTXid:MID \n
		Snippet: driver.source.bb.atsm.mtxId.set_mid(market_id = 1) \n
		Sets the market ID for the transmission. \n
			:param market_id: integer Range: 0 to 511
		"""
		param = Conversions.decimal_value_to_str(market_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:MTXid:MID {param}')

	def get_tid(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MTXid:TID \n
		Snippet: value: int = driver.source.bb.atsm.mtxId.get_tid() \n
		Sets the transmitter ID for the MTXID transmission. \n
			:return: transmitter_id: integer Range: 0 to 31
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:MTXid:TID?')
		return Conversions.str_to_int(response)

	def set_tid(self, transmitter_id: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:MTXid:TID \n
		Snippet: driver.source.bb.atsm.mtxId.set_tid(transmitter_id = 1) \n
		Sets the transmitter ID for the MTXID transmission. \n
			:param transmitter_id: integer Range: 0 to 31
		"""
		param = Conversions.decimal_value_to_str(transmitter_id)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:MTXid:TID {param}')
