from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aattributes:
	"""Aattributes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aattributes", core, parent)

	def set(self, aattributes: enums.NfcAcssAttrib, commandBlock=repcap.CommandBlock.Default, serviceListTable=repcap.ServiceListTable.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SERVice<ST>:AATTributes \n
		Snippet: driver.source.bb.nfc.cblock.service.aattributes.set(aattributes = enums.NfcAcssAttrib.AARO, commandBlock = repcap.CommandBlock.Default, serviceListTable = repcap.ServiceListTable.Default) \n
		Enables the Service Code List Configuration. \n
			:param aattributes: AARW| AARO
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param serviceListTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Service')
		"""
		param = Conversions.enum_scalar_to_str(aattributes, enums.NfcAcssAttrib)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		serviceListTable_cmd_val = self._cmd_group.get_repcap_cmd_value(serviceListTable, repcap.ServiceListTable)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SERVice{serviceListTable_cmd_val}:AATTributes {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default, serviceListTable=repcap.ServiceListTable.Default) -> enums.NfcAcssAttrib:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SERVice<ST>:AATTributes \n
		Snippet: value: enums.NfcAcssAttrib = driver.source.bb.nfc.cblock.service.aattributes.get(commandBlock = repcap.CommandBlock.Default, serviceListTable = repcap.ServiceListTable.Default) \n
		Enables the Service Code List Configuration. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param serviceListTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Service')
			:return: aattributes: AARW| AARO"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		serviceListTable_cmd_val = self._cmd_group.get_repcap_cmd_value(serviceListTable, repcap.ServiceListTable)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SERVice{serviceListTable_cmd_val}:AATTributes?')
		return Conversions.str_to_scalar_enum(response, enums.NfcAcssAttrib)
