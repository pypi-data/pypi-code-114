from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoSlots:
	"""NoSlots commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noSlots", core, parent)

	def set(self, no_slots: enums.NfcNumOfSlots, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NOSLots \n
		Snippet: driver.source.bb.nfc.cblock.noSlots.set(no_slots = enums.NfcNumOfSlots.S1, commandBlock = repcap.CommandBlock.Default) \n
		Determines the number of slots. \n
			:param no_slots: S1| S2| S4| S8| S16
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(no_slots, enums.NfcNumOfSlots)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NOSLots {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcNumOfSlots:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NOSLots \n
		Snippet: value: enums.NfcNumOfSlots = driver.source.bb.nfc.cblock.noSlots.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the number of slots. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: no_slots: S1| S2| S4| S8| S16"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NOSLots?')
		return Conversions.str_to_scalar_enum(response, enums.NfcNumOfSlots)
