from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:STATe \n
		Snippet: driver.source.bb.evdo.user.drclock.state.set(state = False, userIx = repcap.UserIx.Default) \n
		Sets the state of the DRC (Data Rate Control) Lock bit for the selected user. Note: Changes in the DRC Lock state are
		only considered at the interval defined by the parameter DRC Lock Length. \n
			:param state: 1| ON| 0| OFF
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.bool_to_str(state)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:STATe {param}')

	def get(self, userIx=repcap.UserIx.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:STATe \n
		Snippet: value: bool = driver.source.bb.evdo.user.drclock.state.get(userIx = repcap.UserIx.Default) \n
		Sets the state of the DRC (Data Rate Control) Lock bit for the selected user. Note: Changes in the DRC Lock state are
		only considered at the interval defined by the parameter DRC Lock Length. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: state: 1| ON| 0| OFF"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:STATe?')
		return Conversions.str_to_bool(response)
