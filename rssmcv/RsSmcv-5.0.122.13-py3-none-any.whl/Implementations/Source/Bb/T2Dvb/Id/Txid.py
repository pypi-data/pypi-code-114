from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Txid:
	"""Txid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txid", core, parent)

	def get_avail(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:TXID:AVAil \n
		Snippet: value: int = driver.source.bb.t2Dvb.id.txid.get_avail() \n
		Queries if transmitter identification signals are available within the current geographic cell. \n
			:return: avail: integer 8-bit value in hexadecimal representation. Range: #H0 to #HFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:T2DVb:ID:TXID:AVAil?')
		return Conversions.str_to_int(response)

	def set_avail(self, avail: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:T2DVb:ID:TXID:AVAil \n
		Snippet: driver.source.bb.t2Dvb.id.txid.set_avail(avail = 1) \n
		Queries if transmitter identification signals are available within the current geographic cell. \n
			:param avail: integer 8-bit value in hexadecimal representation. Range: #H0 to #HFF
		"""
		param = Conversions.decimal_value_to_str(avail)
		self._core.io.write(f'SOURce<HwInstance>:BB:T2DVb:ID:TXID:AVAil {param}')
