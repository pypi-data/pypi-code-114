from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plength:
	"""Plength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	def set(self, payload_length: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BPGeneric:PLENgth \n
		Snippet: driver.source.bb.nfc.cblock.bpGeneric.plength.set(payload_length = 1, commandBlock = repcap.CommandBlock.Default) \n
		Sets the length of a standard frame. \n
			:param payload_length: integer Range: 1 to 8
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(payload_length)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BPGeneric:PLENgth {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BPGeneric:PLENgth \n
		Snippet: value: int = driver.source.bb.nfc.cblock.bpGeneric.plength.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the length of a standard frame. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: payload_length: No help available"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BPGeneric:PLENgth?')
		return Conversions.str_to_int(response)
