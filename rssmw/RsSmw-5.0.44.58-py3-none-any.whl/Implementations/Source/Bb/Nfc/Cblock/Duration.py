from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, duration: float, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DURation \n
		Snippet: driver.source.bb.nfc.cblock.duration.set(duration = 1.0, commandBlock = repcap.CommandBlock.Default) \n
		Determines the frame period in µs. \n
			:param duration: float Range: 0 to 1E6
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(duration)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DURation {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DURation \n
		Snippet: value: float = driver.source.bb.nfc.cblock.duration.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the frame period in µs. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: duration: float Range: 0 to 1E6"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DURation?')
		return Conversions.str_to_float(response)
