from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wtxm:
	"""Wtxm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wtxm", core, parent)

	def set(self, wtxm: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:WTXM \n
		Snippet: driver.source.bb.nfc.cblock.wtxm.set(wtxm = 1, commandBlock = repcap.CommandBlock.Default) \n
		Determines the WTXM. - Only used when DESELCT/WTX is set to WTX. \n
			:param wtxm: integer Range: 1 to 59
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(wtxm)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:WTXM {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:WTXM \n
		Snippet: value: int = driver.source.bb.nfc.cblock.wtxm.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the WTXM. - Only used when DESELCT/WTX is set to WTX. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: wtxm: integer Range: 1 to 59"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:WTXM?')
		return Conversions.str_to_int(response)
