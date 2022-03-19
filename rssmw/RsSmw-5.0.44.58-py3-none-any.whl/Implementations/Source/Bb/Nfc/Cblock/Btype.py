from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Btype:
	"""Btype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("btype", core, parent)

	def set(self, btype: enums.NfcBlockType, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BTYPe \n
		Snippet: driver.source.bb.nfc.cblock.btype.set(btype = enums.NfcBlockType.TPI, commandBlock = repcap.CommandBlock.Default) \n
		Selects the block type to be sent. \n
			:param btype: TPI| TPR| TPS
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(btype, enums.NfcBlockType)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcBlockType:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BTYPe \n
		Snippet: value: enums.NfcBlockType = driver.source.bb.nfc.cblock.btype.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the block type to be sent. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: btype: TPI| TPR| TPS"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.NfcBlockType)
