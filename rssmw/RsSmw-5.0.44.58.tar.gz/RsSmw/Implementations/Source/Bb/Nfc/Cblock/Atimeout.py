from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Atimeout:
	"""Atimeout commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("atimeout", core, parent)

	def set(self, atimeout: enums.NfcAtnTmot, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ATIMeout \n
		Snippet: driver.source.bb.nfc.cblock.atimeout.set(atimeout = enums.NfcAtnTmot.ATN, commandBlock = repcap.CommandBlock.Default) \n
		Only used with PDU type 'supervisory'. Determines whether an 'ATN' (Attention) or 'Timeout' supervisory PDU type is used. \n
			:param atimeout: ATN| TOUT
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(atimeout, enums.NfcAtnTmot)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ATIMeout {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcAtnTmot:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:ATIMeout \n
		Snippet: value: enums.NfcAtnTmot = driver.source.bb.nfc.cblock.atimeout.get(commandBlock = repcap.CommandBlock.Default) \n
		Only used with PDU type 'supervisory'. Determines whether an 'ATN' (Attention) or 'Timeout' supervisory PDU type is used. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: atimeout: ATN| TOUT"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:ATIMeout?')
		return Conversions.str_to_scalar_enum(response, enums.NfcAtnTmot)
