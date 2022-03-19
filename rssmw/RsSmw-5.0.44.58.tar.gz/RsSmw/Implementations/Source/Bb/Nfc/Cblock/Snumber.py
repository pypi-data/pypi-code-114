from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snumber:
	"""Snumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def set(self, snumber: enums.NfcSlotNumber, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SNUMber \n
		Snippet: driver.source.bb.nfc.cblock.snumber.set(snumber = enums.NfcSlotNumber.SN10, commandBlock = repcap.CommandBlock.Default) \n
		Determines the slot number. \n
			:param snumber: SN2| SN3| SN4| SN5| SN6| SN7| SN8| SN9| SN10| SN11| SN12| SN13| SN14| SN15| SN16
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(snumber, enums.NfcSlotNumber)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SNUMber {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcSlotNumber:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SNUMber \n
		Snippet: value: enums.NfcSlotNumber = driver.source.bb.nfc.cblock.snumber.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the slot number. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: snumber: SN2| SN3| SN4| SN5| SN6| SN7| SN8| SN9| SN10| SN11| SN12| SN13| SN14| SN15| SN16"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SNUMber?')
		return Conversions.str_to_scalar_enum(response, enums.NfcSlotNumber)
