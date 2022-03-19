from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StePresent:
	"""StePresent commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stePresent", core, parent)

	def set(self, std_frame_eod_pres: bool, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:STEPresent \n
		Snippet: driver.source.bb.nfc.cblock.apGeneric.stePresent.set(std_frame_eod_pres = False, commandBlock = repcap.CommandBlock.Default) \n
		Selects if the EoD is present or not. \n
			:param std_frame_eod_pres: 1| ON| 0| OFF
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.bool_to_str(std_frame_eod_pres)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:STEPresent {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:APGeneric:STEPresent \n
		Snippet: value: bool = driver.source.bb.nfc.cblock.apGeneric.stePresent.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects if the EoD is present or not. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: std_frame_eod_pres: 1| ON| 0| OFF"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:APGeneric:STEPresent?')
		return Conversions.str_to_bool(response)
