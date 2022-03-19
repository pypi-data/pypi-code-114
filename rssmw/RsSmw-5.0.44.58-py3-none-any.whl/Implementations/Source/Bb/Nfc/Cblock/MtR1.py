from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MtR1:
	"""MtR1 commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtR1", core, parent)

	def set(self, mt_r_1: enums.NfcMinTr1, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:MTR1 \n
		Snippet: driver.source.bb.nfc.cblock.mtR1.set(mt_r_1 = enums.NfcMinTr1.TR10, commandBlock = repcap.CommandBlock.Default) \n
		Sets the minimum value of TR1 supported. \n
			:param mt_r_1: TR10| TR11| TR12
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(mt_r_1, enums.NfcMinTr1)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:MTR1 {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcMinTr1:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:MTR1 \n
		Snippet: value: enums.NfcMinTr1 = driver.source.bb.nfc.cblock.mtR1.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets the minimum value of TR1 supported. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: mt_r_1: TR10| TR11| TR12"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:MTR1?')
		return Conversions.str_to_scalar_enum(response, enums.NfcMinTr1)
