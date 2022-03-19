from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Miso:
	"""Miso commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("miso", core, parent)

	def get_idx(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:MISo:IDX \n
		Snippet: value: int = driver.source.bb.a3Tsc.miso.get_idx() \n
		Sets the transmitter index for transmission. \n
			:return: transmitter_idx: integer Range: 1 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:MISo:IDX?')
		return Conversions.str_to_int(response)

	def set_idx(self, transmitter_idx: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:MISo:IDX \n
		Snippet: driver.source.bb.a3Tsc.miso.set_idx(transmitter_idx = 1) \n
		Sets the transmitter index for transmission. \n
			:param transmitter_idx: integer Range: 1 to 4
		"""
		param = Conversions.decimal_value_to_str(transmitter_idx)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:MISo:IDX {param}')

	def get_ntx(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:MISo:NTX \n
		Snippet: value: int = driver.source.bb.a3Tsc.miso.get_ntx() \n
		Sets the number of transmitters for transmission. \n
			:return: num_transmitters: integer Range: 2 to 4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:A3TSc:MISo:NTX?')
		return Conversions.str_to_int(response)

	def set_ntx(self, num_transmitters: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:MISo:NTX \n
		Snippet: driver.source.bb.a3Tsc.miso.set_ntx(num_transmitters = 1) \n
		Sets the number of transmitters for transmission. \n
			:param num_transmitters: integer Range: 2 to 4
		"""
		param = Conversions.decimal_value_to_str(num_transmitters)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:MISo:NTX {param}')
