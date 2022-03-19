from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dri:
	"""Dri commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dri", core, parent)

	def set(self, dri: enums.NfcDsiDri, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DRI \n
		Snippet: driver.source.bb.nfc.cblock.dri.set(dri = enums.NfcDsiDri.D1, commandBlock = repcap.CommandBlock.Default) \n
		Sets DRI. \n
			:param dri: D1| D2| D8| D4| D16| D32| D64
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(dri, enums.NfcDsiDri)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DRI {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcDsiDri:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DRI \n
		Snippet: value: enums.NfcDsiDri = driver.source.bb.nfc.cblock.dri.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets DRI. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: dri: D1| D2| D8| D4| D16| D32| D64"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DRI?')
		return Conversions.str_to_scalar_enum(response, enums.NfcDsiDri)
