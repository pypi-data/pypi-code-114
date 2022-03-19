from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Target:
	"""Target commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("target", core, parent)

	def set(self, cw_freq_offset: float, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:TARGet \n
		Snippet: driver.source.bb.gnss.awgn.rf.frequency.target.set(cw_freq_offset = 1.0, path = repcap.Path.Default) \n
		Sets the frequency offset of the sine wave relative to the 'Reference Frequency'. \n
			:param cw_freq_offset: float Range: -250E6 to 250E6
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(cw_freq_offset)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:TARGet {param}')

	def get(self, path=repcap.Path.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:TARGet \n
		Snippet: value: float = driver.source.bb.gnss.awgn.rf.frequency.target.get(path = repcap.Path.Default) \n
		Sets the frequency offset of the sine wave relative to the 'Reference Frequency'. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: cw_freq_offset: float Range: -250E6 to 250E6"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:TARGet?')
		return Conversions.str_to_float(response)
