from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cw:
	"""Cw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cw", core, parent)

	def set(self, cw_frequency: int, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:CW \n
		Snippet: driver.source.bb.gnss.awgn.rf.frequency.cw.set(cw_frequency = 1, path = repcap.Path.Default) \n
		Sets the frequency of the CW interfering signal. \n
			:param cw_frequency: integer Range: 1E9 to 2E9, Unit: Hz
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(cw_frequency)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:CW {param}')

	def get(self, path=repcap.Path.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:FREQuency:CW \n
		Snippet: value: int = driver.source.bb.gnss.awgn.rf.frequency.cw.get(path = repcap.Path.Default) \n
		Sets the frequency of the CW interfering signal. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: cw_frequency: integer Range: 1E9 to 2E9, Unit: Hz"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:FREQuency:CW?')
		return Conversions.str_to_int(response)
