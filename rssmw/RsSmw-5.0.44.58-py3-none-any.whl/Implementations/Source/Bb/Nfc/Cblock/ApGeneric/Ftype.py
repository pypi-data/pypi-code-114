from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ftype:
	"""Ftype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ftype", core, parent)

	def set(self, frame_type: enums.NfcApgEnericFrameType, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:FTYPe \n
		Snippet: driver.source.bb.nfc.cblock.apGeneric.ftype.set(frame_type = enums.NfcApgEnericFrameType.BOSDd, commandBlock = repcap.CommandBlock.Default) \n
		Selects a frame type for 'Command Type > GENERIC'. \n
			:param frame_type: SHORt| STANdard| BOSDd
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(frame_type, enums.NfcApgEnericFrameType)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:FTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcApgEnericFrameType:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:FTYPe \n
		Snippet: value: enums.NfcApgEnericFrameType = driver.source.bb.nfc.cblock.apGeneric.ftype.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects a frame type for 'Command Type > GENERIC'. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: frame_type: SHORt| STANdard| BOSDd"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:FTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.NfcApgEnericFrameType)
