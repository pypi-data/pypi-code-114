from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, filename: str, baseband=repcap.Baseband.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PSEQuencer:[BB<ST>]:FILE:[SELect] \n
		Snippet: driver.source.bb.esequencer.psequencer.bb.file.select.set(filename = '1', baseband = repcap.Baseband.Default) \n
		Selects an existing pulse sequencer file. \n
			:param filename: string
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
		"""
		param = Conversions.value_to_quoted_str(filename)
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:PSEQuencer:BB{baseband_cmd_val}:FILE:SELect {param}')

	def get(self, baseband=repcap.Baseband.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:PSEQuencer:[BB<ST>]:FILE:[SELect] \n
		Snippet: value: str = driver.source.bb.esequencer.psequencer.bb.file.select.get(baseband = repcap.Baseband.Default) \n
		Selects an existing pulse sequencer file. \n
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
			:return: filename: string"""
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:PSEQuencer:BB{baseband_cmd_val}:FILE:SELect?')
		return trim_str_response(response)
