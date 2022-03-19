from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DwSelection:
	"""DwSelection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwSelection", core, parent)

	def set(self, dw_selection: enums.NfcDeselWtx, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DWSelection \n
		Snippet: driver.source.bb.nfc.cblock.dwSelection.set(dw_selection = enums.NfcDeselWtx.DSEL, commandBlock = repcap.CommandBlock.Default) \n
		Selects DESELECT or WTX. \n
			:param dw_selection: DSEL| WTX
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(dw_selection, enums.NfcDeselWtx)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DWSelection {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcDeselWtx:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DWSelection \n
		Snippet: value: enums.NfcDeselWtx = driver.source.bb.nfc.cblock.dwSelection.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects DESELECT or WTX. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: dw_selection: DSEL| WTX"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DWSelection?')
		return Conversions.str_to_scalar_enum(response, enums.NfcDeselWtx)
