from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bodata:
	"""Bodata commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bodata", core, parent)

	def set(self, bo_frame_data: List[str], commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:BOData \n
		Snippet: driver.source.bb.nfc.cblock.apGeneric.bodata.set(bo_frame_data = ['raw1', 'raw2', 'raw3'], commandBlock = repcap.CommandBlock.Default) \n
		Sets the data for a bit oriented SDD frame. \n
			:param bo_frame_data: integer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.list_to_csv_str(bo_frame_data)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:BOData {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:BOData \n
		Snippet: value: List[str] = driver.source.bb.nfc.cblock.apGeneric.bodata.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the data for a bit oriented SDD frame. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: bo_frame_data: integer"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:BOData?')
		return Conversions.str_to_str_list(response)
