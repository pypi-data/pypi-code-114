from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, sm_freq_offset: float, stream=repcap.Stream.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:STReam<ST>:FOFFset \n
		Snippet: driver.sconfiguration.output.mapping.stream.foffset.set(sm_freq_offset = 1.0, stream = repcap.Stream.Default) \n
		Option: R&S SMW-B9 - supported if 'Signal Outputs = Analog Only' Sets an absolute frequency offset. Thus, the streams
		routed to the RF, I/Q Out and BBMM connectors are shifted in the frequency domain. \n
			:param sm_freq_offset: float Range: depends on the installed options, e.g. -60E6 to +60E6 (base unit) Value range depends also on the system confugration mode and signal outputs. For details, see data sheet.
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.decimal_value_to_str(sm_freq_offset)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:STReam{stream_cmd_val}:FOFFset {param}')

	def get(self, stream=repcap.Stream.Default) -> float:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:STReam<ST>:FOFFset \n
		Snippet: value: float = driver.sconfiguration.output.mapping.stream.foffset.get(stream = repcap.Stream.Default) \n
		Option: R&S SMW-B9 - supported if 'Signal Outputs = Analog Only' Sets an absolute frequency offset. Thus, the streams
		routed to the RF, I/Q Out and BBMM connectors are shifted in the frequency domain. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: sm_freq_offset: float Range: depends on the installed options, e.g. -60E6 to +60E6 (base unit) Value range depends also on the system confugration mode and signal outputs. For details, see data sheet."""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:STReam{stream_cmd_val}:FOFFset?')
		return Conversions.str_to_float(response)
