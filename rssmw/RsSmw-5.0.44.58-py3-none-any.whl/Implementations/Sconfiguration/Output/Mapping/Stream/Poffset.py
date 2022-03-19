from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Poffset:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, sm_phas_offset: float, stream=repcap.Stream.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:STReam<ST>:POFFset \n
		Snippet: driver.sconfiguration.output.mapping.stream.poffset.set(sm_phas_offset = 1.0, stream = repcap.Stream.Default) \n
		Option: R&S SMW-B9 - supported if 'Signal Outputs = Analog Only' Sets the phase offset of the corresponding stream. \n
			:param sm_phas_offset: float Range: -999.99 to 999.99
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.decimal_value_to_str(sm_phas_offset)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:STReam{stream_cmd_val}:POFFset {param}')

	def get(self, stream=repcap.Stream.Default) -> float:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:STReam<ST>:POFFset \n
		Snippet: value: float = driver.sconfiguration.output.mapping.stream.poffset.get(stream = repcap.Stream.Default) \n
		Option: R&S SMW-B9 - supported if 'Signal Outputs = Analog Only' Sets the phase offset of the corresponding stream. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: sm_phas_offset: float Range: -999.99 to 999.99"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:STReam{stream_cmd_val}:POFFset?')
		return Conversions.str_to_float(response)
