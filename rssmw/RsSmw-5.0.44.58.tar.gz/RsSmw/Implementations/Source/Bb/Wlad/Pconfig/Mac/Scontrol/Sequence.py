from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	def get_increment(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:INCRement \n
		Snippet: value: int = driver.source.bb.wlad.pconfig.mac.scontrol.sequence.get_increment() \n
		Sets the number of packets required to increment the counter of the sequence bits of the sequence control. \n
			:return: increment: integer Range: 0 to 1024
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:INCRement?')
		return Conversions.str_to_int(response)

	def set_increment(self, increment: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:INCRement \n
		Snippet: driver.source.bb.wlad.pconfig.mac.scontrol.sequence.set_increment(increment = 1) \n
		Sets the number of packets required to increment the counter of the sequence bits of the sequence control. \n
			:param increment: integer Range: 0 to 1024
		"""
		param = Conversions.decimal_value_to_str(increment)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:INCRement {param}')

	def get_start(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:STARt \n
		Snippet: value: List[str] = driver.source.bb.wlad.pconfig.mac.scontrol.sequence.get_start() \n
		Sets the start number of the fragment bits of the sequence control. \n
			:return: start: 12 bits
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:STARt?')
		return Conversions.str_to_str_list(response)

	def set_start(self, start: List[str]) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:STARt \n
		Snippet: driver.source.bb.wlad.pconfig.mac.scontrol.sequence.set_start(start = ['raw1', 'raw2', 'raw3']) \n
		Sets the start number of the fragment bits of the sequence control. \n
			:param start: 12 bits
		"""
		param = Conversions.list_to_csv_str(start)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:SCONtrol:SEQuence:STARt {param}')
