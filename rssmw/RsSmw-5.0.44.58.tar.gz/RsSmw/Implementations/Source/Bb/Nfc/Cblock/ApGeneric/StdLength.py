from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StdLength:
	"""StdLength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stdLength", core, parent)

	def get(self, std_frame_data_len: int, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:STDLength \n
		Snippet: value: int = driver.source.bb.nfc.cblock.apGeneric.stdLength.get(std_frame_data_len = 1, commandBlock = repcap.CommandBlock.Default) \n
		Shows the total length of a standard frame in bytes. \n
			:param std_frame_data_len: integer Range: 1 to 10
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: std_frame_data_len: integer Range: 1 to 10"""
		param = Conversions.decimal_value_to_str(std_frame_data_len)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:STDLength? {param}')
		return Conversions.str_to_int(response)
