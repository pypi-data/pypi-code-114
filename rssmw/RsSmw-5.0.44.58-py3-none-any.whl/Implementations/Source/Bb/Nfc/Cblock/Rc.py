from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rc:
	"""Rc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rc", core, parent)

	def set(self, rc: enums.NfcRc, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:RC \n
		Snippet: driver.source.bb.nfc.cblock.rc.set(rc = enums.NfcRc.APFS, commandBlock = repcap.CommandBlock.Default) \n
		Indicates the Request Code (RC) . \n
			:param rc: NSCI| SCIR| APFS
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(rc, enums.NfcRc)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:RC {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcRc:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:RC \n
		Snippet: value: enums.NfcRc = driver.source.bb.nfc.cblock.rc.get(commandBlock = repcap.CommandBlock.Default) \n
		Indicates the Request Code (RC) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: rc: NSCI| SCIR| APFS"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:RC?')
		return Conversions.str_to_scalar_enum(response, enums.NfcRc)
