from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.EvdoRpcMode, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:MODE \n
		Snippet: driver.source.bb.evdo.user.rpc.mode.set(mode = enums.EvdoRpcMode.DOWN, userIx = repcap.UserIx.Default) \n
		Sets the operation mode for the Reverse Power Control (RPC) Channel within the MAC channel for the selected user. \n
			:param mode: HOLD| UP| DOWN| RANGe| PATTern
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EvdoRpcMode)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EvdoRpcMode:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:MODE \n
		Snippet: value: enums.EvdoRpcMode = driver.source.bb.evdo.user.rpc.mode.get(userIx = repcap.UserIx.Default) \n
		Sets the operation mode for the Reverse Power Control (RPC) Channel within the MAC channel for the selected user. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: mode: HOLD| UP| DOWN| RANGe| PATTern"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoRpcMode)
