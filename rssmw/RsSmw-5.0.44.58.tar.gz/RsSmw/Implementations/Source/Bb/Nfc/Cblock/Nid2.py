from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nid2:
	"""Nid2 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nid2", core, parent)

	def set(self, nfcid_2: List[str], commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NID2 \n
		Snippet: driver.source.bb.nfc.cblock.nid2.set(nfcid_2 = ['raw1', 'raw2', 'raw3'], commandBlock = repcap.CommandBlock.Default) \n
		Determines the entire value of NFCID2. Is a virtual parameter for SCPI to set the NFCID2 either in NFC-DEP or Type 3 Tag
		mode. \n
			:param nfcid_2: integer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.list_to_csv_str(nfcid_2)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NID2 {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NID2 \n
		Snippet: value: List[str] = driver.source.bb.nfc.cblock.nid2.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the entire value of NFCID2. Is a virtual parameter for SCPI to set the NFCID2 either in NFC-DEP or Type 3 Tag
		mode. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nfcid_2: integer"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NID2?')
		return Conversions.str_to_str_list(response)
