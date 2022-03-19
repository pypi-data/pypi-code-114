from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DptListen:
	"""DptListen commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dptListen", core, parent)

	def set(self, dptl: enums.NfcDivisor, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DPTListen \n
		Snippet: driver.source.bb.nfc.cblock.dptListen.set(dptl = enums.NfcDivisor.DIV1, commandBlock = repcap.CommandBlock.Default) \n
		In ATTRIB command, sets the divisor in the corresponding transmission direction. \n
			:param dptl: DIV1| DIV2| DIV4| DIV8
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(dptl, enums.NfcDivisor)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DPTListen {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcDivisor:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DPTListen \n
		Snippet: value: enums.NfcDivisor = driver.source.bb.nfc.cblock.dptListen.get(commandBlock = repcap.CommandBlock.Default) \n
		In ATTRIB command, sets the divisor in the corresponding transmission direction. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: dptl: DIV1| DIV2| DIV4| DIV8"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DPTListen?')
		return Conversions.str_to_scalar_enum(response, enums.NfcDivisor)
