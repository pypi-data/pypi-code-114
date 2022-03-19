from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AnSelection:
	"""AnSelection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anSelection", core, parent)

	def set(self, an_selection: enums.NfcAckNack, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ANSelection \n
		Snippet: driver.source.bb.nfc.cblock.anSelection.set(an_selection = enums.NfcAckNack.ACK, commandBlock = repcap.CommandBlock.Default) \n
		Available only for 'PDU Type > ACK-NACK' or 'Block Type > R-block'. Selects ACK or NACK. \n
			:param an_selection: ACK| NACK
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(an_selection, enums.NfcAckNack)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ANSelection {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcAckNack:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ANSelection \n
		Snippet: value: enums.NfcAckNack = driver.source.bb.nfc.cblock.anSelection.get(commandBlock = repcap.CommandBlock.Default) \n
		Available only for 'PDU Type > ACK-NACK' or 'Block Type > R-block'. Selects ACK or NACK. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: an_selection: ACK| NACK"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ANSelection?')
		return Conversions.str_to_scalar_enum(response, enums.NfcAckNack)
