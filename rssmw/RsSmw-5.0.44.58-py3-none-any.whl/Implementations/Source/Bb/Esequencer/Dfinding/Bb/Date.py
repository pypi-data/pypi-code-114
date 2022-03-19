from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def get(self, baseband=repcap.Baseband.Default) -> str:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:DFINding:[BB<ST>]:DATE \n
		Snippet: value: str = driver.source.bb.esequencer.dfinding.bb.date.get(baseband = repcap.Baseband.Default) \n
		Queries the timestamp of the selected direction finding file. \n
			:param baseband: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bb')
			:return: date: string"""
		baseband_cmd_val = self._cmd_group.get_repcap_cmd_value(baseband, repcap.Baseband)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:DFINding:BB{baseband_cmd_val}:DATE?')
		return trim_str_response(response)
