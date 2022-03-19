from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nsize:
	"""Nsize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nsize", core, parent)

	def set(self, nfc_id_1_sz: enums.NfcNfcid1Sz, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NSIZe \n
		Snippet: driver.source.bb.nfc.cblock.nsize.set(nfc_id_1_sz = enums.NfcNfcid1Sz.DOUBle, commandBlock = repcap.CommandBlock.Default) \n
		Determines the size of NFCID1. \n
			:param nfc_id_1_sz: SINGle| DOUBle| TRIPle
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(nfc_id_1_sz, enums.NfcNfcid1Sz)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NSIZe {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcNfcid1Sz:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:NSIZe \n
		Snippet: value: enums.NfcNfcid1Sz = driver.source.bb.nfc.cblock.nsize.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines the size of NFCID1. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: nfc_id_1_sz: SINGle| DOUBle| TRIPle"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:NSIZe?')
		return Conversions.str_to_scalar_enum(response, enums.NfcNfcid1Sz)
