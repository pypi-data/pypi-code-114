from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	def set(self, system_band_width: int, path=repcap.Path.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:BWIDth \n
		Snippet: driver.source.bb.gnss.awgn.rf.bandwidth.set(system_band_width = 1, path = repcap.Path.Default) \n
		Sets the RF bandwidth to which the set carrier/noise ratio relates. Within this frequency range, the signal is
		superimposed with a noise signal which level corresponds exactly to the set C/N or S/N ratio. \n
			:param system_band_width: integer Range: 1E3 to 500E6
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
		"""
		param = Conversions.decimal_value_to_str(system_band_width)
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:BWIDth {param}')

	def get(self, path=repcap.Path.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:AWGN:[RF<CH>]:BWIDth \n
		Snippet: value: int = driver.source.bb.gnss.awgn.rf.bandwidth.get(path = repcap.Path.Default) \n
		Sets the RF bandwidth to which the set carrier/noise ratio relates. Within this frequency range, the signal is
		superimposed with a noise signal which level corresponds exactly to the set C/N or S/N ratio. \n
			:param path: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rf')
			:return: system_band_width: integer Range: 1E3 to 500E6"""
		path_cmd_val = self._cmd_group.get_repcap_cmd_value(path, repcap.Path)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:AWGN:RF{path_cmd_val}:BWIDth?')
		return Conversions.str_to_int(response)
