from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	def get(self, path=repcap.Path.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:REFerence \n
		Snippet: value: int = driver.source.bb.gnss.awgn.rf.frequency.reference.get(path = repcap.Path.Default) \n
		Queries the reference frequency, that is the RF carrier frequency. Set the freqquency with the following remote command:
		SOURce1:FREQuency \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: reference_freq: integer Range: 1E9 to 2E9"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:REFerence?')
		return Conversions.str_to_int(response)
