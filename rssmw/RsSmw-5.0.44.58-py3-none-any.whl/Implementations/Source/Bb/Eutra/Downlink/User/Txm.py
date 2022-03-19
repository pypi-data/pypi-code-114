from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Txm:
	"""Txm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txm", core, parent)

	def set(self, tx_mode: enums.EutraTxMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:TXM \n
		Snippet: driver.source.bb.eutra.downlink.user.txm.set(tx_mode = enums.EutraTxMode.M1, userIx = repcap.UserIx.Default) \n
		Sets the transmission mode of the according user as defined in . \n
			:param tx_mode: USER| M1| M2| M3| M4| M5| M6| M7| M8| M9| M10 | M10 Option: R&S SMW-K115 TxMode = USER|M1|M2|M6|M9
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(tx_mode, enums.EutraTxMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:TXM {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EutraTxMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:USER<CH>:TXM \n
		Snippet: value: enums.EutraTxMode = driver.source.bb.eutra.downlink.user.txm.get(userIx = repcap.UserIx.Default) \n
		Sets the transmission mode of the according user as defined in . \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: tx_mode: USER| M1| M2| M3| M4| M5| M6| M7| M8| M9| M10 | M10 Option: R&S SMW-K115 TxMode = USER|M1|M2|M6|M9"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:USER{userIx_cmd_val}:TXM?')
		return Conversions.str_to_scalar_enum(response, enums.EutraTxMode)
