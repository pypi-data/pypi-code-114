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
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:WLISt:FILE \n
		Snippet: driver.source.bb.esequencer.rtci.sequencer.wlist.file.set(file = '1', sequencer = repcap.Sequencer.Default) \n
		Selects a waveform list from the default directory. If a waveform list with the specified name does not yet exist, it is
		created. The file extension *.inf_mswv may be omitted. \n
			:param file: string
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.value_to_quoted_str(file)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:WLISt:FILE {param}')

	def get(self, sequencer=repcap.Sequencer.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:WLISt:FILE \n
		Snippet: value: str = driver.source.bb.esequencer.rtci.sequencer.wlist.file.get(sequencer = repcap.Sequencer.Default) \n
		Selects a waveform list from the default directory. If a waveform list with the specified name does not yet exist, it is
		created. The file extension *.inf_mswv may be omitted. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: file: string"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:WLISt:FILE?')
		return trim_str_response(response)
