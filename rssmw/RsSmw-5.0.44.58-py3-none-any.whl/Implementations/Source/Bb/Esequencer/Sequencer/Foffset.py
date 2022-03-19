from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, freq_offset: float, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:FOFFset \n
		Snippet: driver.source.bb.esequencer.sequencer.foffset.set(freq_offset = 1.0, sequencer = repcap.Sequencer.Default) \n
		Sets a frequency offset for the selected sequencer. \n
			:param freq_offset: float Range: -250E6 to 250E6
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.decimal_value_to_str(freq_offset)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:FOFFset {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:FOFFset \n
		Snippet: value: float = driver.source.bb.esequencer.sequencer.foffset.get(sequencer = repcap.Sequencer.Default) \n
		Sets a frequency offset for the selected sequencer. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: freq_offset: float Range: -250E6 to 250E6"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:FOFFset?')
		return Conversions.str_to_float(response)
