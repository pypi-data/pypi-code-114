from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlp4:
	"""Dlp4 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlp4", core, parent)

	def set(self, ta_dlp_4: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DLP4 \n
		Snippet: driver.source.bb.nfc.cblock.dlp4.set(ta_dlp_4 = False, commandBlock = repcap.CommandBlock.Default) \n
		Enables support of divisor 4 for LISTEN to POLL (Bit Rate Capability) . \n
			:param ta_dlp_4: OFF| ON| 1| 0
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(ta_dlp_4)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DLP4 {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DLP4 \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.dlp4.get(commandBlock = repcap.CommandBlock.Default) \n
		Enables support of divisor 4 for LISTEN to POLL (Bit Rate Capability) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: ta_dlp_4: OFF| ON| 1| 0"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DLP4?')
		return Conversions.str_to_bool(response)
