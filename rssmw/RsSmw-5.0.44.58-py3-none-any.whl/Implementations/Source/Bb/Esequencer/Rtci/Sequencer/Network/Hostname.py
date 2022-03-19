from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hostname:
	"""Hostname commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hostname", core, parent)

	def get(self, sequencer=repcap.Sequencer.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:NETWork:HOSTname \n
		Snippet: value: str = driver.source.bb.esequencer.rtci.sequencer.network.hostname.get(sequencer = repcap.Sequencer.Default) \n
		Sets an individual hostname for the R&S SMW. Note:We recommend that you do not change the hostname to avoid problems with
		the network connection. If you change the hostname, be sure to use a unique name. This is a password-protected function.
		Unlock the protection level 1 to access it, see method RsSmw.System.Protect.State.set. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: hostname: string"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:NETWork:HOSTname?')
		return trim_str_response(response)
