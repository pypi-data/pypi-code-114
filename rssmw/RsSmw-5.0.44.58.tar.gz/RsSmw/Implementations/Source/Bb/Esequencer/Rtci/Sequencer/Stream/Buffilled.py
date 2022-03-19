from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Buffilled:
	"""Buffilled commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("buffilled", core, parent)

	def get(self, sequencer=repcap.Sequencer.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:STReam:BUFFilled \n
		Snippet: value: float = driver.source.bb.esequencer.rtci.sequencer.stream.buffilled.get(sequencer = repcap.Sequencer.Default) \n
		Query data from streaming interface registers for system time, write count, read count, executed PDWs, dropped PDWs,
		buffer filled and buffer remain information. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: value: float"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:STReam:BUFFilled?')
		return Conversions.str_to_float(response)
