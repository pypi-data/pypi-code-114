from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bno:
	"""Bno commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bno", core, parent)

	def set(self, bno: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BNO \n
		Snippet: driver.source.bb.nfc.cblock.bno.set(bno = 1, commandBlock = repcap.CommandBlock.Default) \n
		Selects the block number to be read/write. \n
			:param bno: integer Range: 0 to 255
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(bno)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BNO {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BNO \n
		Snippet: value: int = driver.source.bb.nfc.cblock.bno.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the block number to be read/write. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: bno: integer Range: 0 to 255"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BNO?')
		return Conversions.str_to_int(response)
