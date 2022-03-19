from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, phase_offset: float, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:POFFset \n
		Snippet: driver.source.bb.esequencer.sequencer.poffset.set(phase_offset = 1.0, sequencer = repcap.Sequencer.Default) \n
		Sets a phase offset for the selected sequencer. \n
			:param phase_offset: float Range: 0 to 359.99
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.decimal_value_to_str(phase_offset)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:POFFset {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:POFFset \n
		Snippet: value: float = driver.source.bb.esequencer.sequencer.poffset.get(sequencer = repcap.Sequencer.Default) \n
		Sets a phase offset for the selected sequencer. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: phase_offset: float Range: 0 to 359.99"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
