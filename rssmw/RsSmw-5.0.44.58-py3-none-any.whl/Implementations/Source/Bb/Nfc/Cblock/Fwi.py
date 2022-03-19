from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fwi:
	"""Fwi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fwi", core, parent)

	def set(self, fwi: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:FWI \n
		Snippet: driver.source.bb.nfc.cblock.fwi.set(fwi = 1, commandBlock = repcap.CommandBlock.Default) \n
		Determines the FWI which is needed to calculate Frame Waiting Time (FWT) . \n
			:param fwi: integer Range: 1 to 8
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(fwi)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:FWI {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:FWI \n
		Snippet: value: int = driver.source.bb.nfc.cblock.fwi.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the FWI which is needed to calculate Frame Waiting Time (FWT) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: fwi: integer Range: 1 to 8"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:FWI?')
		return Conversions.str_to_int(response)
