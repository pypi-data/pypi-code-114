from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SenRequired:
	"""SenRequired commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("senRequired", core, parent)

	def set(self, sen_required: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SENRequired \n
		Snippet: driver.source.bb.nfc.cblock.senRequired.set(sen_required = False, commandBlock = repcap.CommandBlock.Default) \n
		Determines whether a suppression of EoS (End of Sequence) /SoS (Start of Sequence) is required or not. \n
			:param sen_required: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(sen_required)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SENRequired {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SENRequired \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.senRequired.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines whether a suppression of EoS (End of Sequence) /SoS (Start of Sequence) is required or not. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: sen_required: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SENRequired?')
		return Conversions.str_to_bool(response)
