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

	def get(self, baseStation=repcap.BaseStation.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:W3GPp:BSTation<ST>:DCONflict:[STATe] \n
		Snippet: value: bool = driver.source.bb.w3Gpp.bstation.dconflict.state.get(baseStation = repcap.BaseStation.Default) \n
		The command queries whether there is (response 1) or is not (response 0) a conflict (overlap) in the
		hierarchically-structured channelization codes. The cause of a possible domain conflict can be ascertained by manual
		operation in the 'BS > Code Domain' dialog. \n
			:param baseStation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bstation')
			:return: state: 1| ON| 0| OFF"""
		baseStation_cmd_val = self._cmd_group.get_repcap_cmd_value(baseStation, repcap.BaseStation)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:W3GPp:BSTation{baseStation_cmd_val}:DCONflict:STATe?')
		return Conversions.str_to_bool(response)
