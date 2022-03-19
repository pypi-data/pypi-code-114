from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IbNumber:
	"""IbNumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ibNumber", core, parent)

	def set(self, ib_number: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:IBNumber \n
		Snippet: driver.source.bb.nfc.cblock.ibNumber.set(ib_number = False, commandBlock = repcap.CommandBlock.Default) \n
		Indicates if a Valid I-block or a Valid R(ACK) block is received. \n
			:param ib_number: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(ib_number)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:IBNumber {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:IBNumber \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.ibNumber.get(commandBlock = repcap.CommandBlock.Default) \n
		Indicates if a Valid I-block or a Valid R(ACK) block is received. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: ib_number: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:IBNumber?')
		return Conversions.str_to_bool(response)
