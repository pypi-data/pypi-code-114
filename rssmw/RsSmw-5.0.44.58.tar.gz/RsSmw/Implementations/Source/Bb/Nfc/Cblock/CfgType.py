from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CfgType:
	"""CfgType commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cfgType", core, parent)

	def set(self, conf_type: enums.NfcConfigType, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:CFGType \n
		Snippet: driver.source.bb.nfc.cblock.cfgType.set(conf_type = enums.NfcConfigType._0, commandBlock = repcap.CommandBlock.Default) \n
		Determines what platform or protocol the device in listen mode is configured for. \n
			:param conf_type: T2| T4A| NDEP| DT4A| OFF| 0| ON| 1
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(conf_type, enums.NfcConfigType)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:CFGType {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcConfigType:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:CFGType \n
		Snippet: value: enums.NfcConfigType = driver.source.bb.nfc.cblock.cfgType.get(commandBlock = repcap.CommandBlock.Default) \n
		Determines what platform or protocol the device in listen mode is configured for. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: conf_type: T2| T4A| NDEP| DT4A| OFF| 0| ON| 1"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:CFGType?')
		return Conversions.str_to_scalar_enum(response, enums.NfcConfigType)
