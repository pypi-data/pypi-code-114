from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, offset: float, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:POFFset \n
		Snippet: driver.source.bb.nfc.cblock.poffset.set(offset = 1.0, commandBlock = repcap.CommandBlock.Default) \n
		Determines the power offset value in dB. \n
			:param offset: float Range: -20 to 20
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(offset)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:POFFset {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:POFFset \n
		Snippet: value: float = driver.source.bb.nfc.cblock.poffset.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the power offset value in dB. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: offset: float Range: -20 to 20"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
