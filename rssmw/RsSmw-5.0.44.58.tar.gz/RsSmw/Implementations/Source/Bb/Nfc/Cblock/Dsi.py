from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dsi:
	"""Dsi commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dsi", core, parent)

	def set(self, dsi: enums.NfcDsiDri, commandBlock=repcap.CommandBlock.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DSI \n
		Snippet: driver.source.bb.nfc.cblock.dsi.set(dsi = enums.NfcDsiDri.D1, commandBlock = repcap.CommandBlock.Default) \n
		Sets DSI. \n
			:param dsi: D1| D2| D8| D4| D16| D32| D64
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
		"""
		param = Conversions.enum_scalar_to_str(dsi, enums.NfcDsiDri)
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		self._core.io.write(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DSI {param}')

	# noinspection PyTypeChecker
	def get(self, commandBlock=repcap.CommandBlock.Default) -> enums.NfcDsiDri:
		"""SCPI: [SOURce<HW>]:BB:NFC:CBLock<CH>:DSI \n
		Snippet: value: enums.NfcDsiDri = driver.source.bb.nfc.cblock.dsi.get(commandBlock = repcap.CommandBlock.Default) \n
		Sets DSI. \n
			:param commandBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cblock')
			:return: dsi: D1| D2| D8| D4| D16| D32| D64"""
		commandBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(commandBlock, repcap.CommandBlock)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NFC:CBLock{commandBlock_cmd_val}:DSI?')
		return Conversions.str_to_scalar_enum(response, enums.NfcDsiDri)
