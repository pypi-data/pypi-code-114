from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nack:
	"""Nack commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nack", core, parent)

	def set(self, nack: enums.NfcNack, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NACK \n
		Snippet: driver.source.bb.nfc.cblock.nack.set(nack = enums.NfcNack.NCK0, commandBlock = repcap.CommandBlock.Default) \n
		Determines the value of NACK. \n
			:param nack: NCK1| NCK0| NCK4| NCK5
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(nack, enums.NfcNack)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NACK {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcNack:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NACK \n
		Snippet: value: enums.NfcNack = driver.source.bb.nfc.cblock.nack.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the value of NACK. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nack: NCK1| NCK0| NCK4| NCK5"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NACK?')
		return Conversions.str_to_scalar_enum(response, enums.NfcNack)
