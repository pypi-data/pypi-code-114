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

	def set(self, tx_mode: enums.OneWebTxMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:TXM \n
		Snippet: driver.source.bb.oneweb.downlink.user.txm.set(tx_mode = enums.OneWebTxMode.M1OW, userIx = repcap.UserIx.Default) \n
		Sets the transmission mode. \n
			:param tx_mode: M1OW| M2OW
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(tx_mode, enums.OneWebTxMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:TXM {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.OneWebTxMode:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:USER<CH>:TXM \n
		Snippet: value: enums.OneWebTxMode = driver.source.bb.oneweb.downlink.user.txm.get(userIx = repcap.UserIx.Default) \n
		Sets the transmission mode. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: tx_mode: M1OW| M2OW"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:USER{userIx_cmd_val}:TXM?')
		return Conversions.str_to_scalar_enum(response, enums.OneWebTxMode)
