from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ctype:
	"""Ctype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctype", core, parent)

	def set(self, cmd: enums.NfcCmdType, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:CTYPe \n
		Snippet: driver.source.bb.nfc.cblock.ctype.set(cmd = enums.NfcCmdType.ACK, commandBlock = repcap.CommandBlock.Default) \n
		Selects the command type. \n
			:param cmd: ALAQ| SNAQ| SDAQ| SLAQ| SPAQ| RDAQ| RLAQ| T1RQ| WREQ| WNEQ| RSGQ| RD8Q| WE8Q| WN8Q| T2RQ| T2WQ| SSLQ| RATQ| T4AD| ATRQ| PSLQ| DEPQ| DSLQ| RLSQ| ALBQ| SNBQ| SMAR| SPBQ| ATBQ| T4BD| SNFQ| CHKQ| UPDQ| SNAS| SDAS| SLAS| RDAS| RLAS| T1RS| WRES| WNES| RSGS| RD8S| WE8S| WN8S| T2RS| ACK| NACK| ATSS| ATRS| PSLS| DEPS| DSLS| RLSS| SNBS| SPBS| ATBS| SNFS| CHKS| UPDS| GENE| IDLE| BLNK
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(cmd, enums.NfcCmdType)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:CTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcCmdType:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:CTYPe \n
		Snippet: value: enums.NfcCmdType = driver.source.bb.nfc.cblock.ctype.get(commandBlock = repcap.CommandBlock.Default) \n
		Selects the command type. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: cmd: ALAQ| SNAQ| SDAQ| SLAQ| SPAQ| RDAQ| RLAQ| T1RQ| WREQ| WNEQ| RSGQ| RD8Q| WE8Q| WN8Q| T2RQ| T2WQ| SSLQ| RATQ| T4AD| ATRQ| PSLQ| DEPQ| DSLQ| RLSQ| ALBQ| SNBQ| SMAR| SPBQ| ATBQ| T4BD| SNFQ| CHKQ| UPDQ| SNAS| SDAS| SLAS| RDAS| RLAS| T1RS| WRES| WNES| RSGS| RD8S| WE8S| WN8S| T2RS| ACK| NACK| ATSS| ATRS| PSLS| DEPS| DSLS| RLSS| SNBS| SPBS| ATBS| SNFS| CHKS| UPDS| GENE| IDLE| BLNK"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.NfcCmdType)
