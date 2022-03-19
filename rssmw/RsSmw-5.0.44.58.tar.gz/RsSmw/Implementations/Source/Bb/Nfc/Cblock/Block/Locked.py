from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Locked:
	"""Locked commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("locked", core, parent)

	def set(self, lcontrol: bool, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:LOCKed \n
		Snippet: driver.source.bb.nfc.cblock.block.locked.set(lcontrol = False, commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Enables/disables status information on lock for the corresponding block ('BLOCK-1' to 'BLOCK-C') . \n
			:param lcontrol: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
		"""
		param = Conversions.bool_to_str(lcontrol)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:LOCKed {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:LOCKed \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.block.locked.get(commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Enables/disables status information on lock for the corresponding block ('BLOCK-1' to 'BLOCK-C') . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
			:return: lcontrol: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:LOCKed?')
		return Conversions.str_to_bool(response)
