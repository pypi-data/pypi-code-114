from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdCoding:
	"""AdCoding commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("adCoding", core, parent)

	def set(self, ad_coding: enums.NfcAppDataCod, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ADCoding \n
		Snippet: driver.source.bb.nfc.cblock.adCoding.set(ad_coding = enums.NfcAppDataCod.CRCB, commandBlock = repcap.CommandBlock.Default) \n
		Determines if application is proprietary or CRC-B. \n
			:param ad_coding: PROP| CRCB
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(ad_coding, enums.NfcAppDataCod)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ADCoding {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcAppDataCod:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ADCoding \n
		Snippet: value: enums.NfcAppDataCod = driver.source.bb.nfc.cblock.adCoding.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines if application is proprietary or CRC-B. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: ad_coding: PROP| CRCB"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ADCoding?')
		return Conversions.str_to_scalar_enum(response, enums.NfcAppDataCod)
