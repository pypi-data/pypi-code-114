from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bnumber:
	"""Bnumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bnumber", core, parent)

	def set(self, bnumber: int, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:BNUMber \n
		Snippet: driver.source.bb.nfc.cblock.block.bnumber.set(bnumber = 1, commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Sets the block number in the block list. \n
			:param bnumber: integer Range: 0 to depends on block list length
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
		"""
		param = Conversions.decimal_value_to_str(bnumber)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:BNUMber {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default, fmBlock=repcap.FmBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BLOCk<ST>:BNUMber \n
		Snippet: value: int = driver.source.bb.nfc.cblock.block.bnumber.get(commandBlock = repcap.CommandBlock.Default, fmBlock = repcap.FmBlock.Default) \n
		Sets the block number in the block list. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param fmBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Block')
			:return: bnumber: integer Range: 0 to depends on block list length"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		fmBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(fmBlock, repcap.FmBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BLOCk{fmBlock_cmd_val}:BNUMber?')
		return Conversions.str_to_int(response)
