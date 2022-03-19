from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bfsdd:
	"""Bfsdd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bfsdd", core, parent)

	def set(self, bfsdd: enums.NfcBitFrmSdd, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BFSDd \n
		Snippet: driver.source.bb.nfc.cblock.bfsdd.set(bfsdd = enums.NfcBitFrmSdd.SDD0, commandBlock = repcap.CommandBlock.Default) \n
		Determines Bit frame SDD. \n
			:param bfsdd: SDD0| SDD2| SDD1| SDD4| SDD8| SDD16
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(bfsdd, enums.NfcBitFrmSdd)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BFSDd {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcBitFrmSdd:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:BFSDd \n
		Snippet: value: enums.NfcBitFrmSdd = driver.source.bb.nfc.cblock.bfsdd.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines Bit frame SDD. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: bfsdd: SDD0| SDD2| SDD1| SDD4| SDD8| SDD16"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:BFSDd?')
		return Conversions.str_to_scalar_enum(response, enums.NfcBitFrmSdd)
