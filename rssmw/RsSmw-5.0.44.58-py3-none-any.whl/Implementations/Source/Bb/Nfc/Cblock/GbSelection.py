from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GbSelection:
	"""GbSelection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gbSelection", core, parent)

	def set(self, gb_selection: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:GBSelection \n
		Snippet: driver.source.bb.nfc.cblock.gbSelection.set(gb_selection = 1, commandBlock = repcap.CommandBlock.Default) \n
		Selects 8-byte block to be read/written. \n
			:param gb_selection: integer Range: 0 to 255
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(gb_selection)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:GBSelection {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:GBSelection \n
		Snippet: value: int = driver.source.bb.nfc.cblock.gbSelection.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects 8-byte block to be read/written. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: gb_selection: integer Range: 0 to 255"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:GBSelection?')
		return Conversions.str_to_int(response)
