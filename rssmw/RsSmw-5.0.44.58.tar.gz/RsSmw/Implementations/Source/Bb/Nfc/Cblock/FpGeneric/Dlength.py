from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dlength:
	"""Dlength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dlength", core, parent)

	def get(self, data_length: int, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:FPGeneric:DLENgth \n
		Snippet: value: int = driver.source.bb.nfc.cblock.fpGeneric.dlength.get(data_length = 1, commandBlock = repcap.CommandBlock.Default) \n
		Shows the total length of a standard frame in bytes. \n
			:param data_length: integer Range: 1 to 10
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: data_length: No help available"""
		param = Conversions.decimal_value_to_str(data_length)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:FPGeneric:DLENgth? {param}')
		return Conversions.str_to_int(response)
