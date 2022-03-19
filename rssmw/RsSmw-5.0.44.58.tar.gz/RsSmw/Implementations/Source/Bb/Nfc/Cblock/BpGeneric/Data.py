from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, data: List[str], commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BPGeneric:DATA \n
		Snippet: driver.source.bb.nfc.cblock.bpGeneric.data.set(data = ['raw1', 'raw2', 'raw3'], commandBlock = repcap.CommandBlock.Default) \n
		Sets the data for a standard frame in hexadecimal values. \n
			:param data: integer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.list_to_csv_str(data)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BPGeneric:DATA {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BPGeneric:DATA \n
		Snippet: value: List[str] = driver.source.bb.nfc.cblock.bpGeneric.data.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the data for a standard frame in hexadecimal values. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: data: No help available"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BPGeneric:DATA?')
		return Conversions.str_to_str_list(response)
