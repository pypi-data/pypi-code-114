from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Len:
	"""Len commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("len", core, parent)

	def set(self, bl_length: enums.NfcLength, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:LEN \n
		Snippet: driver.source.bb.nfc.cblock.block.len.set(bl_length = enums.NfcLength.LEN2, commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Sets the block length. \n
			:param bl_length: LEN2| LEN3
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
		"""
		param = Conversions.enum_scalar_to_str(bl_length, enums.NfcLength)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:LEN {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> enums.NfcLength:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:LEN \n
		Snippet: value: enums.NfcLength = driver.source.bb.nfc.cblock.block.len.get(commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Sets the block length. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
			:return: bl_length: LEN2| LEN3"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:LEN?')
		return Conversions.str_to_scalar_enum(response, enums.NfcLength)
