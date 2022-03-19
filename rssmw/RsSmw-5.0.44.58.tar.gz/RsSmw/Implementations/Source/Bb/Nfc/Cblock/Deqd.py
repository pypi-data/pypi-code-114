from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Deqd:
	"""Deqd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deqd", core, parent)

	def set(self, div_eq_div: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DEQD \n
		Snippet: driver.source.bb.nfc.cblock.deqd.set(div_eq_div = False, commandBlock = repcap.CommandBlock.Default) \n
		Determines if the same bit rate divisor for both directions is supported. \n
			:param div_eq_div: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(div_eq_div)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DEQD {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DEQD \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.deqd.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines if the same bit rate divisor for both directions is supported. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: div_eq_div: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DEQD?')
		return Conversions.str_to_bool(response)
