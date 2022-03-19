from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, offset: float, offsetNull=repcap.OffsetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet<CH0>:VALue \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.offset.value.set(offset = 1.0, offsetNull = repcap.OffsetNull.Default) \n
		Specifies Offset0 to Offset5 of the offset setting table. Command sets the values in ms. Query returns values in s. \n
			:param offset: float Range: 0 s to depending on Max. Interval , Unit: ms
			:param offsetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Offset')
		"""
		param = Conversions.decimal_value_to_str(offset)
		offsetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(offsetNull, repcap.OffsetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet{offsetNull_cmd_val}:VALue {param}')

	def get(self, offsetNull=repcap.OffsetNull.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet<CH0>:VALue \n
		Snippet: value: float = driver.source.bb.btooth.econfiguration.pconfiguration.offset.value.get(offsetNull = repcap.OffsetNull.Default) \n
		Specifies Offset0 to Offset5 of the offset setting table. Command sets the values in ms. Query returns values in s. \n
			:param offsetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Offset')
			:return: offset: float Range: 0 s to depending on Max. Interval , Unit: ms"""
		offsetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(offsetNull, repcap.OffsetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet{offsetNull_cmd_val}:VALue?')
		return Conversions.str_to_float(response)
