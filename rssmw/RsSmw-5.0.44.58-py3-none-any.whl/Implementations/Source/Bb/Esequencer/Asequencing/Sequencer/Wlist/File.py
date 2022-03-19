from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, file: str, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:[SEQuencer<ST>]:WLISt:FILE \n
		Snippet: driver.source.bb.esequencer.asequencing.sequencer.wlist.file.set(file = '1', sequencer = repcap.Sequencer.Default) \n
		No command help available \n
			:param file: No help available
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.value_to_quoted_str(file)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:SEQuencer{sequencer_cmd_val}:WLISt:FILE {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:[SEQuencer<ST>]:WLISt:FILE \n
		Snippet: value: str = driver.source.bb.esequencer.asequencing.sequencer.wlist.file.get(sequencer = repcap.Sequencer.Default) \n
		No command help available \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: file: No help available"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:SEQuencer{sequencer_cmd_val}:WLISt:FILE?')
		return trim_str_response(response)
