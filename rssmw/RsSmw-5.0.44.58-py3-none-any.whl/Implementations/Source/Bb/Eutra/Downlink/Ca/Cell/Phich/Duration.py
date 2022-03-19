from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, duration: enums.EuTraDuration, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CA:CELL<CH0>:PHICh:DURation \n
		Snippet: driver.source.bb.eutra.downlink.ca.cell.phich.duration.set(duration = enums.EuTraDuration.EXTended, cellNull = repcap.CellNull.Default) \n
		Sets the PHICH duration and defines the allocation of the PHICH resource element groups over the OFDM symbols. \n
			:param duration: NORMal| EXTended NORMal The first OFDM symbol is allocated EXTended The first three OFDM symbols are allocated.
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(duration, enums.EuTraDuration)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:CA:CELL{cellNull_cmd_val}:PHICh:DURation {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.EuTraDuration:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:CA:CELL<CH0>:PHICh:DURation \n
		Snippet: value: enums.EuTraDuration = driver.source.bb.eutra.downlink.ca.cell.phich.duration.get(cellNull = repcap.CellNull.Default) \n
		Sets the PHICH duration and defines the allocation of the PHICH resource element groups over the OFDM symbols. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: duration: NORMal| EXTended NORMal The first OFDM symbol is allocated EXTended The first three OFDM symbols are allocated."""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:CA:CELL{cellNull_cmd_val}:PHICh:DURation?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraDuration)
