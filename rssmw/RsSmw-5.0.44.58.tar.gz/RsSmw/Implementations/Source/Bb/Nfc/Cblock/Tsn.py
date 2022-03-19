from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsn:
	"""Tsn commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsn", core, parent)

	def set(self, tsn: enums.NfcTsn, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:TSN \n
		Snippet: driver.source.bb.nfc.cblock.tsn.set(tsn = enums.NfcTsn.TSN1, commandBlock = repcap.CommandBlock.Default) \n
		Indicates the TSN (Time Slot Number) . \n
			:param tsn: TSN1| TSN2| TSN4| TSN8| TSN16
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(tsn, enums.NfcTsn)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:TSN {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcTsn:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:TSN \n
		Snippet: value: enums.NfcTsn = driver.source.bb.nfc.cblock.tsn.get(commandBlock = repcap.CommandBlock.Default) \n
		Indicates the TSN (Time Slot Number) . \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: tsn: TSN1| TSN2| TSN4| TSN8| TSN16"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:TSN?')
		return Conversions.str_to_scalar_enum(response, enums.NfcTsn)
