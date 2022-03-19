from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class T1Tconfigured:
	"""T1Tconfigured commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("t1Tconfigured", core, parent)

	def set(self, t_1_tp_configured: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:T1TConfigured \n
		Snippet: driver.source.bb.nfc.cblock.t1Tconfigured.set(t_1_tp_configured = False, commandBlock = repcap.CommandBlock.Default) \n
		Determines whether Type 1 Tag platform is configured or not. \n
			:param t_1_tp_configured: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(t_1_tp_configured)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:T1TConfigured {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:T1TConfigured \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.t1Tconfigured.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines whether Type 1 Tag platform is configured or not. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: t_1_tp_configured: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:T1TConfigured?')
		return Conversions.str_to_bool(response)
