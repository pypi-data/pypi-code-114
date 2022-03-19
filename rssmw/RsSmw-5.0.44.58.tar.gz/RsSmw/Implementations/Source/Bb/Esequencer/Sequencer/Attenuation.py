from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def set(self, attenuation: float, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:ATTenuation \n
		Snippet: driver.source.bb.esequencer.sequencer.attenuation.set(attenuation = 1.0, sequencer = repcap.Sequencer.Default) \n
		Adds an additional attenuation for the selected sequencer. \n
			:param attenuation: float Range: 0 to 50
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:ATTenuation {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:SEQuencer<ST>:ATTenuation \n
		Snippet: value: float = driver.source.bb.esequencer.sequencer.attenuation.get(sequencer = repcap.Sequencer.Default) \n
		Adds an additional attenuation for the selected sequencer. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: attenuation: float Range: 0 to 50"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:SEQuencer{sequencer_cmd_val}:ATTenuation?')
		return Conversions.str_to_float(response)
