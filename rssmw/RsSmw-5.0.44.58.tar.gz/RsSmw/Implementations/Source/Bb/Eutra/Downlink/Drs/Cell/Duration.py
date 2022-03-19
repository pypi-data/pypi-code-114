from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, drs_duration: enums.DrsDuration, cellNull=repcap.CellNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:DURation \n
		Snippet: driver.source.bb.eutra.downlink.drs.cell.duration.set(drs_duration = enums.DrsDuration.DUR1, cellNull = repcap.CellNull.Default) \n
		Sets the DRS duration. \n
			:param drs_duration: DUR1| DUR2| DUR3| DUR4| DUR5 DUR1 For LAA SCells, the DRS is always 1 ms long DUR2|DUR3|DUR4|DUR5 In FDD mode, sets duration of 2 ms to 5 ms
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
		"""
		param = Conversions.enum_scalar_to_str(drs_duration, enums.DrsDuration)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:DURation {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Default) -> enums.DrsDuration:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:DL:DRS:CELL<CH0>:DURation \n
		Snippet: value: enums.DrsDuration = driver.source.bb.eutra.downlink.drs.cell.duration.get(cellNull = repcap.CellNull.Default) \n
		Sets the DRS duration. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:return: drs_duration: DUR1| DUR2| DUR3| DUR4| DUR5 DUR1 For LAA SCells, the DRS is always 1 ms long DUR2|DUR3|DUR4|DUR5 In FDD mode, sets duration of 2 ms to 5 ms"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:DL:DRS:CELL{cellNull_cmd_val}:DURation?')
		return Conversions.str_to_scalar_enum(response, enums.DrsDuration)
