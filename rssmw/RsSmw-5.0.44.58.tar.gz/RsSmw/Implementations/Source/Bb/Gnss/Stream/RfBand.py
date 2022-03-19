from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfBand:
	"""RfBand commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfBand", core, parent)

	def set(self, rf_band: enums.RfBand, stream=repcap.Stream.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:RFBand \n
		Snippet: driver.source.bb.gnss.stream.rfBand.set(rf_band = enums.RfBand.L1, stream = repcap.Stream.Default) \n
		Selects the signal of which RF band is carried by which stream. \n
			:param rf_band: L1| L2| L5
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.enum_scalar_to_str(rf_band, enums.RfBand)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:RFBand {param}')

	# noinspection PyTypeChecker
	def get(self, stream=repcap.Stream.Default) -> enums.RfBand:
		"""SCPI: [SOURce<HW>]:BB:GNSS:STReam<ST>:RFBand \n
		Snippet: value: enums.RfBand = driver.source.bb.gnss.stream.rfBand.get(stream = repcap.Stream.Default) \n
		Selects the signal of which RF band is carried by which stream. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: rf_band: L1| L2| L5"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:STReam{stream_cmd_val}:RFBand?')
		return Conversions.str_to_scalar_enum(response, enums.RfBand)
