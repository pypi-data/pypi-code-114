from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Eupd:
	"""Eupd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eupd", core, parent)

	def set(self, eupdate: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:EUPD \n
		Snippet: driver.source.bb.nfc.cblock.eupd.set(eupdate = 1, commandBlock = repcap.CommandBlock.Default) \n
		Determines the format and value of the Maximum Response Time Information MRTICHECK and MRTIUPDATE. \n
			:param eupdate: integer Range: 0 to 3
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(eupdate)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:EUPD {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:EUPD \n
		Snippet: value: int = driver.source.bb.nfc.cblock.eupd.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the format and value of the Maximum Response Time Information MRTICHECK and MRTIUPDATE. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: eupdate: integer Range: 0 to 3"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:EUPD?')
		return Conversions.str_to_int(response)
