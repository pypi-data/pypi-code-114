from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pad2:
	"""Pad2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pad2", core, parent)

	def set(self, pad_2: List[str], commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PAD2 \n
		Snippet: driver.source.bb.nfc.cblock.pad2.set(pad_2 = ['raw1', 'raw2', 'raw3'], commandBlock = repcap.CommandBlock.Default) \n
		Sets the value of PAD0/PAD1/PAD2 (hex) . \n
			:param pad_2: integer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.list_to_csv_str(pad_2)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PAD2 {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PAD2 \n
		Snippet: value: List[str] = driver.source.bb.nfc.cblock.pad2.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the value of PAD0/PAD1/PAD2 (hex) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: pad_2: integer"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PAD2?')
		return Conversions.str_to_str_list(response)
