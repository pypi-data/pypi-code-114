from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_py: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:RANGe \n
		Snippet: driver.source.bb.evdo.user.rpc.range.set(range_py = 1, userIx = repcap.UserIx.Default) \n
		Sets the number of Reverse Power Control (RPC) bits sent in each direction when the 'RPC Mode = Range'. The specified
		value is used immediately. \n
			:param range_py: integer Range: 1 to 256
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(range_py)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:RANGe {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:RPC:RANGe \n
		Snippet: value: int = driver.source.bb.evdo.user.rpc.range.get(userIx = repcap.UserIx.Default) \n
		Sets the number of Reverse Power Control (RPC) bits sent in each direction when the 'RPC Mode = Range'. The specified
		value is used immediately. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: range_py: integer Range: 1 to 256"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:RPC:RANGe?')
		return Conversions.str_to_int(response)
