from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ifactor:
	"""Ifactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifactor", core, parent)

	def set(self, ifactor: int, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:IFACtor \n
		Snippet: driver.source.bb.evdo.user.ifactor.set(ifactor = 1, userIx = repcap.UserIx.Default) \n
		Controls the number of interleave slots used for the selected user on the forward link. Four interleave slots are defined
		in the 1xEV-DO system. By default, only 1 Interleave slot (Interleave Factor = 1) for an access terminal is configured
		and transmission to that access terminal every fourth slot is selected. For an interleave factor > 1, packets on multiple
		interleave slots are sent, increasing the data throughput to the access terminal. \n
			:param ifactor: integer Range: 1 to 4
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.decimal_value_to_str(ifactor)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:IFACtor {param}')

	def get(self, userIx=repcap.UserIx.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:USER<ST>:IFACtor \n
		Snippet: value: int = driver.source.bb.evdo.user.ifactor.get(userIx = repcap.UserIx.Default) \n
		Controls the number of interleave slots used for the selected user on the forward link. Four interleave slots are defined
		in the 1xEV-DO system. By default, only 1 Interleave slot (Interleave Factor = 1) for an access terminal is configured
		and transmission to that access terminal every fourth slot is selected. For an interleave factor > 1, packets on multiple
		interleave slots are sent, increasing the data throughput to the access terminal. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: ifactor: integer Range: 1 to 4"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:USER{userIx_cmd_val}:IFACtor?')
		return Conversions.str_to_int(response)
