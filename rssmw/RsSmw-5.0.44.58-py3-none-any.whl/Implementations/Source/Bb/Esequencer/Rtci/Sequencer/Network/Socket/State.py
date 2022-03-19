from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def get(self, sequencer=repcap.Sequencer.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:NETWork:SOCKet:STATe \n
		Snippet: value: bool = driver.source.bb.esequencer.rtci.sequencer.network.socket.state.get(sequencer = repcap.Sequencer.Default) \n
		Queries whether the socket is open and thus if the connection between the external PDW simulator and the instrument is
		established. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: socket_state: 0| 1| OFF| ON"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:NETWork:SOCKet:STATe?')
		return Conversions.str_to_bool(response)
