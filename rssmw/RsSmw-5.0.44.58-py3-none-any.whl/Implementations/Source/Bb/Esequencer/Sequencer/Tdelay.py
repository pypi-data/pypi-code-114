from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def set(self, trigger_delay: float, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:TDELay \n
		Snippet: driver.source.bb.esequencer.sequencer.tdelay.set(trigger_delay = 1.0, sequencer = repcap.Sequencer.Default) \n
		Delays the trigger event for the selected sequencer. \n
			:param trigger_delay: float Range: 0 to 688
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.decimal_value_to_str(trigger_delay)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:TDELay {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:TDELay \n
		Snippet: value: float = driver.source.bb.esequencer.sequencer.tdelay.get(sequencer = repcap.Sequencer.Default) \n
		Delays the trigger event for the selected sequencer. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: trigger_delay: float Range: 0 to 688"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:TDELay?')
		return Conversions.str_to_float(response)
