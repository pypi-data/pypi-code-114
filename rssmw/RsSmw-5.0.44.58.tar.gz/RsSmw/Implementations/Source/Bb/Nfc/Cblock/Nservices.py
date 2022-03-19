from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nservices:
	"""Nservices commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nservices", core, parent)

	def set(self, nservice: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NSERvices \n
		Snippet: driver.source.bb.nfc.cblock.nservices.set(nservice = 1, commandBlock = repcap.CommandBlock.Default) \n
		Sets the number of services. \n
			:param nservice: integer Range: 1 to 16
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(nservice)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NSERvices {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NSERvices \n
		Snippet: value: int = driver.source.bb.nfc.cblock.nservices.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the number of services. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nservice: integer Range: 1 to 16"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NSERvices?')
		return Conversions.str_to_int(response)
