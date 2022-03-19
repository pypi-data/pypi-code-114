from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Period:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, period: enums.EvdoDrcPer, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:PERiod \n
		Snippet: driver.source.bb.evdo.user.drclock.period.set(period = enums.EvdoDrcPer.DP0, userIx = repcap.UserIx.Default) \n
		Sets the period (measured in slots) of time between successive transmissions of the DRC (Data Rate Control) Lock bit for
		the selected user. Note: A value of zero disables the DRC Lock subchannel and the MAC RPC channel of the selected user is
		not punctured with the DRC Lock subchannel. \n
			:param period: DP0| DP4| DP8| DP16
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(period, enums.EvdoDrcPer)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:PERiod {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.EvdoDrcPer:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:DRCLock:PERiod \n
		Snippet: value: enums.EvdoDrcPer = driver.source.bb.evdo.user.drclock.period.get(userIx = repcap.UserIx.Default) \n
		Sets the period (measured in slots) of time between successive transmissions of the DRC (Data Rate Control) Lock bit for
		the selected user. Note: A value of zero disables the DRC Lock subchannel and the MAC RPC channel of the selected user is
		not punctured with the DRC Lock subchannel. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: period: DP0| DP4| DP8| DP16"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:DRCLock:PERiod?')
		return Conversions.str_to_scalar_enum(response, enums.EvdoDrcPer)
