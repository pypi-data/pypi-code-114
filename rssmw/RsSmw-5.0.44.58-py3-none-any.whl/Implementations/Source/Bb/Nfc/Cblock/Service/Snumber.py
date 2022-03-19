from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Snumber:
	"""Snumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def set(self, snumber: int, commandBlock=repcap.CommandBlock.Default, serviceListTable=repcap.ServiceListTable.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SERVice<ST>:SNUMber \n
		Snippet: driver.source.bb.nfc.cblock.service.snumber.set(snumber = 1, commandBlock = repcap.CommandBlock.Default, serviceListTable = repcap.ServiceListTable.Default) \n
		Determines the number of services. \n
			:param snumber: integer Range: 0 to 1023
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param serviceListTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Service')
		"""
		param = Conversions.decimal_value_to_str(snumber)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		serviceListTable_cmd_val = self._cmd_group.get_repcap_cmd_value(serviceListTable, repcap.ServiceListTable)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SERVice{serviceListTable_cmd_val}:SNUMber {param}')

	def get(self, commandBlock=repcap.CommandBlock.Default, serviceListTable=repcap.ServiceListTable.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:SERVice<ST>:SNUMber \n
		Snippet: value: int = driver.source.bb.nfc.cblock.service.snumber.get(commandBlock = repcap.CommandBlock.Default, serviceListTable = repcap.ServiceListTable.Default) \n
		Determines the number of services. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:param serviceListTable: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Service')
			:return: snumber: integer Range: 0 to 1023"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		serviceListTable_cmd_val = self._cmd_group.get_repcap_cmd_value(serviceListTable, repcap.ServiceListTable)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:SERVice{serviceListTable_cmd_val}:SNUMber?')
		return Conversions.str_to_int(response)
