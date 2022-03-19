from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fsc:
	"""Fsc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fsc", core, parent)

	def set(self, fsc: enums.NfcFsc, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:FSC \n
		Snippet: driver.source.bb.nfc.cblock.fsc.set(fsc = enums.NfcFsc.F128, commandBlock = repcap.CommandBlock.Default) \n
		Selects the maximum frame size in bytes. \n
			:param fsc: F16| F24| F32| F40| F48| F64| F96| F128| F256
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(fsc, enums.NfcFsc)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:FSC {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcFsc:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:FSC \n
		Snippet: value: enums.NfcFsc = driver.source.bb.nfc.cblock.fsc.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the maximum frame size in bytes. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: fsc: F16| F24| F32| F40| F48| F64| F96| F128| F256"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:FSC?')
		return Conversions.str_to_scalar_enum(response, enums.NfcFsc)
