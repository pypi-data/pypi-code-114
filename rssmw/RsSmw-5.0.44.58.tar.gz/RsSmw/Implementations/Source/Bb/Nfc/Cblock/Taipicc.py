from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Taipicc:
	"""Taipicc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("taipicc", core, parent)

	def set(self, tnai_picc: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:TAIPicc \n
		Snippet: driver.source.bb.nfc.cblock.taipicc.set(tnai_picc = 1, commandBlock = repcap.CommandBlock.Default) \n
		Sets the total number of applications in the PICC (Proximity Inductive Coupling Card) , i.e. in the NFC Forum Device in
		listener mode. \n
			:param tnai_picc: integer Range: 0 to 15
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(tnai_picc)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:TAIPicc {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:TAIPicc \n
		Snippet: value: int = driver.source.bb.nfc.cblock.taipicc.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the total number of applications in the PICC (Proximity Inductive Coupling Card) , i.e. in the NFC Forum Device in
		listener mode. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: tnai_picc: integer Range: 0 to 15"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:TAIPicc?')
		return Conversions.str_to_int(response)
