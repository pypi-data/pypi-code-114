from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpUpper:
	"""SpUpper commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spUpper", core, parent)

	def set(self, sp_upper: int, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SPUPper \n
		Snippet: driver.source.bb.nfc.cblock.spUpper.set(sp_upper = 1, commandBlock = repcap.CommandBlock.Default) \n
		SEL_PAR_UPPER determines the number of full bytes of the SDD_REQ part. \n
			:param sp_upper: integer Range: 2 to 6
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.decimal_value_to_str(sp_upper)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SPUPper {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SPUPper \n
		Snippet: value: int = driver.source.bb.nfc.cblock.spUpper.get(commandBlock = repcap.CommandBlock.Default) \n
		SEL_PAR_UPPER determines the number of full bytes of the SDD_REQ part. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: sp_upper: integer Range: 2 to 6"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SPUPper?')
		return Conversions.str_to_int(response)
