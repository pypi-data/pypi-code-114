from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get(self, sequencer=repcap.Sequencer.Default) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:WLISt:SEGMent:CATalog \n
		Snippet: value: List[str] = driver.source.bb.esequencer.rtci.sequencer.wlist.segment.catalog.get(sequencer = repcap.Sequencer.Default) \n
		Queries the waveform sequence of the currently selected waveform list. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: catalog: string Returns the waveform files separated by commas"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:WLISt:SEGMent:CATalog?')
		return Conversions.str_to_str_list(response)
