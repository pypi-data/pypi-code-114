from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plin:
	"""Plin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plin", core, parent)

	def set(self, pl_indication: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PLIN \n
		Snippet: driver.source.bb.nfc.cblock.plin.set(pl_indication = 1, commandBlock = repcap.CommandBlock.Default) \n
		Only used when DESELCT/WTX is set to WTX. Determines Power Level Indication. \n
			:param pl_indication: integer Range: 0 to 3
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(pl_indication)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PLIN {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PLIN \n
		Snippet: value: int = driver.source.bb.nfc.cblock.plin.get(commandBlock = repcap.CommandBlock.Default) \n
		Only used when DESELCT/WTX is set to WTX. Determines Power Level Indication. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: pl_indication: integer Range: 0 to 3"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PLIN?')
		return Conversions.str_to_int(response)
