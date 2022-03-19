from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aid:
	"""Aid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aid", core, parent)

	def set(self, aid: List[str], commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:AID \n
		Snippet: driver.source.bb.nfc.cblock.aid.set(aid = ['raw1', 'raw2', 'raw3'], commandBlock = repcap.CommandBlock.Default) \n
		Determines the value of AID. \n
			:param aid: integer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.list_to_csv_str(aid)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:AID {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:AID \n
		Snippet: value: List[str] = driver.source.bb.nfc.cblock.aid.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the value of AID. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: aid: integer"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:AID?')
		return Conversions.str_to_str_list(response)
