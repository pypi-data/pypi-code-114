from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scmd:
	"""Scmd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scmd", core, parent)

	def set(self, scmd: enums.NfcSelCmd, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SCMD \n
		Snippet: driver.source.bb.nfc.cblock.scmd.set(scmd = enums.NfcSelCmd.CL1, commandBlock = repcap.CommandBlock.Default) \n
		Selects the cascade level (CL) of the NFCID1 requested by the NFC Forum Device in Poll Mode. \n
			:param scmd: CL1| CL2| CL3
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(scmd, enums.NfcSelCmd)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SCMD {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcSelCmd:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SCMD \n
		Snippet: value: enums.NfcSelCmd = driver.source.bb.nfc.cblock.scmd.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the cascade level (CL) of the NFCID1 requested by the NFC Forum Device in Poll Mode. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: scmd: CL1| CL2| CL3"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SCMD?')
		return Conversions.str_to_scalar_enum(response, enums.NfcSelCmd)
