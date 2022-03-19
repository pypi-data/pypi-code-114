from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nfollowing:
	"""Nfollowing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nfollowing", core, parent)

	def set(self, nfollowing: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NFOLlowing \n
		Snippet: driver.source.bb.nfc.cblock.nfollowing.set(nfollowing = False, commandBlock = repcap.CommandBlock.Default) \n
		Determines if NAD is following. \n
			:param nfollowing: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(nfollowing)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NFOLlowing {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NFOLlowing \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.nfollowing.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines if NAD is following. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nfollowing: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NFOLlowing?')
		return Conversions.str_to_bool(response)
