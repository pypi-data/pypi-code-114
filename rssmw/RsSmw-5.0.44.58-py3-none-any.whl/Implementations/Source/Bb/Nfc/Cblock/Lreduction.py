from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lreduction:
	"""Lreduction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lreduction", core, parent)

	def set(self, lreduction: enums.NfcLenReduct, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:LREDuction \n
		Snippet: driver.source.bb.nfc.cblock.lreduction.set(lreduction = enums.NfcLenReduct.LR128, commandBlock = repcap.CommandBlock.Default) \n
		Selects the length reduction (LR) . \n
			:param lreduction: LR64| LR128| LR192| LR254
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(lreduction, enums.NfcLenReduct)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:LREDuction {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcLenReduct:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:LREDuction \n
		Snippet: value: enums.NfcLenReduct = driver.source.bb.nfc.cblock.lreduction.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the length reduction (LR) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: lreduction: LR64| LR128| LR192| LR254"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:LREDuction?')
		return Conversions.str_to_scalar_enum(response, enums.NfcLenReduct)
