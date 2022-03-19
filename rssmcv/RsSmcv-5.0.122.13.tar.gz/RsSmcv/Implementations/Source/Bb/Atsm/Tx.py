from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tx:
	"""Tx commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tx", core, parent)

	def get_address(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TX:ADDRess \n
		Snippet: value: int = driver.source.bb.atsm.tx.get_address() \n
		Sets the TX address that underlays the RF signal as a watermark. \n
			:return: tx_addr: integer Range: 0 to 4095
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ATSM:TX:ADDRess?')
		return Conversions.str_to_int(response)

	def set_address(self, tx_addr: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ATSM:TX:ADDRess \n
		Snippet: driver.source.bb.atsm.tx.set_address(tx_addr = 1) \n
		Sets the TX address that underlays the RF signal as a watermark. \n
			:param tx_addr: integer Range: 0 to 4095
		"""
		param = Conversions.decimal_value_to_str(tx_addr)
		self._core.io.write(f'SOURce<HwInstance>:BB:ATSM:TX:ADDRess {param}')
