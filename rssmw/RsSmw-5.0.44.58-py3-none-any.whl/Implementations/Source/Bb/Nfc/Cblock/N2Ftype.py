from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N2Ftype:
	"""N2Ftype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n2Ftype", core, parent)

	def set(self, nf_type: enums.NfcNfcid2FmtTp, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:N2FType \n
		Snippet: driver.source.bb.nfc.cblock.n2Ftype.set(nf_type = enums.NfcNfcid2FmtTp.NDEP, commandBlock = repcap.CommandBlock.Default) \n
		Determines which protocol or platform the NFCID2 format is for. \n
			:param nf_type: NDEP| TT3
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(nf_type, enums.NfcNfcid2FmtTp)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:N2FType {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcNfcid2FmtTp:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:N2FType \n
		Snippet: value: enums.NfcNfcid2FmtTp = driver.source.bb.nfc.cblock.n2Ftype.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines which protocol or platform the NFCID2 format is for. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nf_type: NDEP| TT3"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:N2FType?')
		return Conversions.str_to_scalar_enum(response, enums.NfcNfcid2FmtTp)
