from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PduType:
	"""PduType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pduType", core, parent)

	def set(self, pfb_type: enums.NfcPfbType, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PDUType \n
		Snippet: driver.source.bb.nfc.cblock.pduType.set(pfb_type = enums.NfcPfbType.ANACk, commandBlock = repcap.CommandBlock.Default) \n
		Selects the type of PDU. \n
			:param pfb_type: INFO| ANACk| SUPer
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(pfb_type, enums.NfcPfbType)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PDUType {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcPfbType:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:PDUType \n
		Snippet: value: enums.NfcPfbType = driver.source.bb.nfc.cblock.pduType.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the type of PDU. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: pfb_type: No help available"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:PDUType?')
		return Conversions.str_to_scalar_enum(response, enums.NfcPfbType)
