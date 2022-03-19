from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BoLength:
	"""BoLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("boLength", core, parent)

	def set(self, bo_frame_len: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:BOLength \n
		Snippet: driver.source.bb.nfc.cblock.apGeneric.boLength.set(bo_frame_len = 1, commandBlock = repcap.CommandBlock.Default) \n
		Sets the length of the first part of a bit oriented SDD frame. \n
			:param bo_frame_len: integer Range: 16 to 55
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(bo_frame_len)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:BOLength {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:BOLength \n
		Snippet: value: int = driver.source.bb.nfc.cblock.apGeneric.boLength.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the length of the first part of a bit oriented SDD frame. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: bo_frame_len: integer Range: 16 to 55"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:BOLength?')
		return Conversions.str_to_int(response)
